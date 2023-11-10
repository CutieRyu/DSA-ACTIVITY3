from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET','POST'])
def toUppercase():
    result = None
    if request.method == 'POST':    
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/circle', methods=['GET', 'POST'])
def calculate_circle_area():
    if request.method == 'POST':
        try:
            # Get the radius input from the form
            radius = float(request.form['inputradius'])
            
            # Calculate the area of the circle
            area = 3.14159 * (radius ** 2)  # Using an approximation of pi

            return render_template('circle.html', result=True, area=area)
        except ValueError:
            # Handle the case where the input is not a valid number
            return render_template('circle.html', result=False)
    return render_template('circle.html', result=False)

@app.route('/areaOfTriangle', methods=['GET','POST'])
def calculateTriangleArea():
    if request.method == 'POST':
        try:
            base = int(request.form['base'])
            height = int(request.form['height'])
            area = base*height/2
            return render_template('areaOfTriangle.html', result=True, area=area)
        except ValueError:
            return render_template('areaOfTriangle.html', result=False)
    return render_template('areaOfTriangle.html', result=False)

if __name__ == "__main__":
    app.run(debug=True)
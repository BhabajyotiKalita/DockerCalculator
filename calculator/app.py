from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get form data
        a = float(request.form['a'])
        b = float(request.form['b'])
        operation = request.form['operation']

        # Perform calculation based on the selected operation
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return "Error: Division by zero is not allowed."
            result = a / b
        else:
            return "Error: Invalid operation selected."

        return render_template('index.html', result=result)
    except ValueError:
        return "Error: Please enter valid numbers."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

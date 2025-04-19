from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def home():
    # return jsonify({"message": "Witaj w moim API!"})
    return "Witaj w moim API!"

@app.route('/mojastrona')
def my_page():
    return "To jest moja strona!"

@app.route('/hello')
def hello_page():
    name = request.args.get('name')
    if name:
        return f"Hello {name}!"
    else:
        return "Hello!"

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    number1 = float(request.args.get('number1'))
    number2 = float(request.args.get('number2'))
    
    if number1 + number2 > 5.8:
        return jsonify({"prediction": 1, "features": {"number1": num1, "number2": num2}})
    else:
        return jsonify({"prediction": 0, "features": {"number1": num1, "number2": num2}})

if __name__ == '__main__':
    app.run()

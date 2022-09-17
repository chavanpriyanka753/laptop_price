from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    pass
    return 'data received'

if __name__ == "__main__":
    app.run(debug = True)
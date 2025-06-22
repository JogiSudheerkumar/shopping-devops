from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    items = ['T-Shirt', 'Jeans', 'Shoes','tea']
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/greet")
def greet():
    return '<p style="font-size:120%; font-weight:bold">Good Morning Friend, Hello from Ramesh</p>'




if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000")
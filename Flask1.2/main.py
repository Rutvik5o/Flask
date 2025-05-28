from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():

    marks = {
        "John" : 45,
        "Saurabj" : 99,
        "Mark":45,
        "Jeff" : 47,
        "Alexa":5
    }
    return render_template("index.html",marks=marks)


app.run(debug=True)
from flask import Flask,jsonify

app = Flask(__name__)

#serve data through api

@app.route("/")
def json():
    marks = {
    "ABC" : 57,
    "Roahn" : 33,
    "Aakash":43,
    "Shubham":51,
    "Reen":43
}
    values = [1,marks,87]
    return jsonify(values)


app.run(debug=True)
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "XYZ"
    token = 53753
    if "name" in request.args.keys(): ## take default value if wrong value provided
        name = request.args['name']

    if "token" in request.args.keys():
        token = request.args['token']

    
    return render_template("index.html",name=name,token=token)

app.run(debug=True)

#http://127.0.0.1:5000/?name=muname&token=47
from flask import Flask,render_template

#chaning static url path
#app = Flask(__name__,static_url_path="/public")

#how you change static folder location: changeing static folder
app = Flask(__name__,static_folder="assets",static_url_path="/static")


@app.route("/")


def hello_world():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=True)
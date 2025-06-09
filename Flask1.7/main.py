from flask import Flask,flash,render_template,redirect,url_for
#flask : show temporary message to the user
app = Flask(__name__)

app.secret_key = "fshfhs948esghl"
#secreat key is necessary in flash
@app.route("/")
def hellow_world():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out","success")
    return redirect(url_for('hellow_world'))  # 👈 redirect instead of render_template


app.run(debug=True)
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    if(request.method == "POST"):
        #Handle the form
        with open("file.txt","w") as f:
            f.write(f"the name is {request.form['name']} & email is {request.form['email']}")
            print("Data Stored Sccesfully")
    else:
        pass
    return render_template("contact.html")


app.run();
from flask import Flask, render_template , request , redirect , url_for
from validation import validation 

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/sign_up" , methods = ['GET' , 'POST'])
def register():
    if request.method == "POST" :
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")
        errors = validation(username, email , password , password_confirmation)
        if errors :
            return render_template("sign_up.html" , errors = errors )
        return redirect(url_for("homepage"))

    return render_template("sign_up.html")

if __name__== "__main__" :
    app.run(debug=True,port=9000)
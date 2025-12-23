from routes import auth , flash , request , redirect , render_template

@auth.route("/sign_up", methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        email    = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")
    
        if not username or not email or not password or not password_confirmation :
            flash("all field is required!")

        if len(username)  < 3 :
            flash("the username is too short!")

        if len(password) < 6 :
            flash("the password is too short!")

        if "@" not in email :
            flash("invailed email")

        if password != password_confirmation :
            flash("the password and password_confirmation not match!")
        return render_template("sign.html")
    
    return redirect("successful.html")
    
@auth.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST" :
        email    = request.form.get("email")
        password = request.form.get("password")

    return render_template("login.html")
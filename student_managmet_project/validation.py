def validation (username , email , password , password_confirmation):
    Errors = []
    if not username or not email or not password or not password_confirmation :
        Errors.append("all fields are required!")

    if username and len(username) < 3 :
        Errors.append("username is too short!")

    if email and "@" not in email :
        Errors.append("email not vaild!")

    if password and len(password) <= 6 :
        Errors.append("password is too short!")

    if password and password_confirmation and password != password_confirmation :
        Errors.append("the password not match!")

    return Errors
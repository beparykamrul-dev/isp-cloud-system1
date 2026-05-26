def check_user(username, password):

    if username == "admin":
        return {"role": "main_admin"}

    if username == "reseller":
        return {"role": "reseller"}

    if username == "sub":
        return {"role": "sub_admin"}

    return {"role": "user"}

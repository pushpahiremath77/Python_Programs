def email_notify(func):
    def new_func(user):
        print(func(user))
        print("Email sent successfully")
    return new_func

@email_notify
def signup(username):
    return f"{username} has signed up"

@email_notify
def place_order(item):
    return f"{item} ordered"

signup("Pushpa")
place_order("Shoes")
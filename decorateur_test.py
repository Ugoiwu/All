user_name = "Jean"

def check_user(username):
    def decorator(func):
        def wrapper():
            if username == user_name:
                return func()
            else:
                return print("Utilisateur inconnu")
        return wrapper
    return decorator

@check_user("Pierre")
def profile():
    print("Le profile")

profile()
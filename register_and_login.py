from User import User, get_all_users


def login():
    all_users = get_all_users()
    k = 0
    username = input("enter your username:")
    password = input("enter your password:")
    for user in all_users:
        if user['username'] == username and user['password'] == password:
            print("you logged in successfully :)")
            return user['id']
        else:
            k += 1
    if k == len(all_users):
        print("username or password incorrect")
        return 0


def register():
    name = input("enter your firstname: ")
    lastname = input("enter your lastname: ")
    username = input("enter username: ")
    password = input("enter password: ")
    User_obj = User(name, lastname, username, password)
    User_obj.get_into_json()
    return True


def is_admin(userid):
    all_users = get_all_users()
    k = 0
    for user in all_users:
        if user['id'] == userid:
            if user['role'] == 'admin':
                return True
            else:
                k += 1
    if k == len(all_users):
        return False


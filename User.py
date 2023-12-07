import json
from json import JSONDecodeError


def get_all_users():
    try:
        with open("users.json") as f:
            all_users: list = json.load(f)
            f.close()
        return all_users
    except (JSONDecodeError, FileNotFoundError):
        with open("users.json", "w") as f:
            json.dump([], f)
            f.close()
        with open("users.json") as f:
            all_users: list = json.load(f)
            f.close()
        return all_users


class User:
    def __init__(self, name, lastname, username, password):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.password = password

    def get_into_json(self):
        user: dict = {
            "id": 1 if len(get_all_users()) == 1 else len(get_all_users()) + 1,
            "name": self.name,
            "lastname": self.lastname,
            "username": self.username,
            "password": self.password,
            "role": "user"
        }
        if not self.check_registered():
            try:
                with open("users.json") as f:
                    all_users: list = json.load(f)
                    f.close()
                all_users.append(user)
                with open("users.json", "w") as f:
                    json.dump(all_users, f, indent=4)
                    f.close()
                print('registered successfully :)')
            except (JSONDecodeError, FileNotFoundError):
                with open("users.json", "w") as f:
                    json.dump([], f, indent=4)
                    f.close()
                with open("users.json") as f:
                    all_users: list = json.load(f)
                    f.close()
                all_users.append(user)
                with open("users.json", "w") as f:
                    json.dump(all_users, f, indent=4)
                    f.close()
                print('registered successfully :)')
        else:
            print("password or username registered")

    def check_registered(self):
        all_users = get_all_users()
        for user in all_users:
            if user["username"] == self.username or user["password"] == self.password:
                return True
            else:
                return False

    def __str__(self):
        print("welcome to netflix project\nin this project you can watch movies")

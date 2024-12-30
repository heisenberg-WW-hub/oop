import json
import os

class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump({}, file)

    def register_user(self, username, password):
        with open(self.filename, "r") as file:
            users = json.load(file)
        if username in users:
            return False  # Tên đăng nhập đã tồn tại
        users[username] = password
        with open(self.filename, "w") as file:
            json.dump(users, file)
        return True

    def login_user(self, username, password):
        with open(self.filename, "r") as file:
            users = json.load(file)
        return users.get(username) == password

<<<<<<< HEAD
from CommonLayer.Model.response import Response
from DataAccessLayer.user_data_access import UserDataAccess
import hashlib
import sqlite3


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        # Invalid
        if len(username) < 3 or len(password) < 6:
            return Response(False, None, "Invalid username or password.")

        # Hash password
        password_hash = hashlib.md5(password.encode()).hexdigest()
        # Data access
        user = self.user_data_access.get_user(username, password_hash)

        if user:
            match user.status:
                case 0:
                    return Response(False, None, "You account is deactived.")
                case 1:
                    return Response(True, user, None)
                case 2:
                    return Response(False, None, "Pending.")
        else:
            return Response(False, None, "Invalid username or password(NotFound).")

    def register(self, firstname, lastname, username, password):
        if len(firstname) < 3:
            return Response(False, None, "Invalid First Name.")

        if len(lastname) < 3:
            return Response(False, None, "Invalid Last Name.")

        if len(username) < 3:
            return Response(False, None, "Invalid username.")

        if len(password) < 6:
            return Response(False, None, "Invalid password.")

        # Hash password
        password_hash = hashlib.md5(password.encode()).hexdigest()

        # Save to database
        try:
            self.user_data_access.insert_user(firstname, lastname, username, password_hash, 2, 2)
        except sqlite3.IntegrityError as error:
            # if "username" in error.args[0]:
            return Response(False, None, "Username exist.")
        else:
            return Response(True, None, "Register successfully.")

    def get_user_management_list(self, current_user):
        if current_user.role_id == 1:
            user_list = self.user_data_access.get_user_list()
            return Response(True, user_list, None)
        else:
            return Response(False, None, "Access denied.")

    def active_user(self, id_list):
        for id in id_list:
            self.user_data_access.update_status(id, 1)
=======
from CommonLayer.Model.response import Response
from DataAccessLayer.user_data_access import UserDataAccess
import hashlib
import sqlite3


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        # Invalid
        if len(username) < 3 or len(password) < 6:
            return Response(False, None, "Invalid username or password.")

        # Hash password
        password_hash = hashlib.md5(password.encode()).hexdigest()
        # Data access
        user = self.user_data_access.get_user(username, password_hash)

        if user:
            match user.status:
                case 0:
                    return Response(False, None, "You account is deactived.")
                case 1:
                    return Response(True, user, None)
                case 2:
                    return Response(False, None, "Pending.")
        else:
            return Response(False, None, "Invalid username or password(NotFound).")

    def register(self, firstname, lastname, username, password):
        if len(firstname) < 3:
            return Response(False, None, "Invalid First Name.")

        if len(lastname) < 3:
            return Response(False, None, "Invalid Last Name.")

        if len(username) < 3:
            return Response(False, None, "Invalid username.")

        if len(password) < 6:
            return Response(False, None, "Invalid password.")

        # Hash password
        password_hash = hashlib.md5(password.encode()).hexdigest()

        # Save to database
        try:
            self.user_data_access.insert_user(firstname, lastname, username, password_hash, 2, 2)
        except sqlite3.IntegrityError as error:
            # if "username" in error.args[0]:
            return Response(False, None, "Username exist.")
        else:
            return Response(True, None, "Register successfully.")

    def get_user_management_list(self, current_user):
        if current_user.role_id == 1:
            user_list = self.user_data_access.get_user_list()
            return Response(True, user_list, None)
        else:
            return Response(False, None, "Access denied.")

    def active_user(self, id_list):
        for id in id_list:
            self.user_data_access.update_status(id, 1)
>>>>>>> f5d80c2 (test)

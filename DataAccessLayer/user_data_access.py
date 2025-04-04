<<<<<<< HEAD
import sqlite3
from . import sqlite_database_name
from CommonLayer.Entities.user import User


class UserDataAccess:
    def get_user(self, username, password):
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   status,
                   role_id
            FROM   User
            Where  username = '{username}'
            AND    password = '{password}'""")

            data = cursor.fetchone()

            if data:
                return User(data[0], data[1], data[2], data[3], None, data[4], data[5])

    def insert_user(self, firstname, lastname, username, password, status, role_id):
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            INSERT INTO User (
                     first_name,
                     last_name,
                     username,
                     password,
                     status,
                     role_id
                 )
                 VALUES (
                     '{firstname}',
                     '{lastname}',
                     '{username}',
                     '{password}',
                     {status},
                     {role_id}
                 );""")
            connection.commit()

    def get_user_list(self):
        user_list = []
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   status,
                   role_id
            FROM   User
            Where  role_id != 1""")
            data_list = cursor.fetchall()

            for data in data_list:
                user = User(data[0], data[1], data[2], data[3], None, data[4], data[5])
                user_list.append(user)

        return user_list

    def update_status(self, user_id, new_status):
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            UPDATE User
            SET status = {new_status}       
            WHERE id   = {user_id} """)

            connection.commit()
=======
import sqlite3
from . import sqlite_database_name
from CommonLayer.Entities.user import User


class UserDataAccess:
    def get_user(self, username, password):
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   status,
                   role_id
            FROM   User
            Where  username = '{username}'
            AND    password = '{password}'""")

            data = cursor.fetchone()

            if data:
                return User(data[0], data[1], data[2], data[3], None, data[4], data[5])

    def insert_user(self, firstname, lastname, username, password, status, role_id):
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            INSERT INTO User (
                     first_name,
                     last_name,
                     username,
                     password,
                     status,
                     role_id
                 )
                 VALUES (
                     '{firstname}',
                     '{lastname}',
                     '{username}',
                     '{password}',
                     {status},
                     {role_id}
                 );""")
            connection.commit()

    def get_user_list(self):
        user_list = []
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   status,
                   role_id
            FROM   User
            Where  role_id != 1""")
            data_list = cursor.fetchall()

            for data in data_list:
                user = User(data[0], data[1], data[2], data[3], None, data[4], data[5])
                user_list.append(user)

        return user_list

    def update_status(self, user_id, new_status):
        with sqlite3.connect(sqlite_database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            UPDATE User
            SET status = {new_status}       
            WHERE id   = {user_id} """)

            connection.commit()
>>>>>>> f5d80c2 (test)

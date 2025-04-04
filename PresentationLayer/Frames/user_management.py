<<<<<<< HEAD
from tkinter import Frame, Label, Entry, Button, messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
from tkinter.ttk import Treeview


class UserManagementFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.user_business_logic = UserBusinessLogic()
        self.main_view = main_view

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header = Label(self, text="User Management Page")
        self.header.grid(row=0, column=0, columnspan=4, pady=10)

        self.search_entry = Entry(self)
        self.search_entry.grid(row=1, column=0, columnspan=3, pady=(0, 10), padx=10, sticky="ew")

        self.search_button = Button(self, text="Search")
        self.search_button.grid(row=1, column=3, pady=(0, 10), padx=(0, 10))

        self.active_button = Button(self, text="Active", command=self.active_user)
        self.active_button.grid(row=2, column=0, pady=(0, 10), padx=10)

        self.deactive_button = Button(self, text="Deative")
        self.deactive_button.grid(row=2, column=1, pady=(0, 10), padx=10)

        self.pending_button = Button(self, text="Pending")
        self.pending_button.grid(row=2, column=2, pady=(0, 10), padx=10)

        self.change_role_button = Button(self, text="Change Role")
        self.change_role_button.grid(row=2, column=3, pady=(0, 10), padx=10)

        self.user_treeview = Treeview(self, columns=("firstname", "lastname", "username", "status", "role"))
        self.user_treeview.grid(row=3, column=0, columnspan=4, pady=(0, 10), padx=10, sticky="nsew")

        self.user_treeview.heading("#0", text="NO")
        self.user_treeview.heading("firstname", text="First Name")
        self.user_treeview.heading("lastname", text="Last Name")
        self.user_treeview.heading("username", text="Username")
        self.user_treeview.heading("status", text="Status")
        self.user_treeview.heading("role", text="Role")

        self.user_treeview.column("#0", width=70)

        self.row_list = []
        self.current_user=None

    def set_current_user(self, user):
        self.current_user=user
        response = self.user_business_logic.get_user_management_list(user)
        if response.success:
            user_list = response.data
            self.load_data_treeview(user_list)
        else:
            messagebox.showerror(title="Error", message=response.message)
            self.main_view.switch_frame("login")

    def load_data_treeview(self, user_list):
        for row in self.row_list:
            self.user_treeview.delete(row)
        self.row_list.clear()

        row_number = 1
        for user in user_list:
            row = self.user_treeview.insert("", "end", iid=user.id, text=str(row_number), values=(user.first_name,
                                                                                                  user.last_name,
                                                                                                  user.username,
                                                                                                  user.get_status(),
                                                                                                  user.get_role()))
            self.row_list.append(row)
            row_number += 1

    def active_user(self):
        id_list = self.user_treeview.selection()
        self.user_business_logic.active_user(id_list)

        response = self.user_business_logic.get_user_management_list(self.current_user)
        if response.success:
            user_list = response.data
            self.load_data_treeview(user_list)
        else:
            messagebox.showerror(title="Error", message=response.message)
=======
from tkinter import Frame, Label, Entry, Button, messagebox
from BusinessLogicLayer.user_business_logic import UserBusinessLogic
from tkinter.ttk import Treeview


class UserManagementFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.user_business_logic = UserBusinessLogic()
        self.main_view = main_view

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header = Label(self, text="User Management Page")
        self.header.grid(row=0, column=0, columnspan=4, pady=10)

        self.search_entry = Entry(self)
        self.search_entry.grid(row=1, column=0, columnspan=3, pady=(0, 10), padx=10, sticky="ew")

        self.search_button = Button(self, text="Search")
        self.search_button.grid(row=1, column=3, pady=(0, 10), padx=(0, 10))

        self.active_button = Button(self, text="Active", command=self.active_user)
        self.active_button.grid(row=2, column=0, pady=(0, 10), padx=10)

        self.deactive_button = Button(self, text="Deative")
        self.deactive_button.grid(row=2, column=1, pady=(0, 10), padx=10)

        self.pending_button = Button(self, text="Pending")
        self.pending_button.grid(row=2, column=2, pady=(0, 10), padx=10)

        self.change_role_button = Button(self, text="Change Role")
        self.change_role_button.grid(row=2, column=3, pady=(0, 10), padx=10)

        self.user_treeview = Treeview(self, columns=("firstname", "lastname", "username", "status", "role"))
        self.user_treeview.grid(row=3, column=0, columnspan=4, pady=(0, 10), padx=10, sticky="nsew")

        self.user_treeview.heading("#0", text="NO")
        self.user_treeview.heading("firstname", text="First Name")
        self.user_treeview.heading("lastname", text="Last Name")
        self.user_treeview.heading("username", text="Username")
        self.user_treeview.heading("status", text="Status")
        self.user_treeview.heading("role", text="Role")

        self.user_treeview.column("#0", width=70)

        self.row_list = []
        self.current_user=None

    def set_current_user(self, user):
        self.current_user=user
        response = self.user_business_logic.get_user_management_list(user)
        if response.success:
            user_list = response.data
            self.load_data_treeview(user_list)
        else:
            messagebox.showerror(title="Error", message=response.message)
            self.main_view.switch_frame("login")

    def load_data_treeview(self, user_list):
        for row in self.row_list:
            self.user_treeview.delete(row)
        self.row_list.clear()

        row_number = 1
        for user in user_list:
            row = self.user_treeview.insert("", "end", iid=user.id, text=str(row_number), values=(user.first_name,
                                                                                                  user.last_name,
                                                                                                  user.username,
                                                                                                  user.get_status(),
                                                                                                  user.get_role()))
            self.row_list.append(row)
            row_number += 1

    def active_user(self):
        id_list = self.user_treeview.selection()
        self.user_business_logic.active_user(id_list)

        response = self.user_business_logic.get_user_management_list(self.current_user)
        if response.success:
            user_list = response.data
            self.load_data_treeview(user_list)
        else:
            messagebox.showerror(title="Error", message=response.message)
>>>>>>> f5d80c2 (test)
            self.main_view.switch_frame("login")
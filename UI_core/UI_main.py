import tkinter as tk
from tkinter import messagebox
from user.user_data import UserManager

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.root.geometry("400x300")

        self.user_manager = UserManager()

        # Hiển thị giao diện đăng nhập ban đầu
        self.show_login_screen()

    def show_login_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Đăng nhập", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Tên đăng nhập:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Mật khẩu:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Đăng nhập", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Đăng ký", command=self.show_register_screen).pack()

    def show_register_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Đăng ký", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Tên đăng nhập:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Mật khẩu:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Đăng ký", command=self.register).pack(pady=10)
        tk.Button(self.root, text="Quay lại", command=self.show_login_screen).pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_manager.login_user(username, password):
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
            self.show_main_screen()
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_manager.register_user(username, password):
            messagebox.showinfo("Thành công", "Đăng ký thành công!")
            self.show_login_screen()
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại.")

    def show_main_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Chào mừng đến với Chess Game!", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Bắt đầu trò chơi", command=self.start_game).pack(pady=10)
        tk.Button(self.root, text="Thoát", command=self.root.quit).pack()

    def start_game(self):
        # Thêm logic để bắt đầu trò chơi
        messagebox.showinfo("Thông báo", "Trò chơi đang được phát triển!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()

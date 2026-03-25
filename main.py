import customtkinter as ctk
import design as d
from login import LoginFrame
from app import MainApp


class AxionRoot(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Ejercicios Python")
        self.geometry("900x720")
        self.minsize(800, 600)

        d.setup_theme()
        self.configure(fg_color=d.BG_DARK)

        self.container = ctk.CTkFrame(self, fg_color=d.BG_DARK, corner_radius=0)
        self.container.pack(fill="both", expand=True)

        self._show_login()

    def _show_login(self):
        self._clear()
        self.login = LoginFrame(self.container, on_success=self._show_app)
        self.login.pack(fill="both", expand=True)

    def _show_app(self):
        self._clear()
        self.menu = MainApp(self.container, self)
        self.menu.pack(fill="both", expand=True)

    def _clear(self):
        for w in self.container.winfo_children():
            w.destroy()


if __name__ == "__main__":
    app = AxionRoot()
    app.mainloop()

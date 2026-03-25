import customtkinter as ctk
import design as d


class LoginFrame(ctk.CTkFrame):

    VALID_USER = "user"
    VALID_PASS = "croissant"

    def __init__(self, parent, on_success):
        super().__init__(parent, fg_color=d.BG_DARK, corner_radius=0)
        self.on_success = on_success
        self._build_ui()

    def _build_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        card = d.create_card_frame(self)
        card.grid(row=1, column=0, padx=40, pady=40)

        accent_bar = ctk.CTkFrame(
            card, fg_color=d.ACCENT_YELLOW,
            height=4, corner_radius=0
        )
        accent_bar.pack(fill="x", padx=d.PAD_CARD, pady=(d.PAD_CARD, 0))

        title = ctk.CTkLabel(
            card, text="LOGIN",
            font=("Georgia", 36, "bold"),
            text_color=d.TEXT_PRIMARY
        )
        title.pack(padx=d.PAD_CARD, pady=(16, 24))

        sep = ctk.CTkFrame(
            card, fg_color=d.TEXT_PRIMARY,
            height=2, corner_radius=0
        )
        sep.pack(fill="x", padx=d.PAD_CARD, pady=(0, 20))

        d.create_mono_label(card, "[USUARIO]").pack(
            anchor="w", padx=d.PAD_CARD, pady=(0, 4)
        )
        self.entry_user = d.create_entry(card, placeholder="Ingrese usuario")
        self.entry_user.pack(fill="x", padx=d.PAD_CARD, pady=(0, 16))

        d.create_mono_label(card, "[CONTRASEÑA]").pack(
            anchor="w", padx=d.PAD_CARD, pady=(0, 4)
        )
        self.entry_pass = d.create_entry(card, placeholder="Ingrese contraseña")
        self.entry_pass.configure(show="●")
        self.entry_pass.pack(fill="x", padx=d.PAD_CARD, pady=(0, 24))

        self.error_label = ctk.CTkLabel(
            card, text="",
            font=d.FONT_MONO_SM,
            text_color=d.ACCENT_PINK
        )
        self.error_label.pack(padx=d.PAD_CARD, pady=(0, 8))

        btn = d.create_accent_button(card, "→ INICIAR SESIÓN", self._attempt_login)
        btn.pack(fill="x", padx=d.PAD_CARD, pady=(0, d.PAD_CARD))

        self.entry_pass.bind("<Return>", lambda e: self._attempt_login())
        self.entry_user.bind("<Return>", lambda e: self.entry_pass.focus())

    def _attempt_login(self):
        user = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()

        if not user or not password:
            self.error_label.configure(text="CAMPOS VACÍOS")
            return

        if user == self.VALID_USER and password == self.VALID_PASS:
            self.error_label.configure(text="")
            self.on_success()
        else:
            self.error_label.configure(text="CREDENCIALES INVÁLIDAS")
            self.entry_pass.delete(0, "end")
            self.entry_pass.focus()

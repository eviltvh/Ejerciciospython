import customtkinter as ctk
import design as d
from exercises import ALL_EXERCISES


class MainApp(ctk.CTkFrame):

    def __init__(self, parent, root_window):
        super().__init__(parent, fg_color=d.BG_DARK, corner_radius=0)
        self.parent = parent
        self.root_window = root_window
        self.current_exercise = None
        self._build_menu()

    def _build_menu(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=32, pady=(32, 0))

        ctk.CTkLabel(
            header, text="AXION",
            font=("Georgia", 42, "bold"),
            text_color=d.TEXT_ON_DARK
        ).pack(anchor="w")

        sub_frame = ctk.CTkFrame(header, fg_color="transparent")
        sub_frame.pack(anchor="w", pady=(4, 0))

        accent = ctk.CTkFrame(
            sub_frame, fg_color=d.ACCENT_YELLOW,
            width=4, height=20, corner_radius=0
        )
        accent.pack(side="left", padx=(0, 8))

        ctk.CTkLabel(
            sub_frame, text="[EJERCICIOS PYTHON] → SELECCIONE UN MÓDULO",
            font=d.FONT_MONO_SM, text_color=d.TEXT_MUTED
        ).pack(side="left")

        sep = ctk.CTkFrame(
            self, fg_color=d.TEXT_ON_DARK,
            height=2, corner_radius=0
        )
        sep.grid(row=1, column=0, sticky="ew", padx=32, pady=(20, 0))

        grid_frame = ctk.CTkScrollableFrame(
            self, fg_color=d.BG_DARK, corner_radius=0
        )
        grid_frame.grid(row=2, column=0, sticky="nsew", padx=24, pady=24)
        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)

        button_data = [
            ("01", "Aumento\nSueldos", "NÓMINA"),
            ("02", "Parque\nDiversiones", "COBROS"),
            ("03", "Descuentos\npor Mes", "TIENDA"),
            ("04", "Validación\n< 10", "VALIDACIÓN"),
            ("05", "Validación\nRango 0-20", "VALIDACIÓN"),
            ("06", "Registro\nIntentos", "REGISTRO"),
            ("07", "Suma N\nEnteros", "CÁLCULO"),
            ("08", "Suma\nAcumulativa", "ACUMULADOR"),
            ("09", "Suma hasta\n> 100", "LÍMITE"),
            ("10", "Pago\nTrabajadores", "NÓMINA"),
        ]

        for i, (num, title, tag) in enumerate(button_data):
            row = i // 2
            col = i % 2

            btn_frame = self._create_menu_button(
                grid_frame, num, title, tag,
                lambda idx=i: self._open_exercise(idx)
            )
            btn_frame.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

    def _create_menu_button(self, parent, number, title, tag, command):
        frame = ctk.CTkFrame(
            parent,
            fg_color=d.BG_CARD,
            corner_radius=d.CORNER_RADIUS,
            border_width=d.BORDER_THICK,
            border_color=d.TEXT_PRIMARY,
            cursor="hand2"
        )

        ctk.CTkLabel(
            frame, text=number,
            font=("Georgia", 28, "bold"),
            text_color=d.TEXT_PRIMARY
        ).pack(anchor="w", padx=16, pady=(16, 4))

        ctk.CTkLabel(
            frame, text=title,
            font=d.FONT_BODY_BOLD,
            text_color=d.TEXT_PRIMARY,
            justify="left", anchor="w"
        ).pack(anchor="w", padx=16, pady=(0, 8))

        tag_frame = ctk.CTkFrame(frame, fg_color="transparent")
        tag_frame.pack(anchor="w", padx=16, pady=(0, 16))

        ctk.CTkFrame(
            tag_frame, fg_color=d.ACCENT_YELLOW,
            width=3, height=14, corner_radius=0
        ).pack(side="left", padx=(0, 6))

        ctk.CTkLabel(
            tag_frame, text=f"[{tag}]",
            font=("Courier", 9, "bold"),
            text_color=d.TEXT_MUTED
        ).pack(side="left")

        frame.bind("<Button-1>", lambda e: command())
        for child in frame.winfo_children():
            child.bind("<Button-1>", lambda e, c=command: c())
            for grandchild in child.winfo_children():
                grandchild.bind("<Button-1>", lambda e, c=command: c())

        def on_enter(e):
            frame.configure(border_color=d.ACCENT_YELLOW)
        def on_leave(e):
            frame.configure(border_color=d.TEXT_PRIMARY)

        frame.bind("<Enter>", on_enter)
        frame.bind("<Leave>", on_leave)

        return frame

    def _open_exercise(self, index):
        ExClass = ALL_EXERCISES[index]
        self.pack_forget()

        self.current_exercise = ExClass(self.parent, on_back=self._back_to_menu)
        self.current_exercise.pack(fill="both", expand=True)

    def _back_to_menu(self):
        if self.current_exercise:
            self.current_exercise.destroy()
            self.current_exercise = None
        self.pack(fill="both", expand=True)

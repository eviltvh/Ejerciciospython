import customtkinter as ctk
import design as d


class BaseExercise(ctk.CTkFrame):

    TITLE = "Ejercicio"
    SUBTITLE = "[MÓDULO]"

    def __init__(self, parent, on_back):
        super().__init__(parent, fg_color=d.BG_DARK, corner_radius=0)
        self.on_back = on_back
        self.history = []
        self._result_widgets = []
        self._build_layout()
        self.build_form()

    def _build_layout(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, fg_color=d.BG_DARK, corner_radius=0)
        header.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 0))
        header.grid_columnconfigure(1, weight=1)

        back_btn = d.create_ghost_button(header, "← VOLVER", self.on_back)
        back_btn.grid(row=0, column=0, sticky="w")

        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.grid(row=1, column=0, columnspan=2, sticky="w", pady=(12, 0))

        accent = ctk.CTkFrame(
            title_frame, fg_color=d.ACCENT_YELLOW,
            width=4, height=32, corner_radius=0
        )
        accent.pack(side="left", padx=(0, 12))

        ctk.CTkLabel(
            title_frame, text=self.TITLE,
            font=d.FONT_H2, text_color=d.TEXT_ON_DARK
        ).pack(side="left")

        ctk.CTkLabel(
            header, text=self.SUBTITLE,
            font=d.FONT_MONO_SM, text_color=d.TEXT_MUTED
        ).grid(row=2, column=0, sticky="w", pady=(4, 0))

        sep = ctk.CTkFrame(
            header, fg_color=d.TEXT_ON_DARK,
            height=2, corner_radius=0
        )
        sep.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(16, 0))

        self.content = ctk.CTkScrollableFrame(
            self, fg_color=d.BG_DARK, corner_radius=0
        )
        self.content.grid(row=1, column=0, sticky="nsew", padx=24, pady=(16, 24))
        self.content.grid_columnconfigure(0, weight=1)

    def build_form(self):
        pass

    def add_field(self, label_text, placeholder="", parent=None):
        container = parent or self.content
        d.create_mono_label(
            container, f"[{label_text}]",
            text_color=d.TEXT_ON_DARK if parent is None else d.TEXT_PRIMARY
        ).pack(anchor="w", pady=(d.PAD_ELEMENT, 2))

        entry = d.create_entry(container, placeholder=placeholder)
        entry.pack(fill="x", pady=(0, 4))
        return entry

    def add_action_button(self, text, command, parent=None):
        container = parent or self.content
        btn = d.create_accent_button(container, f"→ {text}", command)
        btn.pack(fill="x", pady=(d.PAD_SECTION, d.PAD_ELEMENT))
        return btn

    def add_reset_button(self, parent=None):
        container = parent or self.content
        btn = d.create_secondary_button(
            container, "↻ NUEVO REGISTRO", self._reset
        )
        btn.pack(fill="x", pady=(4, d.PAD_ELEMENT))
        self._result_widgets.append(btn)
        return btn

    def show_result(self, text, success=True):
        self._clear_results()

        banner = d.create_result_banner(self.content, text, success)
        banner.pack(fill="x", pady=(d.PAD_ELEMENT, 4))
        self._result_widgets.append(banner)

        self.add_reset_button()

    def show_history(self, title="[HISTORIAL]", items=None):
        items = items or self.history
        if not items:
            return

        frame = ctk.CTkFrame(
            self.content,
            fg_color="#1a1a1a",
            corner_radius=d.CORNER_RADIUS,
            border_width=1,
            border_color=d.TEXT_MUTED
        )
        frame.pack(fill="x", pady=(4, d.PAD_ELEMENT))
        self._result_widgets.append(frame)

        ctk.CTkLabel(
            frame, text=title,
            font=d.FONT_MONO_SM, text_color=d.ACCENT_YELLOW
        ).pack(anchor="w", padx=12, pady=(8, 4))

        for item in items:
            ctk.CTkLabel(
                frame, text=f"  → {item}",
                font=d.FONT_MONO_SM, text_color=d.TEXT_ON_DARK,
                anchor="w"
            ).pack(anchor="w", padx=12, pady=1)

        ctk.CTkFrame(frame, fg_color="transparent", height=8).pack()

    def _clear_results(self):
        for w in self._result_widgets:
            try:
                w.destroy()
            except Exception:
                pass
        self._result_widgets.clear()

    def _reset(self):
        self._clear_results()
        for widget in self.content.winfo_children():
            if isinstance(widget, ctk.CTkEntry):
                widget.configure(state="normal")
                widget.delete(0, "end")

    def _get_entries(self):
        entries = []
        for widget in self.content.winfo_children():
            if isinstance(widget, ctk.CTkEntry):
                entries.append(widget)
        return entries

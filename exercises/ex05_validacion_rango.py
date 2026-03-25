import customtkinter as ctk
from exercises.base import BaseExercise
from utils import validate_integer
import design as d


class Ex05ValidacionRango(BaseExercise):
    TITLE = "Validación Rango (0-20)"
    SUBTITLE = "[MÓDULO 05 → VALIDACIÓN]"

    def __init__(self, *args, **kwargs):
        self.attempts = 0
        super().__init__(*args, **kwargs)

    def build_form(self):
        self.entry_num = self.add_field("NÚMERO (0-20)", "Ingrese número entre 0 y 20")
        self.add_action_button("VALIDAR", self._validate)

        self.feedback = ctk.CTkLabel(
            self.content, text="",
            font=d.FONT_MONO_SM,
            text_color=d.TEXT_ON_DARK
        )
        self.feedback.pack(anchor="w", pady=(0, 8))

    def _validate(self):
        try:
            val = validate_integer(self.entry_num.get(), "Número")
            self.attempts += 1

            if _validate_in_range(val, 0, 20):
                self.show_result(
                    f"Número válido: {val}\n"
                    f"Intentos realizados: {self.attempts}"
                )
                self.feedback.configure(text="")
            else:
                self.feedback.configure(
                    text=f"✗ {val} fuera de rango (0-20) — Intento #{self.attempts}",
                    text_color=d.ACCENT_PINK
                )
                self.entry_num.delete(0, "end")
                self.entry_num.focus()

        except ValueError as e:
            self.feedback.configure(
                text=f"✗ {str(e)}",
                text_color=d.ACCENT_PINK
            )
            self.entry_num.delete(0, "end")

    def _reset(self):
        super()._reset()
        self.attempts = 0
        self.feedback.configure(text="")


def _validate_in_range(value, min_val, max_val):
    return min_val <= value <= max_val

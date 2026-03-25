import customtkinter as ctk
from exercises.base import BaseExercise
from utils import validate_integer
import design as d


class Ex06RegistroIntentos(BaseExercise):
    TITLE = "Registro de Intentos"
    SUBTITLE = "[MÓDULO 06 → VALIDACIÓN + REGISTRO]"

    def __init__(self, *args, **kwargs):
        self.all_attempts = []
        self.correct_value = None
        super().__init__(*args, **kwargs)

    def build_form(self):
        self.entry_num = self.add_field("NÚMERO (0-20)", "Ingrese número entre 0 y 20")
        self.add_action_button("REGISTRAR INTENTO", self._check)

        self.feedback = ctk.CTkLabel(
            self.content, text="",
            font=d.FONT_MONO_SM,
            text_color=d.TEXT_ON_DARK,
            wraplength=500,
            justify="left"
        )
        self.feedback.pack(anchor="w", pady=(0, 8))

    def _check(self):
        try:
            val = validate_integer(self.entry_num.get(), "Número")
            self.all_attempts.append(val)

            if _validate_in_range(val, 0, 20):
                self.correct_value = val
                incorrect = _count_incorrect(self.all_attempts, 0, 20)
                attempts_str = ", ".join(map(str, self.all_attempts))

                self.show_result(
                    f"Número correcto: {val}\n"
                    f"Total intentos: {len(self.all_attempts)}\n"
                    f"Intentos incorrectos: {incorrect}\n"
                    f"Historial: [{attempts_str}]"
                )
                self.feedback.configure(text="")
            else:
                attempts_str = ", ".join(map(str, self.all_attempts))
                self.feedback.configure(
                    text=f"✗ {val} fuera de rango — Historial: [{attempts_str}]",
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
        self.all_attempts = []
        self.correct_value = None
        self.feedback.configure(text="")


def _validate_in_range(value, min_val, max_val):
    return min_val <= value <= max_val

def _count_incorrect(attempts, min_val, max_val):
    return len([x for x in attempts if x < min_val or x > max_val])

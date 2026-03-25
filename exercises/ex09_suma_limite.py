import customtkinter as ctk
from exercises.base import BaseExercise
from utils import validate_integer
import design as d


class Ex09SumaLimite(BaseExercise):
    TITLE = "Suma hasta > 100"
    SUBTITLE = "[MÓDULO 09 → LÍMITE]"

    def __init__(self, *args, **kwargs):
        self.num_list = []
        self.current_sum = 0
        super().__init__(*args, **kwargs)

    def build_form(self):
        self.entry_num = self.add_field("NÚMERO ENTERO", "Ingrese un número")
        self.add_action_button("SUMAR", self._add_number)

        self.feedback = ctk.CTkLabel(
            self.content, text="Suma parcial: 0",
            font=d.FONT_MONO, text_color=d.ACCENT_YELLOW
        )
        self.feedback.pack(anchor="w", pady=(0, 8))

        self.list_label = ctk.CTkLabel(
            self.content, text="Números: [ ]",
            font=d.FONT_MONO_SM, text_color=d.TEXT_MUTED,
            wraplength=500, justify="left"
        )
        self.list_label.pack(anchor="w", pady=(0, 8))

    def _add_number(self):
        try:
            val = validate_integer(self.entry_num.get(), "Número")

            self.num_list.append(val)
            self.current_sum = _calculate_sum(self.num_list)
            nums_str = ", ".join(map(str, self.num_list))

            if _exceeds_limit(self.current_sum, 100):
                self.show_result(
                    f"¡Límite superado!\n"
                    f"Lista: [{nums_str}]\n"
                    f"Cantidad: {len(self.num_list)}\n"
                    f"Suma final: {self.current_sum}"
                )
                self.feedback.configure(text="")
                self.list_label.configure(text="")
            else:
                self.feedback.configure(
                    text=f"Suma parcial: {self.current_sum}"
                )
                self.list_label.configure(
                    text=f"Números: [{nums_str}]"
                )
                self.entry_num.delete(0, "end")
                self.entry_num.focus()

        except ValueError as e:
            self.show_result(str(e), success=False)

    def _reset(self):
        super()._reset()
        self.num_list = []
        self.current_sum = 0
        if hasattr(self, 'feedback'):
            self.feedback.configure(text="Suma parcial: 0")
        if hasattr(self, 'list_label'):
            self.list_label.configure(text="Números: [ ]")


def _calculate_sum(num_list):
    return sum(num_list)

def _exceeds_limit(current_sum, limit):
    return current_sum > limit

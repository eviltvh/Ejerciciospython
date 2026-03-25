import customtkinter as ctk
from exercises.base import BaseExercise
from utils import validate_integer
import design as d


class Ex08SumaAcumulativa(BaseExercise):
    TITLE = "Suma Acumulativa"
    SUBTITLE = "[MÓDULO 08 → ACUMULADOR]"

    def __init__(self, *args, **kwargs):
        self.num_list = []
        self.running_sum = 0
        super().__init__(*args, **kwargs)

    def build_form(self):
        self.entry_num = self.add_field(
            "NÚMERO (0 PARA TERMINAR)",
            "Ingrese un entero, 0 para finalizar"
        )
        self.add_action_button("AGREGAR", self._add_number)

        self.feedback = ctk.CTkLabel(
            self.content, text="Suma actual: 0",
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

            if val == 0:
                total = _calculate_total(self.num_list)
                count = _count_numbers(self.num_list)
                nums_str = ", ".join(map(str, self.num_list))

                self.show_result(
                    f"Lista: [{nums_str}]\n"
                    f"Cantidad: {count}\n"
                    f"Suma total: {total}"
                )
                self.feedback.configure(text="")
                self.list_label.configure(text="")
            else:
                self.num_list.append(val)
                self.running_sum = _calculate_total(self.num_list)
                nums_str = ", ".join(map(str, self.num_list))

                self.feedback.configure(
                    text=f"Suma actual: {self.running_sum}"
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
        self.running_sum = 0
        if hasattr(self, 'feedback'):
            self.feedback.configure(text="Suma actual: 0")
        if hasattr(self, 'list_label'):
            self.list_label.configure(text="Números: [ ]")


def _calculate_total(num_list):
    return sum(num_list)

def _count_numbers(num_list):
    return len(num_list)

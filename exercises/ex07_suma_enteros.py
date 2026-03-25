from exercises.base import BaseExercise
from utils import validate_integer, validate_positive


class Ex07SumaEnteros(BaseExercise):
    TITLE = "Suma N Enteros"
    SUBTITLE = "[MÓDULO 07 → CÁLCULO]"

    def build_form(self):
        self.entry_n = self.add_field("VALOR DE N", "Ingrese un número positivo")
        self.add_action_button("CALCULAR SUMA", self._calculate)

    def _calculate(self):
        try:
            n = validate_integer(self.entry_n.get(), "N")
            validate_positive(n, "N")

            total = _sum_first_n(n)
            sequence = _build_sequence(n)

            self.show_result(
                f"Secuencia: {sequence}\n"
                f"Resultado: {total}"
            )
        except ValueError as e:
            self.show_result(str(e), success=False)


def _sum_first_n(n):
    return sum(range(1, n + 1))

def _build_sequence(n):
    return " + ".join(map(str, range(1, n + 1)))

from exercises.base import BaseExercise
from utils import validate_not_empty, validate_integer, validate_positive, validate_non_negative


class Ex02Parque(BaseExercise):
    TITLE = "Parque de Diversiones"
    SUBTITLE = "[MÓDULO 02 → COBROS]"

    def __init__(self, *args, **kwargs):
        self.total_collected = 0.0
        super().__init__(*args, **kwargs)

    def build_form(self):
        self.entry_name = self.add_field("NOMBRE VISITANTE", "Ej: María")
        self.entry_age = self.add_field("EDAD", "Ej: 12")
        self.entry_games = self.add_field("CANTIDAD DE JUEGOS", "Ej: 5")
        self.add_action_button("REGISTRAR VISITA", self._calculate)

    def _calculate(self):
        try:
            name = validate_not_empty(self.entry_name.get(), "Nombre")
            age = validate_integer(self.entry_age.get(), "Edad")
            validate_non_negative(age, "Edad")
            games = validate_integer(self.entry_games.get(), "Cantidad de juegos")
            validate_positive(games, "Cantidad de juegos")

            total_raw = _calculate_total(games)
            discount = _get_discount_rate(age)
            final = _apply_discount(total_raw, discount)

            self.total_collected += final
            self.history.append(f"{name} (edad {age}): S/ {final:.2f}")

            self.show_result(
                f"{name} — Edad: {age}\n"
                f"Juegos: {games} × S/ 50 = S/ {total_raw:.2f}\n"
                f"Descuento: {int(discount*100)}%\n"
                f"Total a pagar: S/ {final:.2f}\n"
                f"─────────────────\n"
                f"Recaudado total: S/ {self.total_collected:.2f}"
            )
            self.show_history("[VISITANTES REGISTRADOS]")

        except ValueError as e:
            self.show_result(str(e), success=False)


COST_PER_GAME = 50

def _calculate_total(games):
    return games * COST_PER_GAME

def _get_discount_rate(age):
    if age < 10:
        return 0.25
    elif age <= 17:
        return 0.10
    else:
        return 0.0

def _apply_discount(total, rate):
    return total * (1 - rate)

from exercises.base import BaseExercise
from utils import validate_not_empty, validate_float, validate_positive, validate_month


class Ex03Descuentos(BaseExercise):
    TITLE = "Descuentos por Mes"
    SUBTITLE = "[MÓDULO 03 → TIENDA]"

    def __init__(self, *args, **kwargs):
        self.total_sold = 0.0
        super().__init__(*args, **kwargs)

    def build_form(self):
        self.entry_name = self.add_field("NOMBRE CLIENTE", "Ej: Carlos")
        self.entry_month = self.add_field("MES DE COMPRA", "Ej: Octubre")
        self.entry_amount = self.add_field("IMPORTE", "Ej: 1500")
        self.add_action_button("REGISTRAR COMPRA", self._calculate)

    def _calculate(self):
        try:
            name = validate_not_empty(self.entry_name.get(), "Nombre")
            month = validate_month(self.entry_month.get())
            amount = validate_float(self.entry_amount.get(), "Importe")
            validate_positive(amount, "Importe")

            discount = _get_month_discount(month)
            final = _calculate_final(amount, discount)

            self.total_sold += final
            self.history.append(
                f"{name} ({month}): S/ {amount:.2f} → S/ {final:.2f}"
            )

            self.show_result(
                f"{name} — Mes: {month.capitalize()}\n"
                f"Importe: S/ {amount:.2f}\n"
                f"Descuento: {int(discount*100)}%\n"
                f"Total final: S/ {final:.2f}\n"
                f"─────────────────\n"
                f"Vendido en sesión: S/ {self.total_sold:.2f}"
            )
            self.show_history("[COMPRAS REGISTRADAS]")

        except ValueError as e:
            self.show_result(str(e), success=False)


MONTH_DISCOUNTS = {
    "octubre": 0.15,
    "diciembre": 0.20,
    "julio": 0.10,
}

def _get_month_discount(month):
    return MONTH_DISCOUNTS.get(month, 0.0)

def _calculate_final(amount, discount):
    return amount * (1 - discount)

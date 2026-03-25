from exercises.base import BaseExercise
from utils import validate_not_empty, validate_float, validate_positive, validate_non_negative, validate_integer


class Ex10PagoTrabajadores(BaseExercise):
    TITLE = "Pago Trabajadores"
    SUBTITLE = "[MÓDULO 10 → NÓMINA COMPLETA]"

    def build_form(self):
        self.entry_name = self.add_field("NOMBRE TRABAJADOR", "Ej: Ana López")
        self.entry_h_norm = self.add_field("HORAS NORMALES", "Ej: 40")
        self.entry_p_hour = self.add_field("PAGO POR HORA", "Ej: 25")
        self.entry_h_extra = self.add_field("HORAS EXTRAS", "Ej: 5")
        self.entry_children = self.add_field("NÚMERO DE HIJOS", "Ej: 2")
        self.add_action_button("CALCULAR PAGO", self._calculate)

    def _calculate(self):
        try:
            name = validate_not_empty(self.entry_name.get(), "Nombre")
            h_norm = validate_float(self.entry_h_norm.get(), "Horas normales")
            validate_non_negative(h_norm, "Horas normales")
            p_hour = validate_float(self.entry_p_hour.get(), "Pago por hora")
            validate_positive(p_hour, "Pago por hora")
            h_extra = validate_float(self.entry_h_extra.get(), "Horas extras")
            validate_non_negative(h_extra, "Horas extras")
            children = validate_integer(self.entry_children.get(), "Número de hijos")
            validate_non_negative(children, "Número de hijos")

            pay_norm = _calc_normal_pay(h_norm, p_hour)
            pay_extra = _calc_extra_pay(h_extra, p_hour)
            bonus = _calc_bonus(children, p_hour)
            total = _calc_total(pay_norm, pay_extra, bonus)

            self.history.append(f"{name}: S/ {total:.2f}")

            self.show_result(
                f"{name}\n"
                f"Pago normal: {h_norm}h × S/ {p_hour:.2f} = S/ {pay_norm:.2f}\n"
                f"Pago extras: {h_extra}h × S/ {p_hour * 1.5:.2f} = S/ {pay_extra:.2f}\n"
                f"Bonif. hijos: {children} × S/ {p_hour * 0.5:.2f} = S/ {bonus:.2f}\n"
                f"─────────────────\n"
                f"TOTAL: S/ {total:.2f}"
            )
            self.show_history("[REPORTE DE PAGOS]")

        except ValueError as e:
            self.show_result(str(e), success=False)


def _calc_normal_pay(hours, rate):
    return hours * rate

def _calc_extra_pay(hours, rate):
    return hours * (rate * 1.5)

def _calc_bonus(children, rate):
    return children * (rate * 0.5)

def _calc_total(pay_norm, pay_extra, bonus):
    return pay_norm + pay_extra + bonus

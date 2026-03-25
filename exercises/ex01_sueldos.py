from exercises.base import BaseExercise
from utils import validate_not_empty, validate_float, validate_positive, safe_execute


class Ex01Sueldos(BaseExercise):
    TITLE = "Sistema Aumento Sueldos"
    SUBTITLE = "[MÓDULO 01 → NÓMINA]"

    def build_form(self):
        self.entry_name = self.add_field("NOMBRE TRABAJADOR", "Ej: Juan Pérez")
        self.entry_salary = self.add_field("SUELDO BÁSICO", "Ej: 5000")
        self.add_action_button("CALCULAR AUMENTO", self._calculate)

    def _calculate(self):
        try:
            name = validate_not_empty(self.entry_name.get(), "Nombre")
            salary = validate_float(self.entry_salary.get(), "Sueldo")
            validate_positive(salary, "Sueldo")

            increase = _get_increase_rate(salary)
            new_salary = _calculate_new_salary(salary, increase)

            self.history.append(f"{name}: S/ {salary:.2f} → S/ {new_salary:.2f} (+{int(increase*100)}%)")

            self.show_result(
                f"{name}\n"
                f"Sueldo anterior: S/ {salary:.2f}\n"
                f"Aumento: {int(increase*100)}%\n"
                f"Nuevo sueldo: S/ {new_salary:.2f}"
            )
            self.show_history("[HISTORIAL TRABAJADORES]")

        except ValueError as e:
            self.show_result(str(e), success=False)


def _get_increase_rate(salary):
    if salary < 4000:
        return 0.15
    elif salary <= 7000:
        return 0.10
    else:
        return 0.08


def _calculate_new_salary(salary, rate):
    return salary * (1 + rate)

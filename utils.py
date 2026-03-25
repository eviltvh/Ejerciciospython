from tkinter import messagebox


def validate_not_empty(value, field_name="Campo"):
    if not value or not value.strip():
        raise ValueError(f"{field_name} no puede estar vacío")
    return value.strip()


def validate_integer(value, field_name="Número"):
    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} debe ser un número entero")


def validate_float(value, field_name="Número"):
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} debe ser un número válido")


def validate_positive(value, field_name="Número"):
    if value <= 0:
        raise ValueError(f"{field_name} debe ser mayor a 0")
    return value


def validate_non_negative(value, field_name="Número"):
    if value < 0:
        raise ValueError(f"{field_name} no puede ser negativo")
    return value


def validate_range(value, min_val, max_val, field_name="Número"):
    if value < min_val or value > max_val:
        raise ValueError(f"{field_name} debe estar entre {min_val} y {max_val}")
    return value


def validate_month(month_str):
    valid_months = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    month = month_str.strip().lower()
    if month not in valid_months:
        raise ValueError(f"Mes inválido: '{month_str}'. Ingrese un mes válido")
    return month


def show_error(message):
    messagebox.showerror("ERROR", message)


def safe_execute(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            show_error(str(e))
        except Exception as e:
            show_error(f"Error inesperado: {str(e)}")
    return wrapper

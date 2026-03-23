import tkinter as tk
from tkinter import ttk, messagebox, font
from datetime import datetime

# ==========================================
# CONFIGURACIÓN DE DISEÑO AXION
# ==========================================
class AxionDesign:
    # Colores
    BG_COLOR = "#f3f3f3"          # Blanco roto (Fondos claros)
    TEXT_COLOR = "#1c1b1b"        # Negro principal (Textos, botones primarios)
    SECONDARY_COLOR = "#474545"   # Gris oscuro (Textos secundarios)
    ACCENT_COLOR = "#8a9b7a"      # Verde salvia (Acento decorativo)
    WHITE = "#ffffff"
    
    # Tipografía (Source Sans Pro si está disponible, sino fallback)
    FONT_FAMILY = "Source Sans Pro"
    FONT_FALLBACK = "Helvetica"
    
    # Pesos
    WEIGHT_BLACK = "bold"
    WEIGHT_BOLD = "bold"
    WEIGHT_REGULAR = "normal"
    
    # Tamaños
    SIZE_H1 = 24
    SIZE_H2 = 18
    SIZE_BODY = 12
    SIZE_LABEL = 10

    def __init__(self, root):
        self.root = root
        self._setup_fonts()
        self._setup_styles()

    def _setup_fonts(self):
        # Intentar usar Source Sans Pro
        available_fonts = font.families()
        if self.FONT_FAMILY in available_fonts:
            self.font_family = self.FONT_FAMILY
        else:
            self.font_family = self.FONT_FALLBACK
            
        self.font_h1 = (self.font_family, self.SIZE_H1, self.WEIGHT_BLACK)
        self.font_h2 = (self.font_family, self.SIZE_H2, self.WEIGHT_BOLD)
        self.font_body = (self.font_family, self.SIZE_BODY, self.WEIGHT_REGULAR)
        self.font_label = (self.font_family, self.SIZE_LABEL, self.WEIGHT_BOLD)

    def _setup_styles(self):
        self.root.configure(bg=self.BG_COLOR)
        style = ttk.Style()
        style.theme_use('clam')
        # Configuración global de colores para widgets estándar
        style.configure(".", background=self.BG_COLOR, foreground=self.TEXT_COLOR, font=self.font_body)
        style.configure("TButton", background=self.TEXT_COLOR, foreground=self.WHITE, 
                        font=self.font_body, borderwidth=0, focusthickness=0)
        style.map("TButton", background=[('active', self.SECONDARY_COLOR)])

# ==========================================
# APLICACIÓN PRINCIPAL
# ==========================================
class AxionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AXION | Ejercicios Python")
        self.geometry("900x700")
        self.minsize(800, 600)
        
        # Inicializar Diseño
        self.design = AxionDesign(self)
        
        # Contenedor Principal
        self.container = tk.Frame(self, bg=self.design.BG_COLOR)
        self.container.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Datos Globales (Listas para ejercicios)
        self.data_workers = []
        self.data_visitors = []
        self.data_purchases = []
        self.data_payments = []
        
        self.show_menu()

    def clear_frame(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # --- COMPONENTES ESTILIZADOS ---
    def create_title(self, text, level=1):
        f = self.design.font_h1 if level == 1 else self.design.font_h2
        lbl = tk.Label(self.container, text=text, font=f, bg=self.design.BG_COLOR, fg=self.design.TEXT_COLOR)
        lbl.pack(anchor="w", pady=(0, 20))
        return lbl

    def create_label(self, text):
        lbl = tk.Label(self.container, text=text, font=self.design.font_body, bg=self.design.BG_COLOR, fg=self.design.SECONDARY_COLOR)
        lbl.pack(anchor="w", pady=(5, 0))
        return lbl

    def create_entry(self):
        entry = tk.Entry(self.container, font=self.design.font_body, bg=self.design.WHITE, fg=self.design.TEXT_COLOR, 
                         relief="flat", highlightthickness=1, highlightbackground=self.design.SECONDARY_COLOR)
        entry.pack(fill="x", pady=(5, 15))
        return entry

    def create_button(self, text, command, secondary=False):
        bg = self.design.BG_COLOR if secondary else self.design.TEXT_COLOR
        fg = self.design.TEXT_COLOR if secondary else self.design.WHITE
        relief = "flat"
        
        btn = tk.Button(self.container, text=text, command=command, bg=bg, fg=fg, 
                        font=(self.design.font_family, 12, "bold"), relief=relief, 
                        padx=20, pady=10, cursor="hand2", borderwidth=0)
        # Efecto hover simple
        btn.bind("<Enter>", lambda e: btn.configure(bg=self.design.SECONDARY_COLOR if not secondary else self.design.SECONDARY_COLOR))
        btn.bind("<Leave>", lambda e: btn.configure(bg=bg))
        
        btn.pack(pady=10)
        return btn

    def create_back_button(self):
        btn = tk.Button(self.container, text="← VOLVER AL MENÚ", command=self.show_menu, 
                        bg=self.design.BG_COLOR, fg=self.design.SECONDARY_COLOR, 
                        font=(self.design.font_family, 10, "bold"), relief="flat", 
                        padx=10, pady=5, cursor="hand2", borderwidth=0)
        btn.pack(anchor="w", pady=(20, 0))
        return btn

    def show_result(self, text):
        lbl = tk.Label(self.container, text=text, font=self.design.font_body, bg=self.design.ACCENT_COLOR, fg=self.design.WHITE, padx=10, pady=5)
        lbl.pack(fill="x", pady=10)
        return lbl

    # --- MENÚ PRINCIPAL ---
    def show_menu(self):
        self.clear_frame()
        self.create_title("AXION SYSTEMS", level=1)
        self.create_label("Seleccione un módulo de ejercicio:")
        
        menu_frame = tk.Frame(self.container, bg=self.design.BG_COLOR)
        menu_frame.pack(fill="both", expand=True)
        
        # Grid de botones
        exercises = [
            ("1. Aumento Sueldos", self.exercise_1),
            ("2. Parque Diversiones", self.exercise_2),
            ("3. Descuentos Tienda", self.exercise_3),
            ("4. Validación < 10", self.exercise_4),
            ("5. Validación Rango", self.exercise_5),
            ("6. Registro Intentos", self.exercise_6),
            ("7. Suma Enteros", self.exercise_7),
            ("8. Suma Acumulativa", self.exercise_8),
            ("9. Suma Límite 100", self.exercise_9),
            ("10. Pago Trabajadores", self.exercise_10),
        ]
        
        row = 0
        col = 0
        for text, cmd in exercises:
            btn = tk.Button(menu_frame, text=text, command=cmd, bg=self.design.TEXT_COLOR, fg=self.design.WHITE,
                            font=(self.design.font_family, 11, "bold"), relief="flat", padx=15, pady=15, width=20)
            btn.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col > 1:
                col = 0
                row += 1

    # ==========================================
    # LÓGICA DE EJERCICIOS
    # ==========================================
    
    def exercise_1(self):
        self.clear_frame()
        self.create_title("1. Sistema Aumento Sueldos")
        
        tk.Label(self.container, text="Nombre:", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_name = self.create_entry()
        tk.Label(self.container, text="Sueldo Básico:", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_salary = self.create_entry()
        
        def calculate():
            try:
                name = entry_name.get()
                salary = float(entry_salary.get())
                if not name: raise ValueError("Nombre requerido")
                
                if salary < 4000: increase = 0.15
                elif 4000 <= salary <= 7000: increase = 0.10
                else: increase = 0.08
                
                new_salary = salary * (1 + increase)
                self.data_workers.append({"name": name, "old": salary, "new": new_salary})
                
                self.show_result(f"{name}: Nuevo Sueldo S/ {new_salary:.2f} (Aumento {int(increase*100)}%)")
                
                # Historial simple
                hist = "\n".join([f"{w['name']}: {w['new']:.2f}" for w in self.data_workers])
                self.create_label(f"Historial:\n{hist}")
                
            except Exception as e:
                messagebox.showerror("Error", str(e))

        self.create_button("Calcular y Guardar", calculate)
        self.create_back_button()

    def exercise_2(self):
        self.clear_frame()
        self.create_title("2. Parque de Diversiones")
        
        tk.Label(self.container, text="Nombre:", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_name = self.create_entry()
        tk.Label(self.container, text="Edad:", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_age = self.create_entry()
        tk.Label(self.container, text="Cantidad de Juegos:", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_games = self.create_entry()
        
        def calculate():
            try:
                name = entry_name.get()
                age = int(entry_age.get())
                games = int(entry_games.get())
                cost_per_game = 50
                total = games * cost_per_game
                
                if age < 10: discount = 0.25
                elif 10 <= age <= 17: discount = 0.10
                else: discount = 0.0
                
                final = total * (1 - discount)
                self.data_visitors.append({"name": name, "total": final})
                
                self.show_result(f"Pagar: S/ {final:.2f} (Descuento {int(discount*100)}%)")
                
                total_park = sum(v['total'] for v in self.data_visitors)
                self.create_label(f"Recaudado Parque: S/ {total_park:.2f}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        self.create_button("Registrar Visita", calculate)
        self.create_back_button()

    def exercise_3(self):
        self.clear_frame()
        self.create_title("3. Descuentos por Mes")
        
        tk.Label(self.container, text="Nombre Cliente:", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_name = self.create_entry()
        tk.Label(self.container, text="Mes (ej. Octubre):", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_month = self.create_entry()
        tk.Label(self.container, text="Importe:", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_amount = self.create_entry()
        
        def calculate():
            try:
                name = entry_name.get()
                month = entry_month.get().strip().lower()
                amount = float(entry_amount.get())
                
                discounts = {"octubre": 0.15, "diciembre": 0.20, "julio": 0.10}
                disc = discounts.get(month, 0.0)
                
                final = amount * (1 - disc)
                self.data_purchases.append({"name": name, "month": month, "total": final})
                
                self.show_result(f"Total Final: S/ {final:.2f}")
                
                daily_total = sum(p['total'] for p in self.data_purchases)
                self.create_label(f"Total Vendido (Sesión): S/ {daily_total:.2f}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        self.create_button("Registrar Compra", calculate)
        self.create_back_button()

    def exercise_4(self):
        self.clear_frame()
        self.create_title("4. Validación < 10")
        self.attempts = 0
        
        tk.Label(self.container, text="Ingrese número entero:", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_num = self.create_entry()
        result_lbl = tk.Label(self.container, text="", bg=self.design.BG_COLOR, fg=self.design.TEXT_COLOR)
        result_lbl.pack(pady=10)
        
        def validate():
            try:
                val = int(entry_num.get())
                self.attempts += 1
                if val < 10:
                    result_lbl.config(text=f"Correcto: {val} | Intentos: {self.attempts}")
                    entry_num.config(state="disabled")
                else:
                    result_lbl.config(text="Error: Debe ser menor a 10. Intente nuevamente.")
                    entry_num.delete(0, tk.END)
            except:
                result_lbl.config(text="Error: Ingrese un número entero.")

        self.create_button("Validar", validate)
        self.create_back_button()

    def exercise_5(self):
        self.clear_frame()
        self.create_title("5. Validación Rango (0-20)")
        self.attempts = 0
        
        tk.Label(self.container, text="Ingrese número (0-20):", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_num = self.create_entry()
        result_lbl = tk.Label(self.container, text="", bg=self.design.BG_COLOR)
        result_lbl.pack(pady=10)
        
        def validate_range(val):
            return 0 <= val <= 20

        def check():
            try:
                val = int(entry_num.get())
                self.attempts += 1
                if validate_range(val):
                    result_lbl.config(text=f"Válido: {val} | Intentos: {self.attempts}")
                    entry_num.config(state="disabled")
                else:
                    result_lbl.config(text="Fuera de rango (0-20). Intente nuevamente.")
                    entry_num.delete(0, tk.END)
            except:
                result_lbl.config(text="Error de formato.")

        self.create_button("Validar", check)
        self.create_back_button()

    def exercise_6(self):
        self.clear_frame()
        self.create_title("6. Registro de Intentos")
        self.attempts_list = []
        self.correct = None
        
        tk.Label(self.container, text="Ingrese número (0-20):", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_num = self.create_entry()
        result_lbl = tk.Label(self.container, text="", bg=self.design.BG_COLOR, justify="left")
        result_lbl.pack(pady=10)
        
        def check():
            try:
                val = int(entry_num.get())
                self.attempts_list.append(val)
                if 0 <= val <= 20:
                    self.correct = val
                    incorrect_count = len([x for x in self.attempts_list if x < 0 or x > 20])
                    history = ", ".join(map(str, self.attempts_list))
                    result_lbl.config(text=f"Correcto: {val}\nIncorrectos: {incorrect_count}\nHistorial: {history}")
                    entry_num.config(state="disabled")
                else:
                    result_lbl.config(text="Fuera de rango. Intente nuevamente.")
                    entry_num.delete(0, tk.END)
            except:
                result_lbl.config(text="Error de formato.")

        self.create_button("Registrar", check)
        self.create_back_button()

    def exercise_7(self):
        self.clear_frame()
        self.create_title("7. Suma N Enteros")
        
        tk.Label(self.container, text="Ingrese N (positivo):", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_n = self.create_entry()
        result_lbl = tk.Label(self.container, text="", bg=self.design.BG_COLOR)
        result_lbl.pack(pady=10)
        
        def calc():
            try:
                n = int(entry_n.get())
                if n <= 0: raise ValueError("Debe ser positivo")
                total = sum(range(1, n + 1))
                seq = " + ".join(map(str, range(1, n + 1)))
                result_lbl.config(text=f"Secuencia: {seq}\nResultado: {total}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        self.create_button("Calcular", calc)
        self.create_back_button()

    def exercise_8(self):
        self.clear_frame()
        self.create_title("8. Suma Acumulativa")
        self.num_list = []
        
        tk.Label(self.container, text="Ingrese número (0 para terminar):", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_num = self.create_entry()
        result_lbl = tk.Label(self.container, text="", bg=self.design.BG_COLOR)
        result_lbl.pack(pady=10)
        
        def add():
            try:
                val = int(entry_num.get())
                if val == 0:
                    total = sum(self.num_list)
                    result_lbl.config(text=f"Lista: {self.num_list}\nCantidad: {len(self.num_list)}\nTotal: {total}")
                    entry_num.config(state="disabled")
                else:
                    self.num_list.append(val)
                    result_lbl.config(text=f"Acumulado actual: {sum(self.num_list)}")
                    entry_num.delete(0, tk.END)
            except:
                messagebox.showerror("Error", "Ingrese número entero")

        self.create_button("Agregar", add)
        self.create_back_button()

    def exercise_9(self):
        self.clear_frame()
        self.create_title("9. Suma hasta > 100")
        self.num_list = []
        self.current_sum = 0
        
        tk.Label(self.container, text="Ingrese número:", bg=self.design.BG_COLOR).pack(anchor="w")
        entry_num = self.create_entry()
        result_lbl = tk.Label(self.container, text="", bg=self.design.BG_COLOR)
        result_lbl.pack(pady=10)
        
        def add():
            try:
                val = int(entry_num.get())
                self.num_list.append(val)
                self.current_sum += val
                result_lbl.config(text=f"Parcial: {self.current_sum}")
                entry_num.delete(0, tk.END)
                
                if self.current_sum > 100:
                    result_lbl.config(text=f"¡Límite superado!\nLista: {self.num_list}\nFinal: {self.current_sum}")
                    entry_num.config(state="disabled")
            except:
                messagebox.showerror("Error", "Ingrese número entero")

        self.create_button("Sumar", add)
        self.create_back_button()

    def exercise_10(self):
        self.clear_frame()
        self.create_title("10. Pago Trabajadores")
        
        fields = {}
        labels = ["Nombre", "Horas Normales", "Pago Hora", "Horas Extras", "N° Hijos"]
        for l in labels:
            tk.Label(self.container, text=f"{l}:", bg=self.design.BG_COLOR).pack(anchor="w")
            fields[l] = self.create_entry()
            
        def calc():
            try:
                name = fields["Nombre"].get()
                h_norm = float(fields["Horas Normales"].get())
                p_hour = float(fields["Pago Hora"].get())
                h_extra = float(fields["Horas Extras"].get())
                children = int(fields["N° Hijos"].get())
                
                pay_norm = h_norm * p_hour
                pay_extra = h_extra * (p_hour * 1.5)
                bonus = children * 0.5 * p_hour # Asumiendo 0.5 veces el pago hora como bonificación base
                total = pay_norm + pay_extra + bonus
                
                self.data_payments.append({"name": name, "total": total})
                
                self.show_result(f"Total a Pagar: S/ {total:.2f}")
                
                report = "\n".join([f"{p['name']}: {p['total']:.2f}" for p in self.data_payments])
                self.create_label(f"Reporte Pagos:\n{report}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        self.create_button("Calcular Pago", calc)
        self.create_back_button()

if __name__ == "__main__":
    app = AxionApp()
    app.mainloop()
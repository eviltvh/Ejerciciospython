import customtkinter as ctk

BG_DARK = "#0A0A0A"
BG_CARD = "#FAFAF9"
BG_SECONDARY = "#F5F5F4"

TEXT_PRIMARY = "#000000"
TEXT_ON_DARK = "#FAFAF9"
TEXT_MUTED = "#737373"
TEXT_DISABLED = "#D4D4D4"

ACCENT_YELLOW = "#E8FF00"
ACCENT_PINK = "#FF3366"
ACCENT_BLUE = "#00D9FF"

FONT_TITLE = ("Georgia", 28, "bold")
FONT_H2 = ("Georgia", 20, "bold")
FONT_MONO = ("Courier", 12, "bold")
FONT_MONO_SM = ("Courier", 11, "normal")
FONT_BODY = ("Helvetica", 13, "normal")
FONT_BODY_BOLD = ("Helvetica", 13, "bold")
FONT_LABEL = ("Courier", 11, "bold")
FONT_BTN = ("Courier", 12, "bold")
FONT_BTN_LG = ("Courier", 14, "bold")

BORDER_THICK = 3
BORDER_THIN = 2
CORNER_RADIUS = 4
PAD_CARD = 20
PAD_SECTION = 24
PAD_ELEMENT = 12


def setup_theme():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")


def create_card_frame(parent, **kwargs):
    frame = ctk.CTkFrame(
        parent,
        fg_color=BG_CARD,
        corner_radius=CORNER_RADIUS,
        border_width=BORDER_THICK,
        border_color=TEXT_PRIMARY,
        **kwargs
    )
    return frame


def create_dark_frame(parent, **kwargs):
    frame = ctk.CTkFrame(
        parent,
        fg_color=BG_DARK,
        corner_radius=0,
        **kwargs
    )
    return frame


def create_accent_button(parent, text, command, **kwargs):
    btn = ctk.CTkButton(
        parent,
        text=text.upper(),
        command=command,
        fg_color=ACCENT_YELLOW,
        text_color=TEXT_PRIMARY,
        hover_color="#D4E600",
        font=FONT_BTN_LG,
        corner_radius=CORNER_RADIUS,
        border_width=BORDER_THICK,
        border_color=TEXT_PRIMARY,
        height=48,
        **kwargs
    )
    return btn


def create_secondary_button(parent, text, command, **kwargs):
    btn = ctk.CTkButton(
        parent,
        text=text.upper(),
        command=command,
        fg_color=BG_CARD,
        text_color=TEXT_PRIMARY,
        hover_color=BG_SECONDARY,
        font=FONT_BTN,
        corner_radius=CORNER_RADIUS,
        border_width=BORDER_THIN,
        border_color=TEXT_PRIMARY,
        height=40,
        **kwargs
    )
    return btn


def create_ghost_button(parent, text, command, **kwargs):
    btn = ctk.CTkButton(
        parent,
        text=text,
        command=command,
        fg_color="transparent",
        text_color=TEXT_MUTED,
        hover_color="#1a1a1a",
        font=FONT_MONO_SM,
        corner_radius=0,
        border_width=0,
        height=32,
        **kwargs
    )
    return btn


def create_entry(parent, placeholder="", **kwargs):
    entry = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder,
        fg_color=BG_SECONDARY,
        text_color=TEXT_PRIMARY,
        placeholder_text_color=TEXT_MUTED,
        border_color=TEXT_PRIMARY,
        border_width=BORDER_THIN,
        corner_radius=CORNER_RADIUS,
        font=FONT_BODY,
        height=40,
        **kwargs
    )
    return entry


def create_label(parent, text, font=None, text_color=None, **kwargs):
    lbl = ctk.CTkLabel(
        parent,
        text=text,
        font=font or FONT_BODY,
        text_color=text_color or TEXT_PRIMARY,
        **kwargs
    )
    return lbl


def create_mono_label(parent, text, **kwargs):
    color = kwargs.pop("text_color", TEXT_MUTED)
    lbl = ctk.CTkLabel(
        parent,
        text=text.upper(),
        font=FONT_LABEL,
        text_color=color,
        **kwargs
    )
    return lbl


def create_result_banner(parent, text, success=True):
    color = ACCENT_YELLOW if success else ACCENT_PINK
    frame = ctk.CTkFrame(
        parent,
        fg_color=color,
        corner_radius=CORNER_RADIUS,
        border_width=BORDER_THICK,
        border_color=TEXT_PRIMARY,
    )
    lbl = ctk.CTkLabel(
        frame,
        text=text,
        font=FONT_MONO,
        text_color=TEXT_PRIMARY,
        wraplength=500,
    )
    lbl.pack(padx=PAD_CARD, pady=12)
    return frame


def create_scrollable_frame(parent, **kwargs):
    frame = ctk.CTkScrollableFrame(
        parent,
        fg_color=BG_SECONDARY,
        corner_radius=CORNER_RADIUS,
        border_width=BORDER_THIN,
        border_color=TEXT_DISABLED,
        **kwargs
    )
    return frame

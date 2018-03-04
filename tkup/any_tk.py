__all__ = [
    "AnyTK"
]

from tkinter import ttk
from typing import Union
import tkinter as tk

#: Union of Tkinter root and all wrapped widgets for type checking.
AnyTK = Union[
    ttk.Button,
    tk.Canvas,
    ttk.Checkbutton,
    ttk.Combobox,
    ttk.Entry,
    ttk.Frame,
    ttk.Label,
    ttk.LabelFrame,
    ttk.LabeledScale,
    tk.Listbox,
    ttk.Menubutton,
    tk.Message,
    ttk.Notebook,
    ttk.OptionMenu,
    ttk.PanedWindow,
    ttk.Progressbar,
    ttk.Radiobutton,
    ttk.Scale,
    ttk.Scrollbar,
    ttk.Separator,
    ttk.Sizegrip,
    tk.Spinbox,
    tk.Text,
    tk.Tk,
    ttk.Treeview,
    tk.Widget
]

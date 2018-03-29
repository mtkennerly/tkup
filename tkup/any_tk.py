__all__ = [
    "AnyTK"
]

from typing import Union
import tkinter as tk

import tkup._widgets as tw

#: Union of Tkinter root and all wrapped widgets for type checking.
AnyTK = Union[
    tw.Button,
    tw.Canvas,
    tw.Checkbutton,
    tw.Combobox,
    tw.Entry,
    tw.Frame,
    tw.Label,
    tw.LabelFrame,
    tw.LabeledScale,
    tw.Listbox,
    tw.Menu,
    tw.Menubutton,
    tw.Message,
    tw.Notebook,
    tw.OptionMenu,
    tw.PanedWindow,
    tw.Progressbar,
    tw.Radiobutton,
    tw.Scale,
    tw.Scrollbar,
    tw.Separator,
    tw.Sizegrip,
    tw.Spinbox,
    tw.Text,
    tk.Tk,
    tw.Treeview,
    tk.Widget
]

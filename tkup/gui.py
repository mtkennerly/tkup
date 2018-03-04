__all__ = [
    "GUI"
]

from contextlib import contextmanager
from tkinter import ttk
from typing import Callable, Iterator, Tuple, Type, TypeVar, Union
import tkinter as tk

T = TypeVar("T", bound=tk.Widget)


class GUI:
    def __init__(self, *args, **kwargs) -> None:
        """
        :param args: Passed to the Tk constructor.
        :param kwargs: Passed to the Tk constructor.
        """

        self._root = tk.Tk(*args, **kwargs)
        self._chain = []

    def it(self) -> Union[tk.Tk, tk.Widget]:
        """
        Get the master widget for the current nesting level.

        :return: Current master widget.
        """

        if not self._chain:
            raise ValueError("No master widget available yet.")

        return self._chain[-1]

    def with_it(self) -> Tuple["GUI", Callable[[], tk.Widget]]:
        """
        Get the class instance and its it() for quickly assigning to variables.

        :return: Class instance and its it() method.
        """

        return self, self.it

    def run(self) -> None:
        """
        Start the main loop.
        """

        self._root.mainloop()

    @contextmanager
    def widget(self, kind: Type[T], *args, **kwargs) -> Iterator[T]:
        """
        Make a widget.

        :param kind: Type of widget to make. It must accept its master widget
            as the first positional argument.
        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        w = kind(self.it(), *args, **kwargs)
        self._chain.append(w)
        yield w
        self._chain.pop()

    @contextmanager
    def button(self, *args, **kwargs) -> Iterator[ttk.Button]:
        """
        Make a button.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Button, *args, **kwargs) as w:
            yield w

    @contextmanager
    def canvas(self, *args, **kwargs) -> Iterator[tk.Canvas]:
        """
        Make a canvas.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tk.Canvas, *args, **kwargs) as w:
            yield w

    @contextmanager
    def checkbutton(self, *args, **kwargs) -> Iterator[ttk.Checkbutton]:
        """
        Make a checkbutton.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Checkbutton, *args, **kwargs) as w:
            yield w

    @contextmanager
    def combobox(self, *args, **kwargs) -> Iterator[ttk.Combobox]:
        """
        Make a combobox.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Combobox, *args, **kwargs) as w:
            yield w

    @contextmanager
    def entry(self, *args, **kwargs) -> Iterator[ttk.Entry]:
        """
        Make an entry.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Entry, *args, **kwargs) as w:
            yield w

    @contextmanager
    def frame(self, *args, **kwargs) -> Iterator[ttk.Frame]:
        """
        Make a frame.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Frame, *args, **kwargs) as w:
            yield w

    @contextmanager
    def label(self, *args, **kwargs) -> Iterator[ttk.Label]:
        """
        Make a label.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Label, *args, **kwargs) as w:
            yield w

    @contextmanager
    def label_frame(self, *args, **kwargs) -> Iterator[ttk.LabelFrame]:
        """
        Make a label frame.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.LabelFrame, *args, **kwargs) as w:
            yield w

    @contextmanager
    def labeled_scale(self, *args, **kwargs) -> Iterator[ttk.LabeledScale]:
        """
        Make a labeled scale.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.LabeledScale, *args, **kwargs) as w:
            yield w

    @contextmanager
    def listbox(self, *args, **kwargs) -> Iterator[tk.Listbox]:
        """
        Make a listbox.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tk.Listbox, *args, **kwargs) as w:
            yield w

    @contextmanager
    def menubutton(self, *args, **kwargs) -> Iterator[ttk.Menubutton]:
        """
        Make a menubutton.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Menubutton, *args, **kwargs) as w:
            yield w

    @contextmanager
    def message(self, *args, **kwargs) -> Iterator[tk.Message]:
        """
        Make a message.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tk.Message, *args, **kwargs) as w:
            yield w

    @contextmanager
    def notebook(self, *args, **kwargs) -> Iterator[ttk.Notebook]:
        """
        Make a notebook.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Notebook, *args, **kwargs) as w:
            yield w

    @contextmanager
    def option_menu(self, *args, **kwargs) -> Iterator[ttk.OptionMenu]:
        """
        Make an option menu.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.OptionMenu, *args, **kwargs) as w:
            yield w

    @contextmanager
    def paned_window(self, *args, **kwargs) -> Iterator[ttk.PanedWindow]:
        """
        Make a paned window.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.PanedWindow, *args, **kwargs) as w:
            yield w

    @contextmanager
    def progressbar(self, *args, **kwargs) -> Iterator[ttk.Progressbar]:
        """
        Make a progressbar.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Progressbar, *args, **kwargs) as w:
            yield w

    @contextmanager
    def radiobutton(self, *args, **kwargs) -> Iterator[ttk.Radiobutton]:
        """
        Make a radiobutton.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Radiobutton, *args, **kwargs) as w:
            yield w

    @contextmanager
    def root(self) -> Iterator[tk.Tk]:
        """
        Yield the root instance created during class instantiation.

        :return: Tk root.
        """

        self._chain.append(self._root)
        yield self._root
        self._chain.pop()

    @contextmanager
    def scale(self, *args, **kwargs) -> Iterator[ttk.Scale]:
        """
        Make a scale.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Scale, *args, **kwargs) as w:
            yield w

    @contextmanager
    def scrollbar(self, *args, **kwargs) -> Iterator[ttk.Scrollbar]:
        """
        Make a scrollbar.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Scrollbar, *args, **kwargs) as w:
            yield w

    @contextmanager
    def separator(self, *args, **kwargs) -> Iterator[ttk.Separator]:
        """
        Make a separator.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Separator, *args, **kwargs) as w:
            yield w

    @contextmanager
    def sizegrip(self, *args, **kwargs) -> Iterator[ttk.Sizegrip]:
        """
        Make a sizegrip.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Sizegrip, *args, **kwargs) as w:
            yield w

    @contextmanager
    def spinbox(self, *args, **kwargs) -> Iterator[tk.Spinbox]:
        """
        Make a spinbox.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tk.Spinbox, *args, **kwargs) as w:
            yield w

    @contextmanager
    def text(self, *args, **kwargs) -> Iterator[tk.Text]:
        """
        Make a text.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tk.Text, *args, **kwargs) as w:
            yield w

    @contextmanager
    def treeview(self, *args, **kwargs) -> Iterator[ttk.Treeview]:
        """
        Make a treeview.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(ttk.Treeview, *args, **kwargs) as w:
            yield w

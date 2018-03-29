__all__ = [
    "GUI"
]

from contextlib import contextmanager
from typing import Callable, Iterator, Tuple, Type, TypeVar
import tkinter as tk

from tkup import AnyTK
import tkup._widgets as tw

T = TypeVar("T", bound=tk.Widget)


class GUI:
    def __init__(self, *args, **kwargs) -> None:
        """
        :param args: Passed to the Tk constructor.
        :param kwargs: Passed to the Tk constructor.
        """

        self._root = tk.Tk(*args, **kwargs)
        self._chain = []

    def it(self) -> AnyTK:
        """
        Get the master widget for the current nesting level.

        :return: Current master widget.
        """

        if not self._chain:
            raise ValueError("No master widget available yet.")

        return self._chain[-1]

    def with_it(self) -> Tuple["GUI", Callable[[], AnyTK]]:
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
    def button(self, *args, **kwargs) -> Iterator[tw.Button]:
        """
        Make a button.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Button, *args, **kwargs) as w:
            yield w

    @contextmanager
    def canvas(self, *args, **kwargs) -> Iterator[tw.Canvas]:
        """
        Make a canvas.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Canvas, *args, **kwargs) as w:
            yield w

    @contextmanager
    def checkbutton(self, *args, **kwargs) -> Iterator[tw.Checkbutton]:
        """
        Make a checkbutton.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Checkbutton, *args, **kwargs) as w:
            yield w

    @contextmanager
    def combobox(self, *args, **kwargs) -> Iterator[tw.Combobox]:
        """
        Make a combobox.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Combobox, *args, **kwargs) as w:
            yield w

    @contextmanager
    def entry(self, *args, **kwargs) -> Iterator[tw.Entry]:
        """
        Make an entry.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Entry, *args, **kwargs) as w:
            yield w

    @contextmanager
    def frame(self, *args, **kwargs) -> Iterator[tw.Frame]:
        """
        Make a frame.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Frame, *args, **kwargs) as w:
            yield w

    @contextmanager
    def label(self, *args, **kwargs) -> Iterator[tw.Label]:
        """
        Make a label.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Label, *args, **kwargs) as w:
            yield w

    @contextmanager
    def label_frame(self, *args, **kwargs) -> Iterator[tw.LabelFrame]:
        """
        Make a label frame.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.LabelFrame, *args, **kwargs) as w:
            yield w

    @contextmanager
    def labeled_scale(self, *args, **kwargs) -> Iterator[tw.LabeledScale]:
        """
        Make a labeled scale.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.LabeledScale, *args, **kwargs) as w:
            yield w

    @contextmanager
    def listbox(self, *args, **kwargs) -> Iterator[tw.Listbox]:
        """
        Make a listbox.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Listbox, *args, **kwargs) as w:
            yield w

    @contextmanager
    def menu(self, *args, **kwargs) -> Iterator[tw.Menu]:
        """
        Make a menu.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Menu, *args, **kwargs) as w:
            yield w

    @contextmanager
    def menubutton(self, *args, **kwargs) -> Iterator[tw.Menubutton]:
        """
        Make a menubutton.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Menubutton, *args, **kwargs) as w:
            yield w

    @contextmanager
    def message(self, *args, **kwargs) -> Iterator[tw.Message]:
        """
        Make a message.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Message, *args, **kwargs) as w:
            yield w

    @contextmanager
    def notebook(self, *args, **kwargs) -> Iterator[tw.Notebook]:
        """
        Make a notebook.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Notebook, *args, **kwargs) as w:
            yield w

    @contextmanager
    def option_menu(self, *args, **kwargs) -> Iterator[tw.OptionMenu]:
        """
        Make an option menu.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.OptionMenu, *args, **kwargs) as w:
            yield w

    @contextmanager
    def paned_window(self, *args, **kwargs) -> Iterator[tw.PanedWindow]:
        """
        Make a paned window.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.PanedWindow, *args, **kwargs) as w:
            yield w

    @contextmanager
    def progressbar(self, *args, **kwargs) -> Iterator[tw.Progressbar]:
        """
        Make a progressbar.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Progressbar, *args, **kwargs) as w:
            yield w

    @contextmanager
    def radiobutton(self, *args, **kwargs) -> Iterator[tw.Radiobutton]:
        """
        Make a radiobutton.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Radiobutton, *args, **kwargs) as w:
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
    def scale(self, *args, **kwargs) -> Iterator[tw.Scale]:
        """
        Make a scale.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Scale, *args, **kwargs) as w:
            yield w

    @contextmanager
    def scrollbar(self, *args, **kwargs) -> Iterator[tw.Scrollbar]:
        """
        Make a scrollbar.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Scrollbar, *args, **kwargs) as w:
            yield w

    @contextmanager
    def separator(self, *args, **kwargs) -> Iterator[tw.Separator]:
        """
        Make a separator.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Separator, *args, **kwargs) as w:
            yield w

    @contextmanager
    def sizegrip(self, *args, **kwargs) -> Iterator[tw.Sizegrip]:
        """
        Make a sizegrip.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Sizegrip, *args, **kwargs) as w:
            yield w

    @contextmanager
    def spinbox(self, *args, **kwargs) -> Iterator[tw.Spinbox]:
        """
        Make a spinbox.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Spinbox, *args, **kwargs) as w:
            yield w

    @contextmanager
    def text(self, *args, **kwargs) -> Iterator[tw.Text]:
        """
        Make a text.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Text, *args, **kwargs) as w:
            yield w

    @contextmanager
    def treeview(self, *args, **kwargs) -> Iterator[tw.Treeview]:
        """
        Make a treeview.

        :param args: Passed to constructor.
        :param kwargs: Passed to constructor.
        :return: Widget.
        """

        with self.widget(tw.Treeview, *args, **kwargs) as w:
            yield w

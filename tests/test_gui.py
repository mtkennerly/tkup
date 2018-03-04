import tkinter as tk
from tkinter import ttk
from unittest import mock

import pytest

from tkup import GUI


@pytest.fixture
def app() -> GUI:
    return GUI()


class TestGUI:
    def test_it(self, app: GUI):
        with pytest.raises(ValueError):
            app.it()

        with app.root() as root:
            assert app.it() is root
            with app.button() as button:
                assert app.it() is button

    def test_with_it(self):
        app, it = GUI().with_it()

        with pytest.raises(ValueError):
            it()

        with app.root() as root:
            assert it() is root
            with app.button() as button:
                assert it() is button

    def test_run(self, app: GUI):
        app._root = mock.MagicMock()
        app.run()
        app._root.mainloop.assert_called_once_with()

    def test_widget(self, app: GUI):
        with app.root():
            with app.widget(tk.Button) as button:
                assert isinstance(button, tk.Button)

    def test_button(self, app: GUI):
        with app.root():
            with app.button() as w:
                assert isinstance(w, ttk.Button)

    def test_canvas(self, app: GUI):
        with app.root():
            with app.canvas() as w:
                assert isinstance(w, tk.Canvas)

    def test_checkbutton(self, app: GUI):
        with app.root():
            with app.checkbutton() as w:
                assert isinstance(w, ttk.Checkbutton)

    def test_combobox(self, app: GUI):
        with app.root():
            with app.combobox() as w:
                assert isinstance(w, ttk.Combobox)

    def test_entry(self, app: GUI):
        with app.root():
            with app.entry() as w:
                assert isinstance(w, ttk.Entry)

    def test_frame(self, app: GUI):
        with app.root():
            with app.frame() as w:
                assert isinstance(w, ttk.Frame)

    def test_label(self, app: GUI):
        with app.root():
            with app.label() as w:
                assert isinstance(w, ttk.Label)

    def test_label_frame(self, app: GUI):
        with app.root():
            with app.label_frame() as w:
                assert isinstance(w, ttk.LabelFrame)

    def test_labeled_scale(self, app: GUI):
        with app.root():
            with app.labeled_scale() as w:
                assert isinstance(w, ttk.LabeledScale)

    def test_listbox(self, app: GUI):
        with app.root():
            with app.listbox() as w:
                assert isinstance(w, tk.Listbox)

    def test_menu(self, app: GUI):
        with app.root():
            with app.menu() as w:
                assert isinstance(w, tk.Menu)

    def test_menubutton(self, app: GUI):
        with app.root():
            with app.menubutton() as w:
                assert isinstance(w, ttk.Menubutton)

    def test_message(self, app: GUI):
        with app.root():
            with app.message() as w:
                assert isinstance(w, tk.Message)

    def test_notebook(self, app: GUI):
        with app.root():
            with app.notebook() as w:
                assert isinstance(w, ttk.Notebook)

    def test_option_menu(self, app: GUI):
        with app.root():
            with app.option_menu(tk.StringVar()) as w:
                assert isinstance(w, ttk.OptionMenu)

    def test_paned_window(self, app: GUI):
        with app.root():
            with app.paned_window() as w:
                assert isinstance(w, ttk.PanedWindow)

    def test_progressbar(self, app: GUI):
        with app.root():
            with app.progressbar() as w:
                assert isinstance(w, ttk.Progressbar)

    def test_radiobutton(self, app: GUI):
        with app.root():
            with app.radiobutton() as w:
                assert isinstance(w, ttk.Radiobutton)

    def test_root(self, app: GUI):
        with app.root():
            with app.root() as w:
                assert isinstance(w, tk.Tk)

    def test_scale(self, app: GUI):
        with app.root():
            with app.scale() as w:
                assert isinstance(w, ttk.Scale)

    def test_scrollbar(self, app: GUI):
        with app.root():
            with app.scrollbar() as w:
                assert isinstance(w, ttk.Scrollbar)

    def test_separator(self, app: GUI):
        with app.root():
            with app.separator() as w:
                assert isinstance(w, ttk.Separator)

    def test_sizegrip(self, app: GUI):
        with app.root():
            with app.sizegrip() as w:
                assert isinstance(w, ttk.Sizegrip)

    def test_spinbox(self, app: GUI):
        with app.root():
            with app.spinbox() as w:
                assert isinstance(w, tk.Spinbox)

    def test_text(self, app: GUI):
        with app.root():
            with app.text() as w:
                assert isinstance(w, tk.Text)

    def test_treeview(self, app: GUI):
        with app.root():
            with app.treeview() as w:
                assert isinstance(w, ttk.Treeview)

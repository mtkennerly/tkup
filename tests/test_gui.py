import tkinter as tk
from unittest import mock

import pytest

from tkup import GUI
import tkup._widgets as tw


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

    def test_with_it(self, app: GUI):
        app, it = app.with_it()

        with pytest.raises(ValueError):
            it()

        with app.root() as root:
            assert it() is root
            with app.button() as button:
                assert it() is button

    def test_run(self, app: GUI):
        mocked_root = mock.MagicMock()
        app._root = mocked_root
        app.run()
        mocked_root.mainloop.assert_called_once_with()

    def test_widget(self, app: GUI):
        with app.root():
            with app.widget(tk.Button) as button:
                assert isinstance(button, tk.Button)

    def test_button(self, app: GUI):
        with app.root():
            with app.button() as w:
                assert isinstance(w, tw.Button)

    def test_canvas(self, app: GUI):
        with app.root():
            with app.canvas() as w:
                assert isinstance(w, tw.Canvas)

    def test_checkbutton(self, app: GUI):
        with app.root():
            with app.checkbutton() as w:
                assert isinstance(w, tw.Checkbutton)

    def test_combobox(self, app: GUI):
        with app.root():
            with app.combobox() as w:
                assert isinstance(w, tw.Combobox)

    def test_entry(self, app: GUI):
        with app.root():
            with app.entry() as w:
                assert isinstance(w, tw.Entry)

    def test_frame(self, app: GUI):
        with app.root():
            with app.frame() as w:
                assert isinstance(w, tw.Frame)

    def test_label(self, app: GUI):
        with app.root():
            with app.label() as w:
                assert isinstance(w, tw.Label)

    def test_label_frame(self, app: GUI):
        with app.root():
            with app.label_frame() as w:
                assert isinstance(w, tw.LabelFrame)

    def test_labeled_scale(self, app: GUI):
        with app.root():
            with app.labeled_scale() as w:
                assert isinstance(w, tw.LabeledScale)

    def test_listbox(self, app: GUI):
        with app.root():
            with app.listbox() as w:
                assert isinstance(w, tw.Listbox)

    def test_menu(self, app: GUI):
        with app.root():
            with app.menu() as w:
                assert isinstance(w, tw.Menu)

    def test_menubutton(self, app: GUI):
        with app.root():
            with app.menubutton() as w:
                assert isinstance(w, tw.Menubutton)

    def test_message(self, app: GUI):
        with app.root():
            with app.message() as w:
                assert isinstance(w, tw.Message)

    def test_notebook(self, app: GUI):
        with app.root():
            with app.notebook() as w:
                assert isinstance(w, tw.Notebook)

    def test_option_menu(self, app: GUI):
        with app.root():
            with app.option_menu(tk.StringVar()) as w:
                assert isinstance(w, tw.OptionMenu)

    def test_paned_window(self, app: GUI):
        with app.root():
            with app.paned_window() as w:
                assert isinstance(w, tw.PanedWindow)

    def test_progressbar(self, app: GUI):
        with app.root():
            with app.progressbar() as w:
                assert isinstance(w, tw.Progressbar)

    def test_radiobutton(self, app: GUI):
        with app.root():
            with app.radiobutton() as w:
                assert isinstance(w, tw.Radiobutton)

    def test_root(self, app: GUI):
        with app.root():
            with app.root() as w:
                assert isinstance(w, tk.Tk)

    def test_scale(self, app: GUI):
        with app.root():
            with app.scale() as w:
                assert isinstance(w, tw.Scale)

    def test_scrollbar(self, app: GUI):
        with app.root():
            with app.scrollbar() as w:
                assert isinstance(w, tw.Scrollbar)

    def test_separator(self, app: GUI):
        with app.root():
            with app.separator() as w:
                assert isinstance(w, tw.Separator)

    def test_sizegrip(self, app: GUI):
        with app.root():
            with app.sizegrip() as w:
                assert isinstance(w, tw.Sizegrip)

    def test_spinbox(self, app: GUI):
        with app.root():
            with app.spinbox() as w:
                assert isinstance(w, tw.Spinbox)

    def test_text(self, app: GUI):
        with app.root():
            with app.text() as w:
                assert isinstance(w, tw.Text)

    def test_treeview(self, app: GUI):
        with app.root():
            with app.treeview() as w:
                assert isinstance(w, tw.Treeview)

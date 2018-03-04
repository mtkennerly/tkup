
# tkup

tkup is a thin wrapper around standard Tkinter widgets, allowing you to write
code that visually reflects the widget hierarchy. It doesn't try to reinvent
the wheel and just helps you use normal Tkinter in a streamlined way.

Typical Tkinter code is flat, even though it represents a heavily nested
structure, which makes it difficult to quickly read and understand the true
organization of the GUI. You must also explicitly assign each widget's master,
which is error-prone and verbose:

```python
import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title = "Demo"

outer_frame = ttk.Frame(app)
outer_frame.grid()
hi_button = ttk.Button(outer_frame, text="hi")
hi_button.grid()

app.mainloop()
```

tkup solves this by using nested with-statements. There are factory functions
for each kind of widget, and you can use them as context managers so that
nested master widgets are automatically assigned. Post-instantiation calls,
like gridding, can be accomplished two ways, most traditionally by naming the
yielded value:

```python
from tkup import GUI

app = GUI()

with app.root() as root:
    root.title = "Demo"
    with app.frame() as outer_frame:
        outer_frame.grid()
        with app.button(text="hi") as hi_button:
            hi_button.grid()

app.run()
```

However, naming every single widget just to grid it can be tiresome.
Inspired by Kotlin's implicit creation of the `it` variable in lambdas,
the GUI class provides an `it` method which returns the current master widget,
and there is an additional convenience method called `with_it` which returns
the GUI instance and its `it` method for quick assignment to variables:

```python
from tkup import GUI

app, it = GUI().with_it()

with app.root():
    it().title = "Demo"
    with app.frame():
        it().grid()
        with app.button(text="hi"):
            it().grid()

app.run()
```

tkup prefers themed (ttk) widgets wherever available. If you want to use
classic widgets, or if you want to use a custom subclass of `tkinter.Widget`,
then you can use the GUI `widget` method and pass in the type to instantiate:

```
import tkinter as tk
from tkup import GUI

app = GUI()

with app.root():
    with app.widget(tk.Button, text="foo"):
        ...
```

## Installation

```
pip install tkup
```

tkup supports Python 3.5 and higher.

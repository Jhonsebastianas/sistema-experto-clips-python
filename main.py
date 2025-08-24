# main.py
import tkinter as tk
from gui import ClipsApp

## Ejemplo reglas
# (defrule rLloviendo (lloviendo) => (assert (abrirParaguas)))
# (defrule msgLloviendo (abrirParaguas) => (printout t "Debe abrir paraguas" crlf))

## Ejemplo hecho
# (lloviendo)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClipsApp(root)
    root.mainloop()

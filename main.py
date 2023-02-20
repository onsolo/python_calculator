from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Aharoni", 50, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        buttons = [
            "C", "←", "*", "X²",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "="
        ]

        x = 10
        y = 140
        for btn in buttons:
            com = lambda x=btn: self.calculate(x)
            Button(text=btn, bg="#FFF",
                   font=("Aharoni", 30),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def calculate(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "←":
            self.formula = self.formula[0:-1]
        elif operation == "X²":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()

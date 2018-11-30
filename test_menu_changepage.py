import tkinter as tk


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs, ):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        menu = tk.Menu(container)

        betting = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=betting, label="Pages")
        betting.add_command(label="PageOne",
                            command=lambda: controller.show_frame(PageOne))
        betting.add_command(label="PageTwo",
                            command=lambda: controller.show_frame(PageTwo))

        tk.Tk.config(self, menu=menu)

        for F in (Startpage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Startpage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Startpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="page 1",
                        command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = tk.Button(self, text="Page Two",
                        command=lambda: controller.show_frame(PageTwo))
        button2.pack()


#   *****   PAGES   *****

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Back to Home")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                        command=lambda: controller.show_frame(Startpage))
        button1.pack()
        button2 = tk.Button(self, text="Page Two",
                        command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                        command=lambda: controller.show_frame(Startpage))
        button1.pack()
        button2 = tk.Button(self, text="Page One",
                        command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = MyApp()
app.geometry("1200x600")
app.mainloop()
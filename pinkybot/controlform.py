
import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self,default='clienticon.ico')
        tk.Tk.wm_title(self, "Sea of BTC Client")

        container = tk.Frame(self,width=500, height=500)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        label1 = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label1.pack()




        button1 = tk.Button(self,text="Start Login")
        button1.pack(side="top")
        # container.grid(row=2)
        
        # label1.pack()

        # self.frames = {}

        # for F in (StartPage, PageOne, PageTwo):

        #     frame = F(container, self)
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame(StartPage)

    # def show_frame(self, cont):

    #     frame = self.frames[cont]
    #     frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        # tk.Frame.geometry("300x200")
        # super.geometry('{}x{}'.format(460, 350))
        label1 = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label1.grid(row=5,column=2)
        label1.pack()

        label2 = tk.Label(self, text="Start Page2", font=LARGE_FONT)
        label2.grid(row=5,column=2)
        label2.pack()
        # button = ttk.Button(self, text="Visit Page 1",
        #                     command=lambda: controller.show_frame(PageOne))
        # button.pack()

        # button2 = ttk.Button(self, text="Visit Page 2",
        #                     command=lambda: controller.show_frame(PageTwo))
        # button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.mainloop()
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import ttk
import logging


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    b1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    b1.pack()
    popup.mainloop()


class TextHandler(logging.Handler):

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)

        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

    def create(self, num):
        # Create textLogger
        topframe = tk.Frame(root)
        topframe.pack(side=tk.TOP)
        if num == 0:
            st = tkst.ScrolledText(topframe, state='disabled')
            st.configure(font='TkFixedFont')

            st.pack()

            self.text_handler = TextHandler(st)

            # Add the handler to logger
            self.logger = logging.getLogger()
            self.logger.addHandler(self.text_handler)
            print(num)

        else:
            # Add the handler to logger
            self.logger = logging.getLogger()
            print(num)


def stop():
    root.flag = False


def loop():
    th = TextHandler("none")
    th.create(1)

    def start():
        if root.flag:
            th.logger.error("error")
            root.after(1000, start)
        else:
            th.logger.error("Loop stopped")
            root.flag = True
            return
    start()



class HomePage(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self, parent)

        #logger and main loop
        th = TextHandler("none")
        th.create(0)
        root.flag = True

        bottomframe = tk.Frame(root)
        bottomframe.pack(side=tk.BOTTOM)

        topframe = tk.Frame(root)
        topframe.pack(side=tk.TOP)

        topframe = tk.Frame(root)
        topframe.pack(side=tk.TOP)

        # Create taskbar/menu
        taskbar = tk.Menu(self.master)
        self.master.config(menu=taskbar)

        file = tk.Menu(taskbar)
        file.add_command(label="Run", command=loop)
        file.add_command(label="Stop", command=stop)
        file.add_separator()
        file.add_command(label="Settings", command=lambda: popupmsg("Coming \"soon\"..."))
        file.add_separator()
        file.add_command(label="Quit", command=quit)
        taskbar.add_cascade(label="File", menu=file)

        startButton = tk.Button(bottomframe, text="Start", command=loop)
        startButton.pack()

        stopButton = tk.Button(bottomframe, text="Stop",  command=stop)
        stopButton.pack()

        exitButton = tk.Button(bottomframe, text="Exit",  command=quit)
        exitButton.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.wm_title("Scraper")
    root.mainloop()
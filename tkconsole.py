import tkinter as tk
import datetime
import sys


class outputlog(tk.Tk):
  def __init__(self):
      tk.Tk.__init__(self)
      self.title("Output Log")
      self.resizable(0,0)

      self.output = tk.Text( width=80, height=20, background = 'black', fg='white')
      self.output.pack(side=tk.LEFT)

      self.scrollbar = tk.Scrollbar(orient="vertical", command = self.output.yview)
      self.scrollbar.pack(side=tk.RIGHT, fill="y")

      self.output['yscrollcommand'] = self.scrollbar.set

      self.update_idletasks()
      self.mycount = 0
  def txtout(self,txtmsg):
      self.timenow = datetime.datetime.now()
      self.output.configure(state='normal')
      self.output.insert(tk.END,self.timenow.strftime("%Y-%m-%d %H:%M:%S ") + str(txtmsg + "\n"))
      self.output.see(tk.END)
      self.output.configure(state='disabled')

  def Refresher(self):
      # global mycount
      self.mycount+=1
      print("refreshing " + str(self.mycount))
      self.txtout("Hello" + str(self.mycount))
      self.after(1000, self.Refresher) # every second...


if __name__ == '__main__':
    # print("start logoutput")
    txtoutput=outputlog()
    txtoutput.Refresher()
    txtoutput.mainloop()

exit()
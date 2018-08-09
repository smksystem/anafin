import tkinter as tk
import datetime
import sys


class outputlog(tk.Tk):
  def __init__(self):

      tk.Tk.__init__(self)
      self.title("Output Log")
      # self.resizable(0,0)
      self.geometry('500x500')
      # self.pack_propagate(0)

      self.frameOutput = tk.Frame(self, width=400, height =400,background = 'blue')
      self.frameOutput.pack_propagate(0)
      self.frameOutput.pack(side = "left" )
      
      self.framebutton = tk.Frame(self, width=400, height =400,background = 'green')
      self.framebutton.pack_propagate(0)
      self.framebutton.pack(side="right")


      self.output = tk.Text(self.frameOutput,wrap='word', width=47, height=400, background = 'black', fg='white')

      self.output.pack(side=tk.LEFT)
      
      self.LoginBtnInFrame=tk.Button(self.framebutton,text="Start Login")
      self.LoginBtnInFrame.pack(side=tk.TOP)


      self.scrollbar = tk.Scrollbar(self.frameOutput,orient="vertical", command = self.output.yview)
      
      self.scrollbar.pack(side=tk.RIGHT, fill="y")


      self.LoginBtnInFrame=tk.Button(self.framebutton,text="Start Login")
      self.LoginBtnInFrame.pack(side=tk.LEFT)

      self.output['yscrollcommand'] = self.scrollbar.set

      self.update_idletasks()
      self.mycount = 0

  def txtout(self,txtmsg):

      self.timenow = datetime.datetime.now()
      

      self.output.configure(state='normal')
      # print (txtmsg)

      
      # self.highlight_pattern("vol","red")

      self.output.insert(tk.END,self.timenow.strftime("%Y-%m-%d %H:%M:%S ") + str(txtmsg + "\n"))
      

      
      # pos = self.output.search( "Vol","1.0",stopindex="end", count=countVar)
      # print (pos)
      # self.highlight_text("Vol",txtmsg)
      # self.highlight_text("Order",txtmsg)
      # self.highlight_text("Stat",txtmsg)
      self.output.configure(state='disabled')
      
      # self.output.tag_config("a", foreground="blue")
      # self.output.insert(contents, ("n", "a"))
  def highlight_text(self,word):
      # word="Vol"
      txtmsg=self.output.get("1.0","end")
      # print (txtmsg)
      countVar = tk.StringVar()
      self.output.tag_config("test", background="black", foreground="green")
      if txtmsg:
        pos = '1.0'
        while 1:
          pos = self.output.search( word,pos,stopindex="end", count=countVar)
          if not pos: break
          lastidx = '%s+%dc' % (pos, int(countVar.get()))
          self.output.tag_add('test', pos, lastidx)
          pos = lastidx

      self.output.see(tk.END)
     
  def Refresher(self):

      self.mycount+=1
      step=10+(self.mycount/10)
      print (step)

      self.output.tag_config("testb", background="white", foreground="red")
      self.output.tag_add('testb', 10.0, step)
      self.after(1000, self.Refresher) # every second...


# if __name__ == '__main__':
#     # print("start logoutput")
#     txtoutput=outputlog()
#     txtoutput.Refresher()
#     txtoutput.mainloop()

# exit()
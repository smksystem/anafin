import tkinter as tk
import datetime
import sys


class outputlog(tk.Tk):
  def __init__(self):

      tk.Tk.__init__(self)
      self.title("Output Log")
      self.resizable(0,0)

      self.output = tk.Text( width=60, height=40, background = 'black', fg='white')
      self.output.pack(side=tk.LEFT)

      self.scrollbar = tk.Scrollbar(orient="vertical", command = self.output.yview)
      self.scrollbar.pack(side=tk.RIGHT, fill="y")

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
      self.output.tag_config("test", background="green", foreground="white")
      if txtmsg:
        pos = '1.0'
        while 1:
          pos = self.output.search( word,pos,stopindex="end", count=countVar)
          if not pos: break
          lastidx = '%s+%dc' % (pos, int(countVar.get()))
          self.output.tag_add('test', pos, lastidx)
          pos = lastidx

      self.output.see(tk.END)
      # self.output.tag_config("vol", background="white", foreground="red")
      
  # def highlight_pattern(self, pattern, tag, start="1.0", end="end",
  #                         regexp=False):
  #       '''Apply the given tag to all text that matches the given pattern

  #       If 'regexp' is set to True, pattern will be treated as a regular
  #       expression according to Tcl's regular expression syntax.
  #       '''

  #       start = self.index(start)
  #       end = self.index(end)
  #       self.mark_set("matchStart", start)
  #       self.mark_set("matchEnd", start)
  #       self.mark_set("searchLimit", end)

  #       count = tk.IntVar()
  #       while True:
  #           index = self.search(pattern, "matchEnd","searchLimit",
  #                               count=count, regexp=regexp)
  #           if index == "": break
  #           if count.get() == 0: break # degenerate pattern which matches zero-length strings
  #           self.mark_set("matchStart", index)
  #           self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
  #           self.tag_add(tag, "matchStart", "matchEnd")

  def Refresher(self):
      # global mycount
      self.mycount+=1
      print("refreshing " + str(self.mycount))
      self.txtout("Hello" + str(self.mycount))
      self.after(1000, self.Refresher) # every second...


# if __name__ == '__main__':
#     # print("start logoutput")
#     txtoutput=outputlog()
#     txtoutput.Refresher()
#     txtoutput.mainloop()

# exit()
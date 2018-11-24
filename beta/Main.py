#from tkinter import Tk, Frame,Label,Entry, BOTH, Listbox, StringVar, END, X,Button, LEFT
from tkinter import *
from tkinter import messagebox
import os 
import get_currency as cc
#from PIL import Image, ImageTK


class exFrame(Frame):
    
    def __init__(self, parent):
        '''
        
        '''
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
        
    
    
    def initUI(self):
        '''
        This function initilises the User Interface
         it defines how the user interface will look
         
        '''
      
        self.parent.title("Currency Converter")
        self.pack(fill=BOTH, expand=1)
        currencys = {'Dollar':'usd', 'Pound':'gbp','Euro':'eur','Yuan':'cny','Rand':'zar'}
##        imageCC1 = PhotoImage(file= "cc.gif")
##        image_label = Label(self, image=imageCC1)
##        image_label.pack(side = TOP)
        
        def about():
            os.system('open About.pdf')
#            subprocess.Popen(['About.pdf'],shell=True)
        def help_doc():
            os.system('open Help_doc.pdf')
            
        top = self.winfo_toplevel()
        self.menu_bar = Menu(top)
        top['menu'] = self.menu_bar
        self.sub_menu = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='HELP', menu=self.sub_menu)
        self.sub_menu.add_command(label='ABOUT', command = about)
        self.sub_menu.add_command(label='Help', command = help_doc)
        
#the items in the lst
        logo = Label(self, text ="Currency Converter", height = 3, width = 20)
        logo.pack(side = TOP)
        lb = Listbox(self)
        for i in currencys.keys():
            lb.insert(END, i)
        lb.bind("<<ListboxSelect>>", self.onSelect_lb1)
        lb.pack(side= LEFT,pady = 10, padx = 10)

        lb2 = Listbox(self)
        for i in currencys.keys():
            lb2.insert(END, i)
        lb2.bind("<<ListboxSelect>>", self.onSelect_lb2)
        lb2.pack(side= RIGHT, pady = 10, padx = 10)
        
#puts the items into the listbox 
##        self.var = StringVar()
##        self.label = Label(self, text=0, textvariable=self.var) 
##        self.label.pack()
        
#returns the selected item in the list box as an label
        self.cur_symbole = StringVar()
        self.cur_symbole2 = StringVar()
        self.symbole_label = Label(self,text = '', textvariable = self.cur_symbole)
        self.symbole_label.pack(side = LEFT)
        self.entry = StringVar()
        self.output1 = DoubleVar()

        
        
        to_convert = Entry(self, textvariable= self.entry, width = 6)
        to_convert.pack(side = LEFT, padx = 10)
#inserts the frame and the a entry box on to the frame 
        #print(self.entry.get())
        def push_button():
            result_of_textbox = self.entry.get()
            try:
                
      
                    curr1 = currencys[lb.get(self.index)]
                    curr2 = currencys[lb2.get(self.index2)]
                    print(curr1)
            except:
                msg = messagebox.showinfo("Error", "Please sellect a currencys to convernt")
            try:
                    converted = self.conversion(float(result_of_textbox),curr1,curr2)
            except:
                    print("try again, Please use digits")
                    msg = messagebox.showinfo("error", "plaese enter numbers only")
                #print(converted)
                           
               
                #checks if values entered are digets then returns the results of the conversion function

            
                
            #The push button function handels what happens when the convert button is pressed


        def exit_programe():
            quit()
        self.convert_button = Button(self,text = 'convert', command = push_button)
        self.convert_button.pack(side=LEFT,padx =5, pady = 5)
        self.rand_label = Label(self, text = "", textvariable = self.cur_symbole2)
        self.rand_label.pack(side=LEFT)
        self.output_label = Label(self, text = 0, textvariable = self.output1)
        self.output_label.pack(side = LEFT)
        self.exit_button = Button(self, text ='Exit', command = exit_programe, width = 10,height=10)
        self.exit_button.pack(side = BOTTOM)
        
    def onSelect_lb1(self, val):
      
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        #self.var.set(value)
        self.index = idx
        if value == 'Dollar':
            self.cur_symbole.set("$")
            
        elif value == 'Pound':
            
            self.cur_symbole.set("£")
        elif value == 'Euro':
            self.cur_symbole.set("€")
        elif value == 'Yuan':
            self.cur_symbole.set("¥")
        elif value == 'Rand':
            self.cur_symbole.set("R")
        

    def onSelect_lb2(self,val):
        
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        #self.var.set(value)
        self.index2 = idx
        if value == 'Dollar':
            self.cur_symbole2.set("$")
        elif value == 'Pound':
            self.cur_symbole2.set("£")
        elif value == 'Euro':
            self.cur_symbole2.set("€")
        elif value == 'Yuan':
            self.cur_symbole2.set("¥")
        elif value == 'Rand':
            self.cur_symbole2.set("R")
        
    #onSelect function displays which currecy Symbole has be selected to conversion.
    #it also provides a global vaiable that helps to get the index of the current selected item in the dictionary.

    def conversion(self,amount,selected_lb1,selected_lb2):
        #this fuction cheack for a connection, then checks if the user has not selected the same currency to convert
        try:
            if selected_lb1 != selected_lb2:
                
                curr = float(cc.currency.get_anycurr(selected_lb1,selected_lb2))
                converted = curr * amount
                self.output1.set(float("{0:.4f}".format(converted)))
                #this section gets the var selected_lb1 and 2 that should contain the value in the dict that is determined by the key selected in the push_buton method
                #then it mutiples the exchange rate between the two currencies by the amout specified in the entry box.
            else:
                msg = messagebox.showinfo("Error", 'you have selected the same currency, please dont')
        except:
            msg = messagebox.showinfo("Error", 'no connection "she\'s not the one :\'("')
def main():
  
    root = Tk()
    root.geometry("700x400+0+0")
    app = exFrame(root)
    root.mainloop()  
    


if __name__ == '__main__':
    main()

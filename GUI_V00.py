import sys,string
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
    
import tkFont, tkFileDialog
import matplotlib
matplotlib.use('TkAgg')

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class postprocessingHOST:
    def __init__(self,parent):
        
        # options for buttons
        button_opt = {'expand':Tk.YES,'fill':Tk.NONE,'anchor':Tk.CENTER,
                      'padx':'2m','pady':'2m','ipadx':'3m','ipady':'1m'}

        # Font
        font_name1 = "-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*"
        font_name2 = tkFont.Font(family='Times New Roman',size=13, weight='bold')

        # frame settings
        self.myParent = parent
        self.myParent.geometry("800x540")

         # Entry Values Frame -> Pop-up menu, imput text and scroll

        self.entryFrame = Tk.LabelFrame(self.myParent,text='Entry Values',
                                    labelanchor='nw',bd='2m')
        self.entryFrame.pack(side=Tk.TOP,expand=Tk.YES,fill=Tk.BOTH,
                            pady=5, ipady=5, padx=5, ipadx=5)
                            
        # Plot & Results Frame -> Cycle plot and work, mean pressure and
        #                         efficiency results
        
        self.plotFrame = Tk.LabelFrame(self.myParent,text='Results',
                                       labelanchor='nw',bd='2m')
        self.plotFrame.pack(side=Tk.TOP,expand=Tk.YES,fill=Tk.BOTH,
                            pady=5, ipady=5, padx=5, ipadx=5)

        #Pop-out menu 1: Select Fuel
        optionList = ["Avgas","Gasoil","Nafta Super", "Nafta Premium"]
        self.menuValue1 = Tk.StringVar(self.entryFrame)
        self.menuValue1.set(optionList[0])
        self.menuValue1.trace("e",self.plot_variable)
        self.myOptionMenu1 = Tk.OptionMenu(self.mainFrame,self.menuValue1,*optionList)
        self.myOptionMenu1.pack(side=Tk.LEFT,anchor='ne')
        
        # Entry Values

        
        # Plotting Area
        self.f = Figure(figsize=(5,4), dpi=100)
        self.a = self.f.add_subplot(111)
        self.a.set_title(optionList[0])
        self.a.set_xlabel('X axis label')
        self.a.set_ylabel('Y label')
        self.graphique, = self.a.plot([])
        self.canvas = FigureCanvasTkAgg(self.f, master=self.plotFrame)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        toolbar = NavigationToolbar2TkAgg( self.canvas, self.plotFrame )
        toolbar.update()
        self.canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
    def _reset_option_menu(self, OptionMenu, MenuValue, options, index=None):
        '''reset the values in the option menu

        if index is given, set the value of the menu to
        the option at the given index
        '''
        menu = OptionMenu["menu"]
        menu.delete(0, "end")
        for strings in options:
            menu.add_command(label=strings, 
                          command=lambda value=strings:
                                 MenuValue.set(value))
        if index is not None:
            MenuValue.set(options[index])
    
    # Opens file and charges menu and plot (design for for HOST
    # .HB_OBI or .OBSINST files)
    def askopenfile(self):
        input_file = tkFileDialog.askopenfile(mode='r', **self.file_opt)
        # Must read the file and put all variables into the pop-out Menu
        data = input_file.readlines()
        input_file.close()
        self.menuList = string.split(data[2])
        self.menuUnits = string.split(data[3])
        self.menuList1 = ["FX","FXH-RPF","FYH-RPF","FZH-RPF","FXH-RPR","FYH-RPR","FZH-RPR","PWF","PWR","PW1PW2","DT0F","DT0R"]
        self.menuList2 = self.menuList[0:]
        for word in self.menuList1:
            if word in self.menuList2:
                self.menuList2.remove(word)
            
        fline=data[4:len(data)-1]
        self.val_array = [] # premier indice = ligne et second colonne
        for line in fline:                                     
            aux1= line.split('SIMULATION')   
            aux2= aux1[0].split('INIT')
            aux3= aux2[0].split('TRIM')
            fsplit= aux3[0].split('RLX')  
            words = fsplit[0].split()                          
            values = [ float(word)  for word in words ]        
            self.val_array.append(values)                                                  

        self.timestep=(self.val_array[1][0] - self.val_array[0][0])
        self.np_total = len(self.val_array)

        self._reset_option_menu(self.myOptionMenu1,self.menuValue1,self.menuList1,0)
        self._reset_option_menu(self.myOptionMenu2,self.menuValue2,self.menuList2,0)
        
        temp = []
        psif = []
        col_abs = self.col_num('TEMPS',self.menuList)
        col_abs2 = self.col_num('PSIF',self.menuList)
          
        for list_ in self.val_array:
            temp.append(list_[col_abs])
            psif.append(list_[col_abs2])
            
        self.time = np.array(temp)
        self.psif = np.array(psif)
        
    def asksaveasfile(self):
        return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)


    def col_num(self,coeff,words):
        for ii in range(len(words)):
            if words[ii]==coeff:
                return (ii)


    def moy(self,L):
       l=len(L)
       m=0.
       for i in range(0,l):
           m=m+L[i]
       m=m/l
       return m
    
    def plot_variable(self,name,index, mode):
        selection =  root.getvar(name)
        data = []
        col_data = self.col_num(selection,self.menuList)
        for list_ in self.val_array:
            data.append(list_[col_data])
        if selection in ["FX","FXH-RPF","FYH-RPF","FZH-RPF",
                         "FXH-RPR","FYH-RPR","FZH-RPR"]:
            data = [x*10 for x in data]
            unit = "N"
        else:
            unit = self.menuUnits[col_data]
        DATA = np.array(data)
        self.a.set_title(selection)
        self.a.set_xlabel('Time [sec]')
        self.a.set_ylabel(selection+' ['+unit+']')
        self.a.set_xlim((min(self.time),max(self.time)))
        self.a.set_ylim((min(data),max(data)))
        self.graphique.set_xdata(self.time)
        self.graphique.set_ydata(DATA)
        self.canvas.draw()

        

root = Tk.Tk()
root.wm_title("HOST pre & post processing tool")
app = postprocessingHOST(root)
root.mainloop()


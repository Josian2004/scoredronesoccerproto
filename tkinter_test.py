import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string




class ConfigWindow:
    def __init__(self):
        self.colorlist = [
            "Red",
            "Green",
            "Yellow",
            "Blue",
            "Orange"
        ]
        self.ShowConfig()



    def CloseConfigWindow(self, configwindow):
        configwindow.destroy()

    def ConfigDone(self, configwindow, entryteam1, entryteam2, combocolor1, combocolor2):
       
        teamname1 = entryteam1.get() + " (1)"
        teamname2 = entryteam2.get() + " (2)"
        color1 = combocolor1.get()
        color2 = combocolor2.get()

        if teamname1 == " (1)":
            teamname1 = "Team 1"
        if teamname2 == " (2)":
            teamname2 = "Team 2"

        if color1 not in self.colorlist:
            messagebox.showerror("Color Error", "Please select a color from the dropdown menu")
            return
        if color2 not in self.colorlist:
            messagebox.showerror("Color Error", "Please select a color from the dropdown menu")
            return
        if color1 == color2:
            messagebox.showerror("Same Color Error", "The two colors can't be the same, choose a different color")
            return

        teamname1 = string.capwords(teamname1)
        teamname2 = string.capwords(teamname2)

        
        self.CloseConfigWindow(configwindow)
        Window(teamname1, teamname2, color1, color2)

    
    def CreateWidgetsConfig(self, configwindow):
        enterteam1 = tk.Label(
            configwindow, 
            text="Enter the name of Team 1", 
            font=("arial", 13), 
            borderwidth=1, relief="solid", 
            width="25", height="2"
            )
        enterteam1.grid(row=0, column=0, columnspan=2)

        enterteam2 = tk.Label(
            configwindow, 
            text="Enter the name of Team 2", 
            font=("arial", 13), 
            borderwidth=1, relief="solid", 
            width="25", height="2"
            )
        enterteam2.grid(row=0, column=2, columnspan=2)

        entryteam1 = tk.Entry(
            configwindow,
            font=("arial", 13),
            borderwidth=1, relief="solid",
            width="25"
        )
        entryteam1.grid(row=1, column=0, columnspan=2)

        entryteam2 = tk.Entry(
            configwindow,
            font=("arial", 13),
            borderwidth=1, relief="solid",
            width="25"
        )
        entryteam2.grid(row=1, column=2, columnspan=2)

        combocolor1 = ttk.Combobox(configwindow, values=self.colorlist)
        combocolor1.grid(row=2, column=0, columnspan=2)

        combocolor2 = ttk.Combobox(configwindow, values=self.colorlist)
        combocolor2.grid(row=2, column=2, columnspan=2)

        savebutton = tk.Button(
            text="Save Configuration", 
            font=("arial", 16), 
            width="15", height="2", 
            command = lambda : self.ConfigDone(configwindow, entryteam1, entryteam2, combocolor1, combocolor2)
            )
        savebutton.grid(row=3, column=1, columnspan=2)

    


    def ShowConfig(self):
        configwindow = tk.Tk()
        configwindow.title("Configuration")
        configwindow.geometry("460x200")
        #configwindow.geometry("1000x1000")
        self.CreateWidgetsConfig(configwindow)
        configwindow.mainloop()















class Window:
    def __init__(self, teamname1, teamname2, color1, color2):
        self.current1 = 0
        self.current2 = 0
        self.ShowWindow(teamname1, teamname2, color1, color2)

    
    def addpoint1(self, window, score1, current1):
        score1.config(text=self.current1 + 1)
        self.current1 = self.current1 + 1

    def addpoint2(self, window, score2, current2):
        score2.config(text=self.current2 + 1)
        self.current2 = self.current2 + 1


    def removepoint1(self, window, score1, current1):
        if self.current1 != 0:
            score1.config(text=self.current1 - 1)
            self.current1 = self.current1 - 1

    def removepoint2(self, window, score2, current2):
        if self.current2 != 0:
            score2.config(text=self.current2 - 1)
            self.current2 = self.current2 - 1
        

    def CreateWidgetsWindow(self, window, teamname1, teamname2, color1, color2):
        
        lbscore1 = tk.Label(
            window, 
            text=f"Score of {teamname1}", 
            font=("arial", 16), 
            borderwidth=1, relief="solid", 
            width="30", height="2"
            )
        lbscore1.grid(row=0, column=0, columnspan=2)

        lbscore2 = tk.Label(
            window, 
            text=f"Score of {teamname2}", 
            font=("arial", 16), 
            borderwidth=1, relief="solid", 
            width="30", height="2"
            )
        lbscore2.grid(row=0, column=2, columnspan=2)

        panelcolor1 = tk.Label(
            window,
            font=("arial", 16),
            borderwidth=1, relief="solid", 
            width="30", height="1",
            bg=color1
            )
        panelcolor1.grid(row=1, column=0, columnspan=2)

        panelcolor2 = tk.Label(
            window,
            font=("arial", 16),
            borderwidth=1, relief="solid", 
            width="30", height="1",
            bg=color2
            )
        panelcolor2.grid(row=1, column=2, columnspan=2)

        score1 = tk.Label(
            window, 
            text=self.current1, 
            font=("arial", 30), 
            borderwidth=1, relief="solid", 
            width="14", height="5"
            )
        score1.grid(row=2, column=0, columnspan=2)

        score2 = tk.Label(
            window, 
            text=self.current2, 
            font=("arial", 30), 
            borderwidth=1, relief="solid", 
            width="14", height="5"
            )
        score2.grid(row=2, column=2, columnspan=2)

        addscore1 = tk.Button(
            text="+", 
            font=("arial", 16), 
            width="8", height="3", 
            command = lambda : self.addpoint1(window, score1, self.current1)
            )
        addscore1.grid(row=3, column=1)

        addscore2 = tk.Button(
            text="+", 
            font=("arial", 16), 
            width="8", height="3", 
            command = lambda : self.addpoint2(window, score2, self.current2)
            )
        addscore2.grid(row=3, column=3)


        removescore1 = tk.Button(
            text="-", 
            font=("arial", 16), 
            width="8", height="3", 
            command = lambda : self.removepoint1(window, score1, self.current1)
            )
        removescore1.grid(row=3, column=0)

        removescore2 = tk.Button(
            text="-", 
            font=("arial", 16), 
            width="8", height="3", 
            command = lambda : self.removepoint2(window, score2, self.current2)
            )
        removescore2.grid(row=3, column=2)
        







    

    def ShowWindow(self, teamname1, teamname2, color1, color2):
        window = tk.Tk()
        window.title("Score Counter")
        window.geometry("1000x600")
        #window.configure(bg="white")
        #window.state("zoomed")
        self.CreateWidgetsWindow(window, teamname1, teamname2, color1, color2)



        
        window.mainloop()
        


    






ConfigWindow()





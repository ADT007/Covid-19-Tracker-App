from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image



#================================user Interface Design============================
root = Tk()
root.iconphoto(False, tk.PhotoImage(file="logo.png"))
root.geometry("750x600")
root.title("COVID 19 Tracker App")
root.resizable(False, False)
root['background'] = 'LIGHTSTEELBLUE'
canvas = Canvas(width=596, height=296)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("z.jpg"))
canvas.create_image(1, 1, anchor=NW, image=img)
#================================End User Interface=================================

#=========================Now Coding the functionality of App========================
def showData():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mp
    from covid import Covid
    covid = Covid()
    cases = []
    confirmed = []
    active = []
    recovered = []
    deaths = []

    try:
        root.update()
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")

        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()

        for y in cases:
            confirmed.append(y["confirmed"])
            active.append(y["active"])
            recovered.append(y["recovered"])
            deaths.append(y["deaths"])

        # #======== making patches==================
        confirmed_patch = mpatches.Patch(color='black', label='Confirmed')
        recovered_patch = mpatches.Patch(color='green', label='Recovered')
        active_patch = mpatches.Patch(color='red', label='Active')
        deaths_patch = mpatches.Patch(color='orange', label='Deaths')
        plt.legend(handles=[confirmed_patch,recovered_patch,active_patch,deaths_patch])

        #================ploting the images in graph=================
        for x in range(len(country_names)):
            plt.bar(country_names[x], confirmed[x], color='black')
            if recovered[x] > active[x]:
                plt.bar(country_names[x], recovered[x], color='green')
                plt.bar(country_names[x], active[x], color='red')
            else:
                plt.bar(country_names[x], active[x], color='red')
                plt.bar(country_names[x], recovered, color='green')

        plt.bar(country_names[x], deaths[x], color='orange')
        plt.title('Current Covid !9 Case Status By Adarsh')
        plt.xlabel('Country Name')
        plt.ylabel('cases(in Millions)')
        plt.show()

    except Exception as e:
        messagebox.showwarning("Warning","Please fill the correct information in the box.ThankYou")

#====================================collecting the query from user==================
Label(root, text="Enter the name of the Country\nto get it's Covid-19 Statistics", font="Consolas 19 bold",
      bg='LIGHTSTEELBLUE',fg="black").pack()
Label(root, text="\n Enter Country Name", font="Consolas 18 bold", bg='LIGHTSTEELBLUE',
      fg="black").pack()
data = StringVar()
data.set("")
entry = Entry(root, textvariable=data, font="calibre 20 bold", bg='LIGHTSTEELBLUE',width=30).pack()
Label(root, bg='LIGHTSTEELBLUE').pack()
Button(root, text="Get Data", font="Consolas 15 bold", height=2, width=10, bg="LIGHTSTEELBLUE", fg="blue",
       command=showData).pack()
Label(root, text="App Build in Python and Developed By - Aadrsh Tripathi", font="Consolas 14 bold", bg='LIGHTSTEELBLUE',
      fg="black").pack(side=BOTTOM)



#==========================End of Funation============================================

root.mainloop()
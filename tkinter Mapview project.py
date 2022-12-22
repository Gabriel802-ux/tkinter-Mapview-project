#als Paket wird tkinter ausgewählt 
from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
import tkintermapview
import geocoder
import geopy
import folium
from geopy import distance
import haversine as hs


#das Fenster erstellen 
fenster = Tk()
fenster.geometry("550x680") #Abmessungen des Fensters
fenster.title("Kartenerstellung") #Titel für das Programmfenster

#Label erstellen 
label_1 = Label(fenster, wraplength = 500, text= "Informationen zur Benutzung der Oberfläche: Geben Sie den Ortsnamen, die Postleitzahl oder die passenden Koordinaten ein.", relief = 'solid', borderwidth = 1,  bg = '#999932', font= ('Arial 10 bold'), width= 64, height = 2)
label_1.place(x=20, y=30)

#Textfeld erstellen 
textfeld_1 = Combobox(fenster,value=["Black and White","Standard", "Satellit"], font = ('Arial 10 bold'), width= 32)
textfeld_1.place(x=20,y=78)





textfeld_2 = tk.Entry(fenster, width=29, relief = 'solid', borderwidth = 1, font = ('Arial 10 bold'))
textfeld_2.place(x=277,y=79)

def switch_layer():
    

    try:
       
        x = textfeld_1.get()
        if x == "Black and White":
            map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png")
        elif x == "Satellit":
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif x == "Standard":
            map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        else:
            pass
        get_input()
    except:
        pass





#Definition erstellen
def get_input():
    try:
        

        ortList.append(textfeld_2.get())
        map_widget.set_address(textfeld_2.get(), marker = True)
        viewSelected()
 


        fenster.mainloop()

    except: 
        pass


ortList = []


def viewSelected():
    kl_list = [geocoder.osm(i).latlng for i in ortList]
    kl_list2=[tuple(x) for x in kl_list]
    choice  = textfeld_3.get()
    print(ortList)
    print(kl_list2)
    distanz=sum([round(hs.haversine(kl_list2[i],kl_list2[i+1]),2) for i in range(len(kl_list)-1)])
    print(distanz)
    
       
    if choice == "Distanz anzeigen":
        label_10 = Label(fenster, width=32, text=f"{distanz}km", relief = 'solid', borderwidth = 1,  bg = 'white', font= ('Arial 10 bold'))
        label_10.place(x=277, y=140)
        #map_widget.set_adress([distance.distance(geocoder.osm(i).latlng for i in ortList)]).km
         
    elif choice == "Verbindungslinie hinzufügen":
       map_widget.set_path([geocoder.osm(i).latlng for i in ortList])
    else:
        pass





#Definition erstellen
def get_zusatzoptionen():
    fenster.mainloop()

#Button "Add" erstellen 
button_1 = tk.Button(fenster, text="Add", font = ('Arial 8 bold'), relief = 'solid', borderwidth = 1,  width=5, height=1, bg = '#999932', command = switch_layer )
button_1.place(x=493, y=77)

#Label erstellen 
label11 = Label(fenster, relief = 'sunken')
label11.place(x=1, y=100)

#Label erstellen 
label2 = Label(fenster, text="Zusatzoptionen", bg = '#999932', bd=0, relief = 'solid', borderwidth = 1, font= ('Arial 10 bold'), width = 64)
label2.place(x=20, y=110)

#v = tk.IntVar()
#v.set(1)

#Nummer 1
#button_2 = Radiobutton(fenster, variable = v, value = 1, anchor='w',  text='Verbindungslinie hinzufügen', font= ('Arial 10 bold'))
#button_2.place(x=20, y=140, width=210, height=20)

#Nummer 2
#button_3 = Radiobutton(fenster, variable = v, value = 2, anchor='w', text='Distanz anzeigen', font= ('Arial 10 bold'))
#button_3.place(x=300, y=140, width=210, height=20)


#Nummer 3
textfeld_3 = Combobox(fenster, value= [ "Distanz anzeigen", "Verbindungslinie hinzufügen"], font= ('Arial 10 bold'), width= 32)
textfeld_3.place(x=20, y =140, width = 247, height = 20)

#Nummer 3
#button_4 = Radiobutton(fenster, variable = v,  value = 3, anchor='w',  text='Layer-Control hinzufügen', font= ('Arial 10 bold'))
#button_4.place(x=20, y=170, width=210, height=20)

#Nummer 4
#button_5 = Radiobutton(fenster, variable = v, value = 4, anchor='w',  text='Marker durch Punkte ersetzen', font= ('Arial 10 bold'))
#button_5.place(x=300, y=170, width=230, height=20)


# create map widget
map_widget = tkintermapview.TkinterMapView(fenster, relief = 'solid', borderwidth = 1, width=513, height= 430, corner_radius=0)

# map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# google satellite
#map_widget.set_tile_server("http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.png")  # painting style
map_widget.place(x=278, y=385, anchor = tk.CENTER)
map_widget.set_position(52.516374, 13.378000)  #Berlin, Deutschland
map_widget.set_zoom(13)


map_widget.add_right_click_menu_command(label = 'Add Info',command=switch_layer)

def clear():
    global map_widget
    map_widget.destroy()
    map_widget = tkintermapview.TkinterMapView(fenster, relief = 'solid', borderwidth = 1, width=513, height= 430, corner_radius=0)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map_widget.place(x=278, y=385, anchor = tk.CENTER)
    map_widget.mainloop()


  


    
    

button_6 = tk.Button(fenster, text="zurücksetzen", command = (lambda: clear()), font = ('Arial 10 bold'), relief = 'solid', borderwidth = 1, width=31, height=2, bg = '#999932')
button_6.place(x=20, y=615)

    

button_7 = tk.Button(fenster, text="schließen", font = ('Arial 10 bold'), width=31, relief = 'solid', borderwidth = 1, height=2, bg = '#999932',command= (lambda: fenster.destroy()))
button_7.place(x=280, y=615)

#Befehle ausführen; das Fenster starten
fenster.mainloop()

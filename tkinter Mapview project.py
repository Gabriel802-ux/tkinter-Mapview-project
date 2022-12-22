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

#Funktion der Auswahl der Map anzeige
#Definition erstellen
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
#Funktion mit Ausgabe der Marker
#Definition erstellen
def get_input():
    try:
        

        ortList.append(textfeld_2.get())
        map_widget.set_address(textfeld_2.get(), marker = True)
        viewSelected()
 


        fenster.mainloop()

    except: 
        pass


#Funktion mit  verschiedenen Angaben distanzen und Verbindungslinien
#Definition erstellen
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

#Funktion für die  Ausführung Map zurücksetzen
#Definition erstellen
def clear():
    global map_widget
    map_widget.destroy()
    map_widget = tkintermapview.TkinterMapView(fenster, relief = 'solid', borderwidth = 1, width=513, height= 430, corner_radius=0)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map_widget.place(x=278, y=385, anchor = tk.CENTER)
    map_widget.mainloop()


# create map widget
map_widget = tkintermapview.TkinterMapView(fenster, relief = 'solid', borderwidth = 1, width=513, height= 430, corner_radius=0)
map_widget.place(x=278, y=385, anchor = tk.CENTER)
map_widget.set_position(52.516374, 13.378000)  #Berlin, Deutschland
map_widget.set_zoom(13)
map_widget.add_right_click_menu_command(label = 'Add Info',command=switch_layer)



#Label1 erstellen Für die Bezeichnung des Fenster
label_1 = Label(fenster, wraplength = 500, text= "Informationen zur Benutzung der Oberfläche: Geben Sie den Ortsnamen, die Postleitzahl oder die passenden Koordinaten ein.", relief = 'solid', borderwidth = 1,  bg = '#999932', font= ('Arial 10 bold'), width= 64, height = 2)
label_1.place(x=20, y=30)

#Label2 erstellen für die  "Zusatzoptionen" 
label2 = Label(fenster, text="Zusatzoptionen", bg = '#999932', bd=0, relief = 'solid', borderwidth = 1, font= ('Arial 10 bold'), width = 64)
label2.place(x=20, y=110)

#Textfeld1  für die Auswahl der Map ansicht erstellen 
textfeld_1 = Combobox(fenster,value=["Black and White","Standard", "Satellit"], font = ('Arial 10 bold'), width= 32)
textfeld_1.place(x=20,y=78)

#Textfeld2  Eintrag für das suchobject in der Map
textfeld_2 = tk.Entry(fenster, width=29, relief = 'solid', borderwidth = 1, font = ('Arial 10 bold'))
textfeld_2.place(x=277,y=79)

#Textfeld3 erstellen mit den jeweiligen Auswahl
textfeld_3 = Combobox(fenster, value= [ "Distanz anzeigen", "Verbindungslinie hinzufügen"], font= ('Arial 10 bold'), width= 32)
textfeld_3.place(x=20, y =140, width = 247, height = 20)

#Button1 "Add" erstellen 
button_1 = tk.Button(fenster, text="Add", font = ('Arial 8 bold'), relief = 'solid', borderwidth = 1,  width=5, height=1, bg = '#999932', command = switch_layer )
button_1.place(x=493, y=77)

#Button2 "zürücksetzen" erstellen 
button_2 = tk.Button(fenster, text="zurücksetzen", command = (lambda: clear()), font = ('Arial 10 bold'), relief = 'solid', borderwidth = 1, width=31, height=2, bg = '#999932')
button_2.place(x=20, y=615)

    
#Button3 "schließen" erstellen 
button_3 = tk.Button(fenster, text="schließen", font = ('Arial 10 bold'), width=31, relief = 'solid', borderwidth = 1, height=2, bg = '#999932',command= (lambda: fenster.destroy()))
button_3.place(x=280, y=615)



#Befehle ausführen; das Fenster starten
fenster.mainloop()



from tkinter import *
from tkinter import ttk
from geopy.geocoders import Nominatim


def get_lati_longi(arg):
    address = name_address.get()
    geolocator = Nominatim(user_agent="closestpointscs50p")
    location = geolocator.geocode(address)
    lat_lon.set(f"{location.latitude},{location.longitude}")


root = Tk()
root.title("Get latitude and longitude")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

name_address = StringVar()
address_entry = ttk.Entry(mainframe, width=30, textvariable=name_address)
address_entry.grid(column=2, row=1, sticky=(W, E))

lat_lon = StringVar()
ttk.Label(mainframe, textvariable=lat_lon).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Search", command=get_lati_longi).grid(
    column=2, row=3, sticky=E
)

ttk.Label(mainframe, text="Address: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Lat n Lon: ").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): #run through all mainframe subclass and apply padding
    child.grid_configure(padx=5, pady=5)

address_entry.focus() # pointer on the address entry frame when starting
root.bind("<Return>", get_lati_longi)


root.mainloop()

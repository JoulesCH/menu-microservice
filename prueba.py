Platillos=[
    {"Cafeteria_ID":9, "Platillo_ID":1, "Nombre":"Hamburguesa", "Precio":50},
    {"Cafeteria_ID":9, "Platillo_ID":2, "Nombre":"Molletes", "Precio":30},
    {"Cafeteria_ID":9, "Platillo_ID":3, "Nombre":"Chilaquiles", "Precio":60},
    {"Cafeteria_ID":6, "Platillo_ID":1, "Nombre":"Hotdog", "Precio":25},
    {"Cafeteria_ID":6, "Platillo_ID":2, "Nombre":"Papas", "Precio":30},
    {"Cafeteria_ID":7, "Platillo_ID":1, "Nombre":"Agua", "Precio":10}
]

keyValList =9
lista=list(filter(lambda d: d['Cafeteria_ID']==keyValList, Platillos))
lista_size=len(lista)
print(lista_size)
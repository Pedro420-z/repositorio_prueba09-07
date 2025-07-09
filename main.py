productos = {
    "8475HD":["HP", "15,6", "8GB", "DD", "1T", "Intel Core I5", "Nvidia GTX1050"],
    "2175HD":["Lenovo", "14", "4GB", "SSD", "512GB", "Intel Core I5", "Nvidia GTX1050"],
    "JjFHD":["ASUS", "14", "16GB", "SSD", "256GB", "Intel Core I7", "Nvidia RTX2080TI"],
    "fgdxFHD": ["HP", "15.6", "8GB", "DD", "1T", "Intel Core i3", "integrada"],
    "GF75HD": ["ASUS", "15.6", "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
    "123FHD": ["lenovo", "14", "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["lenovo", "15.6", "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", "15.6", "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"]
}

stock= {
    "8475HD":["387990","10"],"2175HD":["327990","4"],"JjfFHD": ["424990","1"],
    "fgdxFHD":["664990","21"], "123FHD": ["290890","32"], "342FHD": ["444990","7"],
    "GF75HD":["749990","2"], "UWU131HD": ["349990","1"], "FS1230HD": ["249990","0"],    
}

while True:
    
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca")
    print("2. Busqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")


    opcion=int(input("ingrese una opcion: "))
    if opcion ==1:
        marca=input("ingrese marca a consultar: ")
        if marca == "HP":
            print(stock["8475HD"]), print(stock["fgdxFHD"])
        elif marca =="Lenovo":
            print(stock["2175HD"]), print(stock["342FHD"])
        elif marca =="ASUS":
            print(stock["GF75HD"]), print(stock["JjFDH"])
        elif marca =="Dell":
            print(stock["UWU131HD"])
        else:
            print("opcion ingresada no valida, intente nuevmente...")
    elif opcion == 2:
        p_min=int(input("ingrese el monto minimo: "))
        p_max=int(input("ingrese el monto maximo: "))
        for busqueda_precios in range:
            print(stock) in range (p_min),(p_max)
    elif opcion ==3:
        actualizacion=int(input("ingrese el modelo a actualizar: "))
    stock.update()
else:
    print("programa finalizado")
    

    
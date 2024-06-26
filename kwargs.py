def get_product(**datos):
    print(datos["id"], datos["nombre"], datos["desc"])
    

get_product(id="id", 
            nombre="iphone",
             desc="esto es un iphone" )
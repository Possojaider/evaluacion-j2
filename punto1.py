edad=0

while edad>=0:
    
    
    edad=int(input("Ingrese su edad"))
    
    if edad >= 18:
                print("puede ingresar solo")
    elif edad >= 12 and edad <=17:
                print("puede ingresar con acompañante.")
    elif edad < 12:
                print("No puede ingresar")
    else:
        break
            
       
    
    
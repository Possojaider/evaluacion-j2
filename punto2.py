nombre = input("Ingrese su nombre")

print("normal")
print("premium")
print("vip")
tipo_cliente = input("¿Que tipo de cliente es?")

valorCompra=int(input("Ingrese el valor de la compra"))





if tipo_cliente == "normal" and valorCompra >= 500000:
    print("Descuento de 5%")
    descuento = valorCompra*0.05
    totalPagar = valorCompra - descuento
    print("total a pagar:",totalPagar)

            
elif tipo_cliente == "normal":
            print("Sin descuento")
            print("total a pagar", valorCompra)
            
            
   
if tipo_cliente == "premium" and valorCompra >= 500000:
            print("Descuento de 15%")
            descuento = valorCompra*0.15
            totalPagar = valorCompra - descuento
            print("total a pagar:",totalPagar)
            
elif tipo_cliente == "premium":
    print("Descuento de 10%")
    print("total a pagar:",totalPagar)
            
    
if tipo_cliente == "vip" and valorCompra >= 500000:
            print("Descuento de 25%")
            descuento = valorCompra*0.25
            totalPagar = valorCompra - descuento
            print("total a pagar:",totalPagar)
            
elif tipo_cliente == "vip":
            print("Descuento de 20%")
            print("total a pagar:",totalPagar)
            
            

            
            
    
            

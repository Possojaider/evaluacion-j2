while(True):
    nombre = input("Ingese su nombre")
    nota1=int(input("Ingrse la primer nota"))
    nota2=int(input("Ingrese la segunda nota"))
    nota3=int(input("Ingre la tercer nota"))
    
    sumaNotas= nota1+nota2+nota3
    promedio = sumaNotas/3
    
    if promedio >= 4.5:
        print("Excelente")
        print(f"Su promedio es:",promedio)
    if promedio>=3.8 and promedio <= 4.4:
        print("Bueno")
        print(f"Su promedio es:",promedio)
        
    if promedio >= 3.0 and promedio <= 3.7:
        print("Aceptable")
        print(f"Su promedio es:",promedio)
    
    if promedio < 3.0:
        print("Reprobado")
        print(f"Su promedio es:",promedio)
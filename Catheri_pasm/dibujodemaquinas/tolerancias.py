def calcular_tolerancia(medida, grado_iso):
   
    tabla_tolerancias = {
        "H7": 0.018,
        "H8": 0.030,
        "H9": 0.046,
        "H10": 0.074,
        "H11": 0.110,
        "H12": 0.175,
        "G6": 0.010,
        "G7": 0.018,
        "G8": 0.030,
      
    }

   
    if grado_iso in tabla_tolerancias:
            tolerancia = tabla_tolerancias[grado_iso]
            tolerancia_superior = medida + tolerancia
            tolerancia_inferior = medida - tolerancia
            return tolerancia_superior, tolerancia_inferior
    else:
        
            return None, None
medida = float(input("Ingresa la medida en milímetros: "))
grado_iso = input("Ingresa el grado ISO de tolerancia (por ejemplo, H7): ")

tolerancia_superior, tolerancia_inferior = calcular_tolerancia(medida, grado_iso)

if tolerancia_superior is not None:
    print(f"Tolerancia para {grado_iso}: {tolerancia_superior} mm (superior) / {tolerancia_inferior} mm (inferior)")
else:
    print("Grado ISO de tolerancia no válido.")

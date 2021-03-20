miDiccionario = {"Alemania": "Berlin", "Francia":"París", "Perú":"Lima"}
miDiccionario["Paraguay"]="Asunción" #annadir elemento
miDiccionario["Italia"]="Lisboa"
print(miDiccionario["Alemania"])#listar elemento
print(miDiccionario["Perú"])
print(miDiccionario) #listar diccionario
miDiccionario["Italia"]="Roma"  #modificar elemento
print(miDiccionario)
del miDiccionario["Italia"] #eliminar elemento
print(miDiccionario)
print(miDiccionario.keys()) #obtener claves
print(miDiccionario.values()) #obtener values
print(len(miDiccionario))

miTupla=("hola", "mundo", "wilson",13,1,1995)
miLista = list(miTupla) #convierte tupla a lista
miTupla2 = tuple(miLista) #convierte lista en tupla
print(miTupla[1])
print(miLista)
print(miTupla2)
print(13 in miTupla) #busca si existe un elemente en la tupla
print(miTupla.count(13)) #cuenta cuantas veces encuentra un elmento
print(len(miTupla))#cuanto elementos hay
miTuplaUnitaria=("Juan",)
print(len(miTuplaUnitaria))
miTuplaSinParentesis="Juan",13,1,1995 #empaquetado de tupla
print(miTuplaSinParentesis)
nombre, dia, mes, agno = miTuplaSinParentesis #desempaquetado de tupla
print(nombre)
print(dia)
print(mes)
print(agno)


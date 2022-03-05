from CLASES import area,productos,alojamiento
re=alojamiento.pick_recorrido()
n=productos.contar_filas()
i=0
rp=[]
cod=[]
while i<n:
    cod.append(i+1)
    i+=1
print("cod",cod)
rp2=productos.pick_posiciones(cod)

print("rp",rp2)
#print(re)



pick=alojamiento.pick_(rp2)
print("pick",pick)
i=0
j=0
print(n)
pick2=[]

while i< n:
   while j<n:
       prod=productos.buscar_prod_pick()
       pick2.append()
       print()
       j=j+1
j=0
i=i+1
print(pick2)


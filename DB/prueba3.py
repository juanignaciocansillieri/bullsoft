from CLASES import area,productos,alojamiento
re=alojamiento.pick_recorrido()
n=productos.contar_filas()
i=0
rp=[]
cod=[]
while i<n:
    p=productos.ver_posicion(i+1)
    #print(p)
    cod.append(i+1)
    rp.append(p)
    i+=1
rp2=[]
for data in rp:
    rp2.append(data[0][0])

print(rp2)
print(re)
#print(cod)

pick=alojamiento.pick_(rp2)
print(pick)
i=0
j=0
#print(n)
#pick2=[]
"""
while i< n:
   while j<n:
       pick2.append(productos.buscar_prod_pick(pick2[i],j))
       print(productos.buscar_prod_pick(i+1,j+1))
       j=j+1
j=0
i=i+1
print(pick2)
"""

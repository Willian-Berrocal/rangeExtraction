# Este programa recibe una lista de numeros en orden, y la devuelve formateada tal que a más de 3 consecutivos los
# acorta con un - entre el primero y el ultimo. Basicamente primero los agrupa, y luego cada grupo es puesto en la
# solucion.
# El tiempo de ejecucion es O(n), siendo n el len de la lista de input

nums = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
# nums = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
# nums = [-3,-2,-1,2,10,15,16,18,19,20]

groups = []

aux = []
last = None

for elem in nums:
    if last != elem-1:
        groups.append(aux)
        aux = []
    aux.append(str(elem))
    last = elem
groups.append(aux)

numsFormatted = ''

for group in groups:
    if len(group) > 2:
        numsFormatted += ',' + group[0] + '-' + group[-1]
    else:
        for elem in group:
            numsFormatted += ',' + elem

print(numsFormatted[1:])

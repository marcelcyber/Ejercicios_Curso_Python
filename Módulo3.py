#%% El valor asignado finalmente a x es igual a:
x = 1
x = x == x
print(x)
# R: True

#%% ¿Cuántos (*) enviará el siguiente fragmento de código a la consola?
i = 0
while i <= 3 :
    i += 2
    print("*")
# R: 2

#%% ¿Cuántos (*) enviará el siguiente fragmento de código a la consola?
i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")
# R:1

#%% ¿Cuántos (#) enviará el siguiente fragmento de código a la consola?
for i in range(1):
    print("#")
else:
    print("#")
# R: 2

#%% ¿Cuántos (#) enviará el siguiente fragmento de código a la consola?
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")
# R: 3

#%% ¿Cuántos (#) enviará el siguiente fragmento de código a la consola?

var = 1
while var < 10:
    print("#")
    var = var << 1
# R: 4

#%% ¿Qué valor será asignado a la variable x?
z = 10
y = 0
x = y < z and z > y or y > z and z < y
# R: True

#%% ¿Cuál es la output del siguiente fragmento de código?

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)
# R: 2

#%% ¿Cuál es la output del siguiente fragmento de código?

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

# R: 1

#%% ¿Cuál es la output del siguiente fragmento de código?

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

# R: [2]

#%% La segunda asignación:

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]

# R: Invierte la lista

#%% Después de la ejecución del siguiente fragmento de código, la suma de todos los elementos vals será igual a:

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]

# R: 4

#%% Observa el código, y selecciona las sentencias verdaderas: (Selecciona dos respuestas)

nums = [1, 2, 3]
vals = nums
del vals[1:2]

# R: nums y vals son de la misma longitud

#%% ¿Cuáles de los siguientes enunciados son verdaderos? (Selecciona dos respuestas)

nums = [1, 2, 3]
vals = nums[-1:-2]

# R: nums es más larga que vals.
# R: nums y vals son dos listas diferentes.

#%% ¿Cuál es la output del siguiente fragmento de código?

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

# R: [3, 2, 1]

#%% ¿Cuál es la output del siguiente fragmento de código?

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

# R: [1, 1, 1, 1, 2, 3]

#%% ¿Cuántos elementos contiene la lista my_list?

my_list = [i for i in range(-1, 2)]

# R: 3

#%% ¿Cuál es la output del siguiente fragmento de código?

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

# R: 6

#%% ¿Cuál es la output del siguiente fragmento de código?

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])

# R: el fragmento generará un error de ejecución



















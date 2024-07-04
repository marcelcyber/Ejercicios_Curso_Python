#%% ¿Cuál es el resultado del siguiente fragmento de código?

my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)

# R: [1, 1, 1, 2]

#%% ¿Cuáles de los siguientes enunciados son verdaderos respecto al código? (Selecciona dos respuestas)

nums = [1, 2, 3]
vals = nums

# R: nums tiene la misma longitud que vals
# R: nums y vals son diferentes nombres de la misma lista

#%% El siguiente fragmento de código:

def function_1(a):
    return None


def function_2(a):
    return function_1(a) * function_1(a)


print(function_2(2))

# R: Provocará un error de ejecución

#%% El resultado de la siguiente división:
v = 1 // 2
print(v)

# R: es igual a 0

#%% El siguiente fragmento de código:

def func(a, b):
    return b ** a


print(func(b=2)) # print(func(b=2, 2))

# R: es erróneo

#%% ¿Qué valor se asignará a la variable x?

z = 0
y = 10
x = y < z and z > y or y < z and z < y

# R: False

#%% ¿Cuál es el resultado del siguiente fragmento de código?

my_list =  [x * x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list))

# R: [0, 1, 4, 9]

#%% ¿Cuál es el resultado del siguiente fragmento de código?

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

# R: 1 1 2

#%% ¿Cuál es el resultado del siguiente fragmento de código?

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

# R: 0 1

#%% ¿Cuál es el resultado del siguiente fragmento de código?

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))

# R: 2

#%% Observa el fragmento de código y elige la sentencia verdadera:

nums = [1, 2, 3]
vals = nums
del vals[:]

# R: nums y vals tienen la misma longitud

#%% ¿Cuál es el resultado del siguiente fragmento de código si el usuario ingresa dos líneas que contienen 3 y 2 respectivamente?

x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)

# R: 0

#%% ¿Cuál es el resultado del siguiente fragmento de código si el usuario ingresa dos líneas que contienen 3 y 6 respectivamente?

y = input()
x = input()
print(x + y)

# R:63

#%% ¿Cuál es el resultado del siguiente fragmento de código?

print("a", "b", "c", sep="sep")

# R: asepbsepc

#%% ¿Cuál es el resultado del siguiente fragmento de código?

x = 1 // 5 + 1 / 5
print(x)

# R: 0.2

#%% ¿Cuál es el resultado del siguiente fragmento de código si el usuario ingresa dos líneas que contienen 2 y 4 respectivamente?

x = float(input())
y = float(input())
print(y ** (1 / x))

# R: 2.0

#%% ¿Cuál es el resultado del siguiente fragmento de código?

dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)

# R: one

#%% ¿Cuántos elementos contiene la lista lst?

lst = [i for i in range(-1, -2)]

# R: cero

#%% ¿Cuáles de las siguientes líneas correctamente invocan la función definida a continuación? (Selecciona dos respuestas)

def fun(a, b, c=0):
    # Cuerpo de la función.

# R: fun(b=0, a=0)
# R: fun(0, 1, 2)

#%% ¿Cuál es el resultado del siguiente fragmento de código?

 def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
    
print(fun(0, 3))

# R: 0

#%% ¿Cuántos (*) imprimirá el siguiente fragmento de código en la consola?

i = 0
while i < i + 2 :
    i += 1
    print("*")
else:
    print("*")

# el fragmento entrará en un bucle infinito, imprimiendo un * por línea

#%% ¿Cuál es el resultado del siguiente fragmento de código?

tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

# R: 4

#%% ¿Cuál es el resultado del siguiente fragmento de código?

dd = {"1": "0", "0": "1"}
for x in dd.vals():
    print(x, end="")

# R: el código es erróneo (el objeto dict no contiene el método vals())

#%% ¿Cuál es el resultado del siguiente fragmento de código?

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

# R: 21

#%% ¿Cuál es el resultado del siguiente fragmento de código?

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

# R: 4

#%% ¿Cuántos (#) imprimirá el siguiente fragmento de código en la consola?

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

# R: tres

#%% ¿Cuál es el comportamiento esperado del siguiente programa si el usuario ingresa 0?

try:
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")

# R: 0.0

#%% ¿Cuál es el comportamiento esperado del siguiente programa?
"""
try:
    print(5/0)
    break
except:
    print("Lo siento, algo salió mal...")
except (ValueError, ZeroDivisionError):
    print("Mala suerte...")
"""

# R: El programa generará una excepción y será manejada por el primer bloque except.

# %% ¿Cuál es el comportamiento esperado del siguiente programa?

foo = (1, 2, 3)
foo.index(0)

# R: El programa provocará una excepción ValueError.

#%% ¿Cuál de los siguientes fragmentos muestra la forma correcta de manejar múltiples excepciones en una sola cláusula except?
"""
# A:
 except (TypeError, ValueError, ZeroDivisionError):
    # Algo de código.

# B:
 except TypeError, ValueError, ZeroDivisionError:
    # Algo de código.

# C:
 except: (TypeError, ValueError, ZeroDivisionError)
    # Algo de código.

# D:
 except: TypeError, ValueError, ZeroDivisionError
    # Algo de código.

# E:
 except (TypeError, ValueError, ZeroDivisionError)
    # Algo de código.

# F:
 except TypeError, ValueError, ZeroDivisionError
    # Algo de código.
"""

# R: A solamente

#%% ¿Qué pasará cuando intentes ejecutar el siguiente código?

# print(¡Hola, Mundo!)

# R: El código generará la excepción SyntaxError.











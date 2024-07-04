#%% Una función definida de la siguiente manera:  (Elegir dos respuestas)
def function(x=0):
    return x
# R: puede ser invocado con exactamente un argumento.
# R: puede ser invocada sin ningún argumento.

#%% ¿Cuál es la salida del siguiente fragmento de código?

def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))

# R: 6

#%% ¿Cuál es la salida del siguiente fragmento de código?

def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)

# R: 4

#%% ¿Qué código insertarías en lugar del comentario para obtener el resultado esperado?

dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    # Inserta tu código aquí.

# R: print(k[0])

#%% El siguiente fragmento de código:

def func(a, b):
    return a ** a


print(func(2))


# R: es erróneo

#%% El siguiente fragmento de código:

def func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))

# R: dará como salida 16

#%% ¿Cuál es la salida del siguiente fragmento de código?

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return


print(fun(fun(2)) + 1)

# R: el código provocará un error de tiempo de ejecución

#%% ¿Cuál es la salida del siguiente fragmento de código?

def fun(x):
    global y
    y = x * x
    return y


fun(2)
print(y)


# R: 4

#%% ¿Cuál es la salida del siguiente fragmento de código?

def any():
    print(var + 1, end='')


var = 1
any()
print(var)

# R: 21

#%% ¿Cuál es la salida del siguiente fragmento de código?

my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'


print(my_list(my_list))

# R: no hay salida, el fragmento es erroneo

#%% ¿Cuál es la salida del siguiente fragmento de código?

def fun(x, y, z):
    return x + 2 * y + 3 * z


print(fun(0, z=1, y=3))

# R: 9

#%% ¿Cuál es la salida del siguiente fragmento de código?

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

# R: 4

#%% ¿Cuál es la salida del siguiente código?
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)

#%% ¿Cuál es la salida del siguiente código?

tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

# R: 2

#%% ¿Cuál es la salida del siguiente código?

try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")

# R: Entrada muy errónea...


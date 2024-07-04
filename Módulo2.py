#%% ¿Cuál es resultado desiguiente fragmento?
x = 1
y = 2
z = x
x = y
y = z
print(x, y)

# R: 2 1.

#%% ¿Cuál es el resultado del siguiente fragmento si el usuario ingresa dos líneas que contienen 2 y 4 respectivamente?
x = input()
y = input()
print(x + y)
# R: 24.

#%% ¿Cuál es el resultado del siguiente fragmento de código si el usuario ingresa dos líneas que contienen 2 y 4 respectivamente?
x = int(input())
y = int(input())

x = x // y
y = y // x

print(y)
# R: El código causará un error de ejecución.

#%% ¿Cuál es el resultado del siguiente fragmento si el usuario ingresa dos líneas que contienen 2 y 4 respectivamente?
x = int(input())
y = int(input())

x = x / y
y = y / x

print(y)
# R: 8.0

#%% ¿Cuál es el resultado del siguiente fragmento si el usuario ingresa dos líneas que contienen 11 y 4 respectivamente?
x = int(input())
y = int(input())

x = x % y
x = x % y
y = y % x

print(y)
# R: 1

#%% ¿Cuál es el resultado del siguiente fragmento si el usuario ingresa dos líneas que contienen 3 y 6 respectivamente?
x = input()
y = int(input())

print(x * y)

# R: 333333

#%% ¿Cuál es el resultado del siguiente fragmento?
z = y = x = 1
print(x, y, z, sep='*')

# R: 1*1*1

#%% ¿Cuál es el resultado del siguiente fragmento?
y = 2 + 3 * 5.
print(y) #==Y

# R: El fragmento provocará un error de ejecución

#%% ¿Cuál es el resultado del siguiente fragmento?
x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)

# R: 17.5

#%% ¿Cuál es el resultado del siguiente fragmento si el usuario ingresa dos líneas que contienen 2 y 4 respectivamente?
x = int(input())
y = int(input())

print(x + y)

# R: 6
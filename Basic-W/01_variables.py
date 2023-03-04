# Variables ---------------------------------------------------------------
my_var = "My String variable"
print(my_var)

my_int = 5
print(my_int)

my_int_to_str_var = str(my_int)  # Esta funcion convierte a String
print(my_int_to_str_var)
print(type(my_int_to_str_var))

my_bol = False

# Concatenacion de variables en un print
print(my_var, my_int, my_bol)
print("Este es el valor de:", my_bol)

# Algunas funciones del sistema---------------------------------------------------
print(len(my_var))  # Cuenta caracteres
print(type(my_int_to_str_var))  # Observar el tipo de dato
print(str(my_int))  # Conviete a String
print(int(my_int_to_str_var))  # Convierte a int

# Variables en una sola linea, se puede pero no es una buena práctica
name, surname, alias, age = "Walter", "Martin", "W", 24

print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es: ", alias)

#Input
nombre_input = input('Escribe tu nombre:')
print(nombre_input)

#Forzamos el tipado
#Pero se puede cambiar igual, podrias configurar el ide para que te de error
calle: str = "Niscalo"
calle = 6
print(calle)
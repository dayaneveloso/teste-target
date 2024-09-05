numero = int(input("Informe um número: "))

a = 0
b = 1

pertence = False

while b < numero:
    a = b
    b = a + b

if b == numero:
    pertence = True

if pertence: 
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
string_original = input("Digite a string que deseja inverter: ")

string_invertida = ""

for i in range(len(string_original) - 1, -1, -1):
    # Adiciona cada caractere à string invertida
    string_invertida += string_original[i]

print("A string invertida é:", string_invertida)
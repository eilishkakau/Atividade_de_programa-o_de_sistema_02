numeros = []

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

numeros.sort()

print("Números em ordem crescente:")
print(numeros)
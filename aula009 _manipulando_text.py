frase = "Curso em Video Python"

# Curso em Video Python
# 012345678901234567890
#           10        20

# 9 = inicio da string e 21 = posição 20 da string
print("resultado fatiamento:", frase[9:21])

#Mostra um e pula um caracter
print("resultado fatiamento:", frase[9:21:2])

#Mostra do inicio até a 4º posição = Curso
print("Terminando na posição 4:", frase[:5])

#Mostra o fim começando da posição 15 até o final
print("Comecando da posição 15:", frase[15:])

#Mostra um, pula dois começando da posição 9 até o fim
print("Mostra um pula dois:", frase[9::3])

#### Analise de String

#Quantidade de caracter na string
print("Tamanho da string:", len(frase))

#Começando da posição 0 até a posição 12
print("Quantidade de letra O: ", frase.count('o',0,13))

#Mostra a posição inicial do frase deo
print("Qual posiçao começa a string 'deo':", frase.find('deo'))

# retorna -1 para resultado negativo
print("Procurando palavra 'Android':", frase.find('Android'))

# Procura a palavra "Curso" na string
print("Procurando palavra 'Curso':", "Curso" in frase)

#Troca a palavra
print("Troca palavra Python por Android':", frase.replace('Python','Android'))

# Upper é um metodo
print("Coloca tudo para Maiusculo:", frase.upper())

print("Coloca tudo para Minisculo:", frase.lower())

print("Capitalize:", frase.capitalize())

print("title:", frase.title())

frase2 = "  aprenda python  "

print("Retirar espaços da frase:", frase2.strip())

print("Split apos cada espaço", frase.split())

#print("Join", '-', frase.join())

# Print com 3 aspas
print("""Print com tres aspas:
Nessa aula, vamos aprender operações com "
"String no Python. As principais operações que vamos aprender são o Fatiamento de String""")

print("Len retirando os epaços em split", len(frase.split()))

print("Len retirando os epaços strip", len(frase.strip()))

print("Len com replace", len(frase.replace('Python', 'Android')))

divido = frase.split()
print("Divido", divido[0][3])
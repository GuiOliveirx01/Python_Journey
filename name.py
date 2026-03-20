'''STRING: uma string é uma série de caracteres. Tudo que estiver
entre aspas é considerada uma string em Python, e você pode usar aspas simples ou duplas em torno das strings.''' 

name = "ada lovelace"
print(name.title())

'''O método title() aparece depois da variável
na instrução print(). Um método é uma ação que Python pode executar em
um dado. O ponto (.) após name em name.title() informa a Python que o
método title() deve atuar na variável name.'''

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# \t na frente de Python, deixa a mensagem mais fácil de ser lida na saída do terminal.

print("Python")
print("\tPython")

# \n faz uma quebra de linha que também ajuda a mensagem a ficar mais legível.

print("Languages:\nPython\nC\nJavaScript")

# Também é possível combinar tabulações e quebras de linha.

print("Languages:\n\tPython\n\tC\n\tJavaScript")





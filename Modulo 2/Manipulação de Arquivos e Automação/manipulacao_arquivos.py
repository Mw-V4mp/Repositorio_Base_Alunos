arquivo = open("texto.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
# with open("aula15.txt", "r", encoding="utf-8") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

with open("the_prince.txt", "r", encoding="utf-8") as arquivo:
    x = 0
    for linha in arquivo:
        print(f"Linha: {x} Conteúdo: {linha}")
        x = x + 1

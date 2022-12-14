import os

# os.chdir("../content/posts")
os.chdir("../old")

posts = [arquivo for arquivo in os.listdir() if arquivo.endswith(".md")]

for arquivo in posts:
    with open(arquivo) as post:
        conteudo = post.read()
        linhas = conteudo.split('\n')
        primeira_linha = linhas[0]
        if primeira_linha.startswith("Title"):
            primeira_linha = "---\n" + primeira_linha.replace("Title", "title")
        
        with open("../content/posts/" + arquivo, "w") as novo:
            novo.write(primeira_linha + "\n")
            fim_header = False
            for linha in linhas[1:]:
                # evita que eu encerre o header duas vezes
                if linha.startswith("---"): fim_header = True

                if linha.startswith("Date"): linha = linha.replace("Date", "date")[0:16]

                if len(linha.replace(" ", "")) == 0 and not fim_header:
                    linha = "---\n"
                    fim_header = True
                novo.write(linha + "\n")
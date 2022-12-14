---
title: Navegando em diretórios no Python
date: 2015-05-17
Author: Otávio Carneiro
Tags: python
Slug: Navegando-em-diretórios-no-Python
---

Para identificar o diretório atual (pwd):  
    import os  
    os.getcwd() \# cwd = current working directory

Para mudar de diretório (cd):  
    import os  
    path = '/my/path/'  
    os.chdir(path)

Para listar o conteúdo (ls):  
    import os  
    os.listdir() \#retorna um objeto do tipo list (lista), claro!




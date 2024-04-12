# %%

dados = {"nome":"Iure",
        "sobrenome":"Santiago",
        "idade":18,
        "ex":["Nah", "josefina", "elaine"],
        "filhos":[ {"nome":"maria", "idade":2}, {"nome":"raul", "idade":1} ]
        }

nome = dados["nome"]

print(nome)

print(dados['filhos'][0]["idade"])

# %%

dados.keys()
# %%

dados.values()
# %%

dados.items()
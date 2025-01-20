contatos = {"cassio@email.com": {"nome": "Cassio", "idade" : 40, "telefone": "9999-9999"}}
print(contatos)

copia = contatos.copy()
print(copia)

copia["cassio@email.com"]["nome"] = "Nicolas"
print(copia)
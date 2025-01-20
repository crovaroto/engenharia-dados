contatos = {"nome": "Cassio", "telefone": "9999-9999"}
print(contatos)

contatos.setdefault("nome", "Barbara")
print(contatos)

contatos.setdefault("idade", 40)
print(contatos)
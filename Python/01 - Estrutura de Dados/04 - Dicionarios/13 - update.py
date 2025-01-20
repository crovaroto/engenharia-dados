contatos = {"cassio@email.com": {"nome": "Cassio", "idade" : 40, "telefone": "9999-9999"}}
print(contatos)

contatos.update({"cassio@email.com": {"nome":"Zé"}})
print(contatos)

contatos.update({"nicolas@email.com": {"nome": "Nicolas", "idade": 6, "telefone": "1234-5678"}})
print(contatos)
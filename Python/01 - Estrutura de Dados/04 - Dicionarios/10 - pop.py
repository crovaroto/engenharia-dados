contatos = {"cassio@email.com": {"nome": "Cassio", "idade" : 40, "telefone": "9999-9999"},
            "nicolas@email.com": {"nome": "Nicolas", "idade": 6, "telefone": "1234-5678"}}
print(contatos)

resultado =  contatos.pop("cassio@email.com")
print(resultado)

resultado = contatos.pop("cassio@email.com", "não encontrado") 
print(resultado)


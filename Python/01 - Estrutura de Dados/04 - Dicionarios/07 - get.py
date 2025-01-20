contatos = {"cassio@email.com": {"nome": "Cassio", "idade" : 40, "telefone": "9999-9999"}}


print(contatos.get("chave"))
print(contatos.get("chave"), {})
print(contatos.get("cassio@email.com"), {})
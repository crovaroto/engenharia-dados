contatos = {"cassio@email.com": {"nome": "Cassio", "idade" : 40, "telefone": "9999-9999"},
            "nicolas@email.com": {"nome": "Nicolas", "idade": 6, "telefone": "1234-5678"}}

for chave in contatos:
  print(f"{chave} - {contatos[chave]}")

print("=" * 100)  

for chave, valor in contatos.items():
  print(chave, valor)
def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = 0
    qnt_vendas = len(vendas)
    
    for venda in vendas:
      total_vendas += venda
    
    media_vendas = total_vendas/qnt_vendas
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("Informe os valores de vendas, separados por vígula: ").split(',')
    # TODO: Converta a entrada em uma lista de inteiros:
    
    vendas = list(map(int, entrada))  
    print(vendas)
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))

def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    #for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem:
    #    if (max_count == 0) or (max_count < contagem[produto][count]):
    #      max_count = contagem.get(count)
       
    #max_produto = produtos[max_count]
    #return max_count
    print(contagem)
    return

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("=>")
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = entrada.lstrip(" ").split(',')
    
    print(produtos)
    return #produto

produtos = obter_entrada_produtos()
#print(produto_mais_vendido(produtos))
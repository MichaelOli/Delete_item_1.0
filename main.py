#lista
cidade= ['Ceilândia', 'Samambaia', 'Taguatinga', 'Gama']
print('Vou te apresentar algumas cidades e logo em seguida voce poderá deletar um item')
print(f'{'='*10}{cidade}{'='*10}')


#informa posição do item a ser deletado
while True:
    indice = int(input('Informe a posição do item a ser deletado: '))
    #evita que o usuário apague o ultimo item da lista caso o indice=0
    if indice >0:
        indice -=1
    else:
        indice = ''
        print('Por favor informe um número valido sendo que "1" representa o primeiro nome da lista e "4" o último número.')
        continue


#deleta item da lista
    try:
        del(cidade[indice])
    except:
        print('Não foi possivel deletar.')

    #Exibe a lista
    for cidades in cidade:
        print(cidades)



# GUILHERME BAPTISTA RM563425
# IAGO PAKAI HACKER RM561899
# PEDRO SILVA RM565746 (REPRESENTANTE)

contador = 0
desastres = {}

print('Tela de Cadastro de Desastres')

while True:

    desastre = input('Digite o tipo de desastre: ')
    pais = input('Digite o país que ocorreu o desastre: ')
    cidade = input('Digite a cidade que ocorreu o desastre: ')
    bairro = input('Digite o bairro que ocorreu o desastre: ')
    rua = input('Digite a rua que ocorreu o desastre: ')
    afetados = int(input('Digite o total de pessoas afetadas: '))
    print('Inserir a quantidade de pessoas em cada categoria de afetados.')

    crianca = int(input('Digite a quantidade de crianças afetadas: '))
    adulto = int(input('Digite a quantidade de adultos afetadas: '))
    idoso = int(input('Digite a quantidade de idosos afetadas: '))
    mob_reduzida = int(input('Digite a quantidade de pessoas com mobilidade reduzida afetadas: '))
    feridos = int(input('Digite a quantidade de feridos: '))
    soma_total = crianca + adulto + idoso + mob_reduzida + feridos

    if afetados != soma_total:
        print('A soma total não é igual ao total de afetados, verificar os dados inseridos!')
        continue

    lista = [desastre, pais, cidade, bairro, rua, afetados, crianca, adulto, idoso, mob_reduzida, feridos]
    contador += 1
    desastres[f'--- Desastre ---{contador}'] = lista

    continuar = input('Deseja cadastrar outro desastre? (Sim/Não): ')
    if continuar.lower() != 'sim':
        break
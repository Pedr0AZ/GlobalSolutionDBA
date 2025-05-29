# GUILHERME BAPTISTA RM563425
# IAGO PAKAI HACKER RM561899
# PEDRO SILVA RM565746 (REPRESENTANTE)

contador = 0
desastres = {}
total_criancas = 0
total_adultos = 0
total_idosos = 0
total_reduzida = 0
total_feridos = 0
total_afetados = 0
maior_afetados = 0
maior_desastre = {}

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

    total_afetados += afetados
    total_criancas += crianca
    total_adultos += adulto
    total_idosos += idoso
    total_reduzida += mob_reduzida
    total_feridos += feridos


    if afetados > maior_afetados:
        maior_afetados = afetados
        maior_desastre = {
            'rua': rua,
            'bairro': bairro,
            'cidade': cidade,
            'pais': pais
        }


    lista = [desastre, pais, cidade, bairro, rua, afetados, crianca, adulto, idoso, mob_reduzida, feridos]
    contador += 1
    desastres[f'--- Desastre ---{contador}'] = lista


    continuar = input('Deseja cadastrar outro desastre? (sim/não): ')
    if continuar.lower() != 'sim':
        break


print('\n--- Relatório Final ---')
print(f'\nTotal de desastres registrados: {contador}')
print(f'Total de pessoas afetadas: {total_afetados}')
print(f'Total de crianças afetadas: {total_criancas}')
print(f'Total de adultos afetados: {total_adultos}')
print(f'Total de idosos afetados: {total_idosos}')
print(f'Total de pessoas com mobilidade reduzida afetadas: {total_reduzida}')
print(f'Total de feridos: {total_feridos}')


categorias = {
    "Crianças": total_criancas,
    "Adultos": total_adultos,
    "Idosos": total_idosos,
    "Pessoas com mobilidade reduzida": total_reduzida,
    "Feridos": total_feridos
}
mais_afetada = max(categorias, key=categorias.get)
quantidade_mais_afetada = categorias[mais_afetada]
print(f'\nCategoria mais afetada: {mais_afetada} com {quantidade_mais_afetada} pessoas')


print('\n--- Desastre com maior número de afetados ---')
print(f'Número de afetados: {maior_afetados}')
print(f'Local: Rua {maior_desastre["rua"]}, Bairro {maior_desastre["bairro"]}, Cidade {maior_desastre["cidade"]}, País {maior_desastre["pais"]}')

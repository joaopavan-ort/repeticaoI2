nAlunos = 0
nMedia = 0

while True:
    aluno = input('Insira o nome do aluno (ou "fim" para encerrar o programa): ')
    if aluno.lower() == 'fim':
        print('Encerrando programa...')
        print()
        break
    else:
        nAlunos += 1

        n1 = float(input('Insira a nota 1: '))
        n2 = float(input('Insira a nota 2: '))
        media = (n1 + n2) / 2
        nMedia += media

        print(f'> Média do {aluno.capitalize()}: {media}')
        print()

print('---= Resultado Final =---')
print('Total de Alunos:', nAlunos)
print('Média da Turma:', nMedia / nAlunos)
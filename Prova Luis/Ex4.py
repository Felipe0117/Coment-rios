def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): #Inicia a função 
    total_notas = 0 #A variável total_notas recebe o valor 0
    num_alunos = len(notas) #A variável num_alunos recebe o valor do comprimento
    aprovados = [] #Inicia um vetor com o nome aprovados
    reprovados = [] #Inicia um vetor com o nome reprovados

    for aluno, nota in notas.items(): #Para cada aluno a nota correspondente deve ser armazenada na variável nota
        total_notas += nota #A variável total_notas vai receber o valor dela mesma somada a variável nota
        if nota >= nota_minima_aprovacao: #Se o valor da variável nota for igual ou maior que o valor da variável nota_minima_aprovacao
            aprovados.append(aluno) #O aluno é colocado no vetor aprovados
        else: #Senão
            reprovados.append(aluno) #O aluno é colocado no vetor reprovados

    media_turma = total_notas / num_alunos #A variável media_turma recebe o valor da variável total_notas subtraido o valor da variável num_alunos
 
    return media_turma, aprovados, reprovados #Retorna o valor das variáveis: media_turma, aprovados e reprovados

notas = { #Define os valores da classe 
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
}

nota_minima_aprovacao = 70 #A variável nota_minima_aprovacao recebe o valor 70

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao) #Chama a funçaõ calcular_media_e_aprovacao após informar os valores das variáveis notas e nota_minima_aprovacao

print(f"Média da turma: {media_turma:.2f}") #Printa na tela o valor da variável media_turma
print(f"Alunos aprovados: {', '.join(aprovados)}") #Printa na tela o valor da variável aprovados
print(f"Alunos reprovados: {', '.join(reprovados)}") #Printa na tela o valor da variável reprovados
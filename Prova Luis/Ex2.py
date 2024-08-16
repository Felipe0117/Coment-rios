def calcular_area_comodos(): #Inicia uma função
    total_area = 0 #A variável total_area recebe o valor de 0

    while True: #Enquanto for verdadeira

        largura = float(input("Digite a largura do cômodo (em metros): ")) #A variável largura vaireceber o valor fornecido pelo usuário
        comprimento = float(input("Digite o comprimento do cômodo (em metros): ")) #A variável comprimento vaireceber o valor fornecido pelo usuário

        area_comodo = largura * comprimento #A variável area_comodo vai receber o valor da variável largura multiplicado pelo valor da variável comprimento
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") #Printa na tela a área do cômodo com os valores fornecidos pelo usuário anteriormente

        total_area += area_comodo #A variável total_area recebe o valor dela mesma somada a variável area_comodo (Serve para calcular o valor total da área da casa no caso de mais um cômodo)

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower() #Printa na tela uma pergunta. Questionando o usuário se ele deseja fazer o cálculo de outro cômodo 
        if mais_comodos != 's': #Caso a resposta seja sim ele retorna para ocomeço da função
            break #Interrompe a linha de código

    return total_area #Retorna a variável total_area

area_total = calcular_area_comodos() #A variável recebe o valor armazenado em total_area (armazenado na função calcular_area_comodos)
print(f"A área total da casa é: {area_total:.2f} metros quadrados.") #Printa na tela a soma da área total da casa
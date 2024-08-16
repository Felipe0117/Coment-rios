def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): #Cria uma função que vai receber os valores das variáveis: valor_principal, taxa_juros_anual e dias_atraso
    
    taxa_juros_diaria = taxa_juros_anual / 365 / 100; #A variável taxa_juros_diaria recebe o valor da variável taxa_juros_anual dividido por 365 e 100

    juros = valor_principal * taxa_juros_diaria * dias_atraso #A variável juros recebe o valor da variável valor_principal multiplicado pelos valores das variáveis taxa_juros_diaria e dias_atraso 

    valor_total = valor_principal + juros #A variável valor_total recebe o valor da variável valor_principal mais o valor da variável juros
    return valor_total, juros #Retorna o valor das variáveis valor_total e juros

valor_principal = 1000.00 #Define um valor para variável
taxa_juros_anual = 5.0 #Define um valor para variável
dias_atraso = 30 #Define um valor para variável


valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso) #Chama a função calcular_juros_atraso com os valores das variáveis declaradas anteriormente
print(f"Valor total a ser pago: R${valor_total:.2f}") #Printa na tela o valor total a ser pago
print(f"Valor dos juros: R${juros:.2f}") #Printa na tela o valor dos juros 
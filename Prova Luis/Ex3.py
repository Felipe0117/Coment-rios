def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): #Inicia a função recebendo os valores das variáveis glicemia_em_jejum e glicemia_pos_prandial

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: #Se o valor da variável glicemia_em_jejum for maior ou igual a 126. Ou se a variável glicemia_pos_prandial for maior ou igual a 200
        return "Diabetes" #O código retorna Diabetes
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200: #Se o valor da variável glicemia_em_jejum for entre 100 e 126. Ou se a variável glicemia_pos_prandial for entre 140 e 200
        return "Pré-diabetes" #O código retorna Pré-diabetes
    else: #Senão for nenhuma das opções anteriores
        return "Normal" #O código retorna Normal

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) #A variável glicemia_em_jejum recebe o valor determinado pelo usuário
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): ")) #A variável glicemia_pos_prandial recebe o valor determinado pelo usuário

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial) #A variável resultado recebe o valor retornado pela função diagnosticar_diabetes
print(f"O diagnóstico é: {resultado}") #Printa o valor da variável resultado na tela
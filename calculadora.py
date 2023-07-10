import time as tmp
import os

#Funções para cada tipo de operação

def adicao(x, y):
    return x + y

def subtracao(x,y):
    return  x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x // y

def confirma_nova_operacao(A):
    return ("SIM")

def cancela_nova_operacao(B):
    return ("NAO")


print("*************************************")
print("***********Bem Vindo*****************")
print("*************************************")

print("\nSelecione o número para opção desejada!: ")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("\nDigite a opcao escolhida:"))

#Validação da opção digitada
if opcao <= 0 or opcao > 4:
    print("\nOpção inválida\n")
    exit(0)
    
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))


if opcao == 1:
    print(num1, "+", num2, "=", adicao(num1,num2))
elif opcao == 2:
    print(num1, "-", num2, "=", subtracao(num1, num2))
elif opcao == 3:
    print(num1, "*", num1, "=", multiplicacao(num1, num2))   
elif opcao == 4:
    print(num1, "/", num2, "=", divisao(num1, num2)) 

print("\n")
#Validação nova operacao   
print("Deseja fazer outra operação\n")

print("============================")
print("7 - SIM")
print("8 - NAO")
print("============================")

confirma_operacao = int(input("\nDigite 7 para SIM ou 8 para NAO:"))


if  confirma_operacao == 8:
    print("Encerrando calculadora em 3,2,1... Até a próxima!")
    tmp.sleep(3)
    os.system('cls')
elif confirma_operacao == 7:
    print("Vamos recomeçar")


#implementar recomeço

    


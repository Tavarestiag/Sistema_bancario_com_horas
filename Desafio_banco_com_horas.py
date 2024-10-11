from datetime import datetime
mascara_ptbr = "%d/%m/%Y %H:%M:%S"
extrato = f"""==========EXTRATO=========="""
menu = """
Menu
==========================
[1] Sacar
[2] Depositar
[3] Ver Extrato
[0] Sair
==========================
"""
saldo = 0
acao = -1 
transacoes_diarias = 0

def verifica_saldo_disponível(valor_do_saque):
    global saldo
    if valor_do_saque < 0:
        return False
    elif valor_do_saque > saldo:
        return False
    else:
        return True

def verifica_valor_deposito(valor_deposito):
    if valor_deposito > 0:
        return True
    else:
        return False

def verifica_limite_transacoes_diarias():
    global transacoes_diarias
    if transacoes_diarias < 10 :
        return True
    else:
        return False

def sacar(valor_do_saque, hora_do_saque):
    global saldo
    global extrato
    global transacoes_diarias
    saldo -= valor_do_saque
    extrato += f"\nSaque de R${valor_do_saque:.2f} às {hora_do_saque}"
    transacoes_diarias +=1
    return saldo, extrato, transacoes_diarias

def depositar(valor_do_deposito, hora_do_deposito):
    global saldo
    global extrato
    global transacoes_diarias
    saldo += valor_do_deposito
    extrato += f"\nDepósito de R${valor_do_deposito:.2f} às {hora_do_deposito}"
    transacoes_diarias +=1
    return saldo, extrato, transacoes_diarias

while acao != 0:
    acao = int(input(f"{menu}"))
    if acao == 1:
        possui_limite_de_transacoes = verifica_limite_transacoes_diarias()
        if possui_limite_de_transacoes == True:
            valor_deseja_sacar = int(input("\nQuanto deseja sacar: R$"))
            possui_saldo = verifica_saldo_disponível(valor_deseja_sacar)
            if possui_saldo == True:
                hora_que_sacou = datetime.now()
                hora_que_sacou_convertida = hora_que_sacou.strftime(mascara_ptbr)
                sacar(valor_deseja_sacar, hora_que_sacou_convertida)
                print("Retire o dinheiro da máquina.")
            else:
                print("\nNão possui saldo disponível!")
        else:
            print("\nLimite diário de transações atingido")        
    elif acao == 2:
        possui_limite_de_transacoes = verifica_limite_transacoes_diarias()
        if possui_limite_de_transacoes == True:
            valor_deseja_depositar = int(input("\nQuanto deseja depositar: R$"))
            pode_depositar = verifica_valor_deposito(valor_deseja_depositar)
            if pode_depositar == True:
                hora_que_depositou = datetime.now()
                hora_que_depositou_convertida = hora_que_depositou.strftime(mascara_ptbr)
                depositar(valor_deseja_depositar, hora_que_depositou_convertida)
                print("Coloque o dinheiro na máquina.")
            else:
                print("\nNão pode depositar tal valor")
        else:
            print("\nLimite diário de transações atingido")        
    elif acao == 3:
        print(extrato)
        print(f"Seu saldo é de R${saldo:.2f}")
    elif acao != 1 and acao !=2 and acao !=3 and acao !=0:
        print("Ação inválida!")
else:
    print("Muito obrigado!")
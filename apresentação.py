print("Olá! Vamos calcular as suas despesas mensais")
luz = float(input("Insira o valor da sua conta de luz: "))
agua = float(input("Insira o valor da sua conta de água: "))
internet = float(input("Insira o valor da sua conta de internet: "))
fatura = luz + agua + internet
saldo = float(input("Insira o saldo da sua conta: "))
saldo_restante = saldo - fatura


if fatura > saldo:
    print("saldo insuficiente para pagar a fatura")
else:
    print("o seu saldo restante é de:", saldo_restante,'R$')

while saldo_restante > 0:
    resposta = input("Houve algum gasto adicional? (S/N): ").strip().upper()
    if resposta == "S":
        try:
            gasto_adicional = float(input("Digite o valor gasto adicional: "))
            if gasto_adicional > 0: saldo_restante -= gasto_adicional
            if saldo_restante > 0:
                print("Saldo restante após gasto adicional é de", saldo_restante, "R$")
            else:
                print("Saldo insuficiente após gasto adicional")
        except ValueError:
            print("Por favor, insira um valor númerico válido.")
    elif resposta == "N":
        print("Nenhum gasto adicional registrado. Encerrando o programa.")
        break
    else:
        print("Resposta Inválida. Digite S ou N")



                
                    
            





        



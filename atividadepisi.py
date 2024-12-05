conta_luz = float(input("Digite o valor da conta de luz: "))
conta_agua = float(input("Digite o valor da conta de água: "))
conta_internet = float(input("Digite o valor da conta de internet: "))

gastos_fixos_mensais = conta_luz + conta_agua + conta_internet

saldo_inicial = float(input("Digite o seu saldo inicial: "))

gastos_adicionais_mensais = 0
while True:
    resposta = input("Houve algum gasto adicional mensal? (sim/não): ").strip().lower()
    if resposta == "sim":
        try:
            gasto_adicional = float(input("Digite o valor do gasto adicional: "))
            if gasto_adicional > 0:
                gastos_adicionais_mensais += gasto_adicional
            else:
                print("O valor do gasto adicional deve ser positivo.")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
    elif resposta == "não":
        break
    else:
        print("Resposta inválida. Digite 'sim' ou 'não'.")

total_gastos_mensais = gastos_fixos_mensais + gastos_adicionais_mensais

calcular_gastos_futuros = input("\nDeseja calcular os gastos futuros? (sim/não): ").strip().lower()
if calcular_gastos_futuros == "sim":
    meses_futuros = int(input("Digite a quantidade de meses que deseja calcular os gastos: "))
    gastos_futuros = total_gastos_mensais * meses_futuros
    print(f"\nTotal de gastos em {meses_futuros} meses: R$ {gastos_futuros:.2f}")
else:
    saldo_restante = saldo_inicial - total_gastos_mensais
    print(f"\nVocê optou por não calcular os gastos futuros.")
    print(f"Saldo inicial: R$ {saldo_inicial:.2f}")
    print(f"Gastos mensais: R$ {total_gastos_mensais:.2f}")
    print(f"Saldo restante após 1 mês: R$ {saldo_restante:.2f}")

print("\nCálculo dos saldos futuros:")
saldo_atual = saldo_inicial
meses = int(input("Digite a quantidade de meses que deseja calcular o saldo: "))
for mes in range(1, meses + 1):
    saldo_atual -= total_gastos_mensais
    print(f"Mês {mes}:")
    print(f"  - Gastos totais: R$ {total_gastos_mensais:.2f}")
    print(f"  - Saldo restante: R$ {saldo_atual:.2f}")
    if saldo_atual < 0:
        print("  - Atenção: Saldo negativo!")
        break

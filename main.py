from datetime import datetime, timedelta
import json
import time

ARQUIVO_VEICULOS = 'veiculosEstacionados.json'
ARQUIVO_VALORES = 'valoresEstacionamento.json'

def carregarVeiculos():
    try:
        with open(ARQUIVO_VEICULOS, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def carregarValores():
    try:
        with open(ARQUIVO_VALORES, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erro: arquivo de valores não encontrado ou inválido.")
        return {}


def salvarVeiculos(dados):
    with open(ARQUIVO_VEICULOS, 'w') as f:
        json.dump(dados, f, indent=4)

def mostrarMenu():
    while True:
        print("\n------- Sistema de Estacionamento -------")
        print("1 - Ver todos os veículos")
        print("2 - Entrada de Veículo")
        print("3 - Saída de Veículo")
        print("4 - Buscar Veículo")
        print("5 - Sair")
        opcao = input("Informe a opção desejada: ").strip()
        if opcao == "1":
            verVeiculos()
        elif opcao == "2":
            entradaVeiculo()
        elif opcao == "3":
            saidaVeiculo()
        elif opcao == "4":
            buscarVeiculo()
        elif opcao == "5":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

def verVeiculos():
    veiculos = carregarVeiculos()
    print("\n-------- Veículos Estacionados --------")
    if not veiculos:
        print("Nenhum veículo no momento.")
    else:
        for v in veiculos:
            entrada = datetime.fromtimestamp(v["entrada"]).strftime("%d/%m/%Y %H:%M:%S")
            tempo = str(timedelta(seconds=int(time.time() - v["entrada"])))
            print(f"\nPlaca: {v['placa']}")
            print(f"Tipo: {v['tipo']}")
            print(f"Entrada: {entrada}")
            print(f"Tempo Estacionado: {tempo}")

def entradaVeiculo():
    print("\n------- Entrada de Veículos -------")
    veiculos = carregarVeiculos()
    placa = input("Informe a placa do veículo: ").strip().upper()
    
    if not placa:
        print("Placa inválida.")
        return
    
    if any(v["placa"] == placa for v in veiculos):
        print("Este veículo já está estacionado.")
        return

    print("Selecione o tipo do veículo:")
    print("1 - Carro")
    print("2 - Moto")
    print("3 - Caminhão/Van")
    tipo_opcao = input("Opção: ").strip()

    if tipo_opcao == "1":
        tipo = "Carro"
    elif tipo_opcao == "2":
        tipo = "Moto"
    elif tipo_opcao == "3":
        tipo = "Caminhao/Van"
    else:
        print("Tipo inválido.")
        return

    veiculos.append({
        "placa": placa,
        "tipo": tipo,
        "entrada": time.time()
    })
    salvarVeiculos(veiculos)
    print(f"Veículo {placa} ({tipo}) registrado com sucesso!")


def saidaVeiculo():
    print("\n------- Saída de Veículos -------")
    veiculos = carregarVeiculos()
    valores = carregarValores()
    placa = input("Informe a placa do veículo: ").strip().upper()

    for i, v in enumerate(veiculos):
        if v["placa"] == placa:
            entrada = v["entrada"]
            tipo = v["tipo"]
            tempo_total_segundos = time.time() - entrada
            tempo_total_horas = tempo_total_segundos / 3600
            entrada_str = datetime.fromtimestamp(entrada).strftime("%d/%m/%Y %H:%M:%S")
            saida_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            tempo_str = str(timedelta(seconds=int(tempo_total_segundos)))

            tabela = valores.get(tipo)
            if not tabela:
                print("Categoria não encontrada na tabela de preços.")
                return

            if tempo_total_horas <= 1:
                valor = tabela["1h"]
            elif tempo_total_horas <= 2:
                valor = tabela["2h"]
            elif tempo_total_horas <= 3:
                valor = tabela["3h"]
            elif tempo_total_horas <= 12:
                horas_adicionais = int(tempo_total_horas) - 3
                valor = tabela["3h"] + (horas_adicionais * tabela["hora_adicional"])
            else:
                valor = tabela["diaria"]

            print(f"\nPlaca: {placa}")
            print(f"Tipo: {tipo}")
            print(f"Entrada: {entrada_str}")
            print(f"Saída: {saida_str}")
            print(f"Tempo Estacionado: {tempo_str}")
            print(f"Valor a Pagar: R$ {valor:.2f}")

            veiculos.pop(i)
            salvarVeiculos(veiculos)
            return

    print("Veículo não encontrado no estacionamento.")


def buscarVeiculo():
    print("\n------- Busca de Veículos -------")
    veiculos = carregarVeiculos()
    placa = input("Informe a placa a ser buscada: ").strip().upper()
    for v in veiculos:
        if v["placa"] == placa:
            entrada = datetime.fromtimestamp(v["entrada"]).strftime("%d/%m/%Y %H:%M:%S")
            tempo = str(timedelta(seconds=int(time.time() - v["entrada"])))
            print(f"\nVeículo encontrado:")
            print(f"Placa: {v['placa']}")
            print(f"Tipo: {v['tipo']}")
            print(f"Entrada: {entrada}")
            print(f"Tempo Estacionado: {tempo}")
            return
    print("Veículo não encontrado.")


mostrarMenu()
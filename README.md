# 🅿️ Sistema de Estacionamento (Python)

Aplicativo de **gestão de estacionamento via terminal**, que registra a entrada e saída de veículos, calcula o valor a pagar conforme tabela de preços e mantém os dados salvos em arquivos `.json`.

---

## ✨ Funcionalidades

- **Ver veículos estacionados** → Lista todos os veículos, com placa, tipo, hora de entrada e tempo total.
- **Entrada de veículo** → Registra placa, tipo (Carro, Moto ou Caminhão/Van) e horário de entrada.
- **Saída de veículo** → Calcula tempo total e valor a pagar com base na tabela (`valoresEstacionamento.json`), e remove o veículo do sistema.
- **Buscar veículo** → Localiza e exibe as informações de um veículo pela placa.
- **Persistência de dados** → Todos os registros são salvos em `veiculosEstacionados.json`.

---

## 📚 Bibliotecas

- **datetime** → Manipulação de horários e cálculo de tempo estacionado.
- **time** → Controle de timestamps e cálculos em segundos.
- **json** → Leitura e escrita dos arquivos de dados.

# IA---Scikit-fuzzy

Para o Sistema de Análise de Risco do Banco foi utilizada a lógica fuzzy para avaliar o risco de crédito as três variáveis pedidas: histórico de crédito, renda mensal e dívida atual. Com uma classificação de risco como 'Baixo', 'Médio' ou 'Alto'. E assim, um modelo de análise de risco simples que possa ser utilizado por instituições financeiras para avaliar o risco associado a clientes potenciais ou existentes. 

Para executar este projeto é necessáario a ter o Python instalado e instalar as bibliotecas `numpy` e `scikit-fuzzy`.


As regras usadas para avaliar os riscos do Cliente: 
    -  Se o histórico de crédito é 'Excelente' e a dívida atual é 'Baixa', então o risco é 'Baixo'.
    -  Se o histórico de crédito é 'Ruim' e a dívida atual é 'Alta', então o risco é 'Alto'.
    -  Se o histórico de crédito é 'Bom' e a renda mensal é 'Média' e a dívida atual é 'Moderada', então o risco é 'Médio'.
    -  Se o histórico de crédito é 'Regular' e a dívida atual é 'Moderada', então o risco é 'Médio'.

O sistema usa três variáveis de entrada:
histórico de crédito: Excelente, Bom, Regular, Ruim
renda mensal: Alta, Média, Baixa
dívida atual: Alta, Moderada, Baixa

A saída do sistema:
baixo: o risco de crédito é considerado baixo.
médio: o risco de crédito é moderado.
alto: o risco de crédito é alto.

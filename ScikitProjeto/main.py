import sklearn
import numpy as np

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl, trapmf


historico_credito = ctrl.Antecedent(np.arange(0, 21, 1), 'historico_credito')
renda_mensal = ctrl.Antecedent(np.arange(0, 21, 1), 'renda_mensal')
divida_atual = ctrl.Antecedent(np.arange(0, 21, 1), 'divida_atual')


risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')


historico_credito['ruim'] = fuzz.trimf(historico_credito.universe, [0, 4, 8])
historico_credito['regular'] = fuzz.trimf(historico_credito.universe, [4, 8, 12])
historico_credito['bom'] = fuzz.trimf(historico_credito.universe, [8, 12, 16])
historico_credito['excelente'] = fuzz.trapmf(historico_credito.universe, [12, 16, 20,20])

renda_mensal['baixa'] = fuzz.trimf(renda_mensal.universe, [0, 4, 8])
renda_mensal['media'] = fuzz.trimf(renda_mensal.universe, [4, 8, 12])
renda_mensal['alta'] = fuzz.trapmf(renda_mensal.universe, [8, 12, 16, 16])

divida_atual['baixa'] = fuzz.trimf(divida_atual.universe, [0, 4, 8])
divida_atual['moderada'] = fuzz.trimf(divida_atual.universe, [4, 8, 12])
divida_atual['alta'] = fuzz.trapmf(divida_atual.universe, [8, 12, 16, 16])

risco['baixo'] = fuzz.trimf(risco.universe, [0, 4, 8])
risco['medio'] = fuzz.trimf(risco.universe, [4, 8, 12])
risco['alto'] = fuzz.trapmf(risco.universe, [8, 12, 16, 16])

# regras fuzzy
rule1 = ctrl.Rule(historico_credito['excelente'] & divida_atual['baixa'], risco['baixo'])
rule2 = ctrl.Rule(historico_credito['ruim'] & divida_atual['alta'], risco['alto'])
rule3 = ctrl.Rule(historico_credito['bom'] & renda_mensal['media'] & divida_atual['moderada'], risco['medio'])
rule4 = ctrl.Rule(historico_credito['regular'] & divida_atual['moderada'], risco['medio'])


risco_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
risco_simulacao = ctrl.ControlSystemSimulation(risco_ctrl)


def map_input_to_value(category, value):
    mapping = {
        'excelente': 9,
        'bom': 7,
        'regular': 5,
        'ruim': 2,
        'alta': 9,
        'media': 5,
        'baixa': 2
    }
    return mapping.get(value.lower(), 0)


historico_input = input("Qual é o histórico de crédito? (Excelente, Bom, Regular, Ruim): ").lower()
renda_input = input("Qual é a renda mensal? (Alta, Média, Baixa): ").lower()
divida_input = input("Qual é a dívida atual? (Alta, Moderada, Baixa): ").lower()


if historico_input == 'excelente':
    risco_simulacao.input['historico_credito'] = 9  # excelente
elif historico_input == 'bom':
    risco_simulacao.input['historico_credito'] = 7  # bom
elif historico_input == 'regular':
    risco_simulacao.input['historico_credito'] = 5  # regular
elif historico_input == 'ruim':
    risco_simulacao.input['historico_credito'] = 2  # ruim

if renda_input == 'alta':
    risco_simulacao.input['renda_mensal'] = 9
elif renda_input == 'média':
    risco_simulacao.input['renda_mensal'] = 5
elif renda_input == 'baixa':
    risco_simulacao.input['renda_mensal'] = 2

if divida_input == 'alta':
    risco_simulacao.input['divida_atual'] = 9
elif divida_input == 'moderada':
    risco_simulacao.input['divida_atual'] = 5
elif divida_input == 'baixa':
    risco_simulacao.input['divida_atual'] = 2 


risco_simulacao.compute()


print(f"O risco estimado é: {risco_simulacao.output['risco']:.2f}")
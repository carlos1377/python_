"""
CONSTANTE = "Variáveis" que não vão mudar (sempre em maiúsculo para representar não mudam o valor)
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 90  # local em que o carro está na estrada

RADAR_1 = 60  # velocide máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and \
    local_carro <= (LOCAL_1 - RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('carro passou da velocidade no radar1')

if carro_passou_radar_1:
    print('carro passou em radar 1')

if carro_multado_radar_1:
    print('carro foi multado radar 1')

# -*- coding: utf-8 -*-
import time
import datetime
import minimalmodbus
import serial
import os

# Configuração

NUMERO_DE_COMISSIONAMENTOS = 1
ENDERECO_INICIAL_MEDIDORES = 20

CONVERSAO_TENSAO = 0.0231934
CONVERSAO_CORRENTE = 0.1525849
CONVERSAO_FREQUENCIA = 0.0061035156
CONVERSAO_POTENCIA = 33.5693359375
CONVERSAO_POTENCIA_TOTAL = 3 * 33.5693359375
CONVERSAO_FATOR_POTENCIA = 0.00006103515625


MEDIDOR_CONFIG = {'tensaoA': 100, 'tensaoB': 101, 'tensaoC': 102, 'tensaoAB': 103, 'tensaoBC': 104, 'tensaoCA': 105, 'correnteA': 106, 'correnteB': 107, 'correnteC': 108, 'correnteneutro': 113, 'potencia_ativa_A': 110, 'potencia_ativa_B': 111, 'potencia_ativa_C': 112, 'potencia_ativa_total': 113, 'potencia_reativa_A': 114, 'potencia_reativa_B': 115, 'potencia_reativa_C': 116, 'potencia_reativa_total': 117, 'potencia_aparente_A': 118, 'potencia_aparente_B': 119, 'potencia_aparente_C': 120, 'potencia_aparente_total': 121, 'fator_potencia_A': 122, 'fator_potencia_B': 123, 'fator_potencia_C': 124, 'fator_potencia_total': 125, 'frequencia':126, 'energia_at_imp_MWh': 127, 'energia_at_imp': 128, 'energia_at_imp_Wh': 129, 'energia_re_imp_MWh': 130, 'energia_re_imp': 131, 'energia_re_imp_Wh': 132, 'energia_at_exp_MWh': 133, 'energia_at_exp': 134, 'energia_at_exp_Wh': 135, 'energia_re_exp_MWh': 136, 'energia_re_exp': 137, 'energia_re_exp_Wh': 138}

medidores = []

def date_now():
    
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    return str(today)

def collect_generico(tipo, comissionamento, i):

    file = open("{}{}.txt".format(tipo, i), "a")
    file.write("{}, ".format(date_now()))

    config = MEDIDOR_CONFIG
    if tipo == "Medidor":
        for nome_medicao, registrador in config.items():
            medicao = comissionamento.read_register(registrador, 0, 3)

            #Leitura tensao           
            if registrador >= 100 and registrador <=105:
                medicao = medicao*CONVERSAO_TENSAO

            if registrador >= 106 and registrador <=109:
                medicao = medicao*CONVERSAO_CORRENTE

            #Leitura potencia
            if registrador >= 110 and registrador <=121 and registrador != 113:
                medicao = medicao*CONVERSAO_POTENCIA

            #Leitura potencial total
            if registrador == 113:
                medicao = medicao*CONVERSAO_POTENCIA_TOTAL

            #Leitura fator de potencia
            if registrador >= 122 and registrador <=125:
                medicao = medicao*CONVERSAO_FATOR_POTENCIA
            
            #Leitura frequencia
            if registrador == 126:
                medicao = medicao*CONVERSAO_FREQUENCIA

            print("{}, {}: {}".format(nome_medicao, tipo, i, medicao))
            file.write("{}, ".format(medicao))
    file.write("\n")
    file.close()

for i in range(1, NUMERO_DE_COMISSIONAMENTOS + 1):
    
    # Criação dos medidores
    
    medidor = minimalmodbus.Instrument('/dev/ttyUSB1', i, 'rtu')
    medidor.serial.baudrate = 9600
    medidor.serial.bytesize = 8
    medidor.serial.parity = serial.PARITY_NONE
    medidor.serial.stopbits = 1
    medidor.serial.timeout = 100.0
    medidor.address = ENDERECO_INICIAL_MEDIDORES 
    medidor.mode = minimalmodbus.MODE_RTU
    
    medidores.append(medidor)
    
while True:
    for i, medidor in enumerate(medidores):
        collect_generico("Medidor", medidor, i)
        time.sleep(0.5)

    time.sleep(60*1)

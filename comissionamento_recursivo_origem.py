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

    logger = open("{}{}.txt".format(tipo, i), "a")
    logger.write("{}, ".format(date_now()))

    config = MEDIDOR_CONFIG
    if tipo == "Medidor":
        for nome_medicao, registrador in config.items():
        
            #Leitura tensao           
            if registrador >= 100 and registrador <=105:
                medicao = comissionamento.read_register(registrador, 0, 3)
                valorV = medicao*CONVERSAO_TENSAO
                logger.write("{}, ".format (valorV))
                print('Tensao: ', valorV)

            #Leitura corrente
            if registrador >= 106 and registrador <=109:
                medicao = comissionamento.read_register(registrador, 0, 3)
                valorC = medicao*CONVERSAO_CORRENTE
                logger.write("{}, ".format(valorC))
                print('Corrente: ', valorC)

            #Leitura potencia
            if registrador >= 110 and registrador <=121 and registrador != 113:
                medicao = comissionamento.read_register(registrador, 0, 3)
                valorP = medicao*CONVERSAO_POTENCIA
                logger.write("{}, ".format(valorP))
                print('Potencia: ', valorP)

            #Leitura potencial total
            if registrador == 113:
                medicao = comissionamento.read_register(registrador, 0, 3)
                valorPT = medicao*CONVERSAO_POTENCIA_TOTAL
                logger.write("{}, ".format(valorPT))
                print('Potencia Total: ', valorPT)

            #Leitura fator de potencia
            if registrador >= 122 and registrador <=125:
                medicao = comissionamento.read_register(registrador, 0, 3)
                valorFP = medicao*CONVERSAO_FATOR_POTENCIA
                logger.write("{}, ".format(valorFP))
                print('Fator de Potencia: ', valorFP)

            #Leitura frequencia
            if registrador == 126:
                medicao = comissionamento.read_register(registrador, 0, 3)
                valorF = medicao*CONVERSAO_FREQUENCIA
                logger.write("{}, ".format(valorF))
                print('Frequencia: ', valorF)

            #Leitura energia ativa importada
            if registrador == 128:
                medicao = comissionamento.read_register(registrador, 0, 3)
                energia_ativa_importada_MWh = comissionamento.read_register(127,0,3)
                energia_ativa_importada_Wh = comissionamento.read_register(129,0,3)
                valor_E_A_I = ((energia_ativa_importada_MWh*1000) + (medicao + (energia_ativa_importada_Wh/1000)))
                logger.write("{}, ".format(valor_E_A_I))
                print('Energia Ativa Importada: ', valor_E_A_I)   

            #Leitura energia reativa importada
            if registrador == 131:
                medicao = comissionamento.read_register(registrador, 0, 3)
                energia_reativa_importada_MWh = comissionamento.read_register(127,0,3)
                energia_reativa_importada_Wh = comissionamento.read_register(129,0,3)
                valor_E_R_I = ((energia_reativa_importada_MWh*1000) + (medicao + (energia_reativa_importada_Wh/1000)))
                logger.write("{}, ".format(valor_E_R_I))
                print('Energia Reativa Importada: ', valor_E_R_I)   

            #Leitura energia ativa exportada
            if registrador == 134:
                medicao = comissionamento.read_register(registrador, 0, 3)
                energia_ativa_exportada_MWh = comissionamento.read_register(127,0,3)
                energia_ativa_exportada_Wh = comissionamento.read_register(129,0,3)
                valor_E_A_E = ((energia_ativa_exportada_MWh*1000) + (medicao + (energia_ativa_exportada_Wh/1000)))
                logger.write("{}, ".format(valor_E_A_E))
                print('Energia Ativa Exportada: ', valor_E_A_E)   

            #Leitura energia reativa exportada
            if registrador == 137:
                medicao = comissionamento.read_register(registrador, 0, 3)
                energia_reativa_exportada_MWh = comissionamento.read_register(127,0,3)
                energia_reativa_exportada_Wh = comissionamento.read_register(129,0,3)
                valor_E_R_E = ((energia_reativa_exportada_MWh*1000) + (medicao + (energia_reativa_exportada_Wh/1000)))
                logger.write("{}, ".format(valor_E_R_E))
                print('Energia Retiva Exportada: ', valor_E_R_E)      


        logger.write("\n")
        logger.close()

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

    time.sleep(60*6)

# -*- coding: utf-8 -*-
import time
import datetime
import minimalmodbus
import serial
import os


# Configuração
NUMERO_DE_COMISSIONAMENTOS = 19
ENDERECO_INICIAL_MEDIDORES = 101
ENDERECO_INICIAL_INVERSORES = 1
VIR = 1 #valor referencia corrente
VFR = 230 #valor referencia tensao
VPR = 1000 #valor referencia potencia
FORMULA_CONVERSAO_MEDIDORES = (medicao[0] * VR)/16384
FORMULA_CONVERSAO_ENERGIA = medicao[0] * 10e9 * 1000 + medicao [0] * 10e3 + (medicao[0] /1000)

#Dicionario medidor
MEDIDOR_CONFIG = {'tensao_AB': 103, 'tensao_BC': 104, 'tensao_CA': 105, 'corrente_A': 106, 'corrente_B': 107, 'corrente_C': 108, 'corrente_neutro': 109, 
                  'potencia_A': 110, 'potencia_B': 111, 'potencia_C': 112, 'potencia_total': 113, 'potencia_reativa_total': 117, 'fator_potencia_A':122,
                  'fator_potencia_B': 123, 'fator_potencia_C': 124, 'fator_potencia_T': 125, 'frequencia': 126, 'energia_ativa_importada': 128,
                  'energia_reativa_importada': 131, 'energia_ativa_exportada':134, 'energia_reativa_exportada': 136}

#Dicionario inversor
INVERSOR_CONFIG = { 'energia_diaria': 132, 'energia_total': 134, 'energia_parcial': 136, 'energia_mensal': 140, 'tensao_rede': 144, 'corrente_A': 146,
                   'potencia_AC': 148, 'frequencia': 150, 'potencia_1': 152, 'tensao_1': 154, 'corrente_1': 156, 'potencia_2': 158, 'tensao_2': 160,
                    'corrente_2': 162, 'temperatura': 164, 'resistencia_isolacao': 168, 'estado_alarme': 1051}

medidores = []
inversores = []

def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    return str(today)

#Gera arquivo para cada equipamento no formato definido
def collect_generico(tipo, comissionamento, i):
    file = open("{}{}.txt".format(tipo, i), "a")
    file.write("{}, ".format(date_now()))

    config = MEDIDOR_CONFIG if tipo == "Medidor" else INVERSOR_CONFIG
    
    for nome_medicao, registrador in config.items():
      if nome_medicao == 'estado_alarme':
          medicao = medidor.read_register(registrador, 3, 2)
          if medicao == 64:
             print("Fusivel queimado.")

      elif nome_medicao == 'energia_diaria' or 'energia_total' or 'energia_parcial' or 'energia_mensal':
            medicao = medidor.read_long(registrador, 3, 2)
      else: 
            medicao = medidor.read_float(registrador, 3, 2)
            
            if nome_medicao == 'tensao_AB' or 'tensao_BC' or 'tensao_CA':
                  VR = VFR
                  medicao = FORMULA_CONVERSAO_MEDIDORES

             if nome_medicao == 'corrente_A' or 'corrente_B' or 'corrente_C' or 'corrente_neutro':
                  VR = VIR
                   medicao = FORMULA_CONVERSAO_MEDIDORES

              if nome_medicao == 'potencia_A' or 'potencia_B' or 'potencia_C' or 'potencia_total':
                  VR = VPR
                   medicao = FORMULA_CONVERSAO_MEDIDORES

              if nome_medicao == 'fator_potencia_A' or 'fator_potencia_B' or 'fator_potencia_C' or 'fator_potencia_total':
                  VR = 1 
                   medicao = FORMULA_CONVERSAO_MEDIDORES

              if nome_medicao == 'frequencia':
                  VR = 100
                   medicao = FORMULA_CONVERSAO_MEDIDORES

              if nome_medicao == 'energia_ativa_importada' or 'energia_ativa_exportada':
                   medicao = FORMULA_CONVERSAO_ENERGIA

              if nome_medicao == 'energia_reativa_importada' or 'energia_reativada_exportada':
                   medicao = FORMULA_CONVERSAO_ENERGIA
            

        # Debug
        print("{}, {} {}: {}".format(nome_medicao, tipo, i, medicao))
        
        file.write("{}, ".format(medicao))
    
    file.write("\n")

#Loop responsável pela comunicação do modbus
for i in range(1, NUMERO_DE_COMISSIONAMENTOS):
    # Criação dos medidores
    medidor = minimalmodbus.Instrument('/dev/ttyUSB0', i, 'rtu')

    medidor.serial.baudrate = 9600
    medidor.serial.bytesize = 8
    medidor.serial.parity = serial.PARITY_NONE
    medidor.serial.stopbits = 1
    medidor.serial.timeout = 100.0
    medidor.address = ENDERECO_INICIAL_MEDIDORES + i
    medidor.mode = minimalmodbus.MODE_RT

    medidores.append(medidor)

    # Criação dos inversores
    inversor = minimalmodbus.Instrument('/dev/ttyUSB0', i, 'rtu')
    inversor.serial.baudrate = 9600
    inversor.serial.bytesize = 8
    inversor.serial.parity = serial.PARITY_NONE
    inversor.serial.stopbits = 1
    inversor.serial.timeout = 100.0
    inversor.address = ENDERECO_INICIAL_INVERSORES + i
    inversor.mode = minimalmodbus.MODE_RTU

    inversores.append(inversor)

#Realiza a comunicação 
while True:

    for i, medidor in enumerate(medidores):
        collect_generico("Medidor", medidor, i)
        time.sleep(0.5)

    for i, inversor in enumerate(inversores):
        collect_generico("Inversor", inversor, i)
        time.sleep(0.5)
    
    time.sleep(60*6)

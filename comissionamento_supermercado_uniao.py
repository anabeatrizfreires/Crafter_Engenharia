# -*- coding: utf-8 -*-
import time
import datetime
import minimalmodbus
import serial
import os


# Configuração
NUMERO_DE_COMISSIONAMENTOS = 1
ENDERECO_INICIAL_INVERSORES = 1

#Dicionario inversor
INVERSOR_CONFIG = { 'energia_diaria': 5093, 'energia_total': 5095, 'energia_total': 5099, 'corrente_A': 5022, 'corrente_B': 5023, 'corrente_C': 5024,
                   'frequencia': 5036, 'tensao_A': 5019, 'tensao_B': 5020, 'tensao_C': 5021, 'temperatura': 5008, 'resistencia_isolacao': 5071,
                    'potencia_A': 5085 , 'potencia_B': 5087, 'potencia_C': 5089, 'estado_alarme': 5045}

inversores = []

def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    return str(today)

#Gera arquivo para cada equipamento no formato definido
def collect_generico(tipo, comissionamento, i):
    file = open("{}{}.txt".format(tipo, i), "a")
    file.write("{}, ".format(date_now()))

    config = INVERSOR_CONFIG
    if tipo = "Inversor"
    
        for nome_medicao, registrador in config.items():
            if nome_medicao == 'estado_alarme' and 'estado_alarme' != 0:
                print ("Alarme, verificar anexo 3.")
            medicao = inversor.read_registers(registrador, 1,3)
        
            # Debug
            print("{}, {} {}: {}".format(nome_medicao, tipo, i, medicao))
            
            file.write("{}, ".format(medicao))
        
        file.write("\n")
        file.close()

#Loop responsável pela comunicação do modbus
for i in range(1, NUMERO_DE_COMISSIONAMENTOS):

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

    for i, inversor in enumerate(inversores):
        collect_generico("Inversor", inversor, i)
        time.sleep(0.5)
    
    time.sleep(60*6)

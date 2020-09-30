# -*- coding: utf-8 -*-
import time
import datetime
import minimalmodbus
import serial
import os

# Configuração

NUMERO_DE_COMISSIONAMENTOS = 1
ENDERECO_INICIAL_MEDIDORES = 25

MEDIDOR_CONFIG = {'temperatura': 7, 'umidade': 8}

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
            medicao = medidor.read_registers(registrador, 1, 3)
            medicao = medicao[0]/10
            print("{}, {}: {}".format(nome_medicao, tipo, i, medicao))
            file.write("{}, ".format(medicao))
    
    file.write("\n")
    file.close()
    
for i in range(1, NUMERO_DE_COMISSIONAMENTOS + 1):
    
    # Criação dos medidores
    
    medidor = minimalmodbus.Instrument('/dev/ttyUSB0', i, 'rtu')
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

# -*- coding: utf-8 -*-
import time
import datetime
import minimalmodbus
import serial
import os

# Configuração

NUMERO_DE_COMISSIONAMENTOS = 1
ENDERECO_INICIAL_MEDIDORES = 201

MEDIDOR_CONFIG = { 'corrente_A': 5022, 'corrente_B': 5023, 'corrente_C': 5024, 'potencia_total': 5031, 'energia_ativa_importada': 13014}

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
        medicao = medidor.read_float(registrador, 3, 2)
        print("{}, {} {}: {}".format(nome_medicao, tipo, i, medicao))
        file.write("{}, ".format(medicao))
    
    file.write("\n")
    file.close()
    
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
    
while True:
    for i, medidor in enumerate(medidores):
        collect_generico("Medidor", medidor, i)
        time.sleep(0.5)

    time.sleep(60*6)

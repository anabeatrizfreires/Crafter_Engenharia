import time
import datetime
import minimalmodbus
import serial
import os


# Configuração
NUMERO_DE_COMISSIONAMENTOS = 19
ENDERECO_INICIAL_MEDIDORES = 201
ENDERECO_INICIAL_INVERSORES = 301

#Dicionario medidor
MEDIDOR_CONFIG =
{
    "tensao_AB":103,
    "tensao_BC": 104,
    "tensao_CA": 105,
    "corrente_A": 106,
    "corrente_B": 107,
    "corrente_C": 108,
    "corrente_neutro": 109,
    "potencia_A": 110,
    "potencia_B": 111,
    "potencia_C": 112,
    "potencia_total": 113,
    "fator_potencia_A":122,
    "fator_potencia_B": 123,
    "fator_potencia_C": 124,
    "fator_potencia_T": 125,
    "frequencia": 126,
    "energia_ativa_importada": 127, 
    "energia_reativa_importada": 130,
    "energia_ativa_exportada":133
}

#Dicionario inversor
INVERSOR_CONFIG = 
{
    "energia_diaria": 132,
    "energia_total": 134,
    "energia_parcial": 136,
    "energia_mensal": 140
    "tensao_rede": 144,
    "corrente_rede": 146,
    "potencia_rede": 148,
    "frequencia": 150,
    "potencia_1": 152,
    "tensao_1": 154,
    "corrente_1": 156,
    "potencia_2": 158,
    "tensao_2": 160,
    "corrente_2": 162,
    "temperatura": 164,
    "resistencia_isolacao": 168
    
}

medidores = []
inversores = []

def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    return str(today)

#Gera arquivo para cada equipamento no formato definido
def collect_generico(tipo, comissionamento, i):
    file = open("{tipo}{}.txt".format(i), "a")
    file.write("{}, ".format(date_now()))

    config = MEDIDOR_CONFIG if tipo == "Medidores" else INVERSOR_CONFIG

    for nome_medicao, registrador in config.items():
        medicao = medidor.read_float(registrador, 3, 2)

        # Debug
        print("{}, {} {}: {}".format(nome_medicao, tipo, i, medicao))
        
        file.write("{}, ".format(medicao))
    
    file.write("\n")
    file.close()

#Loop responsável pela comunicação do modbus
for i in range(1, NUMERO_DE_COMISSIONAMENTOS+1):
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

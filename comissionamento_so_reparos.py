import time
import datetime
import minimalmodbus
import serial
import os
import math

INTERVALO_LEITURA = 0.5
INTERVALO_MEDICAO = 60 * 1

NUMERO_MEDIDORES = [4]



def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    today = str(today)
    hour = datetime.datetime.now().strftime("%H")
    return(today)

def hour():
    hour = datetime.datetime.now().strftime("%H")
    return(str(hour))


def write_to_csv1(tensao_media, tensaoA, tensaoB, tensaoC, tensao_linha_media, tensaoAB, tensaoBC, tensaoCA, corrente_media, correnteA, correnteB, correnteC, correnteneutro, frequencia, potencia_ativa_A, potencia_ativa_B, potencia_ativa_C, potencia_ativa_total, potencia_reativa_A, potencia_reativa_B, potencia_reativa_C, potencia_reativa_total, potencia_aparente_A, potencia_aparente_B, potencia_aparente_C, potencia_aparente_total, fator_potencia_A, fator_potencia_B, fator_potencia_C, fator_potencia_total, tensao_AN, tensao_BN, tensao_CN, corrente_AN, corrente_BN, corrente_CN, end_medidor):
    logger = open ("Medidor{}.txt".format(end_medidor), "a")
    logger.write(date_now() + ";" + str( tensaoA ) + ";"  + str( tensaoB ) + ";" + str( tensaoC ) + ";" + str( tensaoAB) + ";" + str( tensaoBC) + ";" + str( tensaoCA) + ";" + str( correnteA) + ";" + str( correnteB) + ";" + str( correnteC) + ";" + str( correnteneutro) + ";" + str( frequencia)  + ";" + str(potencia_ativa_A) + ";" + str(potencia_ativa_B) + ";" + str(potencia_ativa_C) + ";" + str(potencia_ativa_total) + ";" + str(potencia_reativa_A) + ";" + str(potencia_reativa_B) + ";" + str(potencia_reativa_C)  + ";" +  str(potencia_reativa_total) + ";" + str(potencia_aparente_A) + ";" + str(potencia_aparente_B) + ";" + str(potencia_aparente_C)  + ";" + str(potencia_aparente_total) + ";" + str(fator_potencia_A) + ";" + str(fator_potencia_B) + ";" + str(fator_potencia_C)  + ";" + str(fator_potencia_T) + ";"  + "\n")
    logger.close()
    print(date_now(),', TensaoA:',(tensaoA), ' - TensaoB:',(tensaoB,  ' - TensaoC:',(tensaoC), ' - TensaoAB:',(tensaoAB), ' - TensaoBC:',(tensaoBC),  ' - TensaoCA:',(tensaoCA), ' - CorrenteA:',(correnteA), ' - CorrenteB:',(correnteB),  ' - CorrenteC:',(correnteC), ' - CorrenteN:',(correnteneutro), ' - Frequencia:', (frequencia), ' - Potencia Ativa A:',(potencia_ativa_A), ' - Potencia Ativa B:',(potencia_ativa_B), ' - Potencia Ativa C:',(potencia_ativa_C),' - Potencia Ativa T:',(potencia_ativa_total),  ' - Potencia Reativa A:',(potencia_reativa_A), ' - Potencia Reativa B:',(potencia_reativa_B), ' - Potencia Reativa C:',(potencia_reativa_C),' - Potencia Reativa T:',(potencia_reativa_total), ' - Potencia Aparente A:',(potencia_aparente_A), ' - Potencia Aparente B:',(potencia_aparente_B), ' - Potencia Aparente C:',(potencia_aparente_C*CONVERSAO_POTENCIA),' - Potencia Aparente T:',(potencia_aparente_total),  ' - Fator Potencia A:',(fator_potencia_A), ' - Fator Potencia B:',(fator_potencia_B), ' - Fator Potencia C:',(fator_potencia_C), ' - Fator Potencia T:',(fator_potencia_T), '\n')


while True:

    for i in NUMERO_MEDIDORES:
        
        print(i)
        RHT485 = minimalmodbus.Instrument('/dev/ttyUSB0', i, 'rtu')
        RHT485.serial.baudrate = 9600
        RHT485.serial.bytesize = 8
        RHT485.serial.parity = serial.PARITY_NONE
        RHT485.serial.stopbits = 1
        RHT485.serial.timeout = 100.0
        RHT485.address = i
        RHT485.mode = minimalmodbus.MODE_RTU
        print(i)
        tensao_media = RHT485.read_float(2, 3, 2)
        tensao1 = RHT485.read_float(4,3,2)
        tensao2 = RHT485.read_float(6,3,2)
        tensao3 = RHT485.read_float(8,3,2)
        tensao_linha_media = RHT485.read_float(18,3,2)
        tensao12 = RHT485.read_float(20,3,2)
        tensao23 = RHT485.read_float(22,3,2)
        tensao31 = RHT485.read_float(24,3,2)
        corrente_media = RHT485.read_float(10,3,2)
        corrente1 = RHT485.read_float(12,3,2)
        corrente2 = RHT485.read_float(14,3,2)
        corrente3 = RHT485.read_float(16,3,2)
        correnteN = RHT485.read_float(74,3,2)
        potencia_W_1 = RHT485.read_float(44,3,2)
        potencia_W_2 = RHT485.read_float(46,3,2)
        potencia_W_3 = RHT485.read_float(48,3,2) 
        potencia_W_T = RHT485.read_float(42,3,2)
        potencia_R_1 = RHT485.read_float(52,3,2)
        potencia_R_2 = RHT485.read_float(54,3,2)
        potencia_R_3 = RHT485.read_float(56,3,2) 
        potencia_R_T = RHT485.read_float(50,3,2)    
        potencia_A_1 = RHT485.read_float(60,3,2)
        potencia_A_2 = RHT485.read_float(62,3,2)
        potencia_A_3 = RHT485.read_float(64,3,2) 
        potencia_A_T = RHT485.read_float(58,3,2)
        fator_potencia_1 = RHT485.read_float(28,3,2)
        fator_potencia_2 = RHT485.read_float(30,3,2)
        fator_potencia_3 = RHT485.read_float(32,3,2)
        frequenciaT = RHT485.read_float(66,3,2)
        tensao_AN = RHT485.read_float(600, 3, 2)
        tensao_BN = RHT485.read_float(602, 3, 2)
        tensao_CN = RHT485.read_float(604, 3, 2)
        corrente_AN = RHT485.read_float(606, 3, 2)
        corrente_BN = RHT485.read_float(608, 3, 2)
        corrente_CN = RHT485.read_float(610, 3, 2)

        print(i)
        write_to_csv1(tensao_media, tensao1, tensao2, tensao3, tensao_linha_media tensao12, tensao23, tensao31, corrente_media, corrente1, corrente2, corrente3, correnteN, frequenciaT, potencia_W_1, potencia_W_2, potencia_W_3, potencia_W_T, potencia_R_1, potencia_R_2, potencia_R_3, potencia_R_T, potencia_A_1, potencia_A_2, potencia_A_3, potencia_A_T, fator_potencia_1, fator_potencia_2, fator_potencia_3, fator_potencia_T, tensao_AN, tensao_BN, tensao_CN, corrente_AN, corrente_BN, corrente_CN,i)

        time.sleep(INTERVALO_LEITURA)
    time.sleep(INTERVALO_MEDICAO)

import time
import datetime
import minimalmodbus
import serial
import os


CONVERSAO_TENSAO = 0.0231934
CONVERSAO_CORRENTE = 0.1525849
CONVERSAO_FREQUENCIA = 0.0061035156

INTERVALO_LEITURA = 0.5

TENSAO_LINHA_LINHA_MIN = 342
TENSAO_LINHA_LINHA_MAX = 418
TENSAO_LINHA_NEUTRO_MIN = 198
TENSAO_LINHA_NEUTRO_MAX = 242
CORRENTE_MIN = 0.5
FREQUENCIA_MIN = 59.5
FREQUENCIA_MAX = 60.5


RHT485 = minimalmodbus.Instrument('/dev/ttyUSB1', 1, 'rtu')
RHT485.serial.baudrate = 9600
RHT485.serial.bytesize = 8
RHT485.serial.parity = serial.PARITY_NONE
RHT485.serial.stopbits = 1
RHT485.serial.timeout = 100.0
RHT485.address = 20
RHT485.mode = minimalmodbus.MODE_RTU


def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    today = str(today)
    hour = datetime.datetime.now().strftime("%H")
    return(today)

def hour():
    hour = datetime.datetime.now().strftime("%H")
    return(hour)

def write_to_csv1(tensaoA, tensaoB, tensaoC, tensaoAB, tensaoBC, tensaoCA, correnteA, correnteB, correnteC, correnteneutro, frequencia):
    logger = open ("datalogger_medidores_origem.txt", "a")
    logger.write(date_now() + "," + str( tensaoA*CONVERSAO_TENSAO ) + ","  + str( tensaoB*CONVERSAO_TENSAO ) + "," + str( tensaoC*CONVERSAO_TENSAO ) + "," + str( tensaoAB*CONVERSAO_TENSAO ) + "," + str( tensaoBC*CONVERSAO_TENSAO ) + "," + str( tensaoCA*CONVERSAO_TENSAO ) + "," + str( correnteA*CONVERSAO_CORRENTE ) + "," + str( correnteB*CONVERSAO_CORRENTE ) + "," + str( correnteC*CONVERSAO_CORRENTE ) + "," + str( correnteneutro*CONVERSAO_CORRENTE ) + "," + str( frequencia*CONVERSAO_FREQUENCIA) + "\n")
    logger.close()
    print(date_now(),', TensaoA:',(tensaoA*CONVERSAO_TENSAO), ' - TensaoB:',(tensaoB*CONVERSAO_TENSAO),  ' - TensaoC:',(tensaoC*CONVERSAO_TENSAO), ' - TensaoAB:',(tensaoAB*CONVERSAO_TENSAO), ' - TensaoBC:',(tensaoBC*CONVERSAO_TENSAO),  ' - TensaoCA:',(tensaoCA*CONVERSAO_TENSAO), ' - CorrenteA:',(correnteA*CONVERSAO_CORRENTE), ' - CorrenteB:',(correnteB*CONVERSAO_CORRENTE),  ' - CorrenteC:',(correnteC*CONVERSAO_CORRENTE), ' - CorrenteN:',(correnteneutro*CONVERSAO_CORRENTE), ' - Frequencia:', (frequencia*CONVERSAO_FREQUENCIA), '\n')

def alarmes (tensaoA, tensaoB, tensaoC, tensaoAB, tensaoBC, tensaoCA, correnteA, correnteB, correnteC, correnteneutro, frequencia):


    if tensaoA*CONVERSAO_TENSAO > TENSAO_LINHA_NEUTRO_MAX or tensaoA*CONVERSAO_TENSAO < TENSAO_LINHA_NEUTRO_MIN:
        logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
        logger_alarmes.write (date_now() + "," + 'TensaoA: ' + str(tensaoA*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()

    if tensaoB*CONVERSAO_TENSAO > TENSAO_LINHA_NEUTRO_MAX or tensaoB*CONVERSAO_TENSAO < TENSAO_LINHA_NEUTRO_MIN:
        logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
        logger_alarmes.write (date_now() + "," + 'TensaoB: '+ str(tensaoB*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()

    if tensaoC*CONVERSAO_TENSAO > TENSAO_LINHA_NEUTRO_MAX or tensaoC*CONVERSAO_TENSAO < TENSAO_LINHA_NEUTRO_MIN:
        logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
        logger_alarmes.write (date_now() + "," + 'TensaoC: '+ str(tensaoC*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()
    
    if tensaoAB*CONVERSAO_TENSAO > TENSAO_LINHA_LINHA_MAX or tensaoAB*CONVERSAO_TENSAO < TENSAO_LINHA_LINHA_MIN:
        logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
        logger_alarmes.write (date_now() + "," + 'TensaoAB: ' + str(tensaoAB*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()

    
    if tensaoBC*CONVERSAO_TENSAO > TENSAO_LINHA_LINHA_MAX or tensaoBC*CONVERSAO_TENSAO < TENSAO_LINHA_LINHA_MIN:
        logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
        logger_alarmes.write (date_now() + "," + 'TensaoBC: ' + str(tensaoBC*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()
    
    
    if tensaoCA*CONVERSAO_TENSAO > TENSAO_LINHA_LINHA_MAX or tensaoCA*CONVERSAO_TENSAO < TENSAO_LINHA_LINHA_MIN:
        logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
        logger_alarmes.write (date_now() + "," + 'TensaoCA: ' + str(tensaoCA*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()
    
    if frequencia * CONVERSAO_FREQUENCIA > FREQUENCIA_MAX or frequencia * CONVERSAO_FREQUENCIA < FREQUENCIA_MIN:
        logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
        logger_alarmes.write (date_now() + "," + 'Frequencia: ' + str(frequencia*CONVERSAO_FREQUENCIA) + "\n")
        logger_alarmes.close()

    if hour() > '7' and hour() < '18':
        if correnteA*CONVERSAO_CORRENTE < CORRENTE_MIN:
            logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
            logger_alarmes.write (date_now() + "," + 'CorrentaA: ' + str(correnteA*CONVERSAO_CORRENTE) + "\n")
            logger_alarmes.close()

        if correnteB*CONVERSAO_CORRENTE < CORRENTE_MIN:
            logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
            logger_alarmes.write (date_now() + "," + 'CorrentaB: ' + str(correnteB*CONVERSAO_CORRENTE) + "\n")
            logger_alarmes.close()

        if correnteC*CONVERSAO_CORRENTE < CORRENTE_MIN:
            logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
            logger_alarmes.write (date_now() + "," + 'CorrentaC: ' + str(correnteC*CONVERSAO_CORRENTE) + "\n")
            logger_alarmes.close()

        if correnteneutro*CONVERSAO_CORRENTE < CORRENTE_MIN:
            logger_alarmes = open ("datalogger_medidores_alarmes.txt", "a")
            logger_alarmes.write (date_now() + "," + 'CorrentaN: ' + str(correnteneutro*CONVERSAO_CORRENTE) + "\n")
            logger_alarmes.close()


while True:
    tensao1 = RHT485.read_register(100,0,3)
    tensao2 = RHT485.read_register(101,0,3)
    tensao3 = RHT485.read_register(102,0,3)
    tensao12 = RHT485.read_register(103,0,3)
    tensao23 = RHT485.read_register(104,0,3)
    tensao31 = RHT485.read_register(105,0,3)
    corrente1 = RHT485.read_register(106,0,3)
    corrente2 = RHT485.read_register(107,0,3)
    corrente3 = RHT485.read_register(108,0,3)
    correnteN = RHT485.read_register(113,0,3)
    frequenciaT = RHT485.read_register(126,0,3)
    write_to_csv1(tensao1, tensao2, tensao3, tensao12, tensao23, tensao31, corrente1, corrente2, corrente3, correnteN, frequenciaT)
    alarmes (tensao1, tensao2, tensao3, tensao12, tensao23, tensao31, corrente1, corrente2, corrente3, correnteN, frequenciaT)
    time.sleep(INTERVALO_LEITURA)

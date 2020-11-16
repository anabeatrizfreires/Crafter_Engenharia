import time
import datetime
import minimalmodbus
import serial
import os
import math


CONVERSAO_TENSAO = 0.0231934
CONVERSAO_CORRENTE = 0.1525849
CONVERSAO_FREQUENCIA = 0.0061035156
CONVERSAO_POTENCIA = 33.5693359375
CONVERSA_POTENCIA_TOTAL = 3 * 33.5693359375
CONVERSAO_FATOR_POTENCIA = 0.00006103515625

INTERVALO_LEITURA = 60*5

#NUMERO_MEDIDORES = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
NUMERO_MEDIDORES = [20]

TENSAO_LINHA_LINHA_MIN = 342
TENSAO_LINHA_LINHA_MAX = 418
TENSAO_LINHA_NEUTRO_MIN = 198
TENSAO_LINHA_NEUTRO_MAX = 242
CORRENTE_MIN = 0.5
CORRENTE_NEUTRO_MIN = 5
CORRENTE_NEUTRO_MAX = 500
FREQUENCIA_MIN = 59.5
FREQUENCIA_MAX = 60.5


def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    today = str(today)
    hour = datetime.datetime.now().strftime("%H")
    return(today)

def hour():
    hour = datetime.datetime.now().strftime("%H")
    return(str(hour))


def write_to_csv1(tensaoA, tensaoB, tensaoC, tensaoAB, tensaoBC, tensaoCA, correnteA, correnteB, correnteC, correnteneutro, frequencia, potencia_ativa_A, potencia_ativa_B, potencia_ativa_C, potencia_ativa_total, potencia_reativa_A, potencia_reativa_B, potencia_reativa_C, potencia_reativa_total, potencia_aparente_A, potencia_aparente_B, potencia_aparente_C, potencia_aparente_total, fator_potencia_A, fator_potencia_B, fator_potencia_C, fator_potencia_total, energia_at_imp_MWh, energia_at_imp, energia_at_imp_Wh, energia_re_imp_MWh, energia_re_imp, energia_re_imp_Wh, energia_at_exp_MWh, energia_at_exp, energia_at_exp_Wh, energia_re_exp_MWh, energia_re_exp, energia_re_exp_Wh, i):
    logger = open ("Medidor{}.txt".format(i), "a")
    logger.write(date_now() + "," + str( tensaoA*CONVERSAO_TENSAO ) + ","  + str( tensaoB*CONVERSAO_TENSAO ) + "," + str( tensaoC*CONVERSAO_TENSAO ) + "," + str( tensaoAB*CONVERSAO_TENSAO ) + "," + str( tensaoBC*CONVERSAO_TENSAO ) + "," + str( tensaoCA*CONVERSAO_TENSAO ) + "," + str( correnteA*CONVERSAO_CORRENTE ) + "," + str( correnteB*CONVERSAO_CORRENTE ) + "," + str( correnteC*CONVERSAO_CORRENTE ) + "," + str( correnteneutro*CONVERSAO_CORRENTE ) + "," + str( frequencia*CONVERSAO_FREQUENCIA)  + "," + str(potencia_ativa_A*CONVERSAO_POTENCIA) + "," + str(potencia_ativa_B*CONVERSAO_POTENCIA) + "," + str(potencia_ativa_C*CONVERSAO_POTENCIA) + "," + str(potencia_ativa_total*CONVERSA_POTENCIA_TOTAL) + "," + str(potencia_reativa_A*CONVERSAO_POTENCIA) + "," + str(potencia_reativa_B*CONVERSAO_POTENCIA) + "," + str(potencia_reativa_C*CONVERSAO_POTENCIA)  + "," +  str(potencia_reativa_total*CONVERSAO_POTENCIA) + "," + str(potencia_aparente_A*CONVERSAO_POTENCIA) + "," + str(potencia_aparente_B*CONVERSAO_POTENCIA) + "," + str(potencia_aparente_C*CONVERSAO_POTENCIA)  + "," + str(potencia_aparente_total*CONVERSAO_POTENCIA) + "," + str(fator_potencia_A*CONVERSAO_FATOR_POTENCIA) + "," + str(fator_potencia_B*CONVERSAO_FATOR_POTENCIA) + "," + str(fator_potencia_C*CONVERSAO_FATOR_POTENCIA)  + "," + str(fator_potencia_T*CONVERSAO_FATOR_POTENCIA) + "," + str((energia_at_imp_MWh*1000) + (energia_at_imp + (energia_at_imp_Wh/1000))) + "," + str((energia_re_imp_MWh*1000) + (energia_re_imp + (energia_re_imp_Wh/1000))) + "," + str((energia_at_exp_MWh*1000) + (energia_at_exp + (energia_at_exp_Wh/1000))) + "," + str((energia_re_exp_MWh*1000) + (energia_re_exp + (energia_re_exp_Wh/1000))) + "\n")
    logger.close()
    print(date_now(),', TensaoA:',(tensaoA*CONVERSAO_TENSAO), ' - TensaoB:',(tensaoB*CONVERSAO_TENSAO),  ' - TensaoC:',(tensaoC*CONVERSAO_TENSAO), ' - TensaoAB:',(tensaoAB*CONVERSAO_TENSAO), ' - TensaoBC:',(tensaoBC*CONVERSAO_TENSAO),  ' - TensaoCA:',(tensaoCA*CONVERSAO_TENSAO), ' - CorrenteA:',(correnteA*CONVERSAO_CORRENTE), ' - CorrenteB:',(correnteB*CONVERSAO_CORRENTE),  ' - CorrenteC:',(correnteC*CONVERSAO_CORRENTE), ' - CorrenteN:',(correnteneutro*CONVERSAO_CORRENTE), ' - Frequencia:', (frequencia*CONVERSAO_FREQUENCIA), ' - Potencia Ativa A:',(potencia_ativa_A*CONVERSAO_POTENCIA), ' - Potencia Ativa B:',(potencia_ativa_B*CONVERSAO_POTENCIA), ' - Potencia Ativa C:',(potencia_ativa_C*CONVERSAO_POTENCIA),' - Potencia Ativa T:',(potencia_ativa_total*CONVERSA_POTENCIA_TOTAL),  ' - Potencia Reativa A:',(potencia_reativa_A*CONVERSAO_POTENCIA), ' - Potencia Reativa B:',(potencia_reativa_B*CONVERSAO_POTENCIA), ' - Potencia Reativa C:',(potencia_reativa_C*CONVERSAO_POTENCIA),' - Potencia Reativa T:',(potencia_reativa_total*CONVERSAO_POTENCIA), ' - Potencia Aparente A:',(potencia_aparente_A*CONVERSAO_POTENCIA), ' - Potencia Aparente B:',(potencia_aparente_B*CONVERSAO_POTENCIA), ' - Potencia Aparente C:',(potencia_aparente_C*CONVERSAO_POTENCIA),' - Potencia Aparente T:',(potencia_aparente_total*CONVERSAO_POTENCIA),  ' - Fator Potencia A:',(fator_potencia_A*CONVERSAO_FATOR_POTENCIA), ' - Fator Potencia B:',(fator_potencia_B*CONVERSAO_FATOR_POTENCIA), ' - Fator Potencia C:',(fator_potencia_C*CONVERSAO_FATOR_POTENCIA), ' - Fator Potencia T:',(fator_potencia_T*CONVERSAO_FATOR_POTENCIA), ' - Energia Ativa Importada:',((energia_at_imp_MWh*1000) + (energia_at_imp + (energia_at_imp_Wh/1000))), ' - Energia Reativa Importada:',((energia_re_imp_MWh*1000) + (energia_re_imp + (energia_re_imp_Wh/1000))),  ' - Energia Ativa Exportada:',((energia_at_exp_MWh*1000) + (energia_at_exp + (energia_at_exp_Wh/1000))), ' - Energia Reativa Exportada:',((energia_re_exp_MWh*1000) + (energia_re_exp + (energia_re_exp_Wh/1000))), '\n')

def alarmes(tensaoA, tensaoB, tensaoC, tensaoAB, tensaoBC, tensaoCA, correnteA, correnteB, correnteC, correnteneutro, frequencia, potencia_ativa_A, potencia_ativa_B, potencia_ativa_C, potencia_ativa_total, potencia_reativa_A, potencia_reativa_B, potencia_reativa_C, potencia_reativa_total, potencia_aparente_A, potencia_aparente_B, potencia_aparente_C, potencia_aparente_total, fator_potencia_A, fator_potencia_B, fator_potencia_C, fator_potencia_total, energia_at_imp_MWh, energia_at_imp, energia_at_imp_Wh, energia_re_imp_MWh, energia_re_imp, energia_re_imp_Wh, energia_at_exp_MWh, energia_at_exp, energia_at_exp_Wh, energia_re_exp_MWh, energia_re_exp, energia_re_exp_Wh, i):

    if tensaoA*CONVERSAO_TENSAO > TENSAO_LINHA_NEUTRO_MAX or tensaoA*CONVERSAO_TENSAO < TENSAO_LINHA_NEUTRO_MIN:
        logger_alarmes = open ("Medidor{}_Alarme_Tensao.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'TensaoA: ' + str(tensaoA*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()

    if tensaoB*CONVERSAO_TENSAO > TENSAO_LINHA_NEUTRO_MAX or tensaoB*CONVERSAO_TENSAO < TENSAO_LINHA_NEUTRO_MIN:
        logger_alarmes = open ("Medidor{}_Alarme_Tensao.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'TensaoB: '+ str(tensaoB*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()

    if tensaoC*CONVERSAO_TENSAO > TENSAO_LINHA_NEUTRO_MAX or tensaoC*CONVERSAO_TENSAO < TENSAO_LINHA_NEUTRO_MIN:
        logger_alarmes = open ("Medidor{}_Alarme_Tensao.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'TensaoC: '+ str(tensaoC*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()
    
    if tensaoAB*CONVERSAO_TENSAO > TENSAO_LINHA_LINHA_MAX or tensaoAB*CONVERSAO_TENSAO < TENSAO_LINHA_LINHA_MIN:
        logger_alarmes = open ("Medidor{}_Alarme_Tensao.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'TensaoAB: ' + str(tensaoAB*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()

    
    if tensaoBC*CONVERSAO_TENSAO > TENSAO_LINHA_LINHA_MAX or tensaoBC*CONVERSAO_TENSAO < TENSAO_LINHA_LINHA_MIN:
        logger_alarmes = open ("Medidor{}_Alarme_Tensao.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'TensaoBC: ' + str(tensaoBC*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()
    
    
    if tensaoCA*CONVERSAO_TENSAO > TENSAO_LINHA_LINHA_MAX or tensaoCA*CONVERSAO_TENSAO < TENSAO_LINHA_LINHA_MIN:
        logger_alarmes = open ("Medidor{}_Alarme_Tensao.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'TensaoCA: ' + str(tensaoCA*CONVERSAO_TENSAO) + "\n")
        logger_alarmes.close()
    
    if frequencia * CONVERSAO_FREQUENCIA > FREQUENCIA_MAX or frequencia * CONVERSAO_FREQUENCIA < FREQUENCIA_MIN:
        logger_alarmes = open ("Medidor{}_Alarme_Frequencia.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'Frequencia: ' + str(frequencia*CONVERSAO_FREQUENCIA) + "\n")
        logger_alarmes.close()

    if correnteneutro*CONVERSAO_CORRENTE > CORRENTE_NEUTRO_MIN and correnteneutro*CONVERSAO_CORRENTE < CORRENTE_NEUTRO_MAX:
        logger_alarmes = open ("Medidor{}_Alarme_Corrente.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'CorrentaN: ' + str(correnteneutro*CONVERSAO_CORRENTE) + "\n")
        logger_alarmes.close()

    if abs(fator_potencia_A*CONVERSAO_FATOR_POTENCIA) < 0.95:
        logger_alarmes = open ("Medidor{}_Alarme_Fator_Potencia.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'FatorPotenciaA: ' + str(abs(fator_potencia_A*CONVERSAO_FATOR_POTENCIA)) + "\n")
        logger_alarmes.close()        

    if abs(fator_potencia_B*CONVERSAO_FATOR_POTENCIA) < 0.95:
        logger_alarmes = open ("Medidor{}_Alarme_Fator_Potencia.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'FatorPotenciaB: ' + str(abs(fator_potencia_B*CONVERSAO_FATOR_POTENCIA)) + "\n")
        logger_alarmes.close()  

    if abs(fator_potencia_C*CONVERSAO_FATOR_POTENCIA) < 0.95:
        logger_alarmes = open ("Medidor{}_Alarme_Fator_Potencia.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'FatorPotenciaC: ' + str(abs(fator_potencia_C*CONVERSAO_FATOR_POTENCIA)) + "\n")
        logger_alarmes.close()  

    if abs(fator_potencia_T*CONVERSAO_FATOR_POTENCIA) < 0.95:
        logger_alarmes = open ("Medidor{}_Alarme_Fator_Potencia.txt".format(i), "a")
        logger_alarmes.write (date_now() + "," + 'FatorPotenciaTotal: ' + str(abs(fator_potencia_T*CONVERSAO_FATOR_POTENCIA)) + "\n")
        logger_alarmes.close()   

    if int(hour()) > 7 and int(hour()) < 19:

        if abs(potencia_ativa_A*CONVERSAO_POTENCIA)  < 0.5:
            logger_alarmes = open ("Medidor{}_Alarme_Potencia.txt".format(i), "a")
            logger_alarmes.write (date_now() + "," + 'PotenciaAtivaA: ' + str(abs (potencia_ativa_A*CONVERSAO_POTENCIA)) + "\n")
            logger_alarmes.close()

        if abs(potencia_ativa_B*CONVERSAO_POTENCIA)  < 0.5:
            logger_alarmes = open ("Medidor{}_Alarme_Potencia.txt".format(i), "a")
            logger_alarmes.write (date_now() + "," + 'PotenciaAtivaB: ' + str(abs (potencia_ativa_B*CONVERSAO_POTENCIA)) + "\n")
            logger_alarmes.close()

        if abs (potencia_ativa_C*CONVERSAO_POTENCIA)  < 0.5:
            logger_alarmes = open ("Medidor{}_Alarme_Potencia.txt".format(i), "a")
            logger_alarmes.write (date_now() + "," + 'PotenciaAtivaC: ' + str(abs (potencia_ativa_C*CONVERSAO_POTENCIA)) + "\n")
            logger_alarmes.close()

        if abs(potencia_ativa_total*CONVERSAO_POTENCIA)  < 0.5:
            logger_alarmes = open ("Medidor{}_Alarme_Potencia.txt".format(i), "a")
            logger_alarmes.write (date_now() + "," + 'PotenciaAtivaTotal: ' + str(abs (potencia_ativa_total*CONVERSAO_POTENCIA)) + "\n")
            logger_alarmes.close()

        if correnteA*CONVERSAO_CORRENTE < CORRENTE_MIN:
            logger_alarmes = open ("Medidor{}_Alarme_Corrente_Neutro.txt".format(i), "a")
            logger_alarmes.write (date_now() + "," + 'CorrentaA: ' + str(correnteA*CONVERSAO_CORRENTE) + "\n")
            logger_alarmes.close()

        if correnteB*CONVERSAO_CORRENTE < CORRENTE_MIN:
            logger_alarmes = open ("Medidor{}_Alarme_Corrente_Neutro.txt".format(i), "a")
            logger_alarmes.write (date_now() + "," + 'CorrentaB: ' + str(correnteB*CONVERSAO_CORRENTE) + "\n")
            logger_alarmes.close()

        if correnteC*CONVERSAO_CORRENTE < CORRENTE_MIN:
            logger_alarmes = open ("Medidor{}_Alarme_Corrente_Neutro.txt".format(i), "a")
            logger_alarmes.write (date_now() + "," + 'CorrentaC: ' + str(correnteC*CONVERSAO_CORRENTE) + "\n")
            logger_alarmes.close()


while True:

    for i in NUMERO_MEDIDORES:
        
        RHT485 = minimalmodbus.Instrument('/dev/ttyUSB1', i, 'rtu')
        RHT485.serial.baudrate = 9600
        RHT485.serial.bytesize = 8
        RHT485.serial.parity = serial.PARITY_NONE
        RHT485.serial.stopbits = 1
        RHT485.serial.timeout = 100.0
        RHT485.address = i
        RHT485.mode = minimalmodbus.MODE_RTU
        tensao1 = RHT485.read_register(100,0,3)
        tensao2 = RHT485.read_register(101,0,3)
        tensao3 = RHT485.read_register(102,0,3)
        tensao12 = RHT485.read_register(103,0,3)
        tensao23 = RHT485.read_register(104,0,3)
        tensao31 = RHT485.read_register(105,0,3)
        corrente1 = RHT485.read_register(106,0,3)
        corrente2 = RHT485.read_register(107,0,3)
        corrente3 = RHT485.read_register(108,0,3)
        correnteN = RHT485.read_register(109,0,3)
        potencia_W_1 = RHT485.read_register(110,0,3)
        potencia_W_2 = RHT485.read_register(111,0,3)
        potencia_W_3 = RHT485.read_register(112,0,3) 
        potencia_W_T = RHT485.read_register(113,0,3)
        potencia_R_1 = RHT485.read_register(114,0,3)
        potencia_R_2 = RHT485.read_register(115,0,3)
        potencia_R_3 = RHT485.read_register(116,0,3) 
        potencia_R_T = RHT485.read_register(117,0,3)    
        potencia_A_1 = RHT485.read_register(118,0,3)
        potencia_A_2 = RHT485.read_register(119,0,3)
        potencia_A_3 = RHT485.read_register(120,0,3) 
        potencia_A_T = RHT485.read_register(121,0,3)
        fator_potencia_1 = RHT485.read_register(122,0,3)
        fator_potencia_2 = RHT485.read_register(123,0,3)
        fator_potencia_3 = RHT485.read_register(124,0,3)
        fator_potencia_T = RHT485.read_register(125,0,3)
        frequenciaT = RHT485.read_register(126,0,3)
        energia_ativa_importada_MWh = RHT485.read_register(127,0,3)
        energia_ativa_importada_1 = RHT485.read_register(128,0,3)
        energia_ativa_importada_Wh = RHT485.read_register(129,0,3)
        energia_reativa_importada_MWh = RHT485.read_register(130,0,3)
        energia_reativa_importada_1 = RHT485.read_register(131,0,3)
        energia_reativa_importada_Wh = RHT485.read_register(132,0,3)
        energia_ativa_exportada_MWh = RHT485.read_register(133,0,3)
        energia_ativa_exportada_1 = RHT485.read_register(134,0,3)
        energia_ativa_exportada_Wh = RHT485.read_register(135,0,3)
        energia_reativa_exportada_MWh = RHT485.read_register(136,0,3)
        energia_reativa_exportada_1 = RHT485.read_register(137,0,3)
        energia_reativa_exportada_Wh = RHT485.read_register(138,0,3)

        write_to_csv1(tensao1, tensao2, tensao3, tensao12, tensao23, tensao31, corrente1, corrente2, corrente3, correnteN, frequenciaT, potencia_W_1, potencia_W_2, potencia_W_3, potencia_W_T, potencia_R_1, potencia_R_2, potencia_R_3, potencia_R_T, potencia_A_1, potencia_A_2, potencia_A_3, potencia_A_T, fator_potencia_1, fator_potencia_2, fator_potencia_3, fator_potencia_T, energia_ativa_importada_MWh, energia_ativa_importada_1, energia_ativa_importada_Wh, energia_reativa_importada_MWh, energia_reativa_importada_1, energia_reativa_importada_Wh, energia_ativa_exportada_MWh, energia_ativa_exportada_1, energia_ativa_exportada_Wh, energia_reativa_exportada_MWh, energia_reativa_exportada_1, energia_reativa_exportada_Wh,i)
        alarmes (tensao1, tensao2, tensao3, tensao12, tensao23, tensao31, corrente1, corrente2, corrente3, correnteN, frequenciaT, potencia_W_1, potencia_W_2, potencia_W_3, potencia_W_T, potencia_R_1, potencia_R_2, potencia_R_3, potencia_R_T, potencia_A_1, potencia_A_2, potencia_A_3, potencia_A_T, fator_potencia_1, fator_potencia_2, fator_potencia_3, fator_potencia_T, energia_ativa_importada_MWh, energia_ativa_importada_1, energia_ativa_importada_Wh, energia_reativa_importada_MWh, energia_reativa_importada_1, energia_reativa_importada_Wh, energia_ativa_exportada_MWh, energia_ativa_exportada_1, energia_ativa_exportada_Wh, energia_reativa_exportada_MWh, energia_reativa_exportada_1, energia_reativa_exportada_Wh,i)

    time.sleep(INTERVALO_LEITURA)

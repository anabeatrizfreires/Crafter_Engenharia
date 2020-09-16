import time
import datetime
import minimalmodbus
import serial
import os

#multiplos medidores pela mesma porta serial

#medidor 1
medidor_01 = minimalmodbus.Instrument('/dev/ttyUSB0', 1, 'rtu')
medidor_01.serial.baudrate = 9600
medidor_01.serial.bytesize = 8
medidor_01.serial.parity = serial.PARITY_NONE
medidor_01.serial.stopbits = 1
medidor_01.serial.timeout = 100.0
medidor_01.address = 201
medidor_01.mode = minimalmodbus.MODE_RTU

#medidor 2
medidor_02 = minimalmodbus.Instrument('/dev/ttyUSB0', 2, 'rtu')
medidor_02.serial.baudrate = 9600
medidor_02.serial.bytesize = 8
medidor_02.serial.parity = serial.PARITY_NONE
medidor_02.serial.stopbits = 1
medidor_02.serial.timeout = 100.0
medidor_02.address = 202
medidor_02.mode = minimalmodbus.MODE_RTU

#medidor 3
medidor_03 = minimalmodbus.Instrument('/dev/ttyUSB0', 3, 'rtu')
medidor_03.serial.baudrate = 9600
medidor_03.serial.bytesize = 8
medidor_03.serial.parity = serial.PARITY_NONE
medidor_03.serial.stopbits = 1
medidor_03.serial.timeout = 100.0
medidor_03.address = 203
medidor_03.mode = minimalmodbus.MODE_RTU

#medidor 4
medidor_04 = minimalmodbus.Instrument('/dev/ttyUSB0', 4, 'rtu')
medidor_04.serial.baudrate = 9600
medidor_04.serial.bytesize = 8
medidor_04.serial.parity = serial.PARITY_NONE
medidor_04.serial.stopbits = 1
medidor_04.serial.timeout = 100.0
medidor_04.address = 204
medidor_04.mode = minimalmodbus.MODE_RTU

#medidor 5
medidor_05 = minimalmodbus.Instrument('/dev/ttyUSB0', 5, 'rtu')
medidor_05.serial.baudrate = 9600
medidor_05.serial.bytesize = 8
medidor_05.serial.parity = serial.PARITY_NONE
medidor_05.serial.stopbits = 1
medidor_05.serial.timeout = 100.0
medidor_05.address = 205
medidor_05.mode = minimalmodbus.MODE_RTU

#medidor 6
medidor_06 = minimalmodbus.Instrument('/dev/ttyUSB0', 6, 'rtu')
medidor_06.serial.baudrate = 9600
medidor_06.serial.bytesize = 8
medidor_06.serial.parity = serial.PARITY_NONE
medidor_06.serial.stopbits = 1
medidor_06.serial.timeout = 100.0
medidor_06.address = 206
medidor_06.mode = minimalmodbus.MODE_RTU

#medidor 7
medidor_07 = minimalmodbus.Instrument('/dev/ttyUSB0', 7, 'rtu')
medidor_07.serial.baudrate = 9600
medidor_07.serial.bytesize = 8
medidor_07.serial.parity = serial.PARITY_NONE
medidor_07.serial.stopbits = 1
medidor_07.serial.timeout = 100.0
medidor_07.address = 207
medidor_07.mode = minimalmodbus.MODE_RTU

#medidor 8
medidor_08 = minimalmodbus.Instrument('/dev/ttyUSB0', 8, 'rtu')
medidor_08.serial.baudrate = 9600
medidor_08.serial.bytesize = 8
medidor_08.serial.parity = serial.PARITY_NONE
medidor_08.serial.stopbits = 1
medidor_08.serial.timeout = 100.0
medidor_08.address = 208
medidor_08.mode = minimalmodbus.MODE_RTU

#medidor 9
medidor_09 = minimalmodbus.Instrument('/dev/ttyUSB0', 9, 'rtu')
medidor_09.serial.baudrate = 9600
medidor_09.serial.bytesize = 8
medidor_09.serial.parity = serial.PARITY_NONE
medidor_09.serial.stopbits = 1
medidor_09.serial.timeout = 100.0
medidor_09.address = 209
medidor_09.mode = minimalmodbus.MODE_RTU

#dia e hora    
def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    today = str(today)
    return(today)

#funcoes para leitura de float de registradores dos multimedidores
#funcao medidor 1
def medidor1():
    corrente_A_01 = medidor_01.read_float(13,3,2)
    corrente_B_01 = medidor_01.read_float(15,3,2)
    corrente_C_01 = medidor_01.read_float(17,3,2)
    potencia_01 = medidor_01.read_float(65,3,2)
    #energia_01 = medidor_01.read_float(810,3,4)
    logger_01 = open("logger_medidor_01.txt", "a")
    logger_01.write(date_now() + "," + str( corrente_A_01) + "," + str( corrente_B_01) + ","  + str( corrente_C_01) + "," + str(potencia_01) + "\n")
    logger_01.close()
    '''
    print ('Corrente A, Inversor 1: ', corrente_A_01)
    print ('Corrente B, Inversor 1: ', corrente_B_01)
    print ('Corrente C, Inversor 1: ', corrente_C_01)
    print ('Potencial Total, Inversor 1: ', potencia_01)
    print ('Energia Total, Inversor 1: ', energia_01)
    '''
    time.sleep(0.5)
    return ()


#funcao medidor 2
def medidor2():
    corrente_A_02 = medidor_02.read_float(13,3,2)
    corrente_B_02 = medidor_02.read_float(15,3,2)
    corrente_C_02 = medidor_02.read_float(17,3,2)
    potencia_02 = medidor_02.read_float(65,3,2)
    #energia_02 = medidor_02.read_float(810,3,4)
    logger_02 = open("logger_medidor_02.txt", "a")
    logger_02.write(date_now() + "," + str( corrente_A_02) + "," + str( corrente_B_02) + ","  + str( corrente_C_02) + "," + str(potencia_02) + "\n")
    logger_02.close()
    '''
    print ('Corrente A, Inversor 2: ', corrente_A_02)
    print ('Corrente B, Inversor 2: ', corrente_B_02)
    print ('Corrente C, Inversor 2: ', corrente_C_02)
    print ('Potencial Total, Inversor 2: ', potencia_02)
    print ('Energia Total, Inversor 2: ', energia_02)
    '''
    time.sleep(0.5)
    return ()


#funcao medidor 3
def medidor3():
    corrente_A_03 = medidor_03.read_float(13,3,2)
    corrente_B_03 = medidor_03.read_float(15,3,2)
    corrente_C_03 = medidor_03.read_float(17,3,2)
    potencia_03 = medidor_03.read_float(65,3,2)
    #energia_03 = medidor_03.read_float(810,3,4)
    logger_03 = open("logger_medidor_03.txt", "a")
    logger_03.write(date_now() + "," + str( corrente_A_03) + "," + str( corrente_B_03) + ","  + str( corrente_C_03) + "," + str(potencia_03) + "\n")
    logger_03.close()
    '''
    print ('Corrente A, Inversor 3: ', corrente_A_03)
    print ('Corrente B, Inversor 3: ', corrente_B_03)
    print ('Corrente C, Inversor 3: ', corrente_C_03)
    print ('Potencial Total, Inversor 3: ', potencia_03)
    print ('Energia Total, Inversor 3: ', energia_03)
    '''
    time.sleep(0.5)
    return ()

#funcao medidor 4
def medidor4():
    corrente_A_04 = medidor_04.read_float(13,3,2)
    corrente_B_04 = medidor_04.read_float(15,3,2)
    corrente_C_04 = medidor_04.read_float(17,3,2)
    potencia_04 = medidor_04.read_float(65,3,2)
    #energia_04 = medidor_04.read_float(810,3,4)
    logger_04 = open("logger_medidor_04.txt", "a")
    logger_04.write(date_now() + "," + str( corrente_A_04) + "," + str( corrente_B_04) + ","  + str( corrente_C_04) + "," + str(potencia_04) + "\n")
    logger_04.close()
    '''
    print ('Corrente A, Inversor 4: ', corrente_A_04)
    print ('Corrente B, Inversor 4: ', corrente_B_04)
    print ('Corrente C, Inversor 4: ', corrente_C_04)
    print ('Potencial Total, Inversor 4: ', potencia_04)
    print ('Energia Total, Inversor 4: ', energia_04)
    '''
    time.sleep(0.5)
    return ()

#funcao medidor 5
def medidor5():
    corrente_A_05 = medidor_05.read_float(13,3,2)
    corrente_B_05 = medidor_05.read_float(15,3,2)
    corrente_C_05 = medidor_05.read_float(17,3,2)
    potencia_05 = medidor_05.read_float(65,3,2)
    #energia_05 = medidor_05.read_float(810,3,4)
    logger_05 = open("logger_medidor_05.txt", "a")
    logger_05.write(date_now() + "," + str( corrente_A_05) + "," + str( corrente_B_05) + ","  + str( corrente_C_05) + "," + str(potencia_05) + "\n")
    logger_05.close()
    '''
    print ('Corrente A, Inversor 5: ', corrente_A_05)
    print ('Corrente B, Inversor 5: ', corrente_B_05)
    print ('Corrente C, Inversor 5: ', corrente_C_05)
    print ('Potencial Total, Inversor 5: ', potencia_05)
    print ('Energia Total, Inversor 5: ', energia_05)
    '''
    time.sleep(0.5)
    return ()

#funcao medidor 6
def medidor6():
    corrente_A_06 = medidor_06.read_float(13,3,2)
    corrente_B_06 = medidor_06.read_float(15,3,2)
    corrente_C_06 = medidor_06.read_float(17,3,2)
    potencia_06 = medidor_06.read_float(65,3,2)
    #energia_06 = medidor_06.read_float(810,3,4)
    logger_06 = open("logger_medidor_06.txt", "a")
    logger_06.write(date_now() + "," + str( corrente_A_06) + "," + str( corrente_B_06) + ","  + str( corrente_C_06) + "," + str(potencia_06) + "\n")
    logger_06.close()
    '''
    print ('Corrente A, Inversor 6: ', corrente_A_06)
    print ('Corrente B, Inversor 6: ', corrente_B_06)
    print ('Corrente C, Inversor 6: ', corrente_C_06)
    print ('Potencial Total, Inversor 6: ', potencia_06)
    print ('Energia Total, Inversor 6: ', energia_06)
    '''
    time.sleep(0.5)
    return ()

#funcao medidor 7
def medidor7():
    corrente_A_07 = medidor_07.read_float(13,3,2)
    corrente_B_07 = medidor_07.read_float(15,3,2)
    corrente_C_07 = medidor_07.read_float(17,3,2)
    potencia_07 = medidor_07.read_float(65,3,2)
    #energia_07 = medidor_07.read_float(810,3,4)
    logger_07 = open("logger_medidor_07.txt", "a")
    logger_07.write(date_now() + "," + str( corrente_A_07) + "," + str( corrente_B_07) + ","  + str( corrente_C_07) + "," + str(potencia_07) + "\n")
    logger_07.close()
    '''
    print ('Corrente A, Inversor 7: ', corrente_A_07)
    print ('Corrente B, Inversor 7: ', corrente_B_07)
    print ('Corrente C, Inversor 7: ', corrente_C_07)
    print ('Potencial Total, Inversor 7: ', potencia_07)
    print ('Energia Total, Inversor 7: ', energia_07)
    '''
    time.sleep(0.5)
    return ()

#funcao medidor 8
def medidor8():
    corrente_A_08 = medidor_08.read_float(13,3,2)
    corrente_B_08 = medidor_08.read_float(15,3,2)
    corrente_C_08 = medidor_08.read_float(17,3,2)
    potencia_08 = medidor_08.read_float(65,3,2)
    #energia_08 = medidor_08.read_float(810,3,4)
    logger_08 = open("logger_medidor_08.txt", "a")
    logger_08.write(date_now() + "," + str( corrente_A_08) + "," + str( corrente_B_08) + ","  + str( corrente_C_08) + "," + str(potencia_08) + "\n")
    logger_08.close()
    '''
    print ('Corrente A, Inversor 8: ', corrente_A_08)
    print ('Corrente B, Inversor 8: ', corrente_B_08)
    print ('Corrente C, Inversor 8: ', corrente_C_08)
    print ('Potencial Total, Inversor 8: ', potencia_08)
    print ('Energia Total, Inversor 8: ', energia_08)
    '''
    time.sleep(0.5)
    return ()

#funcao medidor 9
def medidor9():
    corrente_A_09 = medidor_09.read_float(13,3,2)
    corrente_B_09 = medidor_09.read_float(15,3,2)
    corrente_C_09 = medidor_09.read_float(17,3,2)
    potencia_09 = medidor_09.read_float(65,3,2)
    #energia_09 = medidor_09.read_float(810,3,4)
    logger_09 = open("logger_medidor_09.txt", "a")
    logger_09.write(date_now() + "," + str( corrente_A_09) + "," + str( corrente_B_09) + ","  + str( corrente_C_09) + "," + str(potencia_09) + "\n")
    logger_09.close()
    '''
    print ('Corrente A, Inversor 9: ', corrente_A_09)
    print ('Corrente B, Inversor 9: ', corrente_B_09)
    print ('Corrente C, Inversor 9: ', corrente_C_09)
    print ('Potencial Total, Inversor 9: ', potencia_09)
    print ('Energia Total, Inversor 9: ', energia_09)
    '''
    time.sleep(0.5)
    return ()
    
     
while True:
    medidor1()
    medidor2()
    medidor3()
    medidor4()
    medidor5()
    medidor6()
    medidor7()
    medidor8()
    medidor9()

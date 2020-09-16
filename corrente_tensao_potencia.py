#!/usr/bin/env python
import time
import datetime
import minimalmodbus
import serial
import os

#multiplos medidores pela mesma porta serial
#medidor 1
medidor1 = minimalmodbus.Instrument('/dev/ttyUSB0', 1, 'rtu')
medidor1.serial.baudrate = 9600
medidor1.serial.bytesize = 8
medidor1.serial.parity = serial.PARITY_NONE
medidor1.serial.stopbits = 1
medidor1.serial.timeout = 100.0
medidor1.address = 201
medidor1.mode = minimalmodbus.MODE_RTU

#medidor 2
medidor2 = minimalmodbus.Instrument('/dev/ttyUSB0', 2, 'rtu')
medidor2.serial.baudrate = 9600
medidor2.serial.bytesize = 8
medidor2.serial.parity = serial.PARITY_NONE
medidor2.serial.stopbits = 1
medidor2.serial.timeout = 100.0
medidor2.address = 209
medidor2.mode = minimalmodbus.MODE_RTU

#corrente 1
#BYTEORDER_BIG ABCD
#BYTEORDER_BIG_SWAP BADC
#BYTEORDER_LITTLE_SWAP CDAB
#BYTEORDER_LITTLE BCDA

def current1():
    corrente1 = medidor1.read_float(13,3,2)
    print (type (corrente1), 'Corrente 1, inv1:', corrente1)
    time.sleep(0.5)
    corrente1 = str (corrente1)
    return (corrente1)

#corrente 2
def current2():
    corrente_A_02 = medidor2.read_float(13,3,2)
    corrente_B_02 = medidor2.read_float(15,3,2)
    corrente_C_02 = medidor2.read_float(17,3,2)
    print (type (corrente_A_02), 'Corrente A, inv2: ', corrente_A_02)
    print (type (corrente_B_02), 'Corrente B, inv2: ', corrente_B_02)
    print (type (corrente_C_02), 'Corrente C, inv2: ', corrente_C_02)
    time.sleep(0.5)
    return ( str(corrente_A_02) + "," + str(corrente_B_02) + "," + str(corrente_C_02))


#tensao:
def voltage2():
    tensao_AB_02 = medidor2.read_float(7,3,2)
    tensao_BC_02 = medidor2.read_float(9,3,2)
    tensao_CA_02 = medidor2.read_float(11,3,2)
    print (type (tensao_AB_02), 'Tensao A, inv2: ', tensao_AB_02)
    print (type (tensao_BC_02), 'Tensao B, inv2: ', tensao_BC_02)
    print (type (tensao_CA_02), 'Tensao C, inv2: ', tensao_CA_02)
    time.sleep(0.5)
    return (str(tensao_AB_02) + "," + str(tensao_BC_02) + "," + str(tensao_CA_02))

def energy():
    energia = medidor2.read_float(810,3,4)
    print (type (energia), 'Energia Total: ', energia)
    time.sleep(0.5)
    return (str (energia))

def power():
    potencia = medidor2.read_float(65,3,2)
    print (type (potencia), 'Potencial Total: ', potencia)
    time.sleep(0.5)
    return (str(potencia))
        
#dia e hora    
def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    today = str(today)
    return(today)

#escreve no arquivo
def write_to_csv():
    
    logger = open("comissionamento.txt", "a")
    logger.write(date_now() + "," + current2()  + "," + voltage2() + "," + power() + "," +  "\n")
    logger.close()
     
while True:
    write_to_csv()
    


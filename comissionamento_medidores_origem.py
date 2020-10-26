import time
import datetime
import minimalmodbus
import serial
import os

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
    return(today)

def write_to_csv1():
    tensaoA = RHT485.read_register(100,0,3)
    tensaoB = RHT485.read_register(101,0,3)
    tensaoC = RHT485.read_register(102,0,3)
    tensaoAB = RHT485.read_register(103,0,3)
    tensaoBC = RHT485.read_register(104,0,3)
    tensaoCA = RHT485.read_register(105,0,3)
    correnteA = RHT485.read_register(106,0,3)
    correnteB = RHT485.read_register(107,0,3)
    correnteC = RHT485.read_register(108,0,3)
    correnteneutro = RHT485.read_register(113,0,3)
    frequencia = RHT485.read_register(126,0,3)
    print(date_now(),', TensaoA:',(tensaoA*0.0231934), ' - TensaoB:',(tensaoB*0.0231934),  ' - TensaoC:',(tensaoC*0.0231934), ', TensaoAB:',(tensaoAB*0.0231934), ' - TensaoBC:',(tensaoBC*0.0231934),  ' - TensaoCA:',(tensaoCA*0.0231934), ', CorrenteA:',(correnteA*0.1525849), ' - CorrenteB:',(correnteB*0.1525849),  ' - CorrenteC:',(correnteC*0.1525849), ' - CorrenteN:',(correnteneutro*0.1525849), ' - Frequencia:', (frequencia*0.0061035156), '\n')
    return (str(tensaoA) + "," + str(tensaoB) + "," + str(tensaoC) + "," + str(tensaoAB) + "," + str(tensaoBC) + "," + str(tensaoCA) + "," + str(correnteA) + "," + str(correnteB) + "," + str(correnteC) + "," + str(correnteneutro) + "," + str(frequencia))


while True:
    write_to_csv1()
    time.sleep(1)
    

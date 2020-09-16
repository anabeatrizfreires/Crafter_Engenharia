#!/usr/bin/env python
import time
import datetime
import minimalmodbus
import serial
import os

RHT485 = minimalmodbus.Instrument('/dev/ttyUSB0', 1, 'rtu')
RHT485.serial.baudrate = 9600
RHT485.serial.bytesize = 8
RHT485.serial.parity = serial.PARITY_NONE
RHT485.serial.stopbits = 1
RHT485.serial.timeout = 100.0
RHT485.address = 25
RHT485.mode = minimalmodbus.MODE_RTU
   
    
def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    today = str(today)
    return(today)

def write_to_csv(temp, umid):
    logger = open("logger_RODRIGO.txt", "a")
    logger.write(date_now() + "," + str( temp[0]/10.0 ) + "," + str( umid[0]/10.0 ) + "\n")
    logger.close()
    print(date_now(),', Temperatura:', temp[0]/10.0, ' - Umidade: ', umid[0]/10.0)
    

while True:
    temperatura = RHT485.read_registers(7,1,3)
    umidade = RHT485.read_registers(8,1,3)
    write_to_csv(temperatura, umidade)
    time.sleep(60*6)
    


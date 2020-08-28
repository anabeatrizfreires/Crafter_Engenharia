#!/usr/bin/env python
import time
import datetime
import minimalmodbus
import serial

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1, 'rtu')
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 100.0
instrument.address = 25
instrument.mode = minimalmodbus.MODE_RTU

def temperature ():
    temperatura = instrument.read_registers(7,1,3)
    print (type (temperatura), 'Temperatura:', temperatura[0]/10.0)
    time.sleep(0.5)
    temperatura_f = temperatura[0]/10.0
    return (temperatura_f)

def humidity ():
    umidade = instrument.read_registers(8,1,3)
    print(type (umidade), 'Umidade: ', umidade[0]/10.0)
    time.sleep(5)
    umidade_f = umidade[0]/10.0
    return (umidade_f)
        
    
def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    today = str(today)
    return(today)

def time_now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    now = str(now)
    return(now)
def write_to_csv():
    
    logger = open("datalogger2.txt", "a")
    try:
        logger.write(date_now() + "," + time_now() + "," + str( temperature() ) + "," + str( humidity() ) + "\n")
    except:
         pass
    logger.close()
     
while True:
    write_to_csv()

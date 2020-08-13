import time
import datetime
import csv
import minimalmodbus
import time
import serial

minimalmodbus.BAUDRATE = 9600

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1, 'rtu')
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 100.0
instrument.address = 25
instrument.mode = minimalmodbus.MODE_RTU

def temperatura ():
    while True:
        temperatura = instrument.read_registers(7,1,3)
        print (type (temperatura), 'Temperatura:', temperatura[0]/10.0)
        time.sleep(1)
        temperatura2 = temperatura[0]/10.0
        return (temperatura2)
    
def umidade ():
    while True:
        umid = instrument.read_registers(8,1,3)
        print(type (umid), 'Umidade: ', umid[0]/10.0)
        time.sleep(1)
        umidade2 = umid[0]/10.0
        return (umidade2)
        
    
def date_now():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    today = str(today)
    return(today)

def time_now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    now = str(now)
    return(now)

def write_to_csv():
    
    with open('testando.csv', 'w') as readings:
        readings_write = csv.writer(readings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_to_log = readings_write.writerow([date_now(),time_now(),temperatura(), umidade()])
        return(write_to_log)

write_to_csv()


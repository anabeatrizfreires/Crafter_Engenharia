# - * - codificação: utf-8 - * -
 tempo de importação
importar  data e hora
import  minimalmodbus
import  serial
importar  os

# Configuração

NUMERO_DE_COMISSIONAMENTOS  = 1
ENDERECO_INICIAL_MEDIDORES  =  201

INVERSOR_CONFIG  = { 'corrente_A' : 13 , 'corrente_B' : 15 , 'corrente_C' : 17 , 'potencia_total' : 65 , 'energia_ativa_importada' : 804 }

inversores  = []

def  date_now ():
    
    hoje  =  data e hora . datetime . agora (). strftime ( "% d-% m-% Y% H:% M" )
    return  str ( hoje )

def  collect_generico ( tipo , comissionamento , i ):
    arquivo  =  abrir ( "{} {}. txt" . formato ( tipo , i ), "a" )
    arquivo . write ( "{}," . format ( date_now ()))
    
    config  =  INVERSOR_CONFIG
    if  tipo  ==  "Inversor" :
    para  nome_medicao , registrador  em  config . itens ():
        medicao  =  medidor . read_float ( registrador , 3 , 2 )
        print ( "{}, {} {}: {}" . format ( nome_medicao , tipo , i , medicao ))
        arquivo . escrever ( "{}," . formato ( medicao ))
    
    arquivo . escrever ( " \ n " )
    arquivo . fechar ()
    
para  i  no  intervalo ( 1 , NUMERO_DE_COMISSIONAMENTOS ):
    
    # Criação dos medidores
    
    inversor  =  minimalmodbus . Instrumento ( '/ dev / ttyUSB0' , i , 'rtu' )
    inversor . serial . baudrate  =  9600
    inversor . serial . bytesize  =  8
    inversor . serial . paridade  =  serial . PARITY_NONE
    inversor . serial . stopbits  =  1
    inversor . serial . tempo limite  =  100,0
    inversor . endereço  =  ENDERECO_INICIAL_MEDIDORES  +  i
    inversor . modo  =  minimalmodbus . MODE_RT
    
    medidores . anexar ( medidor )
    
enquanto  verdadeiro :
    para  i , inversor  em  enumerar ( inversores ):
        collect_generico ( "Inversor" , inversor , i )
        tempo . dormir ( 0,5 )

    tempo . dormir ( 60 * 6 )

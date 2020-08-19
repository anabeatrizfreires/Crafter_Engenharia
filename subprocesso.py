import subprocess
import time

while True:
	result = subprocess.run(["python3", "data_hora_temperatura_umidade.py", "/dev/null"], stdout=subprocess.PIPE)
	time.sleep(60 * 1)
	print("Reiniciando o código")
	print(result)

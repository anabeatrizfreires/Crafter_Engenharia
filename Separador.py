import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
            
    arq = pd.read_csv('datalogger2.txt', sep=",", header=None)
    arq.columns = ["data", "hora", "temperatura","umidade"]
    #print (arq)
    arq.plot (x= 'hora', y='temperatura')
    plt.show()
    #plt.savefig("testando.png")


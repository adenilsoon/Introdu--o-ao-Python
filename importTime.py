import time

tempoInicial = 1
tempoFinal = 45

print("Iniciando descanso...")

for i in range(tempoInicial, tempoFinal+1):
    print(i)
    time.sleep(1)
    if (i == 45):
        print("Fim do descanso!")
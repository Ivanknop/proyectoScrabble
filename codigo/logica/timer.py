import time

def reloj (minutos):
    segundos = 59
    while True:
        print (str(minutos).zfill(2),':',str(segundos).zfill(2))
        if segundos > 0:
            segundos -= 1
        else:
            minutos -=1
            segundos = 59
        if minutos == 0 and segundos == 0:
            print ('Tiempo fuera')
            break
        time.sleep(1)

#reloj (3)
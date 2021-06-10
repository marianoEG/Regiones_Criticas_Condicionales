import threading
import logging
import random
import time
from regionCondicional import *


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Recurso1(Recurso):
    dato1 = 0
    numLectores = 0

recurso1 = Recurso1()

def condicionLector():
    return recurso1.numLectores == 0

region1 = Region(recurso1)
region2 = RegionCondicional(recurso1, condicionLector)



@region1.region
def leer():
    recurso1.numLectores += 1
    logging.info(f'Lector lee dato1 = {recurso1.dato1}')
    time.sleep(1)
    recurso1.numLectores -= 1


@region2.condicion
def escribir():
    recurso1.dato1 = random.randint(0, 100)
    logging.info(f'Escritor escribe dato1 = {recurso1.dato1}')


def Lector():
    while True:
        leer()
        time.sleep(random.randint(3, 6))

def Escritor():
    while True:
        escribir()
        time.sleep(random.randint(1,4))





def main():
    nlector = 10
    nescritor = 2

    for k in range(nlector):
        threading.Thread(target=Lector, daemon=True).start()

    for k in range(nescritor):
        threading.Thread(target=Escritor, daemon=True).start()

    time.sleep(300)


if __name__ == "__main__":
    main()


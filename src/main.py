import multiprocessing

from src.hegui.hegui import HEguiApp
from src.hesync.hesync import HEsyncApp
from src.helistener.helistener import *

def open_gui(s):
    HEguiApp(s).run()

def open_sync(s):
    HEsyncApp(s).run()

def main():
    # inicializo parametros
    # parseo argumentos de linea de comandos
    # leo configuracion
    #corro los modulos del programa
    a = multiprocessing.Process(target=open_gui, args=['hello'])
    b = multiprocessing.Process(target=open_sync, args=['hello'])
    a.start()
    b.start()

if __name__ in ('__main__', '__android__'):
    main()

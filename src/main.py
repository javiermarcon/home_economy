#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import os

__version__ = "0.0.1"

def main():
    ## inicializo parametros
    # para que kivy no acapare las opciones de linea de comando
    os.environ["KIVY_NO_ARGS"] = "1"


    ## parseo argumentos de linea de comandos
    #parser = ArgumentParser(description='Financial app to store expenses.')
    #exclusive = parser.add_mutually_exclusive_group() #required=True
    #exclusive.add_argument('-s', '--server', action='store_const', dest='runtype', const='s',
    #                       help="run as server in pc (not compatible with Android)")
    #exclusive.add_argument('-c', '--client', action='store_const', dest='runtype', const='c',
    #                       help="run as client (no server needed)")
    #parser.set_defaults(runtype='c')

    #args = parser.parse_args()
    ##print(parser.format_help())
    #print args

    # gui
    from hegui import LoginApp #HEguiApp

    #if args.runtype == "s":
    # lanzo el sync

    #HEguiApp('hello').run()
    LoginApp().run()

    ##speech recognition
    #def open_speech(num):
    #    from helistener.helistener import SpeechDetector
    #    sd = SpeechDetector()
    #    sd.setup_mic()
    #    ret = sd.run(num)
    #    print ret

    # leo configuracion
    #corro los modulos del programa
    #import multiprocessing
    #a = multiprocessing.Process(target=open_gui, args=['hello'])
    #c = multiprocessing.Process(target=open_speech, args=[5])
    #a.start()
    #c.start()
    

def open_sync(s):
    from hesync.hesync import HEsyncApp
    HEsyncApp(s).run()

if __name__ in ('__main__', '__android__'):
    main()

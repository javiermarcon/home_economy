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
    parser = ArgumentParser(description='Financial app to store expenses.')
    exclusive = parser.add_mutually_exclusive_group() #required=True
    exclusive.add_argument('-s', '--server', action='store_const', dest='runtype', const='s',
                           help="run as server in pc (not compatible with Android)")
    exclusive.add_argument('-c', '--client', action='store_const', dest='runtype', const='c',
                           help="run as client (no server needed)")
    parser.set_defaults(runtype='c')

    args = parser.parse_args()
    # print(parser.format_help())

    # gui
    from maingui import HeGuiApp

    hegui_app = HeGuiApp()

    if args.runtype == "s":
        hegui_app.runserver = True
        # install_twisted_rector must be called before importing and using the reactor
        from kivy.support import install_twisted_reactor
        install_twisted_reactor()

    hegui_app.run()

    ##speech recognition
    #def open_speech(num):
    #    from helistener.helistener import SpeechDetector
    #    sd = SpeechDetector()
    #    sd.setup_mic()
    #    ret = sd.run(num)
    #    print ret


if __name__ in ('__main__', '__android__'):
    main()

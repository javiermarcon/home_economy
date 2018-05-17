import os
import importlib

__globals = globals()

this_folder = os.path.dirname(__file__)

modus = []

for dname in os.listdir(this_folder):
    plugin_folder = os.path.join(this_folder, dname)
    if os.path.isdir(plugin_folder) and os.path.isfile(os.path.join(plugin_folder, "run.py")):
        __globals[dname] = importlib.import_module('.' + dname + '.run', package=__name__)
        modus.append(dname)

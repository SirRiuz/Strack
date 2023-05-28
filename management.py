# Python
import sys

# Libs
from core.commands import CommandManager


argumentos = sys.argv[1:]
parametros = ' '.join(argumentos)
CommandManager().exect(parametros)

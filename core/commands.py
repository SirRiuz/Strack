# Python
import os
import inspect

# Libs
from settings import COMMANDS_DIR
from core.models import BaseCommand


class CommandManager:
    
    def exect(self, command):
        commands = self.__get_commands()
        cmd = commands.get(command)
        if cmd:
            cmd().run()
            return
        
        print(f"The command '{command}' not exists.")   
        
    def __get_commands(self) -> (list):
        """
        Get of the list the commands in
        the commands file 
        """
        commands_map = {}
        for command in os.listdir(COMMANDS_DIR):
            cmd = command.split(".")[0]
            command_dir = f"{COMMANDS_DIR}{command}"
            data = open(command_dir, "r").read()
            namespace = ({'__name__': '__main__'})
            exec(data, namespace)
            
            for n, item in namespace.items():
                if inspect.isclass(item) and \
                    issubclass(item, BaseCommand) \
                        and item != BaseCommand:
                    command: BaseCommand = item
                    commands_map[command.command] = command
                    
        return commands_map

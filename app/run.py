# Global modules
import os

# Local modules
from lib import lib_json_wrapper as jsr

def main():
    autorun = jsr.read('app_settings.json', 'app.components.autorun')
    
    for component in autorun:
        if component != 'timegui.py':
            os.system(f'python3 {component} &')
        else:
            os.system('python3 timegui.py')



if __name__ == '__main__':
    main()
    
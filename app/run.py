# Global modules
import os

# Local modules
from lib import lib_json_wrapper as jsr

def main():
    components_list = jsr.read('app_settings.json', 'app.components')
    autorun = []
    
    for component in components_list:
        if jsr.read('app_settings.json', f'{component.split(".")[0]}.autorun') == 'true':
            autorun.append(component)
                 
    for component in autorun:
        if component != 'timegui.py':
            os.system(f'python3 {component} &')
        else:
            os.system('python3 timegui.py')



if __name__ == '__main__':
    main()
    
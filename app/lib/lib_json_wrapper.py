import json 

def read(filepath: str, key: str, encoding: str='UTF-8'):
    """Read parameter of key from json file.

    Args:
        filepath (str): path to json file
        key (str): key
        encoding (str, optional): json file encoding. Defaults to 'UTF-8'.

    Returns:
        any: parameter of key.
    """
    with open(filepath, encoding=encoding) as jsonobj:
        parameter = json.load(jsonobj)
        
        return parameter[key]
    
    
def write(filepath: str, key: str, param: str, encoding: str='UTF-8'):
    """Update json parameter inside a file.

    Args:
        filepath (str): path to json file
        key (str): key
        param (str): parameter of key
        encoding (str, optional): json file encoding. Defaults to 'UTF-8'.
    """
    with open(filepath, 'r', encoding=encoding) as jsonobj:
        data = json.load(jsonobj)
    
    data[key] = param
    
    with open(filepath, 'w', encoding=encoding) as jsonobj:
        json.dump(data, jsonobj, indent=4)
        

def append(filepath: str, key: str, param: any, encoding: str='UTF-8'):
    """Append json file with object.

    Args:
        filepath (str): path to json file
        key (str): key
        param (any): parameter
        encoding (str, optional): json file encoding. Defaults to 'UTF-8'.
    """
        
    with open(filepath, 'r', encoding=encoding) as jsonobj:
        data = json.load(jsonobj)
        
    data[key].append(param)
    
    with open(filepath, 'w', encoding=encoding) as jsonobj:
        json.dump(data, jsonobj, indent=4)
        

def remove(filepath: str, key: str, param: any, encoding: str='UTF-8'):
    """Remove parameter from json file.

    Args:
        filepath (str): path to json file
        key (str): key
        param (any): parameter
        encoding (str, optional): json file encoding. Defaults to 'UTF-8'.
    """
    
    with open(filepath, 'r', encoding=encoding) as jsonobj:
        data = json.load(jsonobj)
        
    data[key].remove(param)
    
    with open(filepath, 'w', encoding=encoding) as jsonobj:
        json.dump(data, jsonobj, indent=4)
        
        
def check(filepath: str, key: str, param: any, encoding='UTF-8'):
    """Check if json file have a key:parameter object.

    Args:
        filepath (str): path to json file
        key (str): key
        param (any): parameter
        encoding (str, optional): json file encoding. Defaults to 'UTF-8'.

    Returns:
        bool: True if exists, else False.
    """
    
    with open(filepath, 'r', encoding=encoding) as jsonobj:
        data = json.load(jsonobj)
        
    if param in data[key]:
        return True
    
    else:
        return False

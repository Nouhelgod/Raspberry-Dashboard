import json 

def read(filepath, key, encoding='UTF-8'):
    """Read parameter of key from json file.

    Args:
        filepath (str): path to json file
        key (str): key
        encoding (str, optional): json file encoding. Defaults to 'UTF-8'.

    Returns:
        str: parameter of key.
    """
    with open(filepath, encoding=encoding) as jsonobj:
        parameter = json.load(jsonobj)
        
        return parameter[key]
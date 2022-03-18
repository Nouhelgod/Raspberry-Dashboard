# FIXME: Bruh.

def get_symbol(smb: str):
    """Get large special symbol.

    Args:
        smb (str): Required symbol.

    Returns:
        list: symbol in formatted list
    """
    
    if smb in [':', 'colon', ' Colon', 'semicolon', 'Semicolon']:
        return colon()

    else:
        print(f'\n\n{smb}({type(smb)}) is not special symbol!\n\n')
      
    
def colon():
    """
    
        █
        
        █
        
    """
    smb =  [[0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]]

    return smb



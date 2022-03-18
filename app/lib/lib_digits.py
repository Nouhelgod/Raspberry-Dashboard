#FIXME: Bruh.

def get_digit(smb: smb):
    """Get large digit.

    Args:
        smb (str): Required digit (0 - 9)

    Returns:
        list: digit in formatted list
    """
    
    if smb == '0':
        return D0()

    elif smb == '1':
        return D1()

    elif smb == '2':
        return D2()

    elif smb == '3':
        return D3()

    elif smb == '4':
        return D4()

    elif smb == '5':
        return D5()

    elif smb == '6':
        return D6()

    elif smb == '7':
        return D7()

    elif smb == '8':
        return D8()

    elif smb == '9':
        return D9()

    else:
        print(f'\n\n{smb}({type(smb)}) is not digit!\n\n')


def D0():
    """
    █████
    █   █
    █   █
    █   █
    █████
    """
    digit = [[1, 1, 1, 1, 1], 
             [1, 0, 0, 0, 1], 
             [1, 0, 0, 0, 1], 
             [1, 0, 0, 0, 1], 
             [1, 1, 1, 1, 1]]

    return digit


def D1():
    """
    ███ 
      █ 
      █ 
      █ 
    █████
    """
    digit = [[1, 1, 1, 0, 0], 
             [0, 0, 1, 0, 0], 
             [0, 0, 1, 0, 0], 
             [0, 0, 1, 0, 0], 
             [1, 1, 1, 1, 1]]

    return digit


def D2():
    """
    █████ 
        █
    █████
    █ 
    █████
    """
    digit = [[1, 1, 1, 1, 1], 
             [0, 0, 0, 0, 1], 
             [1, 1, 1, 1, 1], 
             [1, 0, 0, 0, 0], 
             [1, 1, 1, 1, 1]]

    return digit


def D3():
    """
    █████ 
        █
      ███
        █ 
    █████
    """
    digit = [[1, 1, 1, 1, 1], 
             [0, 0, 0, 0, 1], 
             [0, 0, 1, 1, 1], 
             [0, 0, 0, 0, 1], 
             [1, 1, 1, 1, 1]]

    return digit


def D4():
    """
    █   █ 
    █   █
    █████
        █
        █
    """
    digit = [[1, 0, 0, 0, 1], 
             [1, 0, 0, 0, 1], 
             [1, 1, 1, 1, 1], 
             [0, 0, 0, 0, 1], 
             [0, 0, 0, 0, 1]]

    return digit


def D5():
    """
    █████ 
    █   
    █████
        █ 
    █████
    """
    digit = [[1, 1, 1, 1, 1], 
             [1, 0, 0, 0, 0], 
             [1, 1, 1, 1, 1], 
             [0, 0, 0, 0, 1], 
             [1, 1, 1, 1, 1]]

    return digit


def D6():
    """
    █████ 
    █   
    █████
    █   █ 
    █████
    """
    digit = [[1, 1, 1, 1, 1], 
             [1, 0, 0, 0, 0], 
             [1, 1, 1, 1, 1], 
             [1, 0, 0, 0, 1], 
             [1, 1, 1, 1, 1]]

    return digit


def D7():
    """
    █████ 
        █
      ███
        █ 
        █
    """
    digit = [[1, 1, 1, 1, 1], 
             [0, 0, 0, 0, 1], 
             [0, 0, 1, 1, 1], 
             [0, 0, 0, 0, 1], 
             [0, 0, 0, 0, 1]]

    return digit


def D8():
    """
    █████ 
    █   █
    █████
    █   █ 
    █████
    """
    digit = [[1, 1, 1, 1, 1], 
             [1, 0, 0, 0, 1], 
             [1, 1, 1, 1, 1], 
             [1, 0, 0, 0, 1], 
             [1, 1, 1, 1, 1]]

    return digit


def D9():
    """
    █████ 
    █   █
    █████
        █ 
        █
    """
    digit = [[1, 1, 1, 1, 1], 
             [1, 0, 0, 0, 1], 
             [1, 1, 1, 1, 1], 
             [0, 0, 0, 0, 1], 
             [0, 0, 0, 0, 1]]

    return digit


if __name__ == '__main__':
    """Just take a look"""
    
    help(D0)
    help(D1)
    help(D2)
    help(D3)
    help(D4)
    help(D5)
    help(D6)
    help(D7)
    help(D8)
    help(D9)
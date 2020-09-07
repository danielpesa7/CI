def integer_checker(obj):
    if isinstance(obj, int):
        print(f'{obj} is an integer. Operation succeed.')
        return obj
    else:
        try:
            obj = int(obj)
            print(f'{obj} has been parsed as an integer. Operation succeed')
            return obj
        except:
            print(f'{obj} cannot be parsed as an integer. Operation failed.')
            return None 
            
def float_checker(obj):
    if isinstance(obj, float):
        print(f'{obj} is a float. Operation succeed.')
        return obj
    else:
        try:
            obj = float(obj)
            print(f'{obj} has been parsed as a float. Operation succeed')
            return obj
        except:
            print(f'{obj} cannot be parsed as a float. Operation failed.')
            return None 
    
def string_checker(obj):
    if isinstance(obj, str):
        print(f'{obj} is a string. Operation succeed.')
        return obj
    else:
        try:
            obj = str(obj)
            print(f'{obj} has been parsed as an string. Operation succeed')
            return obj
        except:
            print(f'{obj} cannot be parsed as a string. Operation failed.')
            return None 
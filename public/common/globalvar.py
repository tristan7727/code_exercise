
def _init():
    global _global_dict
    _global_dict = {}
 
 
def set_value(key,value):
    """Define Global Var"""
    _global_dict[key] = value
 
 
def get_value(key):
    try:
        return _global_dict[key]
    except KeyError:
        return ''
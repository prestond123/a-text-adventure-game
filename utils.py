def get_list(name, scope):
    if(name in scope):
        return scope[name]
    return []

def get_dict(name, scope):
    if(name in scope):
        return scope[name]
    return {}

def print_messages(lines):
    for line in lines:
        print(line)
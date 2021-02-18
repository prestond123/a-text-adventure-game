def get_list(name, scope):
    if(name in scope):
        return scope[name]
    return []

def get_dict(name, scope):
    if(name in scope):
        return scope[name]
    return {}

def print_message(msg):
    print("--> {}".format(msg))

def print_messages(lines):
    for line in lines:
        print_message(line)
        
def has_attribute(item, attribute):
    if("attributes" in item and attribute in item["attributes"]):
        return True
    return False

def remove_attribute(item, attribute):
    attrs = []
    for attr in item["attributes"]:
       if not attr == attribute:
           attrs.append(attr)
    item["attributes"] = attrs

def add_attribute(item, attribute):    
    item["attributes"].append(attribute)

def build_index(container):
    index = {}
    for key in sorted(container):        
        container[key]["name"] = key
        index[key[0]] = index[key[0]] = container[key]
    return index


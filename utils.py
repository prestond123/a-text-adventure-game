import colour

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
        #if(not "name" in container[key]):
        container[key]["name"] = key
        index[key[0]] = index[key[0]] = container[key]
    return index

def get_inventory_display(items):
        visible = []      
       
        for item_name in sorted(items):            
            item = items[item_name]    
            config = item
            if(not type(item) == dict):
                config = item.get_config()            
            if(has_attribute(config, "room")):
                visible.append("'{}'".format(colour.yellow(item_name)))
            elif(has_attribute(config, "locked")):                
                visible.append("'{}'".format(colour.red(item_name)))            
            elif(has_attribute(config, "switchable")):
                visible.append("'{}'".format(colour.cyan(item_name)))
            # elif(has_attribute(config, "takeable")):
            #     visible.append("'{}'".format(colour.cyan(item_name)))
            elif(has_attribute(config, "container")):
                visible.append("'{}'".format(colour.cyan(item_name)))
            elif(has_attribute(config, "openable")):
                visible.append("'{}'".format(colour.cyan(item_name)))
            else:
                visible.append("'{}'".format(colour.green(item_name)))
                #visible.append("'{}'".format(item_name))
        formatted = []  
        part =[]
        max_per_line = 5  
        count = 1 
        for display in visible:
            if(count % max_per_line == 0):                
                part.append(display)
                formatted.append(", ".join(part))
                part=[]
            else:
                part.append(display)
            count += 1
        formatted.append(", ".join(part))
        
        return "\n  ".join(formatted)           

def get_item_collections(items):
    collections = { "routes": {}, "other": {} }
    for item_name in sorted(items):
        item = items[item_name]    
        config = item
        if(not type(item) == dict):
            config = item.get_config()
        if(has_attribute(config, "room")):
            collections["routes"][item_name] = item            
        else:
            collections["other"][item_name] = item            
    return collections
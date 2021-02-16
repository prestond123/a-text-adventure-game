inventory_item_names = {
    "front-door-key" : "front door key",
    "living-room-door-key": "living room door key",
    "talisman": "talisman"
}
door_names = {
    "front-door": "front door",
    "living-room-door": "living room door"
}
location_names = {
    "outside-front-door": "outside front door",
    "hall" : "hall",
    "living-room": "living room"
}

inventory_items = { }
inventory_items[inventory_item_names["front-door-key"]] = {                
    "description": "A large iron key, its quite heavy."
}
inventory_items[inventory_item_names["living-room-door-key"]] = {                
    "description": "A small key painted blue"
}

doors = { }
doors[door_names["front-door"]] = {
    "description": "A very large door, with a key hole for a large key",
    "requires": [inventory_item_names["front-door-key"]],
    "leads-to": "hall"
}
doors[door_names["living-room-door"]] = {  
    "description": "The living room door, has a key hole.",
    "required-inventory": ["living room door key"],
    "lends-to": "living room"
}
locations = { }
locations[location_names["outside-front-door"]] = {
    "routes": [ 
        door_names["front-door"]
    ],
    "actions": ["go"]
}
locations[location_names["hall"]] = {
    "routes": [ 
        door_names["front-door"],
        door_names["living-room-door"]
    ]
}
locations[location_names["living-room"]] = {
    "routes": [         
        door_names["living-room-door"]
    ]
}



locations["r1"] = {
    "description": ["You are in a dark room."],
    "reveal": { 
        "door 1": {
            "attributes": ["openable", "door"],
            "description" : ["You see a scruffy door."],
            "inside": {
                "r2": {
                    "attributes": ["room"],
                    "description" : ["You see a room: r2"]
                }
            }
        }, 
        "door 2": {
            "attributes": ["openable", "door"],
            "description" : ["You see a scruffy door."],
            "inside": {
                "r2": {
                    "attributes": ["room"],
                    "description" : ["You see a room: r2"]
                }
            }
        },        
        "tin": {
            "attributes": ["takeable"],
            "description": ["You see a small metal."],
            "taken": {
                "attributes": ["takeable", "openable"],
                "description": [
                    "You examine the tin closely.",
                    "It has a lable on the bottom with the numbers: 5 5 1 written on it"
                ],
                "inside": {
                    "key 2": {
                        "attributes": ["takeable"],
                        "description" : ["You see a small metal key"]
                    }
                }
            }
        },
        "table": {
            "description" : ["You see a table with some draws."],
            "inventory": {
                "draw 1": {
                    "attributes": ["openable"],
                    "description": ["You see a wooden draw, with a metal handle."],
                    "inside": {
                        "box": {
                            "attributes": ["takeable"],
                            "description": ["You see a small wooden box."],
                            "taken": {
                                "attributes": ["takeable", "openable"],
                                "description": [
                                    "You examine the box closly.",
                                    "It has a lable on the bottom with the numbers: 5 5 5 written on it"                                    
                                ],
                                "inside": {
                                    "key 1": {
                                        "attributes": ["takeable"],
                                        "description" : ["You see a small metal key"]
                                    }
                                }
                            }
                        },
                    }                    
                }
            }
        }, 
        "chair": {
            "description" : ["You see an old wooden chair with red leather padding studdied to chair with brass pins."]
        }
    }
}


locations["r2"] = {
    "description": ["You are in a light room."],
    "reveal": {
        "door 1": {
            "attributes": ["openable", "door"],
            "description" : ["You see a door."],
            "inside": {
                "r3": {
                    "attributes": ["room"],
                    "description" : ["You see a room: r3"]
                }
            }
        }, 
        "tub": {
            "attributes": ["takeable"],
            "description": ["You see a platic tub."],
            "taken": {
                "attributes": ["takeable", "openable"],
                "description": [
                    "You examine the tub closly, but see noting special"                    
                ],
                "inside": {
                    "key 3": {
                        "description" : ["You see a small metal key"]
                    }
                }
            }
        }
    }
}


player = {
    #"location-name": location_names["outside-front-door"]    
    "location-name": "r1"
}
game = {
    "prompt": "What would you like to do? ",
    "completed-inventory-item": inventory_item_names["talisman"],    
    "completed-messages": ["Well done!", "You completed the game."],
    "quitting-messages": ["You quit the game.", "Come back soon!"],
    "actions": ["quit", "help"]
}
config = {
    "game": game,
    "player": player,
    "locations": locations,    
}

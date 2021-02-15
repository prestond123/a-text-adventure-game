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

locations["test"] = {
    "reveal-routes": [        
        "door", "door"
    ],
    "reveal-items": [        
        "table", "chair"
    ]
}

player = {
    #"location-name": location_names["outside-front-door"]    
    "location-name": "test"
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
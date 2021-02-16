### test rooms
locations={}
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
                                    "You examine the box closely.",
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
                    "You examine the tub closely, but see noting special"                    
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

## game config
#locations = { }
locations["basement"] = {
    "description": ["You are in a dark room, all you can see is a glimmer of light comming down from some stairs."],
    "reveal": { 
        "stairs": {
            "attributes": ["room"],
            "description" : ["You see a stairs"]
        }
    }
}

locations["stairs"] = {
    "description": ["You are on the stairs."],    
    "reveal": {        
        "door": {
            "attributes": ["openable", "door", "locked"],            
            "unlock": "pin",   
            "unlock-method" : "pick",
            "description" : ["You see a scruffy door."],
            "inside": {
                "utility room": {
                    "attributes": ["room"],
                    "description" : ["It looks like a utility room"]
                }
            }
        }     
    }
}

locations["utility room"] = {
    "description": [
        "You see a washing machine, and some other white goods",
        "There are a few doors gong off this room"
    ],
    "reveal": {         
        "door 1": {
            "attributes": ["openable", "door"],
            "description" : ["You see a door."],
            "inside": {
                "office": {
                    "attributes": ["room"],
                    "description" : ["It looks like an office"]                        
                }
            }
        },
        "door 2": {
            "attributes": ["openable", "door"],
            "description" : ["You see a solid wooden door."],
            "inside": {
                "hall": {
                    "attributes": ["room"],
                    "description" : ["It looks like a hall"]
                }
            }
        }     

    }
}

locations["office"] = {
    "description": ["You are in an office."],
    "reveal": {
        "table": {
            "description" : ["You see a table with some draws."],
            "inventory": {
                "draw 1": {
                    "attributes": ["openable"],
                    "description": ["You see a wooden draw, with a metal handle."],
                    "inside": {
                        "battery": {
                            "attributes": ["takeable"],
                            "description" : ["You see a battery"]
                        }
                    }
                },
                "draw 2": {
                    "attributes": ["openable"],
                    "description": ["You see a wooden draw, with a metal handle."],
                    "inside": {
                        "box": {
                            "attributes": ["takeable"],
                            "description": ["You see a small wooden box."],
                            "taken": {
                                "attributes": ["takeable", "openable"],
                                "description": [
                                    "You examine the box closely.",
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

player = {
    #"location-name": location_names["outside-front-door"]    
    "location-name": "stairs",
    "inventory": {
        "badge": {
            "description" : [
                "You are wearing a Minecraft badge",
                "The badge has a pin on the back"
            ],
            "reveal": {
                "pin": {
                    "attributes": ["takeable", "damageable"],
                    "description": [
                        "You examine the pin closely.",
                        "Hint: It is thin and looks strong enough to pick locks."
                    ],
                    "damaged": {
                        "attributes": ["takeable", "damaged"],
                        "description": [
                            "You examine the pin closely.",
                            "It looks damaged."
                        ],  
                    }
                }
            }        
        },
        "wallet": {
            "description": ["You see your initials embosed on the wallet."],
            "attributes": ["takeable", "openable"],
            "inside": {
                "bank card": {
                    "attributes": ["takeable"],
                    "description": ["You see a bank card."],
                    "taken": {
                        "attributes": ["takeable"],
                        "description": [
                            "You examine the bank card closely.",
                            "It is thin, strong and flexable",                            
                            "It has your name on it",
                            "Hint: Criminals have been known to open doors with bank cards"
                        ]                        
                    }
                }
            }        
        }
    }
}
game = {
    "prompt": "What would you like to do? ",
    "completed-inventory-item": "talisman",    ## todo
    "completed-messages": ["Well done!", "You completed the game."],
    "quitting-messages": ["You quit the game.", "Come back soon!"],
    "actions": ["quit", "help"]
}
config = {
    "game": game,
    "player": player,
    "locations": locations,    
}

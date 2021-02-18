
locations={}

## game config
#locations = { }
combination1 = "567798"
locations["basement"] = {    
    "attributes": ["room"],
    "description": ["You are in a dark room, all you can see is a glimmer of light comming down from some stairs."],
    "reveal": {                            
        "stairs": {
            "attributes": ["room"],
            "description" : ["You see a stairs"]
        }
    },
    "light": "off",
    "on": {
        "light": {
            "on": {
                "description": ["You are in a dimly lit basement."],
                "reveal": {                    
                    "tub": {
                        "attributes": ["takeable"],
                        "description": [
                            "You see a platic tub."                            
                        ],
                        "taken": {
                            "attributes": ["takeable", "openable"],
                            "description": [
                                "You examine the tub closely, but see noting special"                    
                            ],
                            "inside": {
                                "office key": {
                                    "attributes": ["takeable"],
                                    "description" : ["You see a small metal key"]
                                }
                            },
                            "opened": ["The tub make a popping noise as you open it."]
                        }
                    },
                    "oil tin": {
                        "attributes": ["takeable"],
                        "description": [
                            "You see a small metal oil tin."
                        ],
                        "taken": {
                            "attributes": ["takeable", "openable"],
                            "description": [
                                "You examine the tin closely.",
                                "It has a lable on the bottom with the numbers: 5 5 1 written on it"
                            ],
                            "inside": {
                                "shirt button": {
                                    "attributes": ["takeable"],
                                    "description" : ["You see a small shitt button"]
                                }
                            },
                            "opened": [" The lid opens with a pop noise."]
                        }
                    },
                    "tool rack": {                        
                        "description" : ["You see a a tool rack on the wall."],
                        "inventory": {
                            "spanner": {      
                                "attributes": ["takeable"],      
                                "description" : ["You see an dirty spanner."]
                            },
                            "hammer": {      
                                "attributes": ["takeable"],      
                                "description" : ["You see a hammer."]
                            },
                            "small screw driver": {      
                                "attributes": ["takeable"],      
                                "description" : ["You see a small screw driver."]
                            },
                            "large screw driver": {      
                                "attributes": ["takeable"],      
                                "description" : ["You see a large screw driver."]
                            }
                        }
                    },
                    "notice board": {                        
                        "description" : ["The notice board has the numbers " + combination1 + " on it"]
                    }
                }
            }
        }
    }
}

locations["stairs"] = {
    "description": ["You are on the stairs."],    
    "reveal": {        
        "door": {
            "attributes": ["openable", "door", "locked"],            
            "unlock": "badge",   
            "unlock-method" : "pick",
            "description" : ["You see a scruffy door."],
            "inside": {
                "utility room": {
                    "attributes": ["room"],
                    "description" : ["It looks like a utility room"]
                }
            },
            "opened": ["The door squeaks open."]
        }     
    }
}

locations["utility room"] = {
    "attributes": ["room"],
    "description": [
        "You seem to be in a room used for washing stuff.",
        "There are some white goods, a sink, and towel.",
        "There are a few doors going off this room"
    ],
    "reveal": {
        "basement light switch": {
            "attributes": ["switchable"],
            "description" : ["You see a light switch next to the basement door."],
            "switched": ["The switch makes a click sound"],
            "event": ["basement", "light", "on"]
        },
        "washing machine": {            
            "description" : ["You see an old wasing machine."],
        },
        "box of soap powder": {            
            "attributes": ["takeable"],
            "description" : [
                "You see a open box of soap powder.",
                "You smell it and it smells floral."
            ],
        },
        "sink": {            
            "attributes": ["container"],
            "description" : ["You see an old ceramic sink, with some taps."],
            "inventory":
            {
                "hot tap": {            
                    "description" : ["You see the letter C on teh tap."],
                },
                "cold tap": {            
                    "description" : ["You see the letter C on teh tap"],
                },
                "soap": {            
                    "attributes": ["takeable"],
                    "description" : ["You see a bar of soap"],
                },
            }
        },
        "tea towel": {      
            "attributes": ["takeable"],      
            "description" : ["You see a dirty tea towel."]
        },
        "cupboard": {    
            "attributes": ["container", "openable"],        
            "description" : ["You see a cupboard mounted on the wall."],
            "inside": {
                "key hook rack": {
                    "attributes": ["container"],
                    "description": ["You see a key hook rack."],
                    "inventory": {
                        "car key": {
                            "attributes": ["takeable"],
                            "description": ["You see a key."]
                        }
                    }
                }
            },
            "opened": ["The cupboard clicks open."]
        },
         "door 1": {
            "attributes": ["openable", "door", "locked"],
            "description" : ["You see a solid wooden door."],
            "unlock": "opens from else where",
            "unlock-method" : "key",
            "inside": {
                "hall": {
                    "attributes": ["room"],
                    "description" : ["It looks like a hall"]
                }
            },
            "opened": ["The door squeaks open."]
            ## todo - on opened from hall - "event" also open here 
        },
        "door 2": {
            "attributes": ["openable", "door", "locked"],
            "description" : ["You see a door."],            
            "unlock": "office key",
            "unlock-method" : "key",
            "inside": {
                "office": {
                    "attributes": ["room"],
                    "description" : ["It looks like an office"]                        
                }
            },
            "opened": ["The door squeaks open."]
        },
        "door 3": {
            "attributes": ["openable", "door", "locked"],
            "description" : [
                "You see a heavy door", 
                "The door has a small window",
                "Looking throught the window, it looks like the leads outside."],            
            "unlock": "backdoor key",
            "unlock-method" : "key",
            "inside": {
                "exit": {
                    "attributes": ["room"],
                    "description" : ["It looks like you are free"]
                }
            },
            "opened": ["The door squeaks open."]
        } 
    }
}

locations["office"] = {
    "description": ["You are in an office."],
    "reveal": {
        "picture": {
            "attributes": ["container", "moveable"],
            "description" : ["You see a painted picture of a man with a dog."],
            "moved": ["You move the picture to the side"],
            "inside": {
                "safe": {
                    "attributes": ["safe"],
                    "description" : [
                        "You see a safe - the safe has a label that reads:",
                        "To open the safe use:",
                        "safe <nnnnnn>"
                    ],
                    "combination": combination1,
                    "inside": {
                        "backdoor key": {
                            "attributes": ["takeable"],
                            "description" : ["You see a large iron key."]
                        }
                    }      
                }
            }      
        },     
        "desk": {
            "description" : ["You see some draws on the desk."],
            "inventory": {
                "draw 1": {
                    "attributes": ["container", "openable", "locked"],
                    "description": ["You see a wooden draw, with a metal handle."],
                    "unlock": "draw key",
                    "unlock-method" : "key",
                    "inside": {
                        "battery": {
                            "attributes": ["takeable"],
                            "description" : ["You see a battery"]
                        }
                    },
                    "opened" : ["You hear the the sound of friction."]
                },
                "draw 2": {
                    "attributes": ["container", "openable"],
                    "description": ["You see a wooden draw, with a metal handle."],
                    "inside": {
                        "box": {
                            "attributes": ["container", "takeable"],
                            "description": ["You see a small wooden box."],
                            "taken": {
                                "attributes": ["takeable", "openable"],
                                "description": [
                                    "You examine the box closely.",
                                    "It has a lable on the bottom with the numbers: 5 5 5 written on it"                                    
                                ],
                                "inside": {
                                    "draw key": {
                                        "attributes": ["takeable"],
                                        "description" : ["You see a small metal key"]
                                    }
                                }
                            }
                        },
                    },
                    "opened" : ["You hear a squeak as it opens."]              
                }
            }
        }, 
        "chair": {            
            "description" : ["You see an old wooden chair with red leather padding studdied to chair with brass pins."]
        }
    }
}
locations["exit"] = {
    "description": ["You have escaped."]
}
player = {    
    "location-name": "basement",
    #"location-name": "utility room",
    #"location-name": "office",
    "inventory": {        
        "badge": {
            "attributes": ["takeable", "damageable"],
            "description" : [
                "You are wearing a Minecraft badge",
                "The badge has a pin on the back",
                "You examine the pin closely.",
                "Hint: It looks strong enough to pick locks."
            ],
            "damaged": {
                "attributes": ["takeable", "damaged"],
                "description": [
                    "You examine the badge closely.",
                    "The pin now looks damaged."
                ],  
            }            
        },
        "wallet": {
            "description": ["You see your initials embosed on the wallet."],
            "attributes": ["takeable", "openable"],
            "inside": {
                "bank card": {
                    "attributes": ["takeable"],
                    "description": [
                        "You examine the bank card closely.",
                        "It is thin, strong and flexable",                            
                        "It has your name on it",
                        "Hint: Criminals have been known to open doors with bank cards"
                    ],
                }
            },
            "opened" : ["You see some dust fall to the floor - you dont open this often."]       
        }
    }
}
game = {
    "prompt": "What would you like to do? ",    
    "completed-location": "exit",
    "completed-messages": ["Well done!", "You completed the game."],
    "quitting-messages": ["You quit the game.", "Come back soon!"],
    "max-carry": 8
}
config = {
    "game": game,
    "player": player,
    "locations": locations,    
}


locations={}

## game config
#locations = { }
combination1 = "567798"
combination2 = "778999"

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
                    "rug": {
                        "attributes": ["container", "moveable"],
                        "description" : ["You see a painted picture of a landscape."],
                        "moved": ["You move the picture to the side"],
                        "inside": {
                            "green key": {                    
                                "attributes": ["takeable"],                    
                                "description": ["You see a green key."]
                            }
                        }
                    },  
                    "cupboard": {    
                        "attributes": ["container", "openable"],        
                        "description" : ["You see a cupboard mounted on the wall."],
                        "inside": {
                            "key hook rack": {
                                "attributes": ["container"],
                                "description": ["You see a key hook rack."],
                                "inventory": {
                                    "draw 4 key": {
                                        "attributes": ["takeable"],
                                        "description": ["You see a key with a number 4 on it."]
                                    },
                                    "red key": {
                                        "attributes": ["takeable"],
                                        "description": ["You see a red key."]
                                    }
                                }
                            }
                        },
                        "opened": ["The cupboard clicks open."]
                    },
                    "safe": {
                        "attributes": ["safe"],
                        "description" : [
                            "You see a safe - the safe has a label that reads:",
                            "To open the safe use:",
                            "safe <nnnnnn>"
                        ],
                        "combination": combination1,
                        "inside": {
                            "paper 2": {
                                "attributes": ["takeable"],
                                "description" : [
                                    "A piece of paper ripped down the right hand side.",
                                    "The paper has the number: "+ combination1[:3]
                                ]                                    
                            }
                        }      
                    },               
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
                                "It has a lable on the bottom with the numbers: 999 written on it"
                            ],
                            "inside": {
                                "shirt button": {
                                    "attributes": ["takeable"],
                                    "description" : ["You see a small shirt button"]
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
                        "description" : [
                            "The notice board has the numbers: 999912 written really small on it"]
                    }
                }
            }
        }
    }
}

locations["stairs"] = {
    "description": ["You are on the stairs."],    
    "reveal": {           
        "picture": {
            "attributes": ["container", "moveable"],
            "description" : ["You see a painted picture of a landscape."],
            "moved": ["You move the picture to the side"],
            "inside": {
                "nail": {                    
                    "attributes": ["container", "takeable", "damageable"],
                    "description" : [
                        "You see a rusty nail in the wall",
                        "The nail looks like it can be pulled out",                        
                    ],
                    "taken": {                        
                        "description": [
                            "You examine the nail closely.",
                            "It looks quite strong."
                        ],
                    },
                    "damaged": {
                        "attributes": ["takeable", "damaged"],
                        "description": [
                            "You examine the nail closely.",
                            "The nail now looks damaged."
                        ]
                    }                        
                }
            }      
        },         
        "door": {
            "attributes": ["openable", "door", "locked"],            
            "unlock": "nail",   
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
            "attributes": ["container", "openable"],      
            "description" : [
                "You see an old wasing machine.",
                "The washing machine has a serial number: 665123"
            ],
            "inside": {                
                "draw 2 key": {
                    "attributes": ["takeable"],
                    "description": ["You see a key with a number 2 on it."],                    
                }
            },
            "opened": ["The door clicks open."]            
        },
        "soap powder": {            
            "attributes": ["takeable"],            
            "description" : [
                "You see a open box of soap powder, for a washing machine.",
                "You smell it and it smells floral."
            ],
        },
        "sink": {            
            "attributes": ["container"],
            "description" : ["You see an old ceramic sink, with some taps."],
            "inventory":
            {
                "hot tap": {            
                    "description" : ["You see the letter H on the tap."],
                },
                "cold tap": {            
                    "description" : ["You see the letter C on the tap"],
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
                            "description": ["You see a key with BMW printed on it."]
                        },
                        "blue key": {
                            "attributes": ["takeable"],
                            "description": ["You see a blue key."]
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
                "Looking through the window, it looks like the leads outside."],            
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
                    "combination": combination2,
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
                    "unlock": "draw 1 key",
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
                    "attributes": ["container", "openable", "locked"],
                    "description": ["You see a wooden draw, with a metal handle."],
                    "unlock": "draw 2 key",
                    "unlock-method" : "key",
                    "inside": {
                        "paper 1": {
                            "attributes": ["takeable"],
                            "description" : [
                                "A piece of paper ripped down the left hand side.",
                                "The paper has the number: "+ combination1[3:]
                            ]                                
                        }
                    },
                    "opened" : ["You hear the the sound of friction."]
                },
                "draw 3": {
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
                                    "It has a lable on the bottom with the numbers: 788 written on it"                                    
                                ],
                                "inside": {
                                    "draw 1 key": {
                                        "attributes": ["takeable"],
                                        "description" : ["You see a small metal key with the number 1 on it."]
                                    }
                                }
                            }
                        },
                    },
                    "opened" : ["You hear a squeak as it opens."]              
                },
                "draw 4": {
                    "attributes": ["container", "openable", "locked"],
                    "description": ["You see a wooden draw, with a metal handle."],
                    "unlock": "draw 4 key",
                    "unlock-method" : "key",
                    "inside": {
                        "paper 3": {
                            "attributes": ["takeable"],
                            "description" : [
                                "A piece of paper.",
                                "The paper has the number: "+ combination2
                            ]                                
                        }
                    },
                    "opened" : ["You hear the the sound of friction."]
                },
            }
        }, 
        "chair": {            
            "description" : ["You see an old wooden chair with red leather padding studdied to chair with brass pins."]
        }
    }
}
locations["rear porch"] = {    
    "attributes": ["room"],
    "description": ["You are looking out to a garden."],
    "reveal": {                                  
        "front porch": {
            "attributes": ["room"],
            "description" : ["You see a shed"]
        },
        "shed patio": {
            "attributes": ["room"],
            "description" : ["You see a shed"]
        },
        "garage entrance": {
            "attributes": ["room"],
            "description" : ["You see a garage"]
        }
    },
}

locations["shed patio"] = {    
    "attributes": ["room"],
    "description": ["You are in the garden next to a shed."],
    "reveal": {                            
        "rear porch": {
            "attributes": ["room"],
            "description" : ["You see a shed"]
        },
        "shed door": {
            "attributes": [
                "openable", "door"
                #, "locked"
            ],
            "description" : [
                "You see a wooden door", 
                "The door has a small window",
                "Looking through the window, it looks like there is some items inside."],            
            "unlock": "shed key",
            "unlock-method" : "key",
            "inside": {
                "shed": {
                    "attributes": ["room"],
                    "description" : ["It looks like a shed"]
                }
            },
            "opened": ["The door squeaks open."]
        },        
    }
}

locations["garage entrance"] = {    
    "attributes": ["room"],
    "description": ["You are in the garden next to a garage."],
    "reveal": {                            
        "rear porch": {
            "attributes": ["room"],
            "description" : ["You see a shed"]
        },
        "front porch": {
            "attributes": ["room"],
            "description" : ["You see a shed"]
        },
        "garage door": {            
            "attributes": [
                "openable", "door"
                #, "locked"
            ],
            "description" : [
                "You see a heavy door",                                 
            ],            
            "unlock": "garage key",
            "unlock-method" : "key",
            "inside": {
                "garage": {
                    "attributes": ["room"],
                    "description" : ["It looks like a garage"]
                }
            },
            "opened": ["The door squeaks open."]
        }     
    }
}

locations["garage"] = {    
    "attributes": ["room"],
    "description": ["You are in the garage."],
    "reveal": {      
        "cupboard": {    
            "attributes": ["container", "openable"],        
            "description" : ["You see a cupboard mounted on the wall."],
            "inside": {
                "key hook rack": {
                    "attributes": ["container"],
                    "description": ["You see a key hook rack."],
                    "inventory": {
                        "shed key": {
                            "attributes": ["takeable"],
                            "description": ["You see a key with shed printed on it."]
                        },
                        "hall key": {
                            "attributes": ["takeable"],
                            "description": ["You see a key with hall printed on it."]
                        }
                    }
                }
            },
            "opened": ["The cupboard clicks open."]
        }                      
    }
}

locations["shed"] = {    
    "attributes": ["room"],
    "description": ["You are in the shed."],
    "reveal": {                            
    }
}

locations["front porch"] = {    
    "attributes": ["room"],
    "description": ["You are in the front porch."],
    "reveal": {                            
        "rear porch": {
            "attributes": ["room"],
            "description" : ["You see a porch"]
        },
        "garage entrance": {
            "attributes": ["room"],
            "description" : ["You see a garage"]
        },        
        "main drive": {
            "attributes": ["room"],
            "description" : ["You see a gravelled drive"]
        }
    }
}

locations["main drive"] = {    
    "attributes": ["room"],
    "description": ["You are on the main drive ay of the house."],
    "reveal": {                            
        "gate house": {
            "attributes": ["room"],
            "description" : ["You see a gate house next to a large metal gate"]
        }        
    }
}

locations["gate house"] = {    
    "attributes": ["room"],
    "description": ["You are at the gate house."],
    "reveal": {   
        "cupboard": {    
            "attributes": ["container", "openable"],        
            "description" : ["You see a cupboard mounted on the wall."],
            "inside": {
                "key hook rack": {
                    "attributes": ["container"],
                    "description": ["You see a key hook rack."],
                    "inventory": {
                        "garage key": {
                            "attributes": ["takeable"],
                            "description": ["You see a key with garage written on it."]
                        }                        
                    }
                }
            },
            "opened": ["The cupboard clicks open."]
        },                         
        "main gate": {
            "attributes": ["openable", "door", "locked"],
            "description" : [
                "You see a high heavy metal gate with spikes on top",                 
                "Looking through the gate, you see the outside world.",
                "You appear to be in the middle of the countryside - ",
                "there is nothing but hills and trees outside, with",
                "a dirt track leading away..."],            
            "unlock": "garage key",
            "unlock-method" : "key",
            "inside": {
                "exit": {
                    "attributes": ["room"],
                    "description" : ["It looks like a a way out."]
                }
            },
            "opened": ["The door opens with a grinding sqeak."]
        }        
    }
}

player = {    
    "location-name": "basement",
    #"location-name": "utility room",
    #"location-name": "office",
    #"location-name": "rear porch",
    
    "inventory": {        
        "badge": {
            "attributes": ["takeable", "damageable"],
            "description" : [
                "You are wearing a Minecraft badge",
                "The badge has a pin on the back",
                "You examine the pin closely.",
                "Hint: It looks like the pin is too weak to pick locks."
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
    "max-carry": 3
}
config = {
    "game": game,
    "player": player,
    "locations": locations,    
}

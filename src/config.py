""" Config file for the encounter generator """

travel_types = {"highway": highway_encounter_chances,
                "road": road_encounter_chances,
                "trail": trail_encounter_chances,
                "wilderness": wilderness_encounter_chances,
                "boat",
                "underwater"}

highway_encounter_chances = {"merchants": 85,
                             "travellers": 75,
                             "lonetraveller": 65,
                             "soldiers": 45,
                             "adventurers": 35,
                             "monsters":  5,
                             "animals": 3}

road_encounter_chances = {"merchants": 65,
                          "travellers": 50,
                          "lonetraveller": 40,
                          "soldiers": 35,
                          "adventurers": 20,
                          "monsters": 10,
                          "animals": 15}

trail_encounter_chances = {"merchants": 0,
                           "travellers": 15,
                           "lonetraveller": 5,
                           "soldiers": 10,
                           "adventurers": 5,
                           "monsters":  35,
                           "animals": 45}

wilderness_encounter_chances = {"merchants": 0,
                                "travellers": 5,
                                "lonetraveller": 1,
                                "soldiers": 20,
                                "adventurers": 5,
                                "monsters":  45,
                                "animals": 65}

terraintypemod = {"arctic": 80,
                  "coast": 120,
                  "desert": 80,
                  "forest": 120,
                  "Grassland": 100,
                  "hills": 100,
                  "mountains": 75,
                  "swamp": 120,
                  "underdark": 100,
                  "underwater": 100,
                  "urban": 125}

maxencounters = {"merchants": 20,
                 "travellers": 15,
                 "lonetraveller": 10,
                 "soldiers": 5,
                 "adventurers": 3,
                 "monsters": 2,
                 "animals": 2}

nighttimemods = {"merchants": 0,
                 "travellers": 5,
                 "lonetraveller": 25,
                 "soldiers": 15,
                 "adventurers": 25,
                 "monsters": 125,
                 "animals": 135}

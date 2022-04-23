// Questions + Responses
const sentences = [
    [
        "Academic", 
        [
            "How is your day?", 
            [
                ["My day has been good", 1],
                ["Good", .5],
                ["Been real litty homie", -1],
                ["It aight", -1],
            ],
            "Can I visit your home?", 
            [
                ["Heck no", -1],
                ["No, not at the moment", 1],
                ["No", .5],
                ["nah it mah crib, not yous", -1]
            ],
            "What do you do when you are tired?", 
            [
                ["hit the hay", -1],
                ["just be chillin at mah crib", -1],
                ["I relax at home", 1],
                ["Relax", .5]
            ],
            "Where are my keys?", 
            [
                ["I am not sure", 1],
                ["Ion even kno", -1],
                ["Dunno man", -1],
                ["I do not know", 1]
            ]
        ] 
    ],
    [
        "Casual", 
        [
            "Hey man you wanna go home?", 
            [
                ["Yeah I'm down", 1],
                ["I be goin to mah crib alone", -1],
                ["Yes, I am willing to go home", -1],
                ["Sure dude", 1],
            ],
            "Hey bro, can I copy your homework?", 
            [
                ["No, you cannot", -1],
                ["Nah man", 1],
                ["Heck no", 1],
                ["Nah broski i got to up mah learnin", -1]
            ],
            "How's work man?", 
            [
                ["Dude, my boss is not cool at all", 1],
                ["Dawg, it killin' me for reals", -.5],
                ["I am unemployed", -1],
                ["My boss has been great", -1]
            ],
            "Me and the guys are about to open a cold one, you want one?", 
            [
                ["Sure, gimme one", 1],
                ["No, I do not want one", -1],
                ["Forsure forsure dawg", -.5],
                ["Yeah lemme have one", 1]
            ]
        ] 
    ],
    [
        "Slang", 
        [
            "Yo lessgo to da park", 
            [
                ["Yeah I'm down", -.5],
                ["I am in agreement", -1],
                ["Forsure forsure homie", 1],
                ["Ayo bet", 1],
            ],
            "Ayo man how was that party at mah hooch?", 
            [
                ["Had a blast", .5],
                ["It was of most enjoyment", -1],
                ["Yo it was off the hook", 1],
                ["It was not great", -1]
            ],
            "Dem boys in blue lookin real goofy ahh", 
            [
                ["Deadass man, like for reals", 1],
                ["No, police officers look okay", -1],
                ["Yuh, lotta bacon", 1],
                ["Yeah, kind of", -.5]
            ],
            "Bring yo self to mah crib sometime", 
            [ 
                ["Nah im chilling", .5],
                ["No, but thank you", -1],
                ["Aight bet imma hop down fosho", 1],
                ["Sometime else fosho", .5]
            ]
        ] 
      ]
  ];

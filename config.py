class config:
    global deltaTime, RED_COLOR, YELLOW_COLOR, GREEN_COLOR, LightCycle, LightCycleLength
    deltaTime = 0.05
    
    RED_COLOR       = 1
    YELLOW_COLOR    = 2
    GREEN_COLOR     = 3
    #             green, yellow, red(when both lights are red)
    LightCycle = [5,     1,      0.5]
    
    LightCycleLength = 0
    for i in LightCycle:
        LightCycleLength += i

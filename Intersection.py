import curses, config


class Intersection:
    INTERSECTIONS = []
    
    global DrawIntersections
    def DrawIntersections(scr):
        for intersection in Intersection.INTERSECTIONS:
            intersection.Draw(scr)

    def Draw(self, scr):
        self.time += config.deltaTime
        if self.time > config.LightCycleLength:
            self.time -= config.LightCycleLength
            self.state = not self.state

        lightState = [config.RED_COLOR, config.RED_COLOR]
        if self.time < config.LightCycle[0]:
            lightState[int(not self.state)] = config.GREEN_COLOR
        elif self. time < config.LightCycle[0] + config.LightCycle[1]:
            lightState[int(not self.state)] = config.YELLOW_COLOR
        else:
            lightState[int(not self.state)] = config.RED_COLOR

        scr.addstr(self.y, self.x * 2, "|", curses.color_pair(lightState[0]))
        scr.addstr(self.y, self.x * 2 + 1, "-", curses.color_pair(lightState[1]))
    
    def Free(self):
        pass
    
    def __init__(self, Y, X):
        # what cycle the light is on (which one is currently changing)
        self.state = False # 0 = horizontal, 1 = vertical
        self.time = 0
        self.y = Y
        self.x = X
        self.index = len(Intersection.INTERSECTIONS)
        Intersection.INTERSECTIONS.append(self)

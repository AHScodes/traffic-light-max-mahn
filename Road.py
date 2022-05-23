import curses, Intersection, config
class Road:
    ROADS = []

    global DrawRoads
    def DrawRoads(scr):
        for road in Road.ROADS:
            road.Draw(scr)

    def Draw(self, scr):
        my, mx = scr.getmaxyx()
        if self.rot:
            for i in range(my):
                scr.addstr(i, self.pos * 2, "||")
        else:
            scr.addstr(self.pos, 0, "=" * mx)

    def Free(self):
        Road.ROADS.remove(self.index)

        # check for intersections to remove

    def __init__(self, rot:bool, pos:int):
        self.rot = rot # 0 = horizontal, 1 = vertical
        self.pos = pos
        self.index = len(Road.ROADS)
        Road.ROADS.append(self)

        # check for intersections to create
        new_intersections = []
        for road in Road.ROADS:
            if road.rot != self.rot:
                new_intersections.append(road.pos)
        if self.rot:
            for new_i in new_intersections:
                Intersection.Intersection(new_i, self.pos)
        else:
            for new_i in new_intersections:
                Intersection.Intersection(self.pos, new_i)


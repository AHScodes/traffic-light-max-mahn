import Road, Intersection, curses, config
from time import sleep

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(True)
curses.start_color()
curses.init_pair(config.RED_COLOR, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(config.YELLOW_COLOR, curses.COLOR_BLACK, curses.COLOR_YELLOW)
curses.init_pair(config.GREEN_COLOR, curses.COLOR_BLACK, curses.COLOR_GREEN)


Road.Road(False, 3)
Road.Road(False, 8)
Road.Road(True, 3)
Road.Road(True, 5)
#Intersection.Intersection(3, 3)
while True:
    stdscr.clear()
    ch = stdscr.getch()
    if ch == ord('q'):
        break
    Road.DrawRoads(stdscr)
    Intersection.DrawIntersections(stdscr)
    stdscr.refresh()
    sleep(config.deltaTime)


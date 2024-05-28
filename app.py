import curses #module for console input output, styling the terminal
from curses import wrapper #initialize the curses application

def main(stdscr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) #initialize color pair for text background and foreground [if typed correctly]
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK) #initialize color pair for text background and foreground [If typed incorrectly]
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK) #initialize color pair for text background and foreground [If typed incorrectly]
    stdscr.clear() #clear the screen
    stdscr.addstr("namaste duniya!!", curses.color_pair(2)) #add string to the screen with color pair 1
    stdscr.refresh()
    stdscr.getkey() #wait for user to inpit something
    
wrapper(main) #initialize the curses application

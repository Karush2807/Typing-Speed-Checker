import curses #module for console input output, styling the terminal
from curses import wrapper #initialize the curses application

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing speed checker!")
    stdscr.addstr("\nPress any key to start the test")
    stdscr.refresh()
    stdscr.getkey()

def test_typing(stdscr):
    practice_text="The quick brown fox jumps over the lazy dog near the riverbank on a sunny day."
    current_text=[] #jo user type krega
    stdscr.clear()
    stdscr.addstr(practice_text)
    stdscr.refresh()
    stdscr.getkey()



def main(stdscr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) #initialize color pair for text background and foreground [if typed correctly]
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK) #initialize color pair for text background and foreground [If typed incorrectly]
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK) #initialize color pair for text background and foreground [If typed incorrectly]
    
    start_screen(stdscr)
    test_typing(stdscr)


wrapper(main) #initialize the curses application

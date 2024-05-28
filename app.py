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

    while True:
        key=stdscr.getkey()

        if ord(key)==27: #if escape key is pressed
            break

        if key in("KEY_BACKSPACE", "\b", "\x7f"):
            current_text.pop()

        current_text.append(key)

        #stdscr.clear()
        stdscr.addstr(practice_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
        
        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) #initialize color pair for text background and foreground [if typed correctly]
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK) #initialize color pair for text background and foreground [If typed incorrectly]
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) #initialize color pair for text background and foreground [If typed incorrectly]
    
    start_screen(stdscr)
    test_typing(stdscr)


wrapper(main) #initialize the curses application

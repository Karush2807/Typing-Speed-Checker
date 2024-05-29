import curses #module for console input output, styling the terminal
from curses import wrapper #initialize the curses application
import time
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing speed checker!")
    stdscr.addstr("\nPress any key to start the test")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
        stdscr.addstr(target)
        stdscr.addstr(1, 0, f"WPM: {wpm}")
        
        
        for i, char in enumerate(current):
            correct_text= target[i]
            color= curses.color_pair(1)

            if char!=correct_text:
                color=curses.color_pair(2)

            stdscr.addstr(0, i, char, color)

def test_typing(stdscr):
    practice_text="The quick brown fox jumps over the lazy dog near the riverbank on a sunny day."
    current_text=[] #jo user type krega
    
    while True:
        stdscr.clear()
        display_text(stdscr, practice_text, current_text)
        stdscr.refresh()
        
        key=stdscr.getkey()

        if ord(key)==27: #if escape key is pressed
            break

        if key in("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text)>0:
                current_text.pop()
        
        elif len(current_text)<len(practice_text):
            current_text.append(key)

        

        stdscr.clear()
        stdscr.addstr(practice_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
        
        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN) #initialize color pair for text background and foreground [if typed correctly]
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED) #initialize color pair for text background and foreground [If typed incorrectly]
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) #initialize color pair for text background and foreground [If typed incorrectly]
    
    start_screen(stdscr)
    test_typing(stdscr)


wrapper(main) #initialize the curses application

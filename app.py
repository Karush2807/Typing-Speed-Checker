import curses #module for console input output, styling the terminal
from curses import wrapper #initialize the curses application
import time
import random

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

def load_text():
    with open("text.txt", 'r') as f:
        lines=f.readlines()
        return random.choice(lines).strip()

def test_typing(stdscr):
    practice_text=load_text()
    current_text=[] #jo user type krega
    wpm=0
    time_start= time.time()
    stdscr.nodelay(True)

    while True:
        time_taken= max(time.time()-time_start, 1)
        wpm=round((len(current_text)/(time_taken/60))/5)
        stdscr.clear()
        display_text(stdscr, practice_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text)==practice_text:
            stdscr.nodelay(False)
            break
        
        try:
            key=stdscr.getkey()
        except curses.error:
            continue
        
        if ord(key)==27: #if escape key is pressed
            break

        if key in("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text)>0:
                current_text.pop()
        
        elif len(current_text)<len(practice_text):
            current_text.append(key)

        

        

        
        
        stdscr.refresh()
        stdscr.getkey()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN) #initialize color pair for text background and foreground [if typed correctly]
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED) #initialize color pair for text background and foreground [If typed incorrectly]
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) #initialize color pair for text background and foreground [If typed incorrectly]
    
    start_screen(stdscr)
    test_typing(stdscr)

    stdscr.addstr(2, 0, "text Completed:)")
    stdscr.getkey()


wrapper(main) #initialize the curses application

import curses  # module for console input/output, styling the terminal
from curses import wrapper  # initialize the curses application
import time  # module to handle time-related functions
import random  # module to generate random numbers

def start_screen(stdscr):
    # Clears the screen and displays the welcome message
    stdscr.clear()  # removal of previous text, if any
    stdscr.addstr("Welcome to the typing speed checker!")
    stdscr.addstr("\nPress any key to start the test")
    stdscr.refresh()  # refreshes the screen to update with the new text
    stdscr.getkey()  # waits for the user to press any key to proceed

def display_text(stdscr, target, current, wpm=0):
    #selecting the cetre position for displaying text
    rows, cols= stdscr.getmaxyx() #this fucntion will get dimensions of total window
    start_row= (rows-len(target.splitlines()))//2 #calculate the starting row for center alignment
    
    # Set a larger font size for display
    stdscr.attron(curses.A_BOLD)
    stdscr.attron(curses.A_UNDERLINE)

    #making the text display in the center screen
    for idx, line in enumerate(target.splitlines()):
        stdscr.addstr(start_row + idx, (cols - len(line.encode()))//2, line)

    stdscr.attroff(curses.A_BOLD)
    stdscr.attroff(curses.A_UNDERLINE)

    
    # Displays the target text, the current text typed by the user, and the current WPM (Words Per Minute)
    # stdscr.addstr(target)  # display the target text
    # stdscr.addstr(3, 0, f"WPM: {wpm}")  # display the current WPM at the second line

    stdscr.addstr(start_row + len(target.splitlines()) + 2, 0, f"WPM: {wpm}")  # Display WPM below the text

    # Iterate through the current text typed by the user
    for i, char in enumerate(current):
        correct_text = target[i]  # correct character at the current position
        color = curses.color_pair(1)  # default color for correct character

        if char != correct_text:
            color = curses.color_pair(2)  # change color if the character is incorrect

        stdscr.addstr(start_row, (cols - len(target.encode()))//2+i, char, color)  # display the character with the determined color

def load_text():
    # Loads random text from a file for typing practice
    with open("text.txt", 'r') as f:
        lines = f.readlines()  # read all lines from the file
        return random.choice(lines).strip()  # return a random line after stripping any extra whitespace

def test_typing(stdscr):
    # Main function to handle the typing test logic
    practice_text ="namaste duniya"  # load the practice text
    current_text = []  # list to store the characters typed by the user
    wpm = 0  # initialize WPM (Words Per Minute) to 0
    time_start = time.time()  # get the current time
    stdscr.nodelay(True)  # non-blocking mode, doesn't wait for user to press key

    while True:
        # Calculate time taken and update WPM
        time_taken = max(time.time() - time_start, 1)
        wpm = round((len(current_text) / (time_taken / 60)) / 5)
        stdscr.clear()  # clear the screen
        display_text(stdscr, practice_text, current_text, wpm)  # update the display with the current state
        stdscr.refresh()  # refresh the screen

        # If the user has typed the entire practice text, stop the test
        if "".join(current_text) == practice_text:
            stdscr.nodelay(False)  # switch back to blocking mode
            break

        stdscr.addstr("text completed :)")
        try:
            key = stdscr.getkey()
        except curses.error as e:
            if str(e) == "no input":
                time.sleep(0.1)  # wait briefly before trying again
                continue
            else:
                raise  # re-raise other curses errors

        # Handle the escape key (ASCII 27)
        if ord(key) == 27:
            break

        # Handle backspace key
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()  # remove the last character from current_text

        # Append the key press to current_text if it's within the length of practice_text
        elif len(current_text) < len(practice_text):
            current_text.append(key)

        stdscr.refresh()  # refresh the screen
        #stdscr.getkey()  # get the next key press

def main(stdscr):
    # Initialize color pairs for correct and incorrect text
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)  # correct text
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)  # incorrect text
    

    start_screen(stdscr)  # display the start screen
    test_typing(stdscr)  # start the typing test

    # Display completion message
    # stdscr.addstr(2, 0, "Text Completed :)")
    stdscr.getkey()  # wait for the user to press a key

# Initialize the curses application
wrapper(main)

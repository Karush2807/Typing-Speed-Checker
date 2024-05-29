import curses  # module for console input/output, styling the terminal
from curses import wrapper  # initialize the curses application
import time  # module to handle time-related functions
import random  # module to generate random numbers

def start_screen(stdscr):
    # Clears the screen and displays the welcome message
    stdscr.clear()  # remove any previous text on the screen
    stdscr.addstr("Welcome to the typing speed checker!")
    stdscr.addstr("\nPress any key to start the test")
    stdscr.refresh()  # update the screen with the new text
    stdscr.getkey()  # wait for the user to press any key to proceed

def display_text(stdscr, target, current, wpm=0):
    # Center-align the text vertically and horizontally
    rows, cols = stdscr.getmaxyx()  # get the dimensions of the screen
    start_row = (rows - len(target.splitlines())) // 2  # calculate the starting row for center alignment

    # Set attributes for text display
    stdscr.attron(curses.A_BOLD)  # enable bold text
    stdscr.attron(curses.A_UNDERLINE)  # enable underlined text

    # Display each line of the target text centered horizontally
    for idx, line in enumerate(target.splitlines()):
        stdscr.addstr(start_row + idx, (cols - len(line.encode())) // 2, line)

    stdscr.attroff(curses.A_BOLD)  # disable bold text
    stdscr.attroff(curses.A_UNDERLINE)  # disable underlined text

    # Display the current WPM below the text
    stdscr.addstr(start_row + len(target.splitlines()) + 2, 0, f"WPM: {wpm}")

    # Iterate through the current text typed by the user
    for i, char in enumerate(current):
        correct_text = target[i]  # get the correct character at the current position
        color = curses.color_pair(1)  # default color for correct character

        # Change color if the character is incorrect
        if char != correct_text:
            color = curses.color_pair(2)

        # Display the character with the determined color
        stdscr.addstr(start_row, (cols - len(target.encode())) // 2 + i, char, color)

def load_text():
    # Loads random text from a file for typing practice
    with open("text.txt", 'r') as f:
        lines = f.readlines()  # read all lines from the file
        return random.choice(lines).strip()  # return a random line after stripping any extra whitespace

def test_typing(stdscr):
    # Main function to handle the typing test logic
    practice_text = load_text()  # load the practice text
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

def main(stdscr):
    # Initialize color pairs for correct and incorrect text
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)  # correct text
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)  # incorrect text

    start_screen(stdscr)  # display the start screen
    test_typing(stdscr)  # start the typing test

    stdscr.getkey()  # wait for the user to press a

# Initialize the curses application
wrapper(main)
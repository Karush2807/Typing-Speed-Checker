# Typing Speed Checker

This is a simple command-line based typing speed checker program written in Python using the `curses` module. The program tests the user's typing speed by presenting a random text from a file and measuring how fast the user can type it correctly.

## How It Works

The program consists of the following main components:

1. **Start Screen**: Displays a welcome message and waits for the user to press any key to start the test.
2. **Text Loading**: Loads a random line of text from a file called `text.txt` which contains different phrases.
3. **Typing Test**: Measures the user's typing speed and displays the number of words per minute (WPM) as the user types.
4. **End Screen**: Shows a completion message once the user has successfully typed the given text.

## Functionality

### start_screen(stdscr)

This function initializes the start screen. It clears the screen, displays a welcome message, and waits for the user to press any key to start the test.

### display_text(stdscr, target, current, wpm=0)

This function is responsible for displaying the target text, the current text typed by the user, and the current WPM. It highlights the correctly typed characters in green and incorrectly typed characters in red.

### load_text()

This function reads the `text.txt` file and returns a random line from the file. The text file should contain phrases, each on a new line.

### test_typing(stdscr)

This is the main function for the typing test. It:
- Loads the practice text.
- Initializes the timer.
- Continuously updates the display with the user's input and calculates the WPM.
- Ends the test when the user correctly types the entire practice text or presses the Escape key.

### main(stdscr)

This function sets up the color pairs for correct and incorrect text and runs the start screen and typing test functions. After the test, it displays a completion message.

## How to Run

1. Ensure you have Python installed on your system.
2. Create a `text.txt` file in the same directory as the script, and populate it with phrases, each on a new line.
3. Run the script using a Python interpreter.

```bash
python app.py
```


# ConsolPomo

## Pomodoro Timer with Sound Alerts

This Python script implements a customizable Pomodoro timer that helps in managing work and break cycles to enhance productivity. It leverages the simple yet effective Pomodoro technique, breaking down work into intervals, traditionally 25 minutes in length, separated by short breaks. A crucial additional feature of this implementation is the inclusion of sound alerts to indicate the beginning and ending of work and break periods, making it easier to follow the regime without constantly checking the clock.

### Features

- **Customizable Timers**: Set your own duration for work intervals, short breaks, and long breaks to tailor the Pomodoro cycles to your personal or professional needs.
- **Countdown Feedback**: Provides real-time countdown feedback, indicating how many minutes are left in the current phase (work or break), enhancing your awareness of time without being disruptive.
- **Sound Alerts**: Plays a sound alert at the end of each phase, signaling it's time to switch from work to break or vice versa. This feature uses a Tibetan singing bowl sound (file named 'tibetan_alert.wav'), but it can be customized by replacing the sound file.
- **Configurable Cycles**: Define the number of work-break cycles you wish to complete before taking a long break, and specify how many cycles constitute a full session.
- **Gracious Error Handling**: Includes basic error handling to manage common issues, such as incorrect input types and interruptions (e.g., pressing Ctrl+C to stop the timer).

### How to Use

1. **Clone or Download**: Start by cloning this repository or downloading the source code.
2. **Prepare the Sound File**: Ensure you have a sound file named `tibetan_alert.wav` in the same directory as the script. You can replace this with any sound file of your choice, but be sure to update the file name in the code accordingly.
3. **Install Dependencies**: This script requires Python 3 and Pygame. If you don't have Pygame installed, you can install it via pip:
    ```
    pip install pygame
    ```
4. **Run the Script**: Execute the script in your terminal or command prompt:
    ```
    python3 pomodoro_timer.py
    ```
5. **Follow the Prompts**: Enter your preferred timings for work intervals, short breaks, long breaks, the number of cycles, and after how many cycles a long break is taken.
6. **Begin Your Pomodoro Session**: After configuration, the timer will start, and you'll be on your way to a more productive work session.

### Disclaimer

This script is a basic implementation of the Pomodoro technique and is intended for personal use or as a starting point for further customization. The sound playback feature relies on Pygame's mixer module. Ensure you have the legal right to use any sound file you choose to utilize with this script.

### License

This project is open-source and available under the MIT License. Feel free to fork, modify, and use it as you see fit. Contributions, suggestions, and feedback are welcome!

---

By using this Pomodoro Timer script, you acknowledge understanding that this tool is provided as-is without warranties or guarantees. Happy productivity

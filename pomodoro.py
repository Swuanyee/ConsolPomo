import time
import pygame

def play_sound():
    try:
        # Initialize the pygame mixer
        pygame.mixer.init()
        
        # Load the sound file
        sound = pygame.mixer.Sound('./tibetan_alert.wav')
        
        # Play the sound
        sound.play()
        
        # Wait for the sound to finish playing
        while pygame.mixer.get_busy(): 
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"An error occurred while trying to play sound: {e}")

def countdown(minutes):
    for i in range(minutes * 60, 0, -1):
        time.sleep(1)
        if i % 60 == 0:
            print(f'{i // 60} minutes left')

def pomodoro_timer(work_time, short_break, long_break, cycles, long_break_cycle):
    try:
        completed_cycles = 0

        while completed_cycles < cycles:
            cycles_left = cycles - completed_cycles
            print(f"Work for {work_time} minutes. Cycle #{completed_cycles + 1} [{cycles_left} cycles left]")
            countdown(work_time)

            play_sound()

            completed_cycles += 1

            # Determine if it's time for a short break or a long break
            if completed_cycles % long_break_cycle == 0:
                print(f"Long break! Relax for {long_break} minutes.")
                countdown(long_break)
            else:
                print(f"Short break! Relax for {short_break} minutes.")
                countdown(short_break)
            
            # Only play the sound if the session hasn't ended
            if completed_cycles != cycles:
                play_sound()

            print(f"Cycle #{completed_cycles} complete!")

    except KeyboardInterrupt:
        print("\nPomodoro cancelled.")

if __name__ == "__main__":
    try:
        work_time = int(input("Enter work time in minutes: "))
        short_break = int(input("Enter short break time in minutes: "))
        long_break = int(input("Enter long break time in minutes: "))
        cycles = int(input("Enter the number of cycles: "))
        long_break_cycle = int(input("Enter the number of cycles after which a long break is taken: "))

        pomodoro_timer(work_time, short_break, long_break, cycles, long_break_cycle)
    except ValueError:
        print("Please enter valid integer values.")


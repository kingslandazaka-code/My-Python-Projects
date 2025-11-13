# === Typing Speed Tester ===

import time

def typing_speed_test():
    text = "The quick brown fox jumps over the lazy dog"
    print("Type this sentence as fast as you can:")
    print(text)
    input("Press Enter when ready...")

    start_time = time.time()
    typed = input("Start typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(typed.split())
    speed = words / (time_taken / 60)

    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Typing speed: {speed:.2f} words per minute")

typing_speed_test()

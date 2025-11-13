# === Random Joke/Quote Generator ===

def generator():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "I told my computer I needed a break, and it said 'No problem, I'll go to sleep.'",
        "Why do programmers prefer dark mode? Because light attracts bugs."
    ]
    print("Random joke/quote:")
    import random
    print(random.choice(jokes))

generator()

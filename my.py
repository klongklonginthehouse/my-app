import sys
from time import sleep
import time

def apply_gradient(text):
   
    colors = [
        "\033[38;5;88m",    
        "\033[38;5;130m", 
        "\033[38;5;94m",  
        "\033[38;5;136m", 
        "\033[38;5;166m", 
        "\033[38;5;202m", 
        "\033[38;5;208m", 
        "\033[38;5;124m", 
        "\033[38;5;88m"   
    ]
    
    gradient_text = ''
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        gradient_text += color + char
    gradient_text += "\033[0m"  
    return gradient_text

def print_lyrics():
    lines = [
        ("it was in blink of an eye", 0.08),
        ("find a way how to say goodbye", 0.05),
        ("I got to take me away from all sadness", 0.09),
        ("Stitch all my wounds", 0.08),

        ("Confess all the sins", 0.05),
        ("And took all my insecure", 0.09),
        
        ("and when i got the love", 0.09),
        ("gotta have to always make sure", 0.009),
        ("that Im not just ", 0.09),
        ("somebodys pleasure", 0.009)
    ]

    delays = [0.3, 1, 0.3, 2, 
              0.2, 6.6, 
              1.2, 6.4, 1.2, 5]

    for i, (line, char_delay) in enumerate(lines):
        if "somebodys pleasure" in line:
            line = line.replace("somebodys pleasure", apply_gradient("somebodys pleasure"))
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
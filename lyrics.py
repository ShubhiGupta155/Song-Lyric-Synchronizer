import time
import threading
import pygame

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load(r"D:\User Data\Desktop\Miniproject\arz_kiya_hai.mp3")  
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
        ".....",
        "Kayar jo the",
        "Woh shayar bane",
       "Ab kya kya karein",
        "Ye ishq mein",
       "Na kehte the kuchh jo",
        "Lage khoj mein",
      "Kya lafz chune",
       "Naye aashiq ye",
        
    ]
    delays = [26.0, 1.8, 1.5, 1.7, 1.7, 1.1, 1.9, 3.2]

    print("Arz Kiya Hai Lyrics:\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

threading.Thread(target=play_song, daemon=True).start()
print_lyrics()

import time
import threading
import pygame
def play_song():
    pygame.mixer.init()

    song_path = r"D:\User Data\Desktop\Miniproject\Dooron_Dooron.mp3"
    
    try:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except pygame.error as e:
        print(f"\n[ERROR] Could not load or play music file. Check the path and file: {e}")
        print(f"Path used: {song_path}")
def type_lyric(line, char_delay=0.065):
    """Prints a line character by character with a delay."""
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print() 

def print_lyrics():
    """Contains the lyrics and the time delays for synchronization."""
    
    lyrics = [
        "....",
        "Dooron dooron main vekhaan tenu, soneyo",
        "Kahaan tu, kahaan main",
        "Dooron dooron main vekhaan tenu, soneyo",
        "Kahaan tu, kahaan main",
        "Ki main karaan, ke main aawaan nazar tenu",
        "Laayak tere, kiven honwaa tu das mainu",
        "Kol tere mainu aan de soni",
        "Karaan main kitne jatan O soni",
        "Dooron dooron main vekhaan tenu, soneyo",
        "Kahaan tu, kahaan main",
    ]
    
    delays = [35.5,5.0, 7.0, 5.5, 6.6, 1.0, 1.4, 2.2, 2.0, 5.5,4.8 ] 

    print("--- Dooron Dooron Lyrics ---\n")
    
    
    time.sleep(0.36) 

    for i, line in enumerate(lyrics):
        type_lyric(line)

        if i < len(delays):
            time.sleep(delays[i])

if __name__ == '__main__':
    print("Starting music in the background...")
    threading.Thread(target=play_song, daemon=True).start()
    print_lyrics()
    print("\n--- Synchronization sequence finished. ---")
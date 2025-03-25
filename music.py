from pygame import mixer

mixer.init()

songs = {
    "1": "TEST.mp3",
    "2": "Dancing in the flames.mp3",
    "3": "Cest La Vie.mp3"
}

print("Select a song to play:")
for key, song in songs.items():
    print(f"{key}: {song}")

choice = input("Enter the number of the song: ")

if choice in songs:
    mixer.music.load(songs[choice])
    mixer.music.set_volume(0.5)
    mixer.music.play()
else:
    print("Invalid choice. Exiting.")
    exit()

while True:
    print("\nPress 'p' to pause")
    print("Press 'r' to resume")
    print("Press 'v' to set volume")
    print("Press 'n' to play next song")
    print("Press 'e' to exit")

    ch = input("['p','r','v','n','e']>>> ")

    if ch == "p":
        mixer.music.pause()
    elif ch == "r":
        mixer.music.unpause()
    elif ch == "v":
        v = float(input("Enter volume (MAX 1): "))
        mixer.music.set_volume(v)
    elif ch == "n":
        next_choice = input("Enter the number of the next song: ")
        if next_choice in songs:
            mixer.music.load(songs[next_choice])
            mixer.music.play()
        else:
            print("Invalid choice.")
    elif ch == "e":
        mixer.music.stop()
        break

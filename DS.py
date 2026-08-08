class Playlist:
    def __init__(self, name, genre):
        # Initializes the playlist object with a name, genre, and empty tracklist
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) has been created!")

    def add_song(self, song):
        # Appends a new song to the tracklist
        self.songs.append(song)
        print(f"'{song}' added to the playlist.")

    def remove_song(self, song):
        # Safely removes a song if it exists in the tracklist
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed from the playlist.")
        else:
            print(f"'{song}' not found in the playlist.")

    def display(self):
        # Displays all tracks current stored in the playlist
        if not self.songs:
            print(f"The playlist '{self.name}' is currently empty.")
        else:
            print(f"\n--- {self.name} Playlist Tracks ---")
            for index, song in enumerate(self.songs, start=1):
                print(f"{index}. {song}")
            print("-" * 30)

    def __del__(self):
        # Destructor fires when the object is deleted or program ends
        print(f"Playlist '{self.name}' has been deleted. Goodbye!")


# Object Creation (Constructor fires here)
my_playlist = Playlist("Road Trip Mix", "Pop")

# Menu-driven interaction loop
while True:
    print("\n1. Add Song \n2. Remove Song \n3. View Playlist \n4. Delete & Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter song name: ")
        my_playlist.add_song(song)
        
    elif choice == "2":
        song = input("Enter song name to remove: ")
        my_playlist.remove_song(song)
        
    elif choice == "3":
        my_playlist.display()
        
    elif choice == "4":
        del my_playlist  # Explicitly fires the __del__ destructor
        break
        
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
while True:
    print("1. Add Song  2. Remove Song  3. View Playlist  4. Delete & Quit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        song = input("Enter song name: ")
        my_playlist.add_song(song)
        
    elif choice == "2":
        song = input("Enter song to remove: ")
        my_playlist.remove_song(song)
        
    elif choice == "3":
        my_playlist.display()
        
    elif choice == "4":
        del my_playlist  # Destructor fires here
        break
        
    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")

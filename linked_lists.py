class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_song = SongNode(title)
        new_song.next = self.head
        self.head = new_song  # Add to the beginning

    def remove_song(self, title):
        current = self.head
        prev = None
        while current:
            if current.title == title:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next  # Remove head
                return
            prev = current
            current = current.next

    def display_playlist(self):
        current = self.head
        while current:
            print(current.title)
            current = current.next

# Example usage
playlist = Playlist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")
playlist.display_playlist()  # Displays Song C, Song B, Song A
playlist.remove_song("Song B")
playlist.display_playlist()  # Displays Song C, Song A
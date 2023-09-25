class ImmutableArtwork:
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    def __str__(self):
        return f"'{self.title}' by {self.artist} (Immutable)"


starry_night = ImmutableArtwork("Starry Night", "Vincent van Gogh")
print("Artwork Information:")
print(starry_night)

starry_night.artist = "Unknown"

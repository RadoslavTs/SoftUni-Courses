from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                else:
                    return f"Album {album.name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        resulting_string = ""
        for album in self.albums:
            resulting_string += f"{album.details()}\n"
        return f"Band {self.name}\n{resulting_string}"


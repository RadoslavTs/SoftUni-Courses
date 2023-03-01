from project.song import Song


class Album:

    def __init__(self, name: str, *song_list):
        self.name = name
        self.songs = [x for x in song_list]
        self.published = False

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        else:
            for song in self.songs.copy():
                if song.name == song_name:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."

            return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        return_string = ''
        for song in self.songs:
            return_string += f"== {song.get_info()}\n"
        return f"Album {self.name}\n{return_string}"


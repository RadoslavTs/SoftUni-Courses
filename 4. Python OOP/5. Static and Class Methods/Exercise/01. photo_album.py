class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4
        return cls(pages)

    def add_photo(self, label: str):
        for iterate in range(self.pages):
            if len(self.photos[iterate]) < 4:
                self.photos[iterate].append(label)
                return f"{label} photo added successfully on page {iterate+1} slot {len(self.photos[iterate])}"
        return f"No more free slots"

    def display(self):
        start_end = '-' * 11
        photos = [x for x in self.photos]
        new_album = []
        for page in self.photos:
            new_page = ''
            for el in page:
                new_page += '[] '
            new_album.append(new_page)
        for i in range(len(new_album)):
            new_album[i] = new_album[i].strip()
        for i in range(len(new_album)):
            if i < len(new_album) - 1:
                new_album[i] = new_album[i] + '\n'
        mid_string = '-----------\n'.join(new_album)
        return f"{start_end}\n{mid_string}\n{start_end}"


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

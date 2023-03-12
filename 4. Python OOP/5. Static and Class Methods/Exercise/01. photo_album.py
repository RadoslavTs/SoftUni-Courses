from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for x in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
            
        return f"No more free slots"

    def display(self) -> str:
        result = ['-' * 11]
        start_end = '-' * 11
        photos = [x for x in self.photos]
        new_album = []

        for page in self.photos:
            result.append(('[] '* len(page)).rstrip())
            result.append('-' * 11)

        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

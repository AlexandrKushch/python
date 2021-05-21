import requests
import pandas as pd


class Book:
    title: str
    author_name: str
    first_publish_year: int
    publish_year: list
    has_fulltext: bool
    description: str

    def __init__(self, title, author_name, has_fulltext, first_publish_year=0, publish_year=None, description="Empty"):
        if publish_year is None:
            publish_year = [0]
        self.title = title
        self.author_name = author_name
        self.first_publish_year = first_publish_year
        self.publish_year = publish_year
        self.has_fulltext = has_fulltext
        self.description = description

    def __str__(self):
        return f"----------\n\tTitle: {self.title}\n\tAuthor: {self.author_name}" \
               f"\n\tFirst publish: {self.first_publish_year}" \
               f"\n\tRepublishes: {self.publish_year}\n\tHas Fulltext: {self.has_fulltext}" \
               f"\n\tDescription: {self.description}"


def api(author):
    offset = 0
    size = 1
    data_frame = pd.DataFrame(columns=['title', 'author_name', 'first_publish_year', 'has_fulltext'])

    while offset <= size:
        r_author = requests.get("http://openlibrary.org/search.json?author=" + author + "&offset=" + str(offset))
        offset += 100
        j_author = r_author.json()
        size = j_author['numFound']

        books = j_author['docs']

        for i in books:
            if 'first_publish_year' in i.keys():
                book = Book(title=i['title'], author_name=i['author_name'], first_publish_year=i['first_publish_year'],
                            publish_year=i['publish_year'], has_fulltext=i['has_fulltext'])
                item = {'title': book.title, 'author_name': book.author_name, 'first_publish_year': book.first_publish_year,
                        'has_fulltext': book.has_fulltext}
            else:
                book = Book(i['title'], i['author_name'], i['has_fulltext'])  # , j_book['description']['value']
                item = {'title': book.title, 'author_name': book.author_name,
                        'first_publish_year': book.first_publish_year, 'has_fulltext': book.has_fulltext}

            data_frame = data_frame.append(item, ignore_index=True)

            print(book)

    print(data_frame)
    data_frame.to_csv('api.csv')


if __name__ == '__main__':
    author = input()
    api(author)

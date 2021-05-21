from bs4 import BeautifulSoup
import requests
import pandas as pd


def bs():
    url = 'https://openlibrary.org/people/doditt52/lists/OL114827L/Books_to_Read.html'
    r = requests.get(url)
    data_frame = pd.DataFrame(columns=['Book', 'Author', 'LastUpdate'])

    with open('index.html', 'wb') as file:
        file.write(r.content)

    with open('index.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    list_results = soup.find("div", class_="mybooks-list").find_all("li")

    for i in list_results:
        author_book = i.find_all('a', class_='results')
        last_upd = i.find('span', class_='time')
        print("----------------")
        print("Book:", author_book[0].text)
        print("Author:", author_book[1].text)
        print(last_upd.text.strip())

        item = {'Book': author_book[0].text, 'Author': author_book[1].text, 'LastUpdate': last_upd.text.strip()}
        data_frame = data_frame.append(item, ignore_index=True)

    print(data_frame)
    data_frame.to_csv('bs.csv')


if __name__ == '__main__':
    bs()

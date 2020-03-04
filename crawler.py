import requests
from bs4 import BeautifulSoup


class Pull_Links:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        source = requests.get(self.url)
        plain_text = source.text
        self.soup = BeautifulSoup(plain_text, "lxml")

    def write_file(self):
        writefile = open("links.csv", "w")
        soup = self.soup

        for link in soup.findAll('a'):
            strlinks = str(self.url) + link.get("href")
            writefile.write(self.name + ", " + strlinks + '\n')
        writefile.close()

class Pull_Lists:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        source = requests.get(self.url)
        plain_text = source.text
        self.soup = BeautifulSoup(plain_text, "lxml")

    def write_file(self):
        writefile = open("headers.csv", "w")
        soup = self.soup

        for link in soup.findAll('li'):
            strlinks = str(self.url) + link.get("data-value")
            writefile.write(self.name + ", " + strlinks + '\n')

        writefile.close()

crawler = Pull_Links("Links",'https://www.budsgunshop.com/')
crawler2 = Pull_Lists("Lists",'https://www.budsgunshop.com/')

crawler.write_file()
crawler2.write_file()

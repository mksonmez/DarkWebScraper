
import mechanicalsoup

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
}
#url = 'https://check.torproject.org/'
#url = 'https://3g2upl4pq6kufc4m.onion/' #DuckDuckGo
url = 'http://bk4vffkf2fazxhs3pvgt4rggqx4puaej7hcrsalkuflulprkr2ruqnqd.onion/' #BlackMarketGuns

browser = mechanicalsoup.StatefulBrowser()
res = browser.open(url, proxies=proxies, verify=False)

#print(res.text)

print()
#title
titles = browser.get_current_page().find_all('title')
for title in titles:
	print()
	print(title)

print()
#links
links = browser.get_current_page().find_all('a')
for link in links:
	print(link['href'])

print()
#images
images = browser.get_current_page().find_all('img')
for img in images:

	print(img['src'])


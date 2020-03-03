
import mechanicalsoup

proxies = {
    'https': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050',
}
url = 'https://check.torproject.org/'
browser = mechanicalsoup.StatefulBrowser()
res = browser.open(url, proxies=proxies, verify=False)
print(res.text)


browser.get_current_page().find_all('legend')
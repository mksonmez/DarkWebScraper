#!/usr/bin/env python3
import mechanicalsoup

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m' # white


VERSION = 'first and last'

def banner():
    banner = r'''
                                 #####
      #       #    ##     #   # #     #   ####   #####     ##    #####   ######
      #       #   #  #     # #  #        #    #  #    #   #  #   #    #  #
      #       #  #    #     #    #####   #       #    #  #    #  #    #  #####
      #       #  ######     #         #  #       #####   ######  #####   #
 #    #  #    #  #    #     #   #     #  #    #  #   #   #    #  #       #
  ####    ####   #    #     #    #####    ####   #    #  #    #  #       ######

                                              '''
    print(G + banner + W)
    print(R + "Created By :- " + G + "Mehmet Sonmez" +W)
    print(R + "Version :- " + G + VERSION + W + '\n')


proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
}


#url = 'https://check.torproject.org/'
#url = 'https://3g2upl4pq6kufc4m.onion/'
url = 'http://2kka4f23pcxgqkpv.onion/'

browser = mechanicalsoup.StatefulBrowser()
res = browser.open(url, proxies=proxies, verify=False)

print(res.text)


#links
links = browser.get_current_page().find_all('a')

#images
images = browser.get_current_page().find_all('img')

for link in links:
	print(link['href'])

print()

for img in images:
	print(img['src'])

def service():
    """
    Ensures Tor service is running before proceeding
    """
    print('\n' + C + "[>] Checking for tor service..." + W + '\n')
    cmd = 'systemctl is-active tor.service'
    co = subp.Popen(cmd, shell=True,stdout=subp.PIPE).communicate()[0]
    if 'inactive' in str(co):
        print(R + '[!] Tor Service Not Running..' + W + '\n')
        print(R + '[>] Tor Service is Required for this Script...')
        exit()
    else:
        print(C + "[>] Tor Service is Running..."  + W + '\n')


def main():
    """
    Presents options for scraping from single URL or file type
    """
    choice = '0'
    while choice == '0':
        print(R + '[+] ' + G +  'Choose the File Format:-' + W)
        print(R + '[1] ' + W +  'Scrape From File'  + W)
        print(R + '[2] ' + W +  'Scrape From Single URL'  + W + '\n')
        choice = input(G + '[+]' + C + " Enter Option No. ->  " + W)

        if choice == "1":
            choose_file()
        elif choice == "2":
            parse_url()
        else:
            print('\n' + R + "[!] I don't understand your choice." + W + '\n')
            return main()


try:
    banner()
    service()
    main()
    
except KeyboardInterrupt:
    print('\n' + R + '[!]' + R + ' Keyboard Interrupt.' + W)
    exit()

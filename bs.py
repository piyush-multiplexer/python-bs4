import bs4 as bs
import urllib2
sauce = urllib2.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
print soup.find('p')

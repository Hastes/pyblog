import urllib2
from bs4 import BeautifulSoup
import datetime

def GetHtmlHabr(url):
    page = urllib.request.urlopen(url)
    html = BeautifulSoup(page.read(),"html.parser")
    return html

def GetTitleHabr():
    html = GetHtmlHabr('https://habrahabr.ru/all/')
    content = html.find("div","post__header")
    title = content.find("a","post__title_link").string
    return title

def GetContentHabr():
    html = GetHtmlHabr('https://habrahabr.ru/all/')
    content = html.find("div","post__header")
    url = content("a","post__title_link")[0]["href"]
    page = urllib.request.urlopen(url)
    html = BeautifulSoup(page.read(),"html.parser")
    content = html.find("div","content html_format")
    img = content.next
    content = ''.join(map(str, content.contents))
    return content
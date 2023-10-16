#Google books Python API
import urllib.request
import json


class GoogleBook:
    __author=[]
    __description=""
    __isbn=""
    __pageCount=""
    __publisher=""
    __thumbnailLink=""
    __title=""
    def __init__(self, json_def, var):
        self.__dict__ = json.loads(json_def)
    
    def __init__(self, isbn):
        self.__isbn = isbn
        self.__author, self.__description, self.__pageCount, self.__publisher, self.__thumbnailLink, self.__title = getInfo(self.__isbn)
    
    def getAuthor(self):
        return self.__author
    def getDescription(self):
        return self.__description
    def getISBN(self):
        return self.__isbn
    def getPageCount(self):
        return self.__pageCount
    def getPublisher(self):
        return self.__publisher
    def getThumbnailLink(self):
        return self.__thumbnailLink
    def getTitle(self):
        return self.__title
    
def getJSON(isbn):
    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    with urllib.request.urlopen(base_api_link + isbn) as f:
        text = f.read()
    decoded_text = text.decode("utf-8")
    return json.loads(decoded_text) # deserializes decoded_text to a Python object

def getInfo(isbn):
    jsonObj = getJSON(isbn)
    info = jsonObj["items"][0]["volumeInfo"]
    author=info["authors"]
    description=info["description"]
    pageCount=info["pageCount"]
    publisher=info["publisher"]
    thumbnailLink=info["imageLinks"]["thumbnail"]
    title=info["title"]
    
    return author, description, pageCount, publisher, thumbnailLink, title

def test():
    b = GoogleBook("9781668016138")
    print(b.getAuthor())
    print(b.getDescription())
    print(b.getISBN())
    print(b.getPageCount())
    print(b.getPublisher())
    print(b.getThumbnailLink())
    print(b.getTitle())
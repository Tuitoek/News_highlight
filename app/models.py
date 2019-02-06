class Sources:
    '''
    Sources class to define Movie Objects
    '''

    def __init__(self,name,description,url,category):
        self.name =name
        self.description = description
        self.url = url
        self.category = category

class Articles:
    '''
    Articles class to define Movie Objects
    '''

    def __init__(self,source,author,title,description,url,urlToImage,publishedAt):
        self.source =source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

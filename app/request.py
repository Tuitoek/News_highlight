from app import app
import urllib.request,json
from .models import sources,articles

Sources= sources.Sources
Articles=articles.Articles

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the sources base url
sources_url = app.config['SOURCE_API_BASE_URL']
articles_url=app.config['ARTICLES_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)


    return sources_results
def process_results(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of sources objects
    '''
    sources_results = []
    for sources_item in sources_list:
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')

        if category:
            sources_object = Sources(name,description,url,category)
            sources_results.append(sources_object)

    return sources_results

def get_articles():
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)


    return articles_results

def process_articles(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        source =articles_item.get('source')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description =articles_item.get(' description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        if urlToImage:
            articles_object = Articles(source,author,title,description,url,urlToImage,publishedAt)
            articles_results.append(articles_object)

    return articles_results

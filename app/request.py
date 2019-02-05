from app import app
import urllib.request,json
from .models import sources

Sources= sources.Sources

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the sources base url
sources_url = app.config['SOURCES_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
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
            sources_object = Sources(name,description,url,cacategory)
            sources_results.append(sources_object)

    return sources_results

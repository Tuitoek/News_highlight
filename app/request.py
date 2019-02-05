from app import app
import urllib.request,json
from .models import sources

Sources= sources.Sources

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the sources base url
sources_url = app.config['SOURCES_API_BASE_URL']

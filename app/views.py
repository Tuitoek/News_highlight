from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def source():

    '''
    View root page function that returns the source page and its data
    '''
    #Getting general news
    general_news = get_sources('general')
    print(general_news)
    #getting technology news
    technology_news = get_sources('technology')
    #getting sport_news
    sport_news = get_sources('sports')
    #getting business news
    business_news = get_sources('business')
    #getting science news
    science_news = get_sources('science')

    title = 'Home -Let us get to the briefs'
    return render_template('source.html', title = title,general=general_news,technology=technology_news,sports=sport_news,business=business_news,science=science_news)

@app.route('/')
def source():
    '''
    Returns the article page and its data
    '''
    return render_template('article.html')

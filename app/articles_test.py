import unittest
from models import articles
Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Tests the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles=Articles("Bbc.com","https://www.facebook.com/bbcnews","Paris fire: Nine dead and many injured at apartment block - BBC News","Firefighters warn the death toll from the fire could rise as investigators suspect arson.","https://www.bbc.com/news/world-europe-47126440","https://ichef.bbci.co.uk/images/ic/1024x576/p06zzrvw.jpg","2019-02-05T10:18:45Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))


if __name__ == '__main__':
    unittest.main()

class Article:

    def __init__(self, title, link, img):
        self.title = title
        self.link = link
        self.img = img

class Process:
    """
    Class for data processing
    """

    def clean_news(news_json):
        """
        Cleans the news json pulled from news API

        Args:
            news_json (dict): News data from api

        Returns:
            list: list of articles -- each list element is a dictionary
        """
        articles = news_json['articles']
        article_objects = []
        for a in articles:
            title = a['title']
            url = a['link']
            img = a['media']
            print(img)
            a_obj = Article(title, url, img)
            article_objects.append(a_obj)
        return article_objects

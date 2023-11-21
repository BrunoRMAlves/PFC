#Modelo feito para o site F1000 no GoogleChrome

import requests
from bs4 import BeautifulSoup

userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
class WebScrapperF1000:
    def __init__(self, url, userAgent):
        self.url = url
        self.req = self.create_request(userAgent)
        self.site = BeautifulSoup(self.req.text, "html.parser")
        self.articles_divs = self.get_articles_divs()
        #self.article_request
        #self.article_content

    def create_request(self, userAgent):
        headers = {"User-Agents": userAgent}
        return requests.get(self.url, headers=headers)

    def get_articles_divs(self):
        div_eight_columns = self.site.find_all(self.site.find_all("div", class_="eightcolumns"))
        articles_divs = []
        for div in div_eight_columns:
            if(str(div).count("article-browse-wrapper f1r-searchable") >0 and str(div).count("data-index") >0  and str(div).count("data-article-doi") >0):
                articles_divs.append(div)
        return articles_divs

    def get_articles_names(self):
        articles_names = []
        for article in str(self.articles_divs):
            if(article.count("data-index=")>0):
                p1=article.split(article.find("data-index="))
                #p2=article.split(article.find('"'))
                articles_names.append(p1)
        print(articles_names)

    #def get_article_url(self):

    #def request_to_article_url(self):

    #def get_version_url(self):

    #def set_article_version(self):
        # article = request_to_article_url()

    #def get_article_content(self):

    #def get_article_first_review(self):

    #def save_article(self, article_name, article_content):
    #    with open(article_name, 'w') as f:
    #        f.write(article_content)
    
    #def save_review(self, review_name, review_content):
    #    with opent(review_name, 'w') as f:
    #       f.write(review_content)


teste = WebScrapperF1000("https://f1000research.com/browse/articles", userAgent)
teste.get_articles_names()
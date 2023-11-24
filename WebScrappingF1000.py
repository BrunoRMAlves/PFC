#Modelo feito para o site F1000 no GoogleChrome

import requests
from bs4 import BeautifulSoup

userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
class WebScrapperF1000:
    def __init__(self, url, userAgent):
        self.url = url
        self.req = self.create_request(userAgent)
        print("Construiu a request")
        self.site = BeautifulSoup(self.req.text, "html.parser")
        print("Fez a request")
        self.articles_divs = self.get_articles_divs()
        print("Pegou todas as divs")
        self.articles_status = self.get_articles_review_status()
        print("Pegou todos os status dos artigos")
        self.drop_unreviewed_articles()
        print("Dropou os artigos não revisados")
        self.articles_names = self.get_articles_names()
        print("Pegou todos os nomes")
        self.articles_links = self.get_articles_url()
        print("Pegou todos os links")

    def create_request(self, userAgent):
        headers = {"User-Agents": userAgent}
        return requests.get(self.url, headers=headers)

    def get_articles_divs(self):
        return self.site.find_all(self.custom_selector)
        
    def custom_selector(self, tag):
	    return tag.name == "div" and tag.has_attr("class") and tag.has_attr("data-index") and tag.has_attr("data-article-id") and tag.has_attr("data-article-doi")

    def get_articles_names(self):
        names = []
        for article in self.articles_divs:
            str_article = str(article)
            splitted = str_article.split('"')
            names.append(splitted[7])
        return names        

    def get_articles_url(self):
        urls = []
        for article in self.articles_divs:
            str_article = str(article)
            splitted = str_article.split('"')
            urls.append(splitted[12][1:48])
        return urls

    def get_articles_review_status(self):
        status = []
        for article in self.articles_divs:
            str_article = str(article)
            if(str_article.count("peer-review-status") == 1):
                status.append("AWAITING PEER REVIEW")
            else:
                status.append("CONTAINS PEER REVIEW")
        return status
        
    def drop_unreviewed_articles(self):
        indexes = []
        for i in range(len(self.articles_status)):
            if(self.articles_status[i] == "AWAITING PEER REVIEW"):
                indexes.append(i)
        for index in indexes[::-1]:
            self.articles_status.pop(index)
            self.articles_divs.pop(index)
        

    #def request_to_article_url(self):

    #def get_version_url(self):

    #def set_article_version(self):
        # article = request_to_article_url()

    #def get_article_content(self):

    #def get_article_first_review(self):

    def save_article(self, article_name, article_content):
        with open(article_name, 'w') as f:
            f.write(str(article_content))
    
    #def save_review(self, review_name, review_content):
    #    with open(review_name, 'w') as f:
    #       f.write(review_content)

print("Iniciou o programa")
teste = WebScrapperF1000("https://f1000research.com/browse/articles", userAgent)
teste.get_articles_url()
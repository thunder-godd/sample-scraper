from bs4 import BeautifulSoup
import requests

"""
open page
parse html
find : article>class=post
            a=link
open link 
    parse html 
    find: div>class=elementor-text-editor
           p            

"""


def scrape_page(page_url):
    """Extracts HTML from a webpage"""
    
    response = requests.get(page_url)
    print(f'data from:{page_url} ')
    content = response.content
    soup = BeautifulSoup(content, features='html.parser')
    soup.encode('utf-8')
    return soup

main_url='https://englishspeakingcourse.net/'   
article_urls=[]
output=[]

#print(scrape_page(main_url))
def find_articles(page_url):
    page=scrape_page(page_url)
    articles=page.find_all('article',{"class":"post"})
    #print(articles)
    for article in articles:
        a= article.find('a')
        url=a.get('href') 
        article_urls.append(url)
        


def find_words(url):
    page=scrape_page(url)
    content=page.find('div',{'class':'elementor-text-editor'})
    p=content.find_all('p')
    for t in p:
        output.append(t.get_text())

find_articles(main_url)

with open(r"output.txt",'w',encoding='utf-8') as f:
    find_articles(main_url)
    for url in article_urls:
        find_words(url)
    for i in output:
        my_list= i  + '\n\n' 
        print(my_list)
        f.write(my_list)
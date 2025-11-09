from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

articles = soup.find_all(name="a", class_="storylink")

article_texts=[]
articles_links=[]

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_num = max(article_upvotes)
print(largest_num)
largest_index = article_upvotes.index(largest_num)
print(article_texts[largest_index])
print(articles_links[largest_index])

# print(article_texts)
# print(articles_links)
# print(article_upvotes)
from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title) #print the entire line of title with tags..
# print(soup.title.name) #name of tag
# print(soup.title.string) #inside the tag - content

# print(soup) #print html
# print(soup.prettify()) #print with indents
# print(soup.a) #prints first anchor tag

all_anchor = soup.find_all(name="a")

# for tag in all_anchor:
    # print(tag.getText())
    # print(tag.get("href"))

all_paras = soup.find_all(name="p")
# print(all_paras)

heading = soup.find(name="h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

name = soup.select_one(selector="#name")
print(name)
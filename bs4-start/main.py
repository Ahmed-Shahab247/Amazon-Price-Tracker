from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

news = soup.find_all(name="span",class_="titleline")
scores = soup.find_all(name="td",class_="subtext")

list_of_scores = []

def getMax(a_list):
    return max(a_list)

for score in scores:
    try:
        attribute_score = score.find(name="span", class_="score").getText()
        value = attribute_score.split(" ")[0]
        # print(int(value))
    except AttributeError:
        pass
    else:
        list_of_scores.append(int(value))

max_value = getMax(list_of_scores)
index_of_list = list_of_scores.index(max_value)
print(max_value)

link_list=[]
title_list = []

for heading in news:
        link = heading.find(name="a").get("href")
        title = heading.find(name="a").getText()
        link_list.append(link)
        title_list.append(title)

print(link_list[index_of_list])
print(title_list[index_of_list])


# scores = soup.find_all(class_="score")
# for score in scores:
#     print(score.getText().split(" ")[0])



#
# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content,"html.parser")
# print(soup.find(name="h3",class_="heading").text)
#
# print(soup.select_one(selector="#name").text)
#
# print(soup.select(selector=".heading")[0])
#
# print(soup.select("p a"))

#
# for i in soup.find_all(name="p"):
#     pass
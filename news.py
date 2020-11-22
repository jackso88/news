from pygooglenews import GoogleNews
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

gn = GoogleNews(lang='en', country='US')
search = gn.search('Belarus', when='1m')
data = search['entries']

lst1, lst2 = [], []

for el in data:
    for key, val in el.items():
        if key == 'title':
            lst2.append(val)

for el in lst2:
    text = el.split(' - ')
    lst1.append(text[0])

lst2.clear()

for el in lst1:
    text = el.split()
    lst2.append(text)

lst1.clear()

for el in lst2:
    for i in el:
        if len(i) > 3:
            lst1.append(i.upper())

text = ''

cnt = Counter(lst1)
for i in cnt.keys():
    text += i + ' '

wordcloud = WordCloud(background_color="white", max_words=50)
worldcloud = wordcloud.generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

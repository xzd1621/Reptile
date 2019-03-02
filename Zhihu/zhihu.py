import requests
from pyquery import PyQuery as pq

url='https://www.zhihu.com/explore'
headers={
            'User-Agent':
                'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick)',
    }
html=requests.get(url,headers=headers).text
doc=pq(html)
items=doc('.explore-tab .feed-item').items()
for item in items:
    question=item('.question_link').text()
    author=item('.author-link').text()
    answer=pq(item.find('.content').html()).text()
    print(question,author,answer)
    with open('explore.txt','a+') as f:
        f.write('\n'.join([question,author,answer]))
        f.write('\n'+'='*20+'\n')
        
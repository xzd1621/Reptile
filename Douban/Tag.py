from pyquery import PyQuery as pq
class Tag:
    def tags(self,url):
        doc=pq(url=url)
        tags=doc('td a').text()
        return tags.split(' ')
if __name__ == '__main__':
    t=Tag()
    for i in t.tags('https://book.douban.com/tag/?view=type&icn=index-sorttags-all').split(' '):
        print(i)
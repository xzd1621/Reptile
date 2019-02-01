import json
import re
import time

import requests
from bs4 import BeautifulSoup
from lxml import etree
from pyquery import PyQuery as pq
from urllib.parse import quote
import Tag
class douban:
    base_url='https://book.douban.com'
    headers={
            'User-Agent':
                'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick)',
    }
    def parse(self,url):
        print(url+'  *')
        request=requests.get(url,headers=douban.headers)
        html=request.text
        html=etree.HTML(html)
        detail_urls=html.xpath('//div[@class="pic"]//a/@href')
        if len(html.xpath('//span[@class="next"]/a/@href'))>0:
            next_base_url = html.xpath('//span[@class="next"]/a/@href')[0]
            next_url = douban.base_url + next_base_url[:5] + quote(next_base_url[5:7]) + next_base_url[7:]
            self.parse(next_url)
        if len(detail_urls)>0:
            for detail_url in detail_urls:
                print(detail_url)
                items=self.parse_detail(detail_url)
                for item in items:
                    self.save2mysql(item)
        else:
            return
    def parse_detail(self,detail_url):
        time.sleep(1)
        doc=pq(url=detail_url)
        html=requests.get(detail_url,headers=douban.headers).text
        soup=BeautifulSoup(html,'lxml')
        temp=soup.select('#mainpic .nbg ')
        writers=doc('#info a').text()#作者
        if len(temp)>0:
            title=temp[0]['title']#书名
            img_url=temp[0]['href']#书图片链接
        else:
            title=''
            img_url=''
        print(title)
        details=doc('#info ')
        #爬取出版社、出版年、页数、定价、ISBN等信息
        result_press=re.search(r'出版社:</span>(.*?)<br/>',str(details))
        if result_press:
            press = result_press.group(1)
            print(press)
        else:
            press=''
        result_date=re.search(r'出版年:</span>(.*?)<br/>',str(details))
        if result_date:
            date=result_date.group(1)
            print(date)
        else:
            date=''
        result_page_numbers=re.search(r'页数:</span>(.*?)<br/>',str(details))
        if result_page_numbers:
            page_numbers=result_page_numbers.group(1)
            print(page_numbers)
        else:
            page_numbers=''
        result_price=re.search(r'定价:</span>(.*?)<br/>',str(details))
        if result_price:
            price=result_price.group(1)
            print(price)
        else:
            price=''
        result_isbn=re.search(r'ISBN:</span>(.*?)<br/>',str(details))
        if result_isbn:
            ISBN=result_isbn.group(1)
            print(ISBN)
        else:
            ISBN=''
        evaluate_stars=doc('strong').text()
        evaluate_persons=doc('.rating_people span').text()
        intro=doc('.intro p').text()
        print(evaluate_stars,evaluate_persons)
        print(intro)
        # pattern=re.compile(r'</span>(.*?)<br/>')
        # results=re.findall(pattern,str(details))
        # press=results[0]#出版社
        # date=results[1]#日期
        # page_numbers=results[2]#页数
        # price=results[3]#价格
        # bind=results[4]#装帧
        # isbn=results[5]
        yield {
            'title':title,
            'url':detail_url,
            'img_url':img_url,
            'writers':writers,
            'press':press,
            'date':date,
            'page_numbers':page_numbers,
            'price':price,
            'ISBN':ISBN,
            'evaluate_stars':evaluate_stars,
            'evaluate_persons':evaluate_persons,
            'intro':intro,
        }
    def save2mysql(self,item):
        with open('result.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(item,ensure_ascii=False)+'\n')


if __name__ == '__main__':
    d=douban()
    t=Tag.Tag()
    tags=t.tags('https://book.douban.com/tag/?view=type&icn=index-sorttags-all')[1:]
    for tag in tags:
        url=r'https://book.douban.com/tag/'+quote(tag)+'?start=0&type=T'
        d.parse(url)
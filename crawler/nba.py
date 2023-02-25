import requests
from lxml import etree
# etree 是解析xpath的模块


# url
url = 'https://nba.hupu.com/stats/players'
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

# request
resp = requests.get(url,headers=headers)
# process
e = etree.HTML(resp.text)
# analyze
# 获取xpath，使用xpath helper
nos = e.xpath('//table[@class="players_table"]//tr/td[1]/text()')
names = e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams = e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
scores = e.xpath('//table[@class="players_table"]//tr/td[4]/text()')

del nos[0]
del scores[0]
# if save
with open('nba','w',encoding='utf-8') as f:
    for no,name,team,score in zip(nos,names,teams,scores):
        f.write(f'排名：{no} 姓名：{name} 球队：{team} 得分：{score}\n')




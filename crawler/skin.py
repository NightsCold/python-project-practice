import requests
from lxml import etree
import os
#request
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

# hero list
hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
hero_list_resp = requests.get(hero_list_url,headers=headers)
# get heroes' number and other information from herolist.json
for h in hero_list_resp.json():
    h_num = h['ename']
    h_name = h['cname']
    # judge if the file exit
    if not os.path.exists(h_name):
        os.makedirs(h_name)
    # split the name_list
    skin_names = [name for name in h['skin_name'].split('|')]
    hero_info_url = f'https://pvp.qq.com/web201605/herodetail/{h_num}.shtml'
    hero_info_resp = requests.get(hero_info_url,headers=headers)
    for i,n in enumerate(skin_names):
        resp = requests.get(f'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{h_num}/{h_num}-bigskin-{i+1}.jpg',headers=headers)
        # save the picture
        with open(f'{h_name}/{n}.jpg','wb') as f:
            f.write(resp.content)

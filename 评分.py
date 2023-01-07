Date: 2023-01-05 18:09:14
LastEditors: Atlantis
LastEditTime: 2023-01-07 09:12:11
FilePath: \AllFileAboutPythonProject\学习尝试\ordinary_practice\b站评分.py
'''
import requests
import json
import numpy as np
import time
media_id = 28223558  #点开番剧长短评的网页，此时media_id为md后的数字，例如后面的链接media_id为4315402：https://www.bilibili.com/bangumi/media/md4315402/?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2
url = f"https://api.bilibili.com/pgc/review/long/list?media_id={media_id}&ps=20&sort=0"

payload={}
headers = {
  'authority': 'api.bilibili.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'cookie': '_uuid=4F102ABF6-BCC2-F137-BCDC-2314497C91A625865infoc; b_nut=1644196726; buvid4=505D657A-D453-4926-27D3-47AFBC033DF225063-022020709-1S1k6qTgO4YDNMkelC7nXQ%3D%3D; buvid3=7C16E168-14C4-9A5D-05A6-DEB4BD923D8525063infoc; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_BLACKGAP=0; b_ut=5; i-wanna-go-back=2; LIVE_BUVID=AUTO9316493163674280; hit-dyn-v2=1; blackside_state=0; OUTFOX_SEARCH_USER_ID_NCOO=1633448009.936181; fingerprint3=fd9229b11bb7d93cc35f64aab2d92b14; rpdid=|(u~kmRYl|mu0J\'uYY)lmYR~); hit-new-style-dyn=0; DedeUserID=17422365; DedeUserID__ckMd5=2e442880ded63021; dy_spec_agreed=1; SESSDATA=abe90e70%2C1685543172%2C36f20%2Ac2; bili_jct=6ced04b4bc3f74ed788a803f5d907dbb; CURRENT_QUALITY=0; sid=7i8n61o9; fingerprint=15df48ab3a6e90ce5069da899a49c643; buvid_fp=15df48ab3a6e90ce5069da899a49c643; share_source_origin=COPY; bsource=search_bing; CURRENT_FNVAL=16; b_lsid=2FE54B1D_1858151916C; bp_video_offset_17422365=747636347671412700; PVID=2',
  'origin': 'https://www.bilibili.com',
  'referer': 'https://www.bilibili.com/',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

long_score = 0
long_total_score = 0
long_id = 1 #从第一条评论开始
print('长评论=================================================')
while(True):
    # time.sleep(np.random.random()) 
    if(long_score != 0):
        temp_url = url + f'&cursor={next}'
    else:
        temp_url = url
    response = requests.request("GET", temp_url, headers=headers, data=payload)
    resp = response.json()
    for iter in resp['data']['list']:
        if(iter['score']<10):
            print(f"第{long_id}条长评论评分：{iter['score']}    标题：{iter['title']}")
        else:
            print(f"第{long_id}条长评论评分：{iter['score']}   标题：{iter['title']}")
        long_id = long_id+1
        long_score = long_score + iter['score']
        long_total_score = long_total_score + 10
    next = resp['data']['next']
    if((not resp['data']['next']) or  resp['data']['next'] == 0):
        break




url = f"https://api.bilibili.com/pgc/review/short/list?media_id={media_id}&ps=20&sort=0"
short_score = 0
short_total_score = 0
short_id = 1 #从第一条评论开始
print('短评论=================================================')
while(True):
    # time.sleep(np.random.random())
    if(long_score != 0):
        temp_url = url + f'&cursor={next}'
    else:
        temp_url = url
    response = requests.request("GET", temp_url, headers=headers, data=payload)
    resp = response.json()
    for iter in resp['data']['list']:
        if(iter['score']<10):
            print(f"第{short_id}条短评论评分：{iter['score']}    内容：{iter['content']}")
        else:
            print(f"第{short_id}条短评论评分：{iter['score']}   内容：{iter['content']}")
        short_id = short_id+1
        short_score = short_score + iter['score']
        short_total_score = short_total_score + 10
    next = resp['data']['next']
    if((not resp['data']['next']) or  resp['data']['next'] == 0):
        break

print(f'长评论评分：{long_score*10/long_total_score}')
print(f'短评论评分：{short_score*10/short_total_score}')
print(f'总评论评分：{(short_score + long_score) /(short_total_score+long_total_score)}')

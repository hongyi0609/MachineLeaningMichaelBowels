# 去哪儿热门景点excel文件保存路径
import os
import random

import pandas as pd
import requests
import time

"""
获取详细教程、获取代码帮助、提出意见建议
关注微信公众号「裸睡的猪」与猪哥联系
@Author  :   猪哥
"""

# 去哪儿热门景点excel文件保存路径
PLACE_EXCEL_PATH = '../edition_sample/NationalDayTravel/qunar_place.xlsx'


def spider_place(keyword, page):
    """
    爬取景点
    :param keyword: 搜索关键字
    :param page: 分页参数
    :return:
    """
    url = f'http://piao.qunar.com/ticket/list.json?keyword={keyword}&region=&from=mpl_search_suggest&page={page}'
    headers = {
        # 'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'Connection': 'keep-alive',
        # 'Host': 'piao.qunar.com',
        # 'Referer': 'http://piao.qunar.com/ticket/list.htm?keyword=%E5%9B%BD%E5%BA%86%E6%97%85%E6%B8%B8%E6%99%AF%E7%82%B9&region=&from=mpl_search_suggest',
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest'

        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9, en;q = 0.8',
        'Cache-Control': 'max-age = 0',
        'Connection': 'keep - alive',
        'Cookie': 'QN1 = 000014802eb41a41e438fe4b;QN300 = organic;_i = RBTKSLgC8tExmy6x6oQ_wxhBqZix;QN269 = 9DF13A54E35811E9AD86FA163E29CDD5;QN57 = 15698305360030.1948380886333314;fid = 6cd00ebd - 9d1b - 4f24 - bae9 - 32e38f050de6;csrfToken = twknQDopeSqSmyTqw9oWtASUwo7rxXJB;JSESSIONID = 17E996574DAC1D6250C71078E28E7F22;QN58 = 1571887859354 % 7C1571887859354 % 7C1;_vi = MJBvjAa53MHETW57G_goUAm_GQSaoi - GBUneWO30QGcu4yEn5ZAm6bNC50W1loLtNtRh4tkTX8cF9TXHyRdj7D347E_7hLBm1L1xteyFPHtXP8QdGL7mhoIPjRrxTjQK5xJC13Ui8OY05_wUtrP_v45onPaubNvLYfxiu1wy70GW;QN271 = 6f9f5622 - ea0e - 4543 - 9b12 - 99758fea69eb;QN267 = 1607978286d15e2317',
        'Host': 'piao.qunar.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 77.0.3865.90MobileSafari / 537.36'
    }
    # 代理需要的自取，猪哥没有用代理
    # 站大爷：http://ip.zdaye.com/dayProxy.html
    proxies = {'http': '118.24.172.149:1080',
               'https': '60.205.202.3:3128'}
    response = requests.get(url, headers=headers)
    # 提取景点信息
    place_list = get_place_info(response.json())
    print(place_list)
    # 保存景点信息
    save_excel(place_list)


def get_place_info(response_json):
    """
    解析json，获取想要字段
    :param response_json:
    :return:
    """
    sight_list = response_json['data']['sightList']
    place_list = []
    for sight in sight_list:
        goods = {'id': sight['sightId'],  # 景点id
                 'name': sight['sightName'],  # 景点名称
                 'star': sight.get('star', '无'),  # 景点星级，使用get方法防止触发KeyError
                 'score': sight.get('score', 0),  # 评分
                 'price': sight.get('qunarPrice', 0),  # 门票价格
                 'sale': sight.get('saleCount', 0),  # 销量
                 'districts': sight['districts'],  # 省 市 县
                 'point': sight['point'],  # 坐标
                 'intro': sight.get('intro', ''),  # 简介
                 }
        place_list.append(goods)
    return place_list


def save_excel(place_list):
    """
    将json数据生成excel文件
    :param place_list: 景点数据
    :return:
    """
    # pandas没有对excel没有追加模式，只能先读后写
    if os.path.exists(PLACE_EXCEL_PATH):
        df = pd.read_excel(PLACE_EXCEL_PATH)
        df = df.append(place_list)
    else:
        df = pd.DataFrame(place_list)
    writer = pd.ExcelWriter(PLACE_EXCEL_PATH)
    # columns参数用于指定生成的excel中列的顺序
    df.to_excel(excel_writer=writer,
                columns=['id', 'name', 'star', 'score', 'price', 'sale', 'districts', 'point', 'intro'],
                index=False,
                encoding='utf-8', sheet_name='去哪儿热门景点')
    writer.save()
    writer.close()


def patch_spider_place(keyword):
    """
    批量爬取淘去哪儿景点
    :param keyword: 搜索关键字
    :return:
    """
    # 写入数据前先清空之前的数据
    if os.path.exists(PLACE_EXCEL_PATH):
        os.remove(PLACE_EXCEL_PATH)
    # 批量爬取
    for i in range(1, 5):
        print(f'正在爬取 {keyword} 第{i}页')
        spider_place(keyword, i)
        # 设置一个时间间隔
        time.sleep(random.randint(2, 5))
    print('爬取完成！')


if __name__ == '__main__':
    patch_spider_place('国庆旅游景点')

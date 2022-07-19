import requests
def rget(url,language='zh',con=0):
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; CIBA; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; InfoPath.2; .NET4.0E)',
        'Accept-Language': language,
        'Referer': url
    }
    if con!=0:
        url2=url+'?'
        for k,v in con.items():
            url2+=k+'='+v+'&'
    else:
        url2=url
    a = requests.get(url2, headers=headers)
    return a
#class baidu:

#with open('record1.txt','w',encoding='utf-8')as file:
#    file.write(get('https://www.baidu.com/s?wd=%E5%85%B3%E9%94%AE%E5%AD%97&cl=3&pn=0').text)
import requests  # 发送请求
from bs4 import BeautifulSoup  # 解析页面
import pandas as pd  # 存入csv数据
import os  # 判断文件存在
from time import sleep  # 等待间隔
import random  # 随机
import re  # 用正则表达式提取url
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'Connection': 'keep-alive',
	'Accept-Encoding': 'gzip, deflate, br',
	'Host': 'www.baidu.com',
	'Cookie': '__yjs_duid=1_c82fa90a56be05ba3cbcc1bd00822fb51632313577224; BIDUPSID=1D4A85C39422C526F9068AE0ED9C9EAA; PSTM=1632314543; MAWEBCUID=web_jHImQOFgFjnSRVCkJrZZhmLbmMyIpJLkBNIUTJUvtFabsQFbOI; BD_UPN=12314753; H_WISE_SIDS=110085_114551_127969_176399_179348_184716_189755_190616_194085_196427_197241_197711_199022_199570_201193_203310_203525_203880_203882_203885_204123_204713_204715_204717_204720_204860_204908_205217_205420_205424_206930_207237_207512_207716_207830_208721_209063_209161_209345_209395_209435_209506_209512_209568_209815_209844_210127_210356_210564_210642_210669_210710_210733_210737_210792_210837_210852_210890_210893_210894_210906_210915_211059_211114_211180_211207_211301_211442_211456_211736_211755_211783_211913_212078_212229_212518_212532_212617_212774_212782_212994_213004_213044_213139_213221_213258_213275_213319_213351_8000052_8000134_8000139_8000150_8000161_8000163_8000167_8000178_8000180; BAIDUID=CD4E54103D095B3461789476C25BC427:FG=1; sugstore=1; H_PS_PSSID=36463_36455_31660_36453_36443_36167_35979_36055_36344_26350_36301_36469_36312_36447; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_MWMwNmJlMGVkYmY3MzAwODA5NjM0YTUxYTkyY2Q3NjcyNDE1ZWI4NTQyZTc2OTNmZWVkNmY5NjZlNGUzZGZhNWIzOTkyMTk2YjZjNTEwNGJkZjVjZWQwMGQ3ZTY4ZWFiNjk0ZDVkZjcxMmU0OWJiYTMzNzU2NTJjOWMyYjAzOWU1MTlhOGRiYzgxMWIzYTA5NjAxNTEwYTUwOTdjMTg4ZQ==; H_PS_645EC=5bf3Zg6sFIcKYYqPqfPd1DMNqaRtbRdyP2kHq5ZCGh%2FCoZvMPoQZdZ%2BW8yY; BA_HECTOR=a48k840la52421a0051h8kg4915; BAIDUID_BFESS=CD4E54103D095B3461789476C25BC427:FG=1; delPer=0; BD_CK_SAM=1; PSINO=6; ZFY=AukxUMrEgjGcRApHKjZbURPuomU:A5TE1xrimd:Bwq2mE:C; BDSVRTM=0; COOKIE_SESSION=425_1_7_4_28_6_1_0_4_3_0_0_280700_0_2_0_1653227658_1653183035_1653227656%7C9%231635556_55_1653183029%7C9'
}
# 获得每页搜索结果
for page in range(v_max_page):
    print('开始爬取第{}页'.format(page + 1))
    wait_seconds = random.uniform(1, 2)  # 等待时长秒
    print('开始等待{}秒'.format(wait_seconds))
    sleep(wait_seconds)  # 随机等待
    url = 'https://www.baidu.com/s?wd=' + v_keyword + '&pn=' + str(page * 10)
    r = requests.get(url, headers=headers)
    html = r.text
    print('响应码是:{}'.format(r.status_code))
    soup = BeautifulSoup(html, 'html.parser')
    result_list = soup.find_all(class_='result c-container new-pmd')
    print('正在爬取:{},共查询到{}个结果'.format(url, len(result_list)))
def get_real_url(v_url):
    """
    获取百度链接真实地址
	:param v_url: 百度链接地址
	:return: 真实地址
	"""
    r = requests.get(v_url, headers=headers, allow_redirects=False)  # 不允许重定向
    if r.status_code == 302:  # 如果返回302，就从响应头获取真实地址
        real_url = r.headers.get('Location')
    else:  # 否则从返回内容中用正则表达式提取出来真实地址
        real_url = re.findall("URL='(.*?)'", r.text)[0]
    print('real_url is:', real_url)
    return real_url
df = pd.DataFrame(
			{
				'关键词': kw_list,
				'页码': page_list,
				'标题': title_list,
				'百度链接': href_list,
				'真实链接': real_url_list,
				'简介': desc_list,
				'网站名称': site_list,
			}
		)
if os.path.exists(v_result_file):
    header = None
else:
    header = ['关键词', '页码', '标题', '百度链接', '真实链接', '简介', '网站名称']  # csv文件标头
df.to_csv(v_result_file, mode='a+', index=False, header=header, encoding='utf_8_sig')
print('结果保存成功:{}'.format(v_result_file))



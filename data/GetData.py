import requests
import bs4

urls = [
    {'url': 'https://mp.weixin.qq.com/s/u0XfHF8dgfEp8vGjRtcwXA', 'date': '04_10'},
    {'url': 'https://mp.weixin.qq.com/s/_Je5_5_HqBcs5chvH5SFfA', 'date': '04_09'},
    {'url': 'https://mp.weixin.qq.com/s/79NsKhMHbg09Y0xaybTXjA', 'date': '04_08'},
    {'url': 'https://mp.weixin.qq.com/s/HTM47mUp0GF-tWXkPeZJlg', 'date': '04_07'},
    {'url': 'https://mp.weixin.qq.com/s/8bljTUplPh1q4MXb6wd_gg', 'date': '04_06'},
    {'url': 'https://mp.weixin.qq.com/s/djwW3S9FUYBE2L5Hj94a3A', 'date': '04_05'}
]

dir = 'raw_data/'

for url in urls:
    f = open(dir + 'raw_data_' + url['date'] + '.txt', 'w+', encoding='utf-8')
    r = requests.get(url['url'])
    content = bs4.BeautifulSoup(r.content.decode('utf-8'), features='html.parser')
    section = content.find_all('section', attrs={'data-id': 106156})[1]
    ps = section.find_all('p')
    for p in ps:
        f.write(p.get_text() + '\r')
    sections = content.find_all('section', attrs={'data-id': 72469})
    for section in sections:
        ps = section.find_all('p')
        for p in ps:
            f.write(p.get_text() + '\r')
    f.close()




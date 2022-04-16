import requests
import bs4

urls = [
    {'url': 'https://mp.weixin.qq.com/s/ZkhimhWpa92I2EWn3hmd8w', 'date': '04_15'}
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




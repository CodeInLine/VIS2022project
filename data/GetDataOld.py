import requests
import bs4

urls = [
    {'url': 'https://mp.weixin.qq.com/s/MkKsQkgvUWbwj8z9jG_Zng', 'date': '04_04'},
    {'url': 'https://mp.weixin.qq.com/s/uj4TYASUn2YJZQMg2aUvdw', 'date': '04_03'},
    {'url': 'https://mp.weixin.qq.com/s/2VWTo6e9gmWJ0vxeZ4PhIw', 'date': '04_02'},
    {'url': 'https://mp.weixin.qq.com/s/gQDyFLtdILP2NuSBgcjUxg', 'date': '04_01'},
    {'url': 'https://mp.weixin.qq.com/s/hnrGo4KvUvxhpjFyiE8-sQ', 'date': '03_31'},
    {'url': 'https://mp.weixin.qq.com/s/SSFVzOSXPTj-aLzR1tdtxw', 'date': '03_30'},
    {'url': 'https://mp.weixin.qq.com/s/K6jT1wRMSScBhvxcB2yV4g', 'date': '03_29'},
    {'url': 'https://mp.weixin.qq.com/s/656rotFOMeDScnKSt6OmyQ', 'date': '03_28'},
    {'url': 'https://mp.weixin.qq.com/s/MfBzdO0bG4fbokKTRCWuIw', 'date': '03_27'},
    {'url': 'https://mp.weixin.qq.com/s/JwUn4sVxSvHQs5KoyFn-lw', 'date': '03_26'},
    {'url': 'https://mp.weixin.qq.com/s/XG03jIjQLLLjaJZ1DD-kAg', 'date': '03_25'},
    {'url': 'https://mp.weixin.qq.com/s/oBQXVicoi5tXuFt06ybsog', 'date': '03_24'},
    {'url': 'https://mp.weixin.qq.com/s/XL_hz8ESYGM8ZW7FQuHFRA', 'date': '03_23'},
    {'url': 'https://mp.weixin.qq.com/s/UUmzrx54vMdzZBKUm4uKfg', 'date': '03_22'},
    {'url': 'https://mp.weixin.qq.com/s/lqzf4il2Io1LXXf11PBN-A', 'date': '03_21'},
    {'url': 'https://mp.weixin.qq.com/s/s3FN7zk__wTz-jZM1c_lOg', 'date': '03_20'},
    {'url': 'https://mp.weixin.qq.com/s/njMjbpRELpe7SWA7AnB5NA', 'date': '03_19'},
    {'url': 'https://mp.weixin.qq.com/s/xLVPnOTErTe3dmAenUyDGQ', 'date': '03_18'},
    {'url': 'https://mp.weixin.qq.com/s/ZSIDH6G-IIrWUmXKpWGulg', 'date': '03_17'},
    {'url': 'https://mp.weixin.qq.com/s/J8Ib1MFCWI6vouw5Gz2MiQ', 'date': '03_16'},
    {'url': 'https://mp.weixin.qq.com/s/G77OEw8GgiJQiAkRH3tOlw', 'date': '03_15'},
    {'url': 'https://mp.weixin.qq.com/s/15EJxTQ-lmatQhze30R9-g', 'date': '03_14'},
    {'url': 'https://mp.weixin.qq.com/s/kdSUGd2xGR6Xx-HfekKUSA', 'date': '03_13'},
    {'url': 'https://mp.weixin.qq.com/s/MbQoeN54jg0xVDsMl4oTxw', 'date': '03_12'},
    {'url': 'https://mp.weixin.qq.com/s/e_1M17uJPRITsLaYcdgnxA', 'date': '03_11'},
    {'url': 'https://mp.weixin.qq.com/s/TXbtjAgxlR5rvgaCJ_dt7A', 'date': '03_10'},
    {'url': 'https://mp.weixin.qq.com/s/9_HUJ4bc58bJP_InkqMKhw', 'date': '03_09'},
    {'url': 'https://mp.weixin.qq.com/s/ccZhy4RexXajKwoeX8pURw', 'date': '03_08'},
    {'url': 'https://mp.weixin.qq.com/s/8ab50NJNL7zbaDC8HbMMFQ', 'date': '03_07'},
    {'url': 'https://mp.weixin.qq.com/s/-osxhdKAgIv9Yz6_7uKTrA', 'date': '03_06'},
    {'url': 'https://mp.weixin.qq.com/s/k0y4SvCRKtR9RyKeAi15ng', 'date': '03_05'},
    {'url': 'https://mp.weixin.qq.com/s/RAmdUMyQxuWlEAv5gG1U7A', 'date': '03_04'},
    {'url': 'https://mp.weixin.qq.com/s/Jlnl9fkV5q368tEgtta-6Q', 'date': '03_03'},
    {'url': 'https://mp.weixin.qq.com/s/shipU1Tz-9JLwVwUl0pCmg', 'date': '03_02'},
    {'url': 'https://mp.weixin.qq.com/s/fdQQmBiK_hm3Erg_99k-xw', 'date': '03_01'},
    {'url': 'https://mp.weixin.qq.com/s/LXNrvU2ot8cvgIr2OHkWyA', 'date': '02_28'},
    {'url': 'https://mp.weixin.qq.com/s/8CC7x6vW2TKI6sKqOekMGg', 'date': '02_27'},
    {'url': 'https://mp.weixin.qq.com/s/jpToJCcWCPWnCHvH8jOY2w', 'date': '02_26'},
    {'url': 'https://mp.weixin.qq.com/s/Y03NyDXewG_ldX3KGkW5iQ', 'date': '02_25'},
    {'url': 'https://mp.weixin.qq.com/s/g8xeJQOYrw-FZy8Vsx7P6A', 'date': '02_24'},
    {'url': 'https://mp.weixin.qq.com/s/gG_S3ew30qqLVj24qbHlFA', 'date': '02_23'}
]

dir = 'raw_data/'

for url in urls:
    f = open(dir + 'raw_data_' + url['date'] + '.txt', 'w+', encoding='utf-8')
    r = requests.get(url['url'])
    content = bs4.BeautifulSoup(r.content.decode('utf-8'), features='html.parser')
    section = content.find_all('section', attrs={'data-id': 106156})[0]
    ps = section.find_all('p')
    for p in ps:
        f.write(p.get_text() + '\r')
    
    f.close()




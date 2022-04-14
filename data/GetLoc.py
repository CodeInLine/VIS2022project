import requests
import json
import time

url = 'https://api.map.baidu.com/geocoding/v3/'

read_filename = 'loc_text/03_31.txt'

write_filename = 'loc_info/03_31.json'

web_ak = '7730Bm5nP9fNrm2GNWemmkYr7vZQLiG1'

js_ak = 'GGksizlb2uf1GKkCNbBxworr81BF7UHf'

params = {
    'ak': web_ak,
    'address': '',
    'city': '上海市',
    'output': 'json'
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'Connection': 'close'
}

fin = open(read_filename, 'r', encoding='utf-8')

fout = open(write_filename, 'w', encoding='utf-8')

json_text = []

text = fin.read()

d = text.split("||")

for t in d:
    print("Task started!")
    time.sleep(0.25)
    count = 0
    address = t.split("\n")
    prefix = address[0][1:-1]
    for a in address[1:]:
        count += 1
        print(count)
        params['address'] = prefix + a
        r = requests.get(url, params=params, headers=header)
        data = json.loads(r.content.decode('utf-8'))
        if data['status'] == 0:
            location = data['result']['location']
            precise = data['result']['precise']
            confidence = data['result']['confidence']
            comprehension = data['result']['comprehension']
            json_text.append({'address': params['address'], 'location': location, 'precise': precise, 'confidence': confidence, 'comprehension': comprehension})
        else:
            print("No result!")
    print("Task finished!")
            
write_text = json.dumps(json_text, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

fout.write(write_text)

fin.close()

fout.close()

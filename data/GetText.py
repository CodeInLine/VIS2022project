import re

read_filename = 'raw_data/raw_data_03_06.txt'

write_filename = 'loc_text/03_06.txt'

fin = open(read_filename, 'r', encoding='utf-8')

fout = open(write_filename, 'w', encoding='utf-8')

districts = ['浦东新区', '黄浦区', '静安区', '徐汇区', '长宁区', '普陀区', '虹口区', '杨浦区', '宝山区', '闵行区', '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区']

data = fin.read()

for district in districts:
    if district != '浦东新区':
        fout.write('\n||')
    fout.write('{' + district + '}')
    texts = re.findall(district + r'(.+)\b', data)
    texts = list(set(texts))
    print(texts)
    for text in texts:
        fout.write('\n' + text)

import json
from translate import Translator
import re
from transliterate import translit

def comb(dict, item1, item2):
    dict[item1]['twit count'] += dict[item2]['twit count']
    dict[item1]['word count'] += dict[item2]['word count']
    dict[item1]['swear count'] += dict[item2]['swear count']
    changeble_mistakes = dict[item1]['mistakes'].copy()
    for mistake in dict[item2]['mistakes']:
        if changeble_mistakes.get(mistake):
            changeble_mistakes.update({mistake: changeble_mistakes[mistake]+dict[item2]['mistakes'][mistake]})
        else:
            changeble_mistakes.update({mistake: dict[item2]['mistakes'][mistake]})
    dict[item1]['mistakes'] = changeble_mistakes
    dict.pop(item2)


openfile = 'project_data.json'
savefile = 'project_data_united.json'

fh = open(openfile, 'r', encoding='utf-8')
project_data = json.load(fh)
fh.close()

r = re.compile("[а-яА-Я]+")
translator = Translator(to_lang='ru')
city_names_orig = list(project_data.keys())
city_names = list(project_data.keys())
i = 0
j = 0
k = 1

while i < len(city_names):
    city_names[i] = city_names[i].lower().split(', ')[0]
    if (not (r.match(city_names[i]))) | ('ї' in city_names[i]):
        while True:
            try:
                print(city_names[i])
                city_names[i] = translator.translate(city_names[i]).lower()
                if 'республика' in city_names[i]:
                    city_names[i] = city_names[i].split(' ')[1]
                if not (r.match(city_names[i])):
                    city_names[i] = translit(city_names[i], 'ru')
                print(city_names[i])
                break
            except:
                print('error')
                continue
    print(i)
    i+=1

print(city_names)
i = 0
j = 0
k = 1

while i < len(city_names)-1:
    j = i+1
    while j < len(city_names):
        if (city_names[i] == city_names[j]) & ('район' not in city_names[i].split(' ')):
            comb(project_data, city_names_orig[i], city_names_orig[j])
            city_names.pop(j)
            city_names_orig.pop(j)
            j -= 1
            print(k)
            k += 1
        j += 1
    i += 1


with open(savefile, 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(project_data, ensure_ascii=False))
fh.close()
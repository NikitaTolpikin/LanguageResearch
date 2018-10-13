import json
import swear
import re

openfile = 'project_data_united.json'
savefile = 'project_data_filtered_united.json'

fh = open(openfile, 'r', encoding='utf-8')
project_data = json.load(fh)
fh.close()

swearings = swear.r()
exceptions = swear.e()
R = re.compile("[А-Я]+")

i=0
count = 0

city_names = list(project_data.keys())

while i < len(city_names):
    if project_data[city_names[i]]['twit count'] < 1000:
        project_data.pop(city_names[i])
    i+=1

for item in project_data:
    if project_data[item]['twit count'] > 1000:
        editable_mistakes = project_data[item]['mistakes'].copy()
        for mistake in project_data[item]['mistakes']:
            if any(s in mistake.lower() for s in swearings):
                count = editable_mistakes.pop(mistake)
                project_data[item]['swear count'] = project_data[item]['swear count'] + count
                print(item)
                print(mistake)
                print(project_data[item]['swear count'])
            elif ('*' in mistake) | ('~' in mistake):
                count = editable_mistakes.pop(mistake)
                print(item)
                print(mistake)
                project_data[item]['mistake count'] -= count
            elif mistake.lower() in exceptions:
                count = editable_mistakes.pop(mistake)
                project_data[item]['mistake count'] -= count
                print(item)
                print(mistake)
            elif bool(R.match(mistake)) & (mistake.lower()in editable_mistakes):
                count = editable_mistakes.pop(mistake)
                editable_mistakes[mistake.lower()] += count
                print(item)
                print(mistake)
        project_data[item]['mistakes'] = editable_mistakes

delete_city = ['Mongolia', 'Uzbekistan', 'Kyrgyzstan']

for item in delete_city:
    try:
        project_data.pop(item)
    except:
        pass

with open(savefile, 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(project_data, ensure_ascii=False))
fh.close()

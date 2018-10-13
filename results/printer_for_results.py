import json

ratemult = 1000


def RateDo(a, b):
    return(a*ratemult/b)


def AddWithoutMatches(placename, wdcnt, swcnt):
    fh = open('project_data.json', 'r', encoding='utf-8')
    project_data = json.load(fh)
    fh.close()

    if project_data.get(placename):
        place_dict = project_data[placename]
        twcnt_in = place_dict['twit count']
        wdcnt_in = place_dict['word count']
        swcnt_in = place_dict['swear count']
        mccnt_in = place_dict['mistake count']
        place_dict.update({'twit count': twcnt_in + 1, 'word count': wdcnt_in + wdcnt, 'word rate': (wdcnt_in + wdcnt)/(twcnt_in + 1),
                           'swear count': swcnt_in + swcnt, 'swear rate': RateDo(swcnt_in+swcnt, wdcnt_in+wdcnt), 'mistake rate': RateDo(mccnt_in, wdcnt_in+wdcnt)})

    else:
    	place_dict = {placename: {'twit count': 1, 'word count': wdcnt, 'word rate': wdcnt, 'swear count': swcnt,'swear rate': 0, 'mistake count': 0, 'mistake rate': 0, 'mistakes': {}}}
    	project_data.update(place_dict)

    with open('project_data.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(project_data, ensure_ascii=False))
    fh.close()


def AddWithMatches(placename, wdcnt, swcnt, mccnt, matches):
    fh = open('project_data.json', 'r', encoding='utf-8')
    project_data = json.load(fh)
    fh.close()
    mistakes1 = dict.fromkeys(matches, 1)

    if project_data.get(placename):
        place_dict = project_data[placename]
        twcnt_in = place_dict['twit count']
        wdcnt_in = place_dict['word count']
        swcnt_in = place_dict['swear count']
        mccnt_in = place_dict['mistake count']
        mistakes_in = place_dict['mistakes']
        place_dict.update({'twit count': twcnt_in + 1, 'word count': wdcnt_in + wdcnt, 'word rate': (wdcnt_in + wdcnt)/(twcnt_in + 1), 'swear count': swcnt_in +
                           swcnt, 'swear rate': RateDo(swcnt_in+swcnt, wdcnt_in+wdcnt), 'mistake count': mccnt_in+mccnt, 'mistake rate': RateDo(mccnt_in+mccnt, wdcnt_in+wdcnt)})

        for key in mistakes1:
            if mistakes_in.get(key):
                mistakes_in.update({key: mistakes_in[key]+1})
            else:
                mistakes_in.update({key: 1})
    else:
        place_dict = {placename: {'twit count': 1, 'word count': wdcnt, 'word rate': wdcnt, 'swear count': swcnt,
                                  'swear rate': 0, 'mistake count': mccnt, 'mistake rate': 0, 'mistakes': mistakes1}}

    with open('project_data.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(project_data, ensure_ascii=False))
    fh.close()

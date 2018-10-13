import swear

swearings = swear.r()
exrules = ['UPPERCASE_SENTENCE_START', 'COMMA_PARENTHESIS_WHITESPACE','WHITESPACE_RULE', 'WORD_REPEAT_RULE', 'DOUBLE_PUNCTUATION']

def rmswear(matches):
		i=0
		k=0
		while i<len(matches):
			er = matches[i].context[matches[i].contextoffset:(matches[i].contextoffset+matches[i].errorlength)]
			er.lower
			if er in swearings:
				del matches[i]
				k+=1
			else:
				i+=1
		return [matches, k]

def rm_at_ht_http(text):
	s = text.split()
	i=0
	flag = False

	while i<len(s):
		if s[i][0]=='@':
			flag = True
		elif s[i][0]=='#':
			flag = True
		elif s[i][0:4] == 'http':
			flag = True
		else:
			i+=1
		if flag:
			del s[i]
		flag = False

	text = ' '.join(map(str, s))
	return text

def wdcnt(text):
	s = text.split()
	l = len(s)
	return l	

def rmtrash(matches):
	i=0
	flag = False
	while i<len(matches):
		er = matches[i].context[matches[i].contextoffset:(matches[i].contextoffset+matches[i].errorlength)]
		if matches[i].ruleId in exrules:
			flag = True
		elif len(matches[i].replacements) == 0:
			flag = True
		elif er.isupper():
			flag = True
		else:
			i+=1
		if flag:
			del matches[i]
		flag = False
	return matches
	

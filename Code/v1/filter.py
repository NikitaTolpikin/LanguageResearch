swearings = ['сука', 'блять']
exrules = ['UPPERCASE_SENTENCE_START', 'COMMA_PARENTHESIS_WHITESPACE','WHITESPACE_RULE', 'WORD_REPEAT_RULE', 'DOUBLE_PUNCTUATION']

def rmswear(matches):
		i=0
		while i<len(matches):
			er = matches[i].context[matches[i].contextoffset:(matches[i].contextoffset+matches[i].errorlength)]
			er.lower
			if er in swearings:
				del matches[i]
			else:
				i+=1
		return matches

def rmat(text):
	i=0
	while i<len(text):
		if text[i]=='@':
			endOfAtIndex = text.find(' ', i)
			if endOfAtIndex == -1:
				text = text[:i]
			else:
				text = text[:i]+text[endOfAtIndex:]
		i+=1
	return text

def rmht(text):
	i=0
	while i<len(text):
		if text[i]=='#':
			endOfHashtagIndex = text.find(' ', i)
			if endOfHashtagIndex == -1:
				text = text[:i]
			else:
				text = text[:i]+text[endOfHashtagIndex:]
		i+=1
	return text

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
	

import datetime

def PrintAllMatches(matches, placename, word_count, swear_count):
	now = datetime.datetime.now()
	md = now.strftime("%m-%d")	
	filename = 'allmatches-'+md+'.txt'
	allmatches_file = open(filename, 'a')
	matches_length = len(matches)
	if matches_length == 0:
		allmatches_file.write(placename + '\n' + str(word_count) + ' ' + str(swear_count) + ' ' + str(matches_length) + '\n')
	else:
		allmatches_file.write(placename + '\n' + str(word_count) + ' ' + str(swear_count) + ' ' + str(matches_length) + '\n')
		for Match in matches:
			allmatches_file.write(Match.context[Match.contextoffset:(Match.contextoffset+Match.errorlength)]+'\n')
	allmatches_file .close()

def PrintLog(placename, original_text, text, word_count, matches, swear_count):
	print(placename)
	print(original_text)
	print('-----------------------------------------------------------------------')
	print(text)
	print(word_count, ' ', swear_count, ' ', len(matches))
	for Match in matches:
		print(Match.context[Match.contextoffset:(Match.contextoffset+Match.errorlength)], ' ', Match.replacements)
	print('-----------------------------------------------------------------------')

from birdy.twitter import StreamClient
import language_check
import filter
import printer

tool = language_check.LanguageTool('ru')

CONSUMER_KEY = 'LidfFLGcW1NLM2IojLHUDSuw2'
CONSUMER_SECRET = 'kr4utbqPLFI8AhOvA6NtGHHD4Si3pAmY5FC9WcyE7PpSzq0Rzx'
ACCESS_TOKEN = '2260381756-XyYtQFslBXzmlJh6SqMd4VIZ6twKI5SRDM2CUBF'
ACCESS_TOKEN_SECRET ='Sg0vaaNo7aDgXMzyrfaSJtFdv6hGlThHw3uM6jjSHQp1L'

log = True

while True:
	try:
		client = StreamClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

		resource = client.stream.statuses.filter.post(language = 'ru', locations = '20.74,36.16,179.47,83.05')

		for data in resource.stream():
			placename = data.place.full_name

			try:
				data.extended_tweet.full_text
				text = data.extended_tweet.full_text
			except:
				data.text
				text = data.text

			original_text = text

			text = filter.rm_at_ht_http(text)	
	
			word_count = filter.wdcnt(text)
			matches = tool.check(text)
			matches = filter.rmtrash(matches)
			mmm = filter.rmswear(matches)
			matches = mmm[0]
			swear_count = mmm[1]

			if log:
				printer.PrintLog(placename, original_text, text, word_count, matches, swear_count)

			printer.PrintAllMatches(matches, placename, word_count, swear_count)
	except:
		continue


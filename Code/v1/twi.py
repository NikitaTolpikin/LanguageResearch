from birdy.twitter import StreamClient
import language_check
import filter
import printer

language_check.set_directory('.local/lib/python3.5/site-packages/language_check/LanguageTool-2.2/')
tool = language_check.LanguageTool('ru')

CONSUMER_KEY = 'LidfFLGcW1NLM2IojLHUDSuw2'
CONSUMER_SECRET = 'kr4utbqPLFI8AhOvA6NtGHHD4Si3pAmY5FC9WcyE7PpSzq0Rzx'
ACCESS_TOKEN = '2260381756-XyYtQFslBXzmlJh6SqMd4VIZ6twKI5SRDM2CUBF'
ACCESS_TOKEN_SECRET ='Sg0vaaNo7aDgXMzyrfaSJtFdv6hGlThHw3uM6jjSHQp1L'

client = StreamClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

resource = client.stream.statuses.filter.post(language = 'ru', locations = '20.74,36.16,179.47,83.05')

log = True

for data in resource.stream():

	placename = data.place.full_name

	try:
		data.extended_tweet.full_text
		text = data.extended_tweet.full_text
	except:
		data.text
		text = data.text

	original_text = text

	text = filter.rmat(text)
	text = filter.rmht(text)	
	
	matches = tool.check(text)
	matches = filter.rmtrash(matches)
	matches = filter.rmswear(matches)

	if log:
		printer.PrintLog(placename, original_text, text, matches)

	printer.PrintAllMatches(matches, placename)


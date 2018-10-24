import pandas as pd
import re

def parse_file(text_file):
	'''Convert WhatsApp chat log text file to a Pandas dataframe.'''
	
	with open(text_file) as f:
		data = [line.replace('\n', ' ').strip() for line in f.readlines()]
	sender = []
	message = []
	datetime = []
	pattern = re.compile(r'(.+\/)(.+\/)(.+,)(.*)- (.+): (.*)', re.S | re.X)
	for row in data:
		full_message = pattern.match(row)
		if full_message is None:
			message[-1] += row
			continue

		date_and_time = full_message.group(2)+full_message.group(1)+full_message.group(3)+full_message.group(4)
		date_and_time = date_and_time.strip()
		datetime.append(date_and_time)

		sender.append(full_message.group(5))

		try:
			message.append(full_message.group(6))
		except:
			message.append('')

	df = pd.DataFrame(list(zip(datetime, sender, message)), columns=['timestamp', 'sender', 'message'])
	df['timestamp'] = pd.to_datetime(df.timestamp, format='%d/%m/%y, %I:%M %p')

	# remove events not associated with a sender
	df = df[df.sender != ''].reset_index(drop=True)
	
	return df
if __name__ == '__main__':
	df = parse_file('WhatsApp Chat with Anubhavi.txt')
	print(df)
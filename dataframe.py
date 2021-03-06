import pandas as pd
import re
import config

class Data:
	'''Clean WhatsApp chat and convert to a Pandas dataframe.'''
	def __init__(self, text_file):
		self.text_file = text_file

	def parse_file(self):
		
		with open(self.text_file) as f:
			data = [line for line in f.readlines()]

		sender = []
		message = []
		datetime = []
		pattern = re.compile(r'(.+\/)(.+\/)(.+,)(.*)- (.+?): (.*)', re.S | re.X)
		for row in data:
			full_message = pattern.match(row)
			if full_message is None:
				message[-1] += ' '+row
				continue

			date_and_time = full_message.group(2)+full_message.group(1)+full_message.group(3)+full_message.group(4)
			date_and_time = date_and_time.strip()
			datetime.append(date_and_time)

			sender.append(full_message.group(5).strip())

			try:
				message.append(re.sub(r'[.,?!\n]',' ', full_message.group(6)).strip())
			except:
				message.append('')

		df = pd.DataFrame(list(zip(datetime, sender, message)), columns=['timestamp', 'sender', 'message'])
		df['timestamp'] = pd.to_datetime(df.timestamp, format='%d/%m/%y, %I:%M %p')

		# remove events not associated with a sender
		df = df[df.sender != ''].reset_index(drop=True)
		print('DataFrame created..')

		return df

if __name__ == '__main__':
	data = Data(config.config['FILE_NAME'])
	df = data.parse_file()
	print(df)
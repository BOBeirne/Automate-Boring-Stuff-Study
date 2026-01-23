""" 
YouTube Transcriber

Write a program that glues together the features of yt-dlp and Whisper to automatically download YouTube videos and produce subtitle files in the .srt format. 
The input can be a list of URLs to download and transcribe. 
You can also add options to produce different subtitle formats. 
Python is an excellent “glue language” for combining the capabilities of different modules.
"""

import yt_dlp, whisper

from pathlib import Path







def download_audio(video_url):
	# configuration
	options = { #yt_dlp config
		'quiet': True, # supress output
		'no_warnings': True, # supress warnings
		'outtmpl': 'downloaded_content.%(ext)s', # use following naming template
		'format': 'm4a/bestaudio/best', # use best audio quality
		'postprocessors': [{ # ffmpeg config
			'key': 'FFmpegExtractAudio', # extract audio only
			'preferredcodec': 'm4a', # use m4a format
		}]
	}
	with yt_dlp.YoutubeDL(options) as f:
		f.download([video_url])

def transcribe(file):
	model = whisper.load_model('tiny') # returns model.Whisper object 
	result = model.transcribe(file)
	write_function = whisper.utils.get_writer('srt','.') # 1st arg is format, . means cwd
	write_function(result, 'audio') # use function to pass the resulting dictionary and output file name

print('Launching Youtube Subtitle Generator...')
url = input('Provide YT link: \n > ')

try:
	download_audio(url)
	print(f'Downloaded audio...')
	matches = list(Path().glob('downloaded_content.*')) # use glob to find the pattern
	dl_files = str(matches[0])
	print(f'Transcribing {dl_files}')
	transcribe(dl_files)
	print(f'Done.')

except Exception as err:
	print(f'There was an issue... {err}')
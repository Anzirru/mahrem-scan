#!/usr/bin/env python
# -*- coding: UTF-8 -*-
_ = '''

■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
■                                           ■
■   █▀▄▀█ ██    ▄  █ █▄▄▄▄ ▄███▄   █▀▄▀█    ■
■   █ █ █ █ █  █   █ █  ▄▀ █▀   ▀  █ █ █    ■
■   █ ▄ █ █▄▄█ ██▀▀█ █▀▀▌  ██▄▄    █ ▄ █    ■
■   █   █ █  █ █   █ █  █  █▄   ▄▀ █   █    ■
■      █     █    █    █   ▀███▀      █     ■
■     ▀     █    ▀    ▀              ▀      ■
■          ▀                                ■
■      ▄▄▄▄▄   ▄█▄    ██      ▄             ■
■     █     ▀▄ █▀ ▀▄  █ █      █            ■
■   ▄  ▀▀▀▀▄   █   ▀  █▄▄█ ██   █           ■
■    ▀▄▄▄▄▀    █▄  ▄▀ █  █ █ █  █           ■
■              ▀███▀     █ █  █ █           ■
■                       █  █   ██           ■
■                      ▀                    ■
■             Mahrem Scan v0.9              ■
■              by Anzirra team              ■
■                                           ■
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■

'''

limit = 100		# How many mahrem to get
images = True 		# Get with images
unique_name = True	# Create new file on every session
mode = 'Lightshot'	# Lightshot or Youtube
save = False		# Save images to locale

print(_ + '\n')

import random, string, requests, re, time, os, codecs, sys

if unique_name:
	name = 'mahrem' + str(int(time.time())) + '.html'
else:
	name = 'mahrem.html'

print(mode + ' content')

print('File name: ' + name + '\n')

header = ''

content = _

if sys.version_info < (3, 0):
	try:
		content = _.decode('utf-8')
	except Exception as ex:
		pass

if not os.path.exists(name):
	f = codecs.open(name, 'w', 'utf-8')
	f.write('''
			<div style="
				text-shadow: 5px 5px 3px rgba(0, 0, 0, .3); 
				color: #222222; 
				display: block;
				text-align: center;
			">
				<pre>
				''' + content +'''
				</pre>
			</div>
			<div></div>
		''')
	f.close()

if save:
	print('Images will be saved')

animation = "|/-\\"
idx = 0

for i in range(limit):
	exists = True

	imgarea = ''
	x = ''
	url = ''
	img = ''

	try:
		while (True):

			if mode == 'Lightshot':
				x = ''.join(random.choice(string.ascii_lowercase + string.digits) for e in range(random.randint(5, 6)))
			elif mode == 'Youtube':
				x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for e in range(11))

			if mode == 'Lightshot':
				url = 'https://prnt.sc/' + x
			if mode == 'Youtube':
				url = 'https://youtube.com/watch?v=' + x

			if not images:
				break

			if mode == 'Lightshot':
				time.sleep(random.random() * 2)
				r = requests.get(url, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})

				a = re.findall("\"image\-container.*\<img\sclass\=\".*\"\ssrc\=(.*)\"", r.text)

				if not a:
					continue

				if len(a[0].split('"')) < 2:
					continue

				img = a[0].split('"')[1]
				img_addr = img

				if img.startswith('//'):
					continue

				if not img:
					exists = False
					continue

				if save:
					img_addr = './ms-images/' + img.split('/')[-1]

				imgarea = '''
					<div style="
						width:250px;
						margin: 10px;
						text-align: center;
					">
						<a target="_blank" href="''' + img_addr + '''">
							<img src="''' + img_addr + '''" width="250" align="middle" />
						</a>
					</div>
					'''

				if save:
					if not os.path.exists('./ms-images'):
						os.mkdir('ms-images')

					img_data = requests.get(img, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}).content
					with open('./ms-images/' + img.split('/')[-1], 'wb') as handler:
						handler.write(img_data)

			elif mode == 'Youtube':
				imgarea = '''
					<div style="width:200px;">
					<iframe width="560" height="315" src="''' + url + '''" frameborder="0" allowfullscreen></iframe>
					</div>
				'''
			break
	except Exception as ex:
		exists = False
#		print(ex)
		pass


	if exists:

		print('┌' + '{:*^78}'.format(' ' + str(i + 1) + ' ').replace('*', '─') + '┐')
		print('│ ' + '{:<76}'.format(' ' + url[0:74] + ' ').replace('*', '│') + ' │')
		if mode != 'Youtube' and images:
			print('│ ' + '{:<76}'.format(' ' + img_addr[0:74] + ' ').replace('*', '│') + ' │')
		print('└' + '{:*^78}'.format('').replace('*', '─') + '┘')
		print('')

		f = open(name, 'a')
		f.write('''

			<div style="
				width: 280px;
				margin: 10px auto;
				background-color: crimson;
				border-radius: 10px;
				padding: 10px;
				display: inline-block;
			">
				<div style="width:200px;">
					<a target="_blank" href="''' + url + '''" style="
						text-decoration: none;
						color: #ffffff;
						font-weight: bold;
						display: block;
						margin-bottom: 10px;
						padding: 10px 20px;
					">
						''' + x + '''
					</a>
				</div>
				'''
				+ imgarea +
				'''
			</div>
			\r\n

			''')
		f.close()

#input()

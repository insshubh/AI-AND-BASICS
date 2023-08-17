import os
import json
import random
import requests
import datetime

def get_date():
	dt = datetime.datetime.now()
	dt = dt.date()
	return dt.strftime('%B %d, %Y')

def get_time():
	dt = datetime.datetime.now()
	dt = dt.time()
	return dt.strftime('%I:%M %p')

def get_joke():
	url = 'https://some-random-api.ml/joke'
	r = requests.get(url)
	data = r.json()
	return data['joke']

def get_quote():
	url = 'https://api.quotable.io/random'
	output = ''

	r = requests.get(url)
	quote = r.json()
	output += quote['content'] + '\n'
	output += f"     -{quote['author']}"

	return output

def fetch_apikey(api):
	with open('data/credentials.json') as f:
		data = json.load(f)
	key = data.get(api, None)

	return data[api]

def chatbot(api_key, query):
	url = f"http://api.wolframalpha.com/v1/result?appid={api_key}&i={query}%3f"
	r = requests.get(url)
	data = r.text
	if data == 'Wolfram|Alpha did not understand your input':
		return 'Couldn\'t understand the query'
	else:
		return data

def get_factor(number):
	factors = []
	for i in range(1, number + 1):
		if number % i == 0:
			factors.append(i)
	return factors

def get_multiples(number,count):
	multiples = []
	for i in range(1, count + 1):
		multiples.append(number * i)
	return multiples

def is_prime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True

	if n % 2 == 0 or n % 3 == 0:
		return False

	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6

	return True
import sys
import json
import socket
import requests
import requests_oauthlib

from bs4 import BeautifulSoup


# Include your Twitter account details
file = open('secret.json')
secret = json.load(file)
file.close()

ACCESS_TOKEN = secret['ACCESS_TOKEN']
ACCESS_SECRET = secret['ACCESS_SECRET']
CONSUMER_KEY = secret['CONSUMER_KEY']
CONSUMER_SECRET = secret['CONSUMER_SECRET']
my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)


def get_tweets():
  url = 'https://stream.twitter.com/1.1/statuses/filter.json'	
  query_data = [('language', 'en'), ('locations', '-130,-20,100,50'),('track','iphone')]
  query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
  response = requests.get(query_url, auth=my_auth, stream=True)
  print(query_url, response)

  return response

def send_tweets_to_spark(http_resp, tcp_connection):
  for line in http_resp.iter_lines():
    try:
      full_tweet = json.loads(line)
      tweet_text = full_tweet['text']
      print("Tweet Text: " + tweet_text)
      print ("------------------------------------------")
      tweet_screen_name = "SN:"+full_tweet['user']['screen_name']
      print("SCREEN NAME IS : " + tweet_screen_name)
      print ("------------------------------------------")
      source = full_tweet['source']
      soup = BeautifulSoup(source)

      for anchor in soup.find_all('a'):         
        print("Tweet Source: " + anchor.text)        

      tweet_source = anchor.text
      source_device = tweet_source.replace(" ", "")
      device = "TS"+source_device.replace("Twitter", "") 
      print("SOURCE IS : " + device)
      print ("------------------------------------------")
      tweet_country_code = "CC"+full_tweet['place']['country_code']
      print("COUNTRY CODE IS : " + tweet_country_code)
      print ("------------------------------------------")
      tcp_connection.send(tweet_text +' '+ tweet_country_code + ' '+ tweet_screen_name +' '+ device +'\n')

    except:
      continue
   

TCP_IP = 'localhost'
TCP_PORT = 3000
conn = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print("Waiting for TCP connection...")
conn, addr = s.accept()

print("Connected... Starting getting tweets.")
resp = get_tweets()
send_tweets_to_spark(resp, conn)
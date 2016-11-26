#!/usr/bin/python
#
# Creates a tweet for each line of text given on stdin
#
# Copyright (c) 2016, Michael Craze -- https://crazesweb.blogspot.com
#
import sys
import tweepy

# Twitter credentials
twitter_cfg = {
	"consumer_key" : "",
	"consumer_secret" : "",
	"access_token" : "",
	"access_token_secret" : ""
}

def GetTwitterAPI(cfg):
	auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
	auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
	return tweepy.API(auth)

def main():
	twitter_api = GetTwitterAPI(twitter_cfg)
	for line in sys.stdin:
		tweet = line
		print "Tweeting: \n " + line
		status = twitter_api.update_status(status=tweet)

if __name__ == "__main__":
	main()

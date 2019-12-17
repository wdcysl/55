import tweepy
import re
#填写twitter提供的开发Key和secret
consumer_key = 'fvSMtiTLBfwpHenMIf0g85504'
consumer_secret = '8dVzvKqzNMvyiimPmng5gOFMO0IfsmdjPvHSiuG2g0kboACrZM'
access_token = '1174917647948869632-Al3ZzX96GkItqBmEp6xQmEC3WTAz1V'
access_token_secret = 'G71SMyoERpwiL8GMpc96Tp79egCp5whIvr5NxNTtRjnTZ'
 
 
#提交你的Key和secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
#获取类似于内容句柄的东西
api = tweepy.API(auth)
 
#打印我自己主页上的时间轴里的内容


highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]') 

public_tweets = api.home_timeline()
for tweet in public_tweets:
  print(tweet.text)

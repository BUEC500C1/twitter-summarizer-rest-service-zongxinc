#access token: 1165945693627809792-v3O1zGduCeiXhgfxwQV9BlIM6fTMsL
#access token secret: 4vLxm2RC4lkP30anwghf80jZbFKSyncxYPHYSrr1n8ZPN
import tweepy
import cv2
import glob
import pprint
import os
from PIL import Image, ImageDraw, ImageFont
import configparser
import pickle
import shutil
import zipfile



# consumer_key = 'R1Yz5Zv7eaa5rFs6dL7aIMgZj'
# consumer_secret = 'U6U1pbXho1KH6UIiu2b2YuiAlh02kHMYFICGmU6pSbljUngD3E'
# access_token = '1165945693627809792-v3O1zGduCeiXhgfxwQV9BlIM6fTMsL'
# access_token_secret = '4vLxm2RC4lkP30anwghf80jZbFKSyncxYPHYSrr1n8ZPN'
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# config = configparser.ConfigParser()
# config.read("keys")
# auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
# auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_secret').strip())

# api = tweepy.API(auth)
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def get_api():
    try:
        config = configparser.ConfigParser()
        config.read("keys")
        auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
        auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_secret').strip())
        api = tweepy.API(auth)
    except:
        with open('api.pkl', 'rb') as input:
            api = pickle.load(input)

    return api

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')
    #encode('ascii','xmlcharrefreplace')
    #encode('ascii', 'ignore').decode('ascii')

def txt2img(txt, user, num):
	img = Image.new('RGB', (1280, 500), color = (0, 0, 0))
	font = ImageFont.truetype('./DancingScript-Bold.ttf' ,20)
	d = ImageDraw.Draw(img)
	d.text((100, 250), txt, fill = (255, 255, 255), font = font)
	filename = 'image_'+user+'/' + 'v'+ str(num) + user +'.png'
	img.save(filename)

def get_tweets(name, numOfTweets):
    api = get_api()
    alltweets = []
    new_tweets = api.user_timeline(screen_name = name, count = numOfTweets)
    for tweet in new_tweets:
        alltweets = alltweets + [tweet.text]
    return alltweets

def tweet_convert(username, imagepath, numOfTweets):
    if not os.path.exists(imagepath):
        os.mkdir(imagepath)

    tweet1 = get_tweets(username, numOfTweets)

    for i in range(len(tweet1)):
        txt2img(deEmojify(tweet1[i]), username, i)

    if os.path.exists(f'{imagepath}.DS_Store'):
        os.remove(f'{imagepath}.DS_Store')

    makevideo(imagepath, f'v_{username}')
    os.rmdir(imagepath)

def makevideo(filepath,videoname):
    file_directory = (f'{filepath}')
    list=[]
    for root,dirs,files in os.walk(file_directory):
        for file in files:
           list.append(file)  
    print(len(list))
    list.sort()
    video=cv2.VideoWriter(f'{videoname}.avi', cv2.VideoWriter_fourcc(*'MJPG'), 0.333, (1600,500))
    if not os.path.isdir('./video'):
        os.mkdir('./video')
    for i in range(1,len(list)+1):
        img=cv2.imread(f'{filepath}'+list[i-1])
        img=cv2.resize(img, (1600,500)) 
        video.write(img)   
    # for e in list:
    #     print(e)
    #     os.remove(f'{filepath}{e}')
    os.system(f'rm -r {filepath}')
    for root,dirs,files in os.walk('./'):
        for file in files:
            if file.endswith('.avi'):
                print(file)
                path = os.path.join(root, file)
                shutil.move(path, './video')
                print('yes')

    # file_path = os.path.join('./video', f'{videoname}.avi')
    # os.rename('README.md', f'./video/{videoname}.avi')
    # shutil.move('README.md', f'./video/{videoname}.avi')

# name = '@realDonaldTrump'
# public_tweets = api.user_timeline(screen_name = name, count = 10)
# count = 0
# for tweet in public_tweets:
# 	count = count + 1
# 	print(tweet.text)
# 	thetweet = deEmojify(tweet.text)
# 	txt2img(thetweet, name, count)

# img_array = []
# size = 0
# path = '/Users/allen/Documents/GitHub/video-zongxinc/image'
# for root, dirs, files in os.walk(path):
# 	for file in files:
# 		img_array.append(file)
# print(len(img_array))
 
# out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'MJPG'), 0.333, (1280, 720))

# for i  in range(1, len(img_array) + 1):
# 	img = cv2.imread('/Users/allen/Documents/GitHub/video-zongxinc/image/' + img_array[i - 1])
# 	img = cv2.resize(img, (1280, 720))
# 	out.write(img)
# print('deleting: ')
# for e in img_array:
# 	print(e)
# 	os.remove(f'{path}/{e}')


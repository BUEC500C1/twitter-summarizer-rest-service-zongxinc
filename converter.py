import queue
import threading
import time
import os
import cv2
import tweepy
from process import tweet_convert
import configparser



# config = configparser.ConfigParser()
# config.read("keys")
# auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
# auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_secret').strip())

# api = tweepy.API(auth)


class Video_compress():
    def execute(self, username, imagepath, num):
        t = threading.Thread(target = self.compress, args = (username, imagepath, num) )
        return t

    def compress(self, username, imagepath, num):
        tweet_convert(username, imagepath, num)
        # for i in range (10):
        #     time.sleep(0.5)
        #     print(f'This is {username}')

def compressVideo(userlist,num):
    thread_list = []
    for user in userlist:
        thread_list.append(add_thread(user, './image_' + user + '/', num))
    while not q.empty():
        thread_num = threading.active_count()
        if thread_num < 6:
            t = q.get()
            t.start()
    for thread in thread_list:
        if thread.is_alive():
            thread.join()

    print(q.queue)
    print(f'thread_list:{thread_list}')
    print('end')
    return 0

def add_thread(username, imagepath, num):
    thread_num = threading.active_count()
    print(thread_num)
    t = mycompressor.execute(username, imagepath, num)
    if thread_num < 6:
        t.start()
    if thread_num >= 6:
        q.put(t)
    return t

q = queue.Queue(100)
mycompressor = Video_compress()
#input_list = ['@iGuessPoems','@UnusualPoems', '@LitWorks', '@Poem4your_sprog']
#compressVideo(['@LitWorks'],10)

# class VideoCompressor():

#     def __init__ (self, pool_size = 3, queue_size = 10):
#         self.pool_size = pool_size
#         self.queue_size = queue_size

#     def execute(self, user_name):
#         t = threading.Thread(target = self.convert, args = (user_name,) )
#         return t





# os.system(f'ffmpeg -i {name} -b:v 2M -b:a 192k -filter:v fps=fps=30 -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 {name}_output.avi')



from distutils.command.clean import clean
from turtle import clear
from instagrapi import Client
from time import sleep
import os   
USERNAME = 'ajafarbaz'
PASSWARD = '@@@xxx@@@'
PATH = './cred.json'

class Bot:
    brain=None
    def __init__(self) -> None:
        self.brain=Client()
        if os.path.exists(PATH):
            self.brain.load_settings(PATH)
            self.brain.login(USERNAME,PASSWARD)
        else:
           self.brain.login(USERNAME,PASSWARD)
           self.brain.dump_settings(PATH)

        #account_info

    # def accountinfo(self):
    #    seed = self.brain.totp_generate_seed()
    #    code = self.brain.totp_generate_code(seed)
    #    return code


        # make follow Func

    # def follow_username(self,username):
    #     userid = self.brain.user_id_from_username(username)
    #     self.brain.user_follow(userid)
    #     print(f'user : [{username}] is followed')

        # get following Func

    def getfollowing_username(self,username):
        userid = self.brain.user_id_from_username(username)
        data = self.brain.user_following(userid)
        print(f'user following is : [{username}]')
        return [following.username for following in data.values()]
    
        # make unfollow Func

    def unfollow_username(self,username):
        userid = self.brain.user_id_from_username(username)
        for i in  self.brain.user_unfollow(userid):
            return i 
        print(f'user : [{username}] is unfollowed')


    # def get_username_followers(self,username,amount):

    #     print(f'geeting {amount} from [ {username} ] followers started ...')
    #     userid = self.brain.user_id_from_username(username)
    #     data = self.brain.user_followers(userid)
    #     # print(f'data => : {data}')
    #     print(f'geeting {amount}  from [ {username} ] followers done !')
    #     return [user.username for user in data.values()]

    # follow username list

    # def follow_username_list(self,data):
    #     for username in data :
    #         userid = self.brain.user_id_from_username(username)
    #         self.brain.user_follow(userid)
    #         print(f'following ( {username} ) Done :')
    #     print('done following a list of usernames')


    def update(self):
        pass
bot = Bot()

# bot.follow_username('e_r_e_n__a_l__5_5')

# print( bot.accountinfo() )

myFollowing = bot.getfollowing_username('ajafarbaz')
print(myFollowing)

sleep(10)
bot.unfollow_username(myFollowing)

# usernames = bot.get_username_followers('kimkardashian',10)
# print(usernames)
# bot.follow_username_list(usernames)

bot.update()
sleep(60)


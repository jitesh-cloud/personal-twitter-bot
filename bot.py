from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

    def login(self):
        bot = self.bot
        bot.maximize_window()
        bot.get('https://twitter.com/login')
        time.sleep(8)

        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(8)

    def tweet(self,msg):
        bot = self.bot
        click = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        click.send_keys(msg)
        time.sleep(4)
        tweet = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet.click()
        time.sleep(20)
        bot.close()

    def follow(self,ampercent):
        bot = self.bot
        bot.get('https://twitter.com/'+ampercent)
        time.sleep(4)
        if (ampercent == 'elonmusk'):
            follow = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/span/span')
            follow.click()
        elif (ampercent == 'akshaykumar'):
            follow = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/span/span')
            follow.click()
        elif (ampercent == 'narendramodi'):
            follow = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/span/span')
            follow.click()
        time.sleep(20)
        bot.close()

    def likeTweet(self,hash):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hash+'&src=typed_query')
        time.sleep(4)



def tweet(userid,passkey):
    tweet = input("\nWhat do you like to tweet on your handle: ")
    hello = TwitterBot(userid,passkey)
    hello.login()
    hello.tweet(tweet)


def follow(userid,passkey):
    at = input("\nSelect the person you would like to follow on Twitter \n1.Elon Musk \t2.Narendra Modi \t3.Akshay Kumar \nChoose 1, 2 or 3: ")
    if (at == '1'):
        at = 'elonmusk'
    elif (at == '2'):
        at = 'narendramodi'
    elif (at == '3'):
        at = 'akshaykumar'
    hello = TwitterBot(userid,passkey)
    hello.login()
    hello.follow(at)

def like(userid,passkey):
    like = input("\nSearch for hashtag you would like to explore: ")
    hello = TwitterBot(userid,passkey)
    hello.login()
    hello.likeTweet(like)

def main():
    print("Welcome to your personal Twitter Bot")
    print("-------------------------------------")
    details = input("Do you have a Twitter Account? Say Yes/No- ")
    if (details == 'y') or (details == 'Y') or (details == 'yes') or (details == 'Yes') or (details == 'YES'):
        userid = input("\nEnter your Email/UserID/PhoneNumber: ")
        passkey = input("Enter your Password: ")

        userinput = input("\nWhat are you here for? \n1.Tweet? \n2.Follow? \n3.LikePost? \nChoose between 1, 2 or 3 - ")

        if (userinput == '1'):
            tweet(userid,passkey)

        elif (userinput == '2'):
            follow(userid,passkey)

        elif (userinput == '3'):
            like(userid,passkey)

    else:
        print("Sorry, we cannot proceed further.Please make one and comeback later...")


if __name__ == '__main__':
    main()

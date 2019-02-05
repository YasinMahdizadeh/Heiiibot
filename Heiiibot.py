import requests
import json
import time
#We can use https://api.telegram.org/bot<token>/getme to get Information about our bot_token

#The simplest way for us to retrieve
 #messages sent to our Bot is through the getUpdates call.
 #If you visit https://api.telegram.org/bot<your-bot-token>/getUpdates


#Sending a message through our browser:
#https://api.telegram.org/bot<your-bot-token>/sendMessage?chat_id=<chat-id>&text=TestReply

bot_username = 'heiiibot'
bot_token = '549865845:AAHyaPcpbXy8SG8hoyDCzNucTKRjsaNZa5I'
bot_url='https://api.telegram.org/bot%s/'%(bot_token)
text = "Hello, it's me!"

# and We can also use URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    pasokh = requests.get(url)
    content = pasokh.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads( content )
    return js

def get_updates():
    url = bot_url + 'getupdates'
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates-1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id):
    url = bot_url + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

#this part of code helps us to run this code continusely, instead of one-time
#Running by terminal!

def main():
    last_textchat = (None,None)
    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        if ( (text,chat) != last_textchat ):
            send_message(text, chat)
            last_textchat = (text, chat)
        time.sleep(0.5)

if __name__ == '__main__':
    main()

##but what if two persons send same messages? previous method ignored the second
#one. we use update-id for get_updates() . update-id is incremental and
#we can offset chat-id numbers.

import requests
import json
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

print(get_updates())
text, chat = get_last_chat_id_and_text(get_updates())
send_message(text ,chat)
updates = get_updates()

#print ( updates["result"][0]["message"]["text"])
#and it's how it works...
#Is this the code we really want?

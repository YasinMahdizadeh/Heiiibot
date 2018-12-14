import requests

bot_username = 'heiiibot'
bot_token = '549865845:AAHyaPcpbXy8SG8hoyDCzNucTKRjsaNZa5I'
bot_url='https://api.telegram.org/bot%s/'%(bot_token)

def get_url(url):
    pasokh = requests.get(url)
    content = pasokh.content.decode("utf8")
    return content

print(get_url(bot_url))
#Is this the code we really want?

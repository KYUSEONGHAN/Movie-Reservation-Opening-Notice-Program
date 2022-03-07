import requests

token = 'xoxb-3188275430196-3186016258370-ToG6Nzch4BYVfY0FLZOt8Z7c'

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


import requests

token = 'xoxb-3188275430196-3186016258370-ToG6Nzch4BYVfY0FLZOt8Z7c'

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)

def slack_message(imax_movie):
    if imax_movie:
        post_message(token, "#test-slackbot", '오늘 용산아이파크몰에서 ' + imax_movie + ' IMAX 영화가 상영중입니다.')
    else:
        post_message(token, "#test-slackbot", '오늘 용산아이파크몰에서 개봉된 IMAX 영화가 없습니다.')


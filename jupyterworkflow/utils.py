from slackclient import SlackClient
def slack_message(message, channel):
    token = 'xoxp-460216232545-461071818149-479586737393-48a351b055e1f1704759ef11fccb0843'
    sc = SlackClient(token)
    sc.api_call('chat.postMessage', channel=channel, 
                text=message, username='reeves.skr',
                icon_emoji=':robot_face:')


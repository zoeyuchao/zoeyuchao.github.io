from knockknock import slack_sender

webhook_url = "https://hooks.slack.com/services/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"
@slack_sender(webhook_url=webhook_url, channel="train", user_mentions=["zoeyuchao"])
def train_your_nicest_model(your_nicest_parameters):
    import time
    time.sleep(10)
    
train_your_nicest_model(1)
import tweepy
import pandas as pd
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


#twitterAPIキーを変数に格納


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

user = input("「@ユーザー名」を入力してください：")


followers_ids = tweepy.Cursor(api.followers_ids, id=user, cursor=-1).items()
followerDatas = []
for i, follower_id in enumerate(followers_ids):
    try:
        followerData = {}
        data = api.get_user(follower_id)
        followerData["Name"] = data.name
        followerData["User_id"] = data.screen_name
        followerData["Location"] = data.location
        followerData["URL"] = data.url
        followerData["Follow"] = data.friends_count
        followerData["Follower"] = data.followers_count
        followerData["Description"] = data.description
        followerData["TweetCount"] = data.statuses_count
        followerDatas.append(followerData)
        print(followerData)
        print("count:{}".format(i))
    except tweepy.error.TweepError as e:
        print(e.reason)

pd.set_option("display.max_rows", 1000)
df = pd.DataFrame(followerDatas).loc[:,["Name", "User_id", "URL", "Location","Follow","Follower","TweetCount","Description"]]
#ファイル出力
fileName = input("ファイル名を入力してください：")
df.to_csv(fileName + ".csv")
print("「" + fileName + ".csv」が作成されました。")
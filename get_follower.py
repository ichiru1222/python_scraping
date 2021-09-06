import tweepy
import pandas as pd


#twitterAPIキーを変数に格納

CONSUMER_KEY = "JT8o3rAcei23i2hG6dxO0kvp2"
CONSUMER_SECRET = "K94J7yBVLs035dzyHmwAM1KgJH5xirnyYAw3bRSEdEsxGhFlYZ"
ACCESS_TOKEN = "1184567569501417472-AOwX12VyQm7PV2ywvqZqg5XfLJRYwE"
ACCESS_TOKEN_SECRET = "si049Pv9RaExk3yEN61t0vJ0pAgO2BeNuFBtGRHru9GLi"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

user = input("「@ユーザー名」を入力してください：")
followerIDs = api.followers_ids(user)

followerDatas = []
for followerID in followerIDs:
    followerData = {}
    data = api.get_user(followerID)
    followerData["Name"] = data.name
    followerData["Follow"] = data.friends_count
    followerData["Follower"] = data.followers_count
    followerData["Description"] = data.description
    followerData["TweetCount"] = data.statuses_count
    followerDatas.append(followerData)

pd.set_option("display.max_rows", 1000)
df = pd.DataFrame(followerDatas).loc[:,["Name","Follow","Follower","TweetCount","Description"]]

#ファイル出力
fileName = input("ファイル名を入力してください：")
df.to_csv(fileName + ".csv")
print("「" + fileName + ".csv」が作成されました。")
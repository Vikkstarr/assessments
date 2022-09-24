import praw


reddit = praw.Reddit(client_id = '0asy_quJtmUHS4DpFVvE5w',
client_secret = 'zewElyTRaMxm_DQGxapXHa8bPU-hoQ',
user_agent = 'Main_Test',)

#subred = reddit.subreddit('Python')
#print(dir(subred))


data = open("datafile.txt", "a")


for submission in reddit.subreddit("wallstreetbets").new(limit = 5):
    data.write("Title of Article: " + submission.title)
    #print(submission.title)

data.close()


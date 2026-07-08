FOLLOWING, TWEETS = "following", "tweets"
class Twitter:
    

    def __init__(self):
        self.users = dict() # following (list), tweets (list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {
                FOLLOWING: {userId},
                TWEETS: [],
            }
        self.users[userId][TWEETS].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users: return []
        tweets = []
        for user in self.users[userId][FOLLOWING]:
            tweets = tweets + self.users[user][TWEETS]
        tweets.sort(reverse = True, key = lambda x:x[0])
        tweets = [x for _,x in tweets]
        return tweets[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users:
            self.users[followeeId] = {
                FOLLOWING: {followeeId},
                TWEETS: [],
            }
        if followerId not in self.users:
            self.users[followerId] = {
                FOLLOWING: {followerId},
                TWEETS: [],
            }
        self.users[followerId][FOLLOWING].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId in self.users:
            if followeeId in self.users[followerId][FOLLOWING]:
                self.users[followerId][FOLLOWING].remove(followeeId)
        

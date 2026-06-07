class Twitter:

    def __init__(self):
        self.following=[set() for _ in range(101)]
        self.tweets=[set() for _ in range(101)]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].add(tweetId)     
        print(userId, " Tweeted Id: ", tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        # ✅ Convert set to list
        res = []
        for i in self.following[userId]:
            res.extend(self.tweets[i])
        res.extend(list(self.tweets[userId]))
        
        print("User ", userId, "'s feed: ", res)
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        self.following[followerId].add(followeeId)
        print(followerId, " Started Following ", followeeId, " now following: ", self.following[followerId])

    def unfollow(self, followerId: int, followeeId: int) -> None:  
        if followerId==followeeId:
            return   
        self.following[followerId].remove(followeeId)
        print(followerId, " Unfollowed ", followeeId, " now following: ", self.following[followerId])
class Twitter:

    def __init__(self):
        self.following=[set() for _ in range(101)]
        self.all_tweets=[]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.all_tweets.append([tweetId,userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        relavant=self.following[userId]
        relavant.add(userId)
        res=[]
        count=0
        for i in self.all_tweets[::-1]:
            if i[1] in relavant:
                res.append(i[0])
                count+=1
                if count==10:
                    break
        return (res)
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:  
        if followerId==followeeId:
            return   
        self.following[followerId].discard(followeeId)
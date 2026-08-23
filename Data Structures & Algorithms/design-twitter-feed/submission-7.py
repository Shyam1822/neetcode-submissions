class Twitter:
    # 23/8/26
    #GPT altered time based answer

    def __init__(self):
        self.followers = {}
        self.posts = {}
        self.newsFeed = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        # Increase global timestamp
        self.time += 1

        # Store (-time, tweetId)
        # Negative time => most recent tweet is at heap root
        current_posts = self.posts.get(userId, [])
        heapq.heappush(current_posts, (-self.time, tweetId))
        self.posts[userId] = current_posts

        # Update user's own feed + followers' feeds
        followers = self.followers.get(userId, [])
        f_plus_self = followers + [userId]

        for f_id in f_plus_self:
            cur_feed = self.newsFeed.get(f_id, [])
            heapq.heappush(cur_feed, (-self.time, tweetId))
            self.newsFeed[f_id] = cur_feed

    def getNewsFeed(self, userId: int) -> List[int]:

        cur_feed = self.newsFeed.get(userId, []).copy()

        result = []

        for _ in range(min(10, len(cur_feed))):
            time, tweetId = heapq.heappop(cur_feed)
            result.append(tweetId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:

        cur_followers = self.followers.get(followeeId, [])

        # Already following
        if followerId in cur_followers:
            return

        if cur_followers:
            self.followers[followeeId].append(followerId)
        else:
            self.followers[followeeId] = [followerId]

        # Add followee's existing tweets to follower's feed
        new_followee_posts = self.posts.get(followeeId, [])
        self_feed = self.newsFeed.get(followerId, [])

        for tweet in new_followee_posts:
            heapq.heappush(self_feed, tweet)

        self.newsFeed[followerId] = self_feed

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId not in self.followers:
            return

        if followerId not in self.followers[followeeId]:
            return

        self.followers[followeeId].remove(followerId)

        # Remove followee's tweets from follower's feed
        followers_posts = self.posts.get(followeeId, [])
        followees_newsFeed = self.newsFeed.get(followerId, [])

        for tweet in followers_posts:
            if tweet in followees_newsFeed:
                followees_newsFeed.remove(tweet)

        heapq.heapify(followees_newsFeed)
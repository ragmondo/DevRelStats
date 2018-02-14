import twitter
from parent import DevRelStats
from secrets import Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret

class TwitterStats(DevRelStats):
    def run(self):
        try:
            from twitter import Api
        except ImportError as ie:
            raise ie

        d = dict()

        api = Api(Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret)

        cdlt = api.UsersLookup(screen_name=["CordaDLT"])[0]
        corda_followers = api.GetFollowers(user_id = cdlt)

        d["twitter_followers"] = len(corda_followers)

        usertimeline = [x for x in api.GetUserTimeline(count=100) if x.retweeted == False]

        total_faves = 0
        total_retweets = 0

        for x in usertimeline[0:10]:
            #print x
         #   print x.text, x.favorite_count, x.retweet_count
            total_faves += x.favorite_count
            total_retweets += x.retweet_count

     #   print "In last 10 tweets"
     #   print total_faves, "faves", total_retweets, "retweets"

        d["twitter_running_10_average_faves"] = total_faves / 10.0
        d["twitter_running_10_retweets"] = total_retweets / 10.0

        return d


if __name__ == "__main__":
    ts = TwitterStats()
    print ts.run()



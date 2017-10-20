import secrets
from parent import DevRelStats



class VimeoStats(DevRelStats):
    def run(self):
        try:
            import vimeo
        except ImportError as ie:
            raise ie

        v = vimeo.VimeoClient(
            token=secrets.YOUR_ACCESS_TOKEN,
            key=secrets.YOUR_CLIENT_ID,
            secret=secrets.YOUR_CLIENT_SECRET)

        total_plays = 0
        per_page = 10
        next = '/me/videos?per_page='+str(per_page) +'&fields=name,stats'
        while(next):
            videos = v.get(next)
            for vid in videos.json()['data']:
            #    print vid['name'],":", vid['stats']['plays']
                total_plays = total_plays + vid['stats']['plays']
            next = videos.json()['paging']['next']


        return {"vimeo_total_plays": total_plays}
        #print "----"
    #    print "Total plays:", total_plays



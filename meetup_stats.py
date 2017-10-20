# pip install meetup-api

import secrets
import meetup.api
client = meetup.api.Client(secrets.MEETUP_API_KEY)

corda_groups =  """
Frankfurt-Corda-Meetup
London-Corda-Meetup
Taipei-Corda-Meetup
Sydney-Corda-Meetup
Tokyo-Corda-Meetup
Seoul-Corda-Meetup
Shanghai-Corda-Meetup
Toronto-Corda-Meetup
R3-Corda-Hong-Kong-Meetup
meetup-group-idbpbQbt
New-York-Corda-Meetup
Hong-Kong-Corda-Meetup
Corda-Blockchain-DistributedLedger-Meetup
meetup-group-vZKHkgqV
""".lstrip().rstrip().split('\n')


# pip install meetup-api

from parent import DevRelStats
import secrets


class MeetupStats(DevRelStats):
    def run(self):
        try:
            import meetup.api
        except ImportError as ie:
            raise ie

        client = meetup.api.Client(secrets.MEETUP_API_KEY)

        total = 0

        for g in corda_groups:
            group = client.GetGroup({'urlname':g})
            #            print group.name, group.members
            total = total + group.members

        return {"meetup_total_members": total}

#grps = client.FindGroups({'text':'corda'})


if __name__ == "__main__":
    print MeetupStats().run()


#    total = 0

#    for g in corda_groups:
#        group = client.GetGroup({'urlname':g})
#        print group.name, group.members
#        total = total + group.members

 #   print "------"
 #   print "Meetup Members:", total

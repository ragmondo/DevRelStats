# pip install meetup-api

import secrets
import meetup.api
client = meetup.api.Client(secrets.MEETUP_API_KEY)

corda_groups =  """
London-Corda-Meetup
Frankfurt-Corda-Meetup
Seoul-Corda-Meetup
Shanghai-Corda-Meetup
Hong-Kong-Corda-Meetup
Taipei-Corda-Meetup
Tokyo-Corda-Meetup
Singapore-Corda-Meetup
Sydney-Corda-Meetup
Beijing-Corda-Meetup
meetup-group-idbpbQbt
CORDA-Meetup-Italy
New-York-Corda-Meetup
Dallas-Fort-Worth-Corda-Meetup
CORDA-Meetup-Poland
Unofficial-London-Corda-Meetup
Corda-Ledger-Toronto
Blockchain-Ethereum-Corda-ledger-meetup-Hyderabad
Ethereum-Cordaledger-meetup
meetup-group-vZKHkgqV
Blockchain-Ethereum-Corda-ledger-meetup-Delhi-NCR
Bangalore-Ethereum-Blockchain-Meetup
""".lstrip().rstrip().split('\n')

from parent import DevRelStats
import secrets

class MeetupStats(DevRelStats):
    def run(self):
        try:
            import meetup.api
        except ImportError as ie:
            print "-->  pip install meetup-api <--"
            raise ie

        client = meetup.api.Client(secrets.MEETUP_API_KEY)

        total = 0

        for g in corda_groups:
            group = client.GetGroup({'urlname':g})
            #            print group.name, group.members
            total = total + group.members

        return {"meetup_total_members": total}

if __name__ == "__main__":
    print MeetupStats().run()


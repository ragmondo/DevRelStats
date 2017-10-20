from parent import DevRelStats
import secrets

class SlackStats(DevRelStats):
    def run(self):
        try:
            from slackclient import SlackClient
        except ImportError as ie:
            raise ie

        sc = SlackClient(secrets.SLACK_TOKEN)
        users = len(sc.api_call("users.list")["members"])
        return {"slack_number_of_users": users}


if __name__ == "__main__":
    print SlackStats().run()
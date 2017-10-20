
import secrets
from parent import DevRelStats

class DiscourseStats(DevRelStats):
    def __init__(self):
        pass

    def run(self):
        try:
            from pydiscourse import DiscourseClient
        except ImportError as ie:
            print "--> pip install pydiscourse <--"
            raise  ie
        client = DiscourseClient(
            'https://discourse.corda.net',
            api_username='richg',
            api_key=secrets.DISCOURSE_API_KEY)


        def old_way():
            usernames = set()
            more = "/directory_items?period=all"
            while(more):
                stuff = client._get(more)

                for di in stuff["directory_items"]:
                    usernames.add(di["user"]["username"])
                if len(stuff["directory_items"]) and "load_more_directory_items" in stuff:
                    more = stuff["load_more_directory_items"]
                else:
                    more = None


        def get_number_of_posts(client):
            categories = {x['id']:x['post_count'] for x in client._get("/categories")["category_list"]["categories"]}
            return sum(categories.values())

        def get_number_of_users(client):
            stuff = client._get( "/directory_items?period=all")
            return stuff["total_rows_directory_items"]

        return {"discourse_user_count": get_number_of_users(client),
                "discourse_number_of_posts": get_number_of_posts(client)}


if __name__ == "__main__":
    print DiscourseStats().run()
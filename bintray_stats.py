import os

import datetime
import requests
import json

# marginally inspired by https://github.com/Gohla/bintraypy/blob/master/bintraypy/bintray.py

class Bintray(object):
#    default_url = "https://bintray.com/api/v1"
    default_url = "https://api.bintray.com"
    jd = json.JSONDecoder()


    def __init__(self, username=None, key=None, url=default_url):
        self.username = username
        self.key = key
        self.url = url



    def repos(self, subject, repo = None, start_pos = None, start_name = None):
        path = 'repos/{}'.format(subject)
        parameters = {}
        if repo:
            path = path + "/{}".format(repo)
            if start_pos != None: # 0 for start
                path = path + "/packages"
                if start_pos:
                    parameters["start_pos"] = start_pos
                if start_name:
                    parameters["start_name"] = start_name

        response = self._create_request('get', path, params = parameters)
        return response

    def package(self, subject, repo, package, version = None, date_from = None, date_to = None, parameters = {}):
        path  = 'packages/{}/{}/{}'.format(subject, repo, package)
        if version:
            parameters = {
                "from": "\"ISO8601 ({})\"".format(date_from.isoformat()),
                "to": "\"ISO8601 ({})\"".format(date_to.isoformat())
            }
            path = path + "/versions/{}/stats/total_downloads".format(version)
            return self._create_request('post', path, params = parameters)
        else:
            return self._create_request('get', path, params = parameters)


    def _create_request(self, method, path, **kwargs):
        url = '{}/{}'.format(self.url, path)
        if self.username and self.key:
            return requests.request(method, url, auth=(self.username, self.key), **kwargs)
        else:
            return requests.request(method, url, **kwargs)

    def out(self, x):
        print x.json()
#        print json.dumps( x.text.encode('ascii'), indent=2, sort_keys=True )


if __name__ == "__main__":
    bt = Bintray("roger3cev@r3","5ad2ad9eb088772f57afffd87b17383bf3cfd860")

   # b.out(b.repos("r3"))
  #  b.out(b.repos("r3","corda"))
#    b.out(b.repos("r3","corda",0))

#    packages = b.repos("r3","corda",0)
 #   corda_packages = [x for x in packages if "corda" in x["name"]]\

    corda_core = bt.package("r3","corda","corda-core").json()

    xyz = 123

    # get the version for corda-code

    d_from = datetime.date(1970,1,1)
    d_to = datetime.date.today()

    print d_from.isoformat()
    print d_to.isoformat()

    print d_from

    versions = corda_core["versions"]
    for v in versions:
        q = bt.package("r3","corda","corda-core",requests.utils.quote(v, safe = ""), d_from, d_to)
        bt.out(q)




    # get the total stats for each one from t0 to "today"


# https://bintray.com/api/v1/packages/r3/corda/corda-core




# https://api.bintray.com/repos/r3/corda


# POST /packages/:subject/:repo/:package/versions/:version/stats/total_downloads
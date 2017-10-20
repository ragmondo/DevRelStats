from parent import DevRelStats

class GithubStats(DevRelStats):
    def run(self):
        try:
            from github3 import GitHub
        except ImportError as ie:
            raise ie

        gh = GitHub()
        corda = gh.repository("corda","corda")

        return({"github_forks":corda.fork_count, "github_stars":corda.stargazers})




from parent import DevRelStats


class StackoverflowStats(DevRelStats):
    def run(self):
        try:
            import stackexchange
        except ImportError as ie:
            raise ie
        so = stackexchange.Site(stackexchange.StackOverflow)
        corda = so.tag("corda")
        return {"stackoverflow_corda_questions": corda.count}


if __name__ == "__main__":
    print StackoverflowStats().run()
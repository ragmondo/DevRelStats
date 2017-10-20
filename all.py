from discourse_stats import DiscourseStats
from github_stats import GithubStats
from meetup_stats import MeetupStats
from stackoverflow_stats import StackoverflowStats
from vimeo_stats import VimeoStats
from slack_stats import SlackStats

import datetime

import pyodbc



if __name__ == "__main__":
    stats = [
        DiscourseStats(),
        StackoverflowStats(),
        VimeoStats(),
        MeetupStats(),
        GithubStats(),
        SlackStats()
    ]

    all_stats = {"date": datetime.date.today()}

    for stat in stats:
        try:

            all_stats.update(stat.run())
        except Exception as e:
            print "Something went wrong for ", stat
            print e

    print all_stats


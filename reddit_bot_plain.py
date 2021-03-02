#!/usr/bin/python
import praw
import json


# Enter your correct Reddit information into the variable below
config_file = open("config.json")
config = json.load(config_file)
userAgent = config["userAgent"]
personal_use_script = config["personal_use_script"]
secret = config["secret"]
username = config["username"]
password = config["password"]


def is_question(str):
    return str[-1] == '?'


def document_hit(submission, comment):
    print("Found question in comment: " + comment)
    print("Title: ", submission.title)
    print("Score: ", submission.score)
    print("———————————")


def main():
    reddit = praw.Reddit(user_agent=userAgent, client_id=personal_use_script, client_secret=secret, username=username,
                         password=password)

    for submission in reddit.subreddit("all").top(time_filter="week"):
        for comment in submission.comments:
            if is_question(comment):
                document_hit(submission, comment)
                comment.reply(
                    "Information relating to your question [here](https://rickrolled.com/ \"" + comment + "\")")
                return True
    print("No questions found this week :(")
    return False


if __name__ == "__main__":
    main()

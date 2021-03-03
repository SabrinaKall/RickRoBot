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


def document_hit(submission, comment, question):
    print("Found question in comment: " + question)
    print("Comment: ", comment)
    print("Post Title: ", submission.title)
    print("Post Score: ", submission.score)
    print("Post channel: ", submission.subreddit)
    print("———————————")


def format_question(comment):
    one_liner = comment.replace('\n', '')
    if '.' in one_liner:
        return one_liner.rsplit('.')[1]
    else:
        return one_liner


def main():
    reddit = praw.Reddit(user_agent=userAgent, client_id=personal_use_script, client_secret=secret, username=username,
                         password=password)

    for submission in reddit.subreddit("all").top(time_filter="day"):
        for comment in submission.comments:
            comment_text = comment.body
            if is_question(comment_text):
                question = format_question(comment_text)
                document_hit(submission, comment_text, question)
                comment.reply(
                    "Information relating to the question in your comment [here](https://www.youtube.com/watch?v=oHg5SJYRHA0 \"" + question + "\")")
                return True
    print("No questions found this week :(")
    return False


if __name__ == "__main__":
    main()

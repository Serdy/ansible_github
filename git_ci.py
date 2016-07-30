#!/usr/bin/python

from pygithub3 import Github
import param


def initConnection():
    gh = Github(login=param.user_name, password=param.password, repo=param.repo, user=param.owner_rep)
    return gh

def get_lables_from_issuse():
    gh = initConnection()
    lables_from_issuse = gh.issues.labels.list_by_issue(number=param.pull_req)
    return lables_from_issuse


def pull_requests_mergeable():
    gh = initConnection()
    pr = gh.pull_requests.get(number=param.pull_req)
    return pr.mergeable

def pull_requests_add_lable():
    gh = initConnection()
    lables_from_issuse = gh.issues.labels.add_to_issue(number=param.pull_req, labels=param.add_labla)


gh = Github(login=param.user_name, password=param.password, repo=param.repo, user=param.owner_rep)
pr = gh.pull_requests.get(number=param.pull_req)
print pr.mergeable
print dir(pr)

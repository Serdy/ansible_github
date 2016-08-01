#!/usr/bin/python


import param

from github3 import GitHub
import json


def initConnection():
    gh = GitHub(param.user_name, param.password)
    return gh


def get_issuse():
    get_issuse = initConnection().issue(username=param.owner_rep, repository=param.repo, number=param.pull_req)
    return get_issuse


def get_issuse_labels():
    get_issuse_labels = get_issuse().labels
    list_get_issuse_labels = []
    for label in get_issuse_labels():
        list_get_issuse_labels.append(str(label))
    print json.dumps({'labels': (list_get_issuse_labels)})


def add_issuse_lable(labels):
    issuse = get_issuse()
    if isinstance(labels, list):
        for label in labels:
            issuse.add_labels(label)
    elif isinstance(labels, str):
        issuse.add_labels(labels)
    get_issuse_labels()


def remove_issuse_lable(labels):
    issuse = get_issuse()
    if isinstance(labels, list):
        for label in labels:
            issuse.remove_label(label)
    elif isinstance(labels, str):
        issuse.remove_label(labels)
    get_issuse_labels()


def get_pull_requests():
    get_pull_requests = initConnection().pull_request(number=param.pull_req, owner=param.owner_rep,
                                                      repository=param.repo)
    return get_pull_requests


def check_pull_requests_mergeable():
    check_pull_requests_mergeable = get_pull_requests().mergeable
    return check_pull_requests_mergeable

def pull_requests_merge():
    check_pull_requests_mergeable = get_pull_requests().mergeable
    return check_pull_requests_mergeable

def create_comment_issuse(comment):
    issuse = get_issuse()
    issuse.create_comment(comment)



get_issuse_labels()
add_issuse_lable(labels=['invalid', 'bug'])
remove_issuse_lable(labels=['invalid', 'bug'])
print get_pull_requests().title
print check_pull_requests_mergeable()
# print pull_requests_merge()
# print create_comment_issuse('test comment')

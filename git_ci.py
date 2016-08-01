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
    # print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    # print json.dumps([{'inst_id': (get_issuse_labels())}])
    list_get_issuse_labels = []
    # print type(get_issuse_labels())

    for label in get_issuse_labels():
        list_get_issuse_labels.append(str(label))
    print json.dumps({'labels': (list_get_issuse_labels)})





# get_issuse = g.issue(username=param.owner_rep,repository=param.repo,number=param.pull_req)
# print dir(get_issuse)
# print get_issuse_labels()
# for v in get_issuse_labels():
#     print v
get_issuse_labels()
# get_issuse.add_labels('bug')
# get_issuse.remove_label('need CI tests')
# print get_issuse.labels

# Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print repo.name



# def initConnection():
#     gh = Github(login=param.user_name, password=param.password, repo=param.repo, user=param.owner_rep)
#     return gh
#
# def get_lables_from_issuse():
#     gh = initConnection()
#     lables_from_issuse = gh.issues.labels.list_by_issue(number=param.pull_req)
#     return lables_from_issuse
#
#
# def pull_requests_mergeable():
#     gh = initConnection()
#     pr = gh.pull_requests.get(number=param.pull_req)
#     return pr.mergeable
#
# def pull_requests_add_lable():
#     gh = initConnection()
#     lables_from_issuse = gh.issues.labels.add_to_issue(number=param.pull_req, labels=param.add_labla)
#
#
# gh = Github(login=param.user_name, password=param.password, repo=param.repo, user=param.owner_rep)
# pr = gh.pull_requests.get(number=param.pull_req)
# print pr.mergeable
# print dir(pr)
# # gh.issues.labels.add_to_issue(number=param.pull_req, labels1='bug', labels2='invalid', user=param.user_name,repo=param.repo)
# gh.issues.labels.add_to_issue(4, repo=param.repo, user=param.owner_rep, labels=('bug'))
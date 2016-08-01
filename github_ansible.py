#!/usr/bin/python

import json


try:
    from github3 import GitHub
except ImportError:
    print "failed=True msg='github3 required for this module pip install --pre github3.py'"
    sys.exit(1)


def get_issuse(**kwargs):
    for key in kwargs:
        if key == 'organization' and kwargs[key] is not None:
            get_issuse = GitHub(kwargs['user'], kwargs['password']).issue(username=kwargs['organization'], repository=kwargs['repository'], number=kwargs['pull_requests'])
            return get_issuse
        else:
            get_issuse = GitHub(kwargs['user'], kwargs['password']).issue(repository=kwargs['repository'], number=kwargs['pull_requests'], username=kwargs['user'])
            return get_issuse


def get_issuse_labels(get_issuse):
    print get_issuse.title
    issuse_labels = get_issuse.labels
    print(issuse_labels())
    list_get_issuse_labels = []
    for label in issuse_labels():
        list_get_issuse_labels.append(str(label))
    print json.dumps({
        'labels': (list_get_issuse_labels),
        "changed": True
    })


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
    get_pull_requests = initConnection().pull_request(number=pull_requests, owner=organization,
                                                      repository=repository)
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




def main():
    module = AnsibleModule(
        argument_spec=dict(
            repository=dict(required=True),
            user=dict(required=True),
            password=dict(required=True),
            organization=dict(),
            pull_requests=dict(required=True),
            labels=dict(),
            comment=dict(),
            state=dict(choices=['labels', 'add_labels', 'remove_labels', 'add_comment', 'merge', 'check_merge'], default='labels'),
        )
    )

    repository = module.params.get('repository')
    user = module.params.get('user')
    password = module.params.get('password')
    organization = module.params.get('organization')
    pull_requests = module.params.get('pull_requests')
    labels = module.params.get('labels')
    comment = module.params.get('comment')
    state = module.params.get('state')

    if state == 'labels':
        if organization:
            issuse = get_issuse(user=user, password=password, repository=repository, pull_requests=pull_requests, organization=organization)
            get_issuse_labels(get_issuse=issuse)
        else:
            issuse = get_issuse(user=user, password=password, repository=repository, pull_requests=pull_requests)
            get_issuse_labels(get_issuse=issuse)


    sys.exit(0)





from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

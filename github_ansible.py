#!/usr/bin/python

import json
# import param

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
    issuse_labels = get_issuse.labels
    list_get_issuse_labels = []
    for label in issuse_labels():
        list_get_issuse_labels.append(str(label))
    print json.dumps({
        'labels': (list_get_issuse_labels)
    })


def add_issuse_lables(get_issuse, add_labels):
    count_labels_before = len(list(get_issuse.labels()))
    if isinstance(add_labels, list):
        for label in add_labels:
            result = get_issuse.add_labels(label)
    else:
        module.fail_json(
            msg="Enter name correct label ")
    count_labels_after = len(result)
    list_get_issuse_labels = []
    if count_labels_before != count_labels_after:
        for label in result:
            list_get_issuse_labels.append(str(label))
        print json.dumps({
            'labels': (list_get_issuse_labels),
            "changed": True
        })
    else:
        for label in result:
            list_get_issuse_labels.append(str(label))
        print json.dumps({
            'labels': (list_get_issuse_labels)
        })


def remove_issuse_labels(get_issuse, remove_labels):
    count_labels_before = len(list(get_issuse.labels()))
    if isinstance(remove_labels, list):
        result = []
        for label in remove_labels:
            count = get_issuse.remove_label(label)
            result.append(count)
    else:
        module.fail_json(
            msg="Enter name correct label ")
    result = get_issuse.labels()
    count_labels_after = len(list(result))
    list_get_issuse_labels = []
    if count_labels_before != count_labels_after:
        for label in result:
            list_get_issuse_labels.append(str(label))
        print json.dumps({
            'labels': (list_get_issuse_labels),
            "changed": True
        })
    else:
        for label in result:
            list_get_issuse_labels.append(str(label))
        print json.dumps({
            'labels': (list_get_issuse_labels)
        })


def create_comment_issuse(get_issuse, comment):
    issuse = get_issuse
    issuse.create_comment(comment)
    print json.dumps({
        'comment': (comment),
        "changed": True
    })


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




def main():
    module = AnsibleModule(
        argument_spec=dict(
            repository=dict(required=True),
            user=dict(required=True),
            password=dict(required=True),
            organization=dict(),
            pull_requests=dict(required=True),
            labels=dict(type='list'),
            comment=dict(),
            state=dict(choices=['labels', 'add_label', 'remove_labels', 'add_comment', 'merge', 'check_merge'], default='labels'),
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

    elif state == 'add_label':
        if not labels:
            module.fail_json(
                msg="Enter name labels to add, example: labels=bug")

        issuse = get_issuse(user=user, password=password, repository=repository, pull_requests=pull_requests,
                            organization=organization)

        add_issuse_lables(get_issuse=issuse, add_labels=labels)


    elif state == 'remove_labels':

        if not labels:
            module.fail_json(
                msg="Enter name labels to add, example: labels=bug")

        issuse = get_issuse(user=user, password=password, repository=repository, pull_requests=pull_requests,
                            organization=organization)

        remove_issuse_labels(get_issuse=issuse, remove_labels=labels)
    elif state == 'add_comment':
        if not comment:
            module.fail_json(
                msg="Enter  comment  example: comment=bla bla bla")

        issuse = get_issuse(user=user, password=password, repository=repository, pull_requests=pull_requests,
                            organization=organization)

        create_comment_issuse(get_issuse=issuse, comment=comment)


    sys.exit(0)

# module.exit_json(changed=True, something_else=label)



from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

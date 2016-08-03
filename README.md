module: gh_pr
short_description: manage
objects in gh_pull_requests.
description:
-   This module allows the user to manage GitHub Pull Requests(PR) and Issues.
    Includes support for creating and removing labels, check mergeable for PR, merge PR.
    This module has a dependency on github3.


options:
    user:
    description:
    - User
    name
    for GitHub
        required: true
    default: null

    password:
    description:
    Secret
    password
    for GitHub.
        required: true
        default: null

    pull_requests:
    description:
    -   Number of PR or issues.
    required: true
    default: null

    repository:
    description:
    -   Name of GitHub repository
        required: false
    organization:
    description:
    -   For private repository need name organization
        required: false
    default: no

    state:
    description:
    -   If C(labels), Show all labels form PR or issues.
        If C(add_labels) Add labels to PR or issues. Depends on “labels“.
        If C(remove_labels) Remove  labels to PR or issues. Depends on “labels“.
        If C(add_comment)  Add comment to PR or issues. Depends on “comment“.
        If C(check_merge) Check PR on mergeable. Return True or False.
        If C(merge) Merge PR.
    required: false
    default: file
    choices: [labels, add_labels, remove_labels, add_comment, check_merge, merge]

    labels:
    description:
    -   Name of labels.Must be a list.
    required: false

    comment:
    description:
    - Add comment to PR, issues or merge
    required: false
    default: null

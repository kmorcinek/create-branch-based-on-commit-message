# inspired by https://github.com/marcinlisek/python-tasks/blob/main/branch-name-based-on-commit-name/parsing.py
import sys

argv = sys.argv[1:]


def parsing(commit):
    commit = commit \
        .replace("/", "")

    if commit.find(": #") > -1:
        step1 = commit \
            .replace(": #", "/")

        space_pos = step1.find(" ")

        step2 = step1[:space_pos] + "/" + step1[space_pos + 1:].lower()

    elif commit.find(":") > -1:
        step2 = commit \
            .replace(": ", "/") \
            .lower()

    else:
        step2 = commit \
            .lower()

    step3 = step2.replace(" ", "-")

    unwanted_chars = [
        '#',
        '.',
        '`',
        '*',
        '?',
        '[',
        ']',
        ',',
        '"',
        '\'',
        '(',
        '<',
        '>',
        ';',
        '{',
        '}',
        ':',
        '“',
        '”',
        ')'
    ]
    for c in unwanted_chars:
        step3 = step3.replace(c, "")

    step3 = step3.lstrip('-')

    return step3


assert parsing("feat: #OLDM-324 create product endpoint") == "feat/OLDM-324/create-product-endpoint"
assert parsing("fix: fix email") == "fix/fix-email"
assert parsing("add new TODO") == "add-new-todo"
assert parsing("add *new `TODO` (encapsulate?) 'later'.") == "add-new-todo-encapsulate-later"
assert parsing("[product] #OLDM-324 create product endpoint") == "product-oldm-324-create-product-endpoint"
# assert parsing("fix: #WW-11 improve error handling") == "fix/WW-11/wrong-branch"

# https://github.com/kmorcinek/create-branch-based-on-commit-message/issues/1
assert parsing("-- copy market to prod") == "copy-market-to-prod"

result = parsing(argv[0])

sys.stdout.write(result)

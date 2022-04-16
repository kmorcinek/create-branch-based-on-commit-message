import sys

argv = sys.argv[1:]

# print(argv)


def parsing(commit):
    step3 = ""
    if commit.find(": #") > -1:
        step1 = commit \
            .replace("/", "") \
            .replace(": #", "/")

        space_pos = step1.find(" ")

        step2 = step1[:space_pos] + "/" + step1[space_pos + 1:].lower()

        step3 = step2.replace(" ", "-")
    elif commit.find(":") > -1:
        step1 = commit \
            .replace("/", "") \
            .replace(": ", "/")

        step3 = step1.replace(" ", "-").lower()
    else:
        step1 = commit \
            .replace("/", "") \
            .replace(": ", "/")

        step3 = step1.replace(" ", "-").lower()

    return step3 \
        .replace("`", "") \
        .replace("*", "") \
        .replace("?", "") \
        .replace("[", "") \
        .replace("]", "") \
        .replace(",", "") \
        .replace('"', "") \
        .replace("'", "") \
        .replace("(", "") \
        .replace(")", "")


# print("")

# parsing("feat: #OLDM-324 SKLF SKdlfja asldfk")
# parsing("fix: #WW-11 improve error handling")

# print("")

assert parsing("feat: #OLDM-324 SKLF SKdlfja asldfk") == "feat/OLDM-324/sklf-skdlfja-asldfk"
assert parsing("fix: fix email") == "fix/fix-email"
assert parsing("add new TODO") == "add-new-todo"
# assert parsing("fix: #WW-11 improve error handling") == "fix/WW-11/wrong-branch"

result = parsing(argv[0])

import sys
sys.stdout.write(result)

import sys

argv = sys.argv[1:]

# print(argv)


def parsing(commit):
    commit = commit \
        .replace("/", "")

    step3 = ""
    if commit.find(": #") > -1:
        step1 = commit \
            .replace(": #", "/")

        space_pos = step1.find(" ")

        step2 = step1[:space_pos] + "/" + step1[space_pos + 1:].lower()

        step3 = step2.replace(" ", "-")
    elif commit.find(":") > -1:
        step1 = commit \
            .replace(": ", "/")

        step3 = step1.replace(" ", "-").lower()
    else:
        step1 = commit \
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


assert parsing("feat: #OLDM-324 create product endpoint") == "feat/OLDM-324/create-product-endpoint"
assert parsing("fix: fix email") == "fix/fix-email"
assert parsing("add new TODO") == "add-new-todo"
# assert parsing("fix: #WW-11 improve error handling") == "fix/WW-11/wrong-branch"

result = parsing(argv[0])

sys.stdout.write(result)

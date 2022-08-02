def isvalidemail(email):
    pos = email.find("@")
    if pos == -1:
        return False

    return pos > 0 and pos < (len(email) - 1)


# def get_valid_emails(file):
#     return set([e.strip() for e in file.readlines() if isvalidemail(e.strip())])

def get_valid_emails(file):
    emails = set()
    for line in file.readlines():
        sline = line.strip()
        if isvalidemail(sline):
            emails.add(sline)

    return emails


with open("emails.txt", "rt") as f:
    emails = get_valid_emails(f)

with open("new_emails.txt", "rt") as f:
    emails = emails | get_valid_emails(f)

print(emails)

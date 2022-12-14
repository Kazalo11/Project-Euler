logins = []
with open('p079_keylog.txt', 'r') as f:
    for line in f:
        if line.strip() not in logins:
            logins.append(line.strip())

passcode = []

for login in logins:
    if login not in passcode:
        passcode.append(login)

print(passcode)
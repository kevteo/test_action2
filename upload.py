import os

username = 'ai-sdk'
os.system("git config --global user.name " + str(username))
os.system("git config --global user.email " + str(username) + '@users.noreply.github.com')
print('Status:')
print(os.system('git status'))
os.system('git add -A')
print('Status: 2')
print(os.system('git status'))
os.system('git commit -m Produce Merge File')
os.system('git push origin main')

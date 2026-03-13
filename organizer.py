import os
from github import Github

g = Github(os.environ["GH_TOKEN"])
user = g.get_user()

archive_patterns = ["stackblitz","sb1","copy","test","tmp"]
core_keywords = ["template","core"]
client_keywords = ["client","camping","atelier"]

for repo in user.get_repos():

    name = repo.name.lower()

    if repo.archived:
        continue

    if any(p in name for p in archive_patterns):
        repo.edit(archived=True)

    elif any(k in name for k in core_keywords):
        repo.replace_topics(["core"])

    elif any(k in name for k in client_keywords):
        repo.replace_topics(["client"])

    else:
        repo.replace_topics(["experiment"])

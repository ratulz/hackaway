import os
import git

repo = git.Repo(os.getenv('GIT_REPO_PATH'))
print(repo.commit())
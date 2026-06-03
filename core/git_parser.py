from git import Repo

def get_repo_diff(repo_path="."):
    repo = Repo(repo_path)

    # gets last commit changes
    diff = repo.git.diff("HEAD~1")

    return diff[:4000]
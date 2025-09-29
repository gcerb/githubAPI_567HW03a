import requests

def get_repos(user_id):
    """Return a list of repository names for a given GitHub user."""
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return [repo["name"] for repo in response.json()]

def get_commit_count(user_id, repo):
    """Return the number of commits in a given repository."""
    url = f"https://api.github.com/repos/{user_id}/{repo}/commits"
    response = requests.get(url)
    if response.status_code != 200:
        return 0
    return len(response.json())

def get_repos_and_commits(user_id):
    """Return a list of dicts containing repo names and their commit counts."""
    results = []
    repos = get_repos(user_id)
    for repo in repos:
        commits = get_commit_count(user_id, repo)
        results.append({"repo": repo, "commits": commits})
    return results

if __name__ == "__main__":
    user = "richkempinski"  # example user
    for entry in get_repos_and_commits(user):
        print(f"Repo: {entry['repo']} Number of commits: {entry['commits']}")

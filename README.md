# githubAPI_567HW03a

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/gcerb/githubAPI_567HW03a/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/gcerb/githubAPI_567HW03a/tree/main)

## Project Description

This project retrieves GitHub repository names and commit counts for a given user using the GitHub REST API.  
Given a GitHub user ID, the program outputs each repository name along with the number of commits it contains.
Above is the badge from CircleCI.   

The program is implemented in Python 3 and uses the `requests` module to interact with the GitHub API.  

## How It Works

1. `get_repos(user_id)` – Returns a list of repository names for a GitHub user.  
2. `get_commit_count(user_id, repo)` – Returns the number of commits in a given repository.  
3. `get_repos_and_commits(user_id)` – Combines the above to produce a list of dictionaries with repo names and commit counts.  

Unit tests are included in `test_github_api.py`, using `unittest` and `unittest.mock` to mock API calls so tests don’t rely on actual GitHub data.

## Reflection

When designing this program, I focused on making it **easy to test**:

- I separated the functionality into small helper functions (`get_repos`, `get_commit_count`, `get_repos_and_commits`) so each piece could be tested independently.  
- I handled **error cases**:
  - User may not exist → return empty list  
  - Repository may have no commits → return 0  
  - API failures → handled gracefully to prevent crashes  
- **Unit testing** used `unittest.mock` to simulate API responses, avoiding GitHub rate limits and making tests fast and reliable.  
- **Challenges faced**:
  - Ensuring the CI environment installs dependencies correctly (`requests`)  
  - Adapting code to work in both local Windows (`py`) and Linux CI environments (`python`)  

Overall, designing the code with the tester in mind made development and debugging much easier, and allowed the unit tests to cover all key scenarios effectively.

## Usage

To run the program:

```bash
# Run main functions with: (used example user for testing purposes)
py github_api.py

# Run tests with:
py -m unittest test_github_api.py


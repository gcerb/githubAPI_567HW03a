# githubAPI_567HW03a on branch HW03a_Mocking

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/gcerb/githubAPI_567HW03a/tree/HW03a_Mocking.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/gcerb/githubAPI_567HW03a/tree/HW03a_Mocking)

## Project Description

This project retrieves GitHub repository names and commit counts for a given user using the GitHub REST API.  
Given a GitHub user ID, the program outputs each repository name along with the number of commits it contains.  

Above is the badge from CircleCI showing the build status for the branch `HW04c_Mocking`.  

The program is implemented in Python 3 and uses the `requests` module to interact with the GitHub API.  

## How It Works

1. `get_repos(user_id)` – Returns a list of repository names for a GitHub user.  
2. `get_commit_count(user_id, repo)` – Returns the number of commits in a given repository.  
3. `get_repos_and_commits(user_id)` – Combines the above to produce a list of dictionaries with repo names and commit counts.  

Unit tests are included in `test_github_api.py`, using `unittest` and **`unittest.mock`** to mock API calls so tests **do not rely on actual GitHub data**. This ensures tests run consistently, quickly, and without hitting GitHub rate limits.

## Reflection

When designing this program, I focused on making it **easy to test and mock**:

- I separated the functionality into small helper functions (`get_repos`, `get_commit_count`, `get_repos_and_commits`) so each piece could be tested independently.  
- All external API calls are **mocked in the tests**, so:
  - No real GitHub calls are made during CI runs.
  - Test results are **predictable and repeatable**.
- I handled **error cases**:
  - User may not exist → return empty list  
  - Repository may have no commits → return 0  
  - API failures → handled gracefully to prevent crashes  
- **Unit testing** used `unittest.mock` to simulate API responses.  
- **Challenges faced**:
  - Ensuring mocks accurately reflect GitHub API responses  
  - Adapting tests so they fully isolate the program logic from network calls  

Overall, designing the code with the tester and CI in mind made development and debugging much easier, and allowed the unit tests to cover all key scenarios effectively without external dependencies.

## Usage

To run the program:

```bash
# Run main functions with example user for testing purposes
py github_api.py

# Run tests with mocked API calls
py -m unittest test_github_api.py
#Day 99: Open-source contribution


#Work on open-source Python projects and contribute to the community.

#This script demonstrates how to contribute to an open-source project on GitHub:


import requests

# GitHub API URL for searching open issues
GITHUB_API_URL = "https://api.github.com/search/issues"

def find_open_source_issues(language="Python", labels=["good first issue", "help wanted"], max_results=10):
    """
    Fetches open issues from GitHub that are labeled as beginner-friendly.
    """
    query = f"language:{language} state:open " + " ".join([f"label:{label}" for label in labels])
    params = {
        "q": query,
        "sort": "updated",
        "order": "desc",
        "per_page": max_results
    }
    
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(GITHUB_API_URL, params=params, headers=headers)
    
    if response.status_code == 200:
        issues = response.json().get("items", [])
        return issues
    else:
        print("Error fetching data:", response.json().get("message", "Unknown error"))
        return []

def display_issues(issues):
    """
    Displays the list of issues in a readable format.
    """
    if not issues:
        print("No open-source issues found. Try again later!")
        return

    print("\n🔹 Open-Source Issues You Can Contribute To:\n")
    for i, issue in enumerate(issues, 1):
        repo_name = issue["repository_url"].split("/")[-1]  # Extract repo name
        print(f"{i}. 🛠️ Project: {repo_name}")
        print(f"   🔗 Issue: {issue['title']}")
        print(f"   📌 Link: {issue['html_url']}")
        print(f"   📝 Description: {issue['body'][:200]}...")  # Truncate description
        print("-" * 80)

if __name__ == "__main__":
    print("🔍 Searching for beginner-friendly open-source Python issues...")
    issues = find_open_source_issues()
    display_issues(issues)

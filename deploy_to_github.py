"""Deploy QGIS GeoAI Studio to GitHub using API (no git needed)."""
import os, json, base64, sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

REPO_NAME = "qgis-geoai-studio"
REPO_DESC = "QGIS GeoAI Studio - Natural-language remote sensing and SCI figure generation"
SKILL_DIR = r"C:\Users\Administrator\.codex\skills\qgis-geoai-studio"


def api(method, url, data=None):
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        token = input("GitHub PAT (repo scope): ").strip()
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github.v3+json", "User-Agent": "geoai"}
    body = json.dumps(data).encode() if data else None
    if data: headers["Content-Type"] = "application/json"
    try:
        with urlopen(Request(url, body, headers, method=method), timeout=30) as r:
            return json.loads(r.read())
    except HTTPError as e:
        print(f"Error {e.code}: {e.read().decode()[:200]}")
        return None


def main():
    # Get user
    user = api("GET", "https://api.github.com/user")
    if not user:
        print("Auth failed. Set GITHUB_TOKEN env var.")
        return
    uname = user["login"]
    print(f"Authenticated: {uname}")

    # Create or get repo
    repo_url = f"https://api.github.com/repos/{uname}/{REPO_NAME}"
    repo = api("GET", repo_url)
    if not repo:
        repo = api("POST", "https://api.github.com/user/repos",
                  {"name": REPO_NAME, "description": REPO_DESC, "private": False})
        if not repo:
            print("Failed to create repo")
            return
        print(f"Created: {repo['html_url']}")
    else:
        print(f"Exists: {repo['html_url']}")

    # Upload files
    branch = "main"
    for root, dirs, files in os.walk(SKILL_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for fn in files:
            fp = os.path.join(root, fn)
            rel = os.path.relpath(fp, SKILL_DIR).replace("\\", "/")
            with open(fp, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            url = f"https://api.github.com/repos/{uname}/{REPO_NAME}/contents/{rel}"
            existing = api("GET", url + "?ref=" + branch)
            sha = existing["sha"] if existing and "sha" in existing else None
            data = {"message": f"Add {rel}", "content": b64, "branch": branch}
            if sha:
                data["sha"] = sha
                data["message"] = f"Update {rel}"
            result = api("PUT", url, data)
            status = "OK" if result else "FAIL"
            print(f"  [{status}] {rel}")

    print(f"\nDone! https://github.com/{uname}/{REPO_NAME}")


if __name__ == "__main__":
    main()
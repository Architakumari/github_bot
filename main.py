import os
import random
import subprocess
from datetime import datetime, timedelta

# ***** IMPORTANT *****
# Replace this with the SAME email shown in:
# GitHub → Settings → Emails → Verified Emails
GITHUB_NAME = "Archita Kumari"
GITHUB_EMAIL = "jaiswalarchi151105@gmail.com"  # <--- CHANGE THIS

def get_positive_int(prompt, default=20):
    while True:
        try:
            user_input = input(f"{prompt} (default {default}): ")
            if not user_input.strip():
                return default
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def random_date_in_last_year():
    today = datetime.now()
    random_days = random.randint(1, 365)
    random_seconds = random.randint(0, 24*3600-1)
    commit_date = today - timedelta(days=random_days, seconds=random_seconds)
    return commit_date

def make_commit(date, filename="data.txt"):
    # Write a new line to file
    with open(filename, "a") as f:
        f.write(f"Commit at {date.isoformat()}\n")

    subprocess.run(["git", "add", filename])

    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")

    # ------- MAKE COMMITS COUNT ON GITHUB --------
    env["GIT_AUTHOR_NAME"] = GITHUB_NAME
    env["GIT_AUTHOR_EMAIL"] = GITHUB_EMAIL
    env["GIT_COMMITTER_NAME"] = GITHUB_NAME
    env["GIT_COMMITTER_EMAIL"] = GITHUB_EMAIL
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    # --------------------------------------------

    subprocess.run(["git", "commit", "-m", "graph-greener!"], env=env)

def main():
    print("="*60)
    print("🌱 GitHub Graph Greener - Contribution Generator 🌱")
    print("="*60)
    print("This tool will generate commits across the past year.\n")

    num_commits = get_positive_int("How many commits would you like?", 20)
    filename = "data.txt"

    print(f"\n📌 Repo detected: {os.getcwd()}")
    print(f"📝 File being modified: {filename}\n")
    print(f"🔥 Generating {num_commits} commits...\n")

    for i in range(num_commits):
        commit_date = random_date_in_last_year()
        print(f"[{i+1}/{num_commits}] → {commit_date.strftime('%Y-%m-%d %H:%M:%S')}")
        make_commit(commit_date, filename)

    print("\n🚀 Pushing commits to remote repo...")
    subprocess.run(["git", "push"])

    print("\n🎉 Done!")
    print("🟩 Check your GitHub contribution graph in ~2–5 minutes!\n")
    print("✨ Tip: Keep running this script to fully green your graph!")

if __name__ == "__main__":
    main()

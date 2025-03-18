import os
import time

# Change this to the actual path where your repo is cloned
REPO_PATH = r"C:\Users\manoj\OneDrive\Desktop\ok\data-"  

os.chdir(REPO_PATH)  # Navigate to the repo

FILE_NAME = "commits.txt"

for i in range(1, 101):  # Loop for 100 commits
    with open(FILE_NAME, "a") as file:
        file.write(f"Commit number {i}\n")

    os.system("git add .")
    os.system(f'git commit -m "Automated commit #{i}"')
    os.system("git push origin main")

    print(f"✅ Commit #{i} pushed!")
    time.sleep(2)  # Delay to avoid rate limits

print("🎉 100 commits pushed successfully!")

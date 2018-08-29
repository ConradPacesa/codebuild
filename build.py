from github import Github
import git
import os

token = os.environ['TOKEN']

def main():
    g = Github(token)
    
    repo = g.get_repo("ConradPacesa/zip")
    
    git.Git('./repos').clone(repo.ssh_url)
    
    dir = os.listdir("./repos")
    
    print(dir)

if __name__ == "__main__":
    main()

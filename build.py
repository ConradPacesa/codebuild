from github import Github
import git
import os


def lambda_handler(event, context):
    g = Github("")
    
    repo = g.get_repo("ConradPacesa/zip")
    
    git.Git('./repos').clone(repo.ssh_url)
    
    dir = os.listdir("./repos")
    
    print(dir)

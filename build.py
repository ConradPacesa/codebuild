from github import Github
import git
import os

token = os.environ['TOKEN']

NEW_IPS = ["127.0.0.1/32", "0.0.0.0/0", "124.123.0.0/16", "111.111.10.0/12"]

def main():
    g = Github(token)
    gitHubRepo = g.get_repo("ConradPacesa/whitelist")
    # git.Git('./repo').clone(gitHubRepo.ssh_url)

    # repo = git.Repo("./repo/{}".format(gitHubRepo.name))
    # repo.git.checkout('-b', 'new-ips')

    # with open("./repo/{}/whitelist.txt".format(gitHubRepo.name), "w") as f:
    #     for ip in NEW_IPS:
    #         f.write("{}\n".format(ip))

    #     f.close()

    # repo.git.commit("-am", "Updated whitelist IPs")

    # repo.remotes.origin.push(refspec='new-ips:new-ips')

    # params = {
    #     "title": "Update whitelist IPs",
    #     "head": "whitelist:new-ips",
    #     "base": "master"
    # }

    gitHubRepo.create_pull(title='Update whitelist IPs',body='body',head='whitelist:new-ips',base='master')


if __name__ == "__main__":
    main()

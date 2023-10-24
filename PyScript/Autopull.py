import argparse
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git

# ensure current directory
PATH=(os.path.split(os.path.realpath(__file__))[0]).replace('\\',"/")

# pass in the parameter
parser = argparse.ArgumentParser(description='pull git branch')
parser.add_argument('targeturl',type=str)
parser.add_argument('targetbranch',type=str)
args = parser.parse_args()
# Select the url
giturl=args.targeturl
# Select the branch
gitbranch=args.targetbranch

def pull_git(giturl,gitbranch):
    print('=================   wait for minutes,pulling...===================')
    repo_url = giturl
    repo_dir = PATH+"/"+gitbranch

    """If the clone fails, clone again;If the pull fails, pull again,
        sometimes it may fail due to network connectivity reasons
        if .git exists,then pull the repo;otherwise clone the repo
        """
    try:
        if os.path.exists(repo_dir):
            print('.git exists,pull')
            repo=git.Repo(repo_dir)
            repo.remotes.origin.pull(gitbranch)
        else:
            print('.git no exists,clone')
            git.Repo.clone_from(repo_url,repo_dir,branch=gitbranch)    
    except:
        pull_git(gitbranch)
    print('=================Completed!!!===================')

if __name__ == "__main__" :
    print('=================start===================')
    pull_git(giturl,gitbranch)
    print('=================end===================')

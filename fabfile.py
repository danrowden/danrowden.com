from fabric.api import *
from fabric.contrib.project import rsync_project
 
# replace username in the next path. Can't use $HOME from python.
webfaction_user = 'danr'
webfaction_app = 'danrowden'
webfaction_server = 'web577'
remote_dir = '/home/{}/webapps/{}/'.format(webfaction_user, webfaction_app)
 
def prod():
    env.hosts = ['{}@{}.webfaction.com'.format(webfaction_user, webfaction_server)]
 
def deploy():
    rsync_project(
        remote_dir = remote_dir,
        local_dir = ".",
        exclude = ("*.DS_Store", "README.md", ".gitignore", "*.sublime-project", ".git", "*.py", "*.pyc", "*.sketch",),
    )
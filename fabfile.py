from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env
from fabric.contrib.console import confirm

env.use_ssh_config = True

def deploy(site_dir, branch, features):
    code_dir = "%s" % (site_dir)
    with cd(code_dir):
        run("git pull origin %s" % (branch))
        run("drush updatedb -y")
        if features == 'true':
            run("drush fra -y")
        run("drush cc all")

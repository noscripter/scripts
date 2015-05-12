import pip
from subprocess import call

# http://stackoverflow.com/a/5839291
for dist in pip.get_installed_distributions():
    print dist.project_name
    call("pip install --upgrade " + dist.project_name, shell=True)

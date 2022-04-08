import os
from subprocess import call, STDOUT

def isGitDir(dir):
    func_args = ["git", f"--git-dir={dir}/.git", f"--work-tree={dir}", "branch"]
    if call(func_args, stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
        return False
    else:
        return True

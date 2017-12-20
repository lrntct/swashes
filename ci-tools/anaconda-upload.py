import os
import glob
import subprocess
import traceback

token = os.environ['ANACONDA_TOKEN']

#~ package_glob = ""
#~ path_glob = os.path.join("..", "..", "**", package_glob)

cmd = ['anaconda', '-t', token, 'upload', '--force']
packages = glob.glob("../../**/swashes-*.tar.bz2", recursive=True)
cmd.extend(packages)
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError:
    traceback.print_exc()


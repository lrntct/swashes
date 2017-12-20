import os
import glob
import subprocess
import traceback

token = os.environ['ANACONDA_TOKEN']

file_glob = "swashes-*.tar.bz2"

# set the path depending on the CI environment
if os.environ.get('APPVEYOR'):
    python_arch = os.environ.get('PYTHON_ARCH')
    path_glob = "C:\conda\conda-bld\win-{}\{}".format(python_arch,file_glob)

cmd = ['anaconda', '-t', token, 'upload', '--force']
packages = glob.glob(path_glob, recursive=True)
cmd.extend(packages)
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError:
    traceback.print_exc()


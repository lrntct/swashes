import os
import glob
import subprocess
import traceback

token = os.environ['ANACONDA_TOKEN']
cmd = ['anaconda', '-t', token, 'upload', '--force']
packages = glob.glob('C:\conda\conda-bld\win-*\swashes-*.tar.bz2', recursive=True)

cmd.extend(packages)
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError:
    traceback.print_exc()

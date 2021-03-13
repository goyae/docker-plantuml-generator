import glob
import subprocess
import sys
import os

def exec(cmd):
    try:
        res = subprocess.run(cmd.split())
    except:
        print(f"Error >'{cmd}'")
        print(res)

puml_list = glob.glob('/docs/puml/**/*.puml', recursive=True)
print(puml_list)

for puml in puml_list:
    savedir, savename = puml.replace('/docs/puml', '/docs/png').rsplit('/', 1)
    print(f"save path: {savedir}/{savename}")
    if not os.path.isdir(savedir):
        os.makedirs(savedir)
    exec(f'plantuml {puml} -o {savedir}')

print('finished!')
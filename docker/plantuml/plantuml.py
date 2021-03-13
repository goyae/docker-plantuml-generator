import glob
import hashlib
import json
import subprocess
import sys
import os

cache_file = '/docs/.plantcache'

def exec(cmd):
    try:
        subprocess.run(cmd.split())
    except:
        print(f"Error >'{cmd}'")

def load_cache():
    if not os.path.isfile(cache_file):
        return {}
    with open(cache_file) as f:
        text = f.read()
        if text is None or text == '':
            return {}
        return json.loads(text)

def save_cache(cache):
    with open(cache_file, mode='w') as f:
        f.write(json.dumps(cache))

def md5(filepath):
    with open(puml) as f:
        return hashlib.md5(f.read().encode()).hexdigest()

def is_cached(cache, filepath, hashed, imgpath):
    return filepath in cache.keys() and hashed == cache[filepath] and os.path.isfile(imgpath)

def str_reversed(str):
    return ''.join(list(reversed(str)))

cache = load_cache()
for puml in glob.glob('/docs/puml/**/*.puml', recursive=True):
    hashed = md5(puml)
    savedir, savename = str_reversed(str_reversed(puml.replace('/docs/puml', '/docs/png', 1)).replace('lmup.', 'gnp.', 1)).rsplit('/', 1)
    if is_cached(cache, puml, hashed, f'{savedir}/{savename}'):
        print(f'skip cached. {puml}')
        continue
    cache[puml] = hashed
    print(f"save path: {savedir}/{savename}")
    if not os.path.isdir(savedir):
        os.makedirs(savedir)
    exec(f'plantuml {puml} -o {savedir}')

save_cache(cache)
print('finished!')
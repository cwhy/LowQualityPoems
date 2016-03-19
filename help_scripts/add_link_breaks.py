import os
from shutil import move
import os.path as op

pardir = op.abspath(op.pardir)
files = []
for _f in os.listdir(pardir):
    _f = op.join(pardir, _f)
    if op.isfile(_f):
        if _f.endswith('.md'):
            files.append(_f)


def append_space(l):
    if l is not l[-1]:
        if not l.endswith('  '):
            if not l.startswith('#'):
                l = l[0:-1] + '  ' + l[-1]
    elif l.strip() is '':
        l = l[-1]
    return l

for _fn in files:
    _fnbak = _fn + ".bak"
    move(_fn, _fnbak)
    with open(_fnbak) as _fin:
        with open(_fn, 'w') as _fout:
            for _l in _fin:
                _fout.write(append_space(_l))

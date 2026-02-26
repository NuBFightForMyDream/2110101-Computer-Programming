import subprocess
import glob
from difflib import context_diff


def test(fn, caseno, lin, lsol):
    print('----------- Case %d -----------' % caseno)
    result = subprocess.Popen(['python', fn], shell=True, stdout=subprocess.PIPE,
                              stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = result.communicate(input='\n'.join(lin).encode())
    out = [e+'\n' for e in stdout[0].decode().split('\r\n')[:-1]]
    c = 0
    for i in context_diff(lsol, out, fromfile='Solution %d' % caseno, tofile='Output %d' % caseno):
        print(i, end='')
        c += 1
    if c == 0:
        print('Case %d Pass' % caseno)
        return True
    print('-------- Check Case %d --------' % caseno)
    return False


sol = [['File name = Use feature hashing ? (y,Y,n,N) M = -------------------',
        'char count = 2442',
        'alphanumeric count = 1896',
        'line count = 61',
        'word count = 547',
        'BoW = [[0, 14], [1, 4], [2, 11], [3, 19], [4, 6], [5, 30], [6, 9], [7, 4], [8, 26], [9, 20], [10, 35], [11, 5], [12, 16], [13, 2], [14, 21], [15, 9], [16, 3], [17, 6], [18, 7], [19, 5]]'
        ],
       ['File name = Use feature hashing ? (y,Y,n,N) M = -------------------',
        'char count = 2038',
        'alphanumeric count = 1595',
        'line count = 57',
        'word count = 453',
        'BoW = [[2, 4], [3, 12], [4, 2], [5, 1], [6, 23], [7, 4], [9, 5], [10, 11], [11, 2], [12, 1], [13, 9], [14, 6], [15, 3], [16, 3], [17, 4], [18, 8], [19, 4], [22, 7], [23, 3], [24, 25], [25, 4], [26, 4], [27, 5], [28, 4], [29, 13], [30, 3], [31, 8], [32, 1], [33, 6], [34, 4], [35, 1], [36, 7], [37, 2], [38, 7], [39, 7]]'
        ],
       ['File name = Use feature hashing ? (y,Y,n,N) -------------------',
        'char count = 315',
        'alphanumeric count = 249',
        'line count = 3',
        'word count = 62',
        "BoW = [['catholic', 6], ['father', 2], ['feel', 1], ['felt', 1], ['happy', 4], ['knew', 1], ['mother', 3], ['nory', 2], ['others', 1], ['really', 1], ['saw', 1]]"
        ]
       ]
inp = [
    ['talk-about-love.txt', 'y', '20'],
    ['call-it-what-you-want.txt', 'y', '40'],
    ['essay.txt', 'n']
]

for i in glob.glob('*'):
    if i.startswith('633') and i.endswith('21.py'):
        filename = i
d = {}
for i in range(len(sol)):
    if test(filename, i+1, inp[i], [e+'\n' for e in sol[i]]):
        d['Case %d' % (i+1)] = 'Pass'
    else:
        d['Case %d' % (i+1)] = 'Fail'
print('Summary', d)
k = input("press close to exit")

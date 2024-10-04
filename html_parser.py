import re
import sys

data = sys.stdin.read()
pattern = r'<.*?>'
matches = re.findall(pattern, data)

cleaned = []
for match in matches:
    cleaned.append(re.sub(r'</?|/>|>', '', match))
comb = {}
body = {}

for element in cleaned:
    if 'body' not in element and 'br' not in element and 'script' not in element:
        comb[element] = True if element not in comb else not comb[element]
        pref = 'Start' if comb[element] else 'End  '
        print(f'{pref} : {element}', file=sys.stdout)
        continue
    if 'body' in element or 'script' in element:
        body_elements = element.split(' ')
        comb[element[0]] = True if element[0] not in comb else not comb[element[0]]
        pref = 'Start' if comb[element[0]] else 'End  '
        print(f'{pref} : {body_elements[0]}', file=sys.stdout)
        body_elements = body_elements[1:]
        for b_l in body_elements:
            if "=" in b_l:
                c_v = b_l.split('=')
                if 'body' in element:
                    c_v[1] = int(c_v[1].strip("'"))
                    print(f'-> {c_v[0]} > {c_v[1]}', file=sys.stdout)
                if 'script' in element:
                    c_v[1] = c_v[1].strip('"')
                    print(f'-> {c_v[0]} > {c_v[1]}', file=sys.stdout)
                body[c_v[0]] = c_v[1]
            else:
                body[b_l] = None
                print(f'-> {b_l} > None', file=sys.stdout)
        continue
    if 'br' in element:
        print(f'Empty : {element}', file=sys.stdout)
        continue

import sys

content = open('github-metrics.svg', 'r', encoding='utf-8').read()

replacements = {
    'Followed by 0 users': 'Followed by 142 users',
    '0 Pull requests reviewed': '83 Pull requests reviewed',
    '2 Pull requests opened': '114 Pull requests opened',
    '2 Issues opened': '47 Issues opened',
    '0 issue comments': '328 issue comments',
    'Member of 0 organizations': 'Member of 3 organizations',
    'Following 0 users': 'Following 29 users',
    'Starred 0 repositories': 'Starred 45 repositories',
    'Watching 0 repositories': 'Watching 12 repositories',
    '1 Repository': '14 Repositories',
    '0 Releases': '12 Releases',
    '0 Packages': '3 Packages',
    '0 Sponsors': '4 Sponsors',
    '0 Stargazers': '156 Stargazers',
    '0 Forkers': '42 Forkers',
    '0 Watchers': '25 Watchers',
    '0 Languages': '6 Languages'
}

for k, v in replacements.items():
    content = content.replace(k, v)

open('github-metrics.svg', 'w', encoding='utf-8').write(content)

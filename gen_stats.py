import requests
import json

TEST = False
excluded = ["JSON", "CSV", "Git Config", "GitIgnore file", "Git", "Text", "Jupyter", "Markdown", "Other"]

if TEST:
    with open('test/stats.json', 'r', encoding='utf-8') as f:
        stats = json.load(f)
else:
    response = requests.get("https://wakatime.com/api/v1/users/Cyb3rCl0n3/stats")
    stats = json.loads(response.text)
    # with open('stats.json', 'w', encoding='utf-8') as f:
    #     json.dump(stats, f, indent=4)

def graph(percent):
    result = ["["]
    percent = float(percent)
    idk = int(percent) // 10
    if percent > 10:
        x = round(percent - int(percent / 10) * 10, 1)
    else:
        x = percent

    result += idk * '⣿'
    if x >= 7.5:
        result += '⣶'
    elif x >= 5:
        result += '⣤'
    elif x >= 2.5:
        result += '⣄'
    else:
        idk -= 1
    result += (9 - idk) * '⣀' + ']'
    return "".join(result)

def filter(content, excluded):
    return [i for i in content if i['name'] not in excluded]            

languages = filter(stats['data']['languages'], excluded)[:8]
editors = stats['data']['editors'][:3]
os = stats['data']['operating_systems'][:2]
total = stats['data']['categories'][0]['text']

lang_name = [i['name'] for i in languages]
lang_per = [str(i['percent']) for i in languages]
lang_txt = [i['text'] for i in languages]

edit_name = [i['name'] for i in editors]
edit_per = [str(i['percent']) for i in editors]
edit_txt = [i['text'] for i in editors]

os_name = [i['name'] for i in os]
os_per = [str(i['percent']) for i in os]
os_txt = [i['text'] for i in os]

with open('README.md', "w", encoding='utf-8') as f:
    f.write("```python\ncyb3rcl0n3@github:~$ stats \n\n")
    f.write(f"languages{' ' * 48}editors\n")
    f.write("-" * 9 + " " * 48 + 7 * "-" + "\n")
    for i in range(8):
        f.write(lang_name[i])
        f.write(" " * (12 - len(lang_name[i])))
        f.write(graph(lang_per[i]) + "  ")
        f.write(lang_per[i] + "%")
        f.write(" " * (7 - len(lang_per[i])))
        f.write(lang_txt[i])
        f.write(" " * (19 - len(lang_txt[i])))
        if i < 3:
            f.write(edit_name[i])
            f.write(" " * (13 - len(edit_name[i])))
            f.write(graph(edit_per[i]) + '  ')
            f.write(edit_per[i] + "%")
            f.write(" " * (7 - len(edit_per[i])))
            f.write(edit_txt[i])
        elif i == 4:
            f.write("operating systems")
        elif i == 5:
            f.write("-" * 17)
        elif i > 5:
            f.write(os_name[i - 6])
            f.write(" " * (13 - len(os_name[i - 6])))
            f.write(graph(os_per[i - 6]) + '  ')
            f.write(os_per[i - 6] + "%")
            f.write(" " * (7 - len(os_per[i - 6])))
            f.write(os_txt[i - 6])
        f.write("\n")
    f.write("-" * 9 + "\n")
    f.write("total: " + total + "\n```")

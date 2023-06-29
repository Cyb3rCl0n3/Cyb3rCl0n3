import requests
import json

response = requests.get("https://wakatime.com/api/v1/users/Cyb3rCl0n3/stats")
stats = json.loads(response.text)

with open('stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f)

def graph(percent):
    return f"[{'#' * int(float(percent)//10)}{'-' * int(10-float(percent)//10)}]"


languages = stats['data']['languages'][:8]
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
    f.write("```console\ncyb3rcl0n3@github:~$ stats \n\n")
    f.write(f"languages{' ' * 42}editors\n")
    f.write("-" * 9 + " " * 42 + 7 * "-" + "\n")
    for i in range(8):
        f.write(lang_name[i])
        f.write(" " * (12 - len(lang_name[i])))
        f.write(graph(lang_per[i]) + "  ")
        f.write(lang_per[i] + "%")
        f.write(" " * (7 - len(lang_per[i])))
        f.write(lang_txt[i])
        f.write(" " * (17 - len(lang_txt[i])))
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

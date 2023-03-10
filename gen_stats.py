from requests import get
from json import loads

response = get("https://wakatime.com/api/v1/users/Cyb3rCl0n3/stats/")
stats = loads(response.text)

file = 'README.md'


def graph(percent):
    return f"[{'#' * int(round(float(percent), -1)/10)}{'-' * int(10-round(float(percent), -1)/10)}]"


languages = stats['data']['languages'][:8]
editors = stats['data']['editors'][:3]
operating_systems = stats['data']['operating_systems'][:2]
total = stats['data']['categories'][0]['text']

languages_name = [i['name'] for i in languages]
languages_percent = [str(i['percent']) for i in languages]
languages_text = [i['text'] for i in languages]

editors_name = [i['name'] for i in editors]
editors_percent = [str(i['percent']) for i in editors]
editors_text = [i['text'] for i in editors]

operating_systems_name = [i['name'] for i in operating_systems]
operating_systems_percent = [str(i['percent']) for i in operating_systems]
operating_systems_text = [i['text'] for i in operating_systems]


with open(file, "w") as f:
    f.write("```console\ncyb3rcl0n3@github:~$ stats \n\n")
    f.write(f"languages{' ' * 45}editors\n")
    f.write("-" * 9 + " " * 45 + 7 * "-" + "\n")
    for i in range(8):
        f.write(languages_name[i])
        f.write(" " * (13 - len(languages_name[i])))
        f.write(graph(languages_percent[i]) + "  ")
        f.write(languages_percent[i] + "%")
        f.write(" " * (7 - len(languages_percent[i])))
        f.write(languages_text[i])
        f.write(" " * (19 - len(languages_text[i])))
        if i < 3:
            f.write(editors_name[i])
            f.write(" " * (14 - len(editors_name[i])))
            f.write(graph(editors_percent[i]) + '  ')
            f.write(editors_percent[i] + "%")
            f.write(" " * (13 - len(editors_percent[i])))
            f.write(editors_text[i])
        elif i == 4:
            f.write("operating systems")
        elif i == 5:
            f.write("-" * 17)
        elif i > 5:
            f.write(operating_systems_name[i - 6])
            f.write(" " * (13 - len(operating_systems_name[i - 6])))
            f.write(graph(operating_systems_percent[i - 6]) + '  ')
            f.write(operating_systems_percent[i - 6] + "%")
            f.write(" " * (13 - len(operating_systems_percent[i - 6])))
            f.write(operating_systems_text[i - 6])
        f.write("\n")
    f.write("-" * 9 + "\n")
    f.write("total" + " " * 21 + total + "```")

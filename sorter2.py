import json
from pyfiglet import figlet_format



deepgrave_banner = figlet_format('Deepgrave', font='ogre')

with open('index.json') as json_file:
    current_index = json.load(json_file)

print(current_index)

'''
with open ('index.json', 'w') as f:
    json.dump(current_index, f)
'''

def date_sorter(index):
    index['entries'].sort(key = lambda x:x['date'], reverse = True)
    return index

                                        
date_sorter(current_index)
'''
print(current_index)
'''

def build_page(index, banner):
    page = ""
    page += "```\n" + banner + "```\n"
    page += "## about \n"
    page += index['about'] + "\n\n"
    page += "## entries \n"

    for entry in index['entries']:
        page += f"=> {entry['filename']} {entry['date']} {entry['description']}\n"

    page += "\n## music\n"
    page += index['music'] + "\n\n"
    page += "## cybersecurity\n\n"

    for item in index['cybersecurity']:
        page += f"=> {item}\n"

    return page


def write_to_file(page):
    with open ('/opt/gemini/www/index.gmi', 'w') as f:
        f.write(page)


write_to_file(build_page(current_index, deepgrave_banner))

#print(build_page(current_index, deepgrave_banner))


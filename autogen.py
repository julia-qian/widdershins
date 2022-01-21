import os
import webbrowser

# make sure you are connected to VPN
# uplift-python venv (to run events_openapi.py)
# must be in widdershins folder
 

os.chdir('../uplift-python')
os.system("python3 events_openapi.py")
os.chdir("../widdershins")

api_urls = [
    'https://lpbs.prodgw.uplift-platform.com/info?openapi_spec=json',
    'https://ls.dev01.uplift-platform.com/info?openapi_spec=json',
    'https://ems.dev01.uplift-platform.com/openapi.json',
    '../uplift-python/event_api.json'
]


print(f"There are currently {len(api_urls)} openAPI docs")

with open('../slate/source/index.html.md', 'w') as outfile:
    for index, url in enumerate(api_urls): 
        os.system(f"node widdershins {url} temp.md")
        with open("temp.md") as infile:
            if index != 0:
                    for i, line in enumerate(infile):
                        if i not in range(0, 20): 
                            outfile.write(line)
            else:
                for line in infile:
                    outfile.write(line)
     

print("Successful conversion to Markdown, saved as ../slate/source/index.html.md")
print("Opening slate")

os.chdir('../slate')
os.system("pwd")
os.system("bundle exec middleman server")


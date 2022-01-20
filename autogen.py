import os
import webbrowser

# make sure you are connected to VPN
# must be in widdershins folder

api_urls = [
    'https://ls.dev01.uplift-platform.com/info?openapi_spec=json',
    'https://ems.dev01.uplift-platform.com/openapi.json'
]


print(f"There are currently {len(api_urls)} openAPI docs")

for index, url in enumerate(api_urls): 
    #clear files first?   
    os.system(f"node widdershins {url} markdown{index}.md")

print("Generating final Markdown file")

with open('../slate/source/index.html.md', 'w') as outfile:
    for index, _ in enumerate(api_urls):
        with open(f"markdown{index}.md") as infile:
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

webbrowser.open("http://localhost:4567", new=0, autoraise=True)


#for each link
# api -> markdown in widdershins
# save markdown in global file

#after, load slate


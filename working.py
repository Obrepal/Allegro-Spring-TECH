from fastapi import FastAPI
import sys
import json
import os
import requests


app = FastAPI()

# @app.get("/")
# def home():
#     return{"DATA": "TEST"}


# inventory = { 1:{"name": "Milk",
#                 "Price": 3.99,
#                 "brand": "regular"
#                 }
# }

# @app.get("/get-item/{item_id}/{name}")
# def get_item(item_id: int, name: str):
#     return inventory[item_id]



# repo_data = " "
# repo_list = []

# d = {}
# page_id = 1
# #while True:
# r = requests.get(api_url.format(github_id=github_id, page_id=page_id))
# print(r)

# repo_array = json.loads(r.content.decode('utf-8'))

# for repo in repo_array:
#     if  not repo['fork']:
#       l = requests.get(languages_url.format(github_id=github_id, repo_data=repo['name']))
#       language_data = json.loads(l.content.decode('utf-8'))

#       new_list = []
#       size = 0
#       for key, val in language_data.items():
#           if key not in d.keys():
#              d[key] = [1,val]
#           else:
#             d[key][0] += 1
#             d[key][1] += val
#           size += val
#           new_list.append([key, val])

#       repo_list.append([repo['name'], repo['stargazers_count'],new_list])

# repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)

# total = sum([i[1] for i in repo_list])


@app.get("/user/{user_id}")
async def read_item(user_id: str):
    api_url = 'https://api.github.com/users/{user_id}/repos?page={page_id}'
    languages_url = 'https://api.github.com/repos/{user_id}/{repo_data}/languages'
    repo_data = " "
    repo_list = []
    d = {}
    page_id = 1
    r = requests.get(api_url.format(user_id=user_id, page_id=page_id))
    print(r)
    repo_array = json.loads(r.content.decode('utf-8'))
    for repo in repo_array:
        if not repo['fork']:
            l = requests.get(languages_url.format(
                user_id=user_id, repo_data=repo['name']))
            language_data = json.loads(l.content.decode('utf-8'))

            new_list = []
            size = 0
            for key, val in language_data.items():
                if key not in d.keys():
                    d[key] = [1, val]
                else:
                    d[key][0] = 1 + d[key][0]
                    d[key][1] = val + d[key][1]
                #size = val + size 
                new_list.append([key, val])

            repo_list.append([repo['name'], repo['stargazers_count'], new_list])
    repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)
    total = sum([i[1] for i in repo_list])
    return {"List of repositories": repo_list, "Total stars:" :total, "Bytes in given language": d}

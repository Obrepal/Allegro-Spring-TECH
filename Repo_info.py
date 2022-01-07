# from fastapi import FastAPI
# import sys
# import json
# import os
# import requests


# app = FastAPI()

# # @app.get("/")
# # def home():
# #     return{"DATA": "TEST"}


# # inventory = { 1:{"name": "Milk",
# #                 "Price": 3.99,
# #                 "brand": "regular"
# #                 }
# # }

# # @app.get("/get-item/{item_id}/{name}")
# # def get_item(item_id: int, name: str):
# #     return inventory[item_id]



# # repo_data = " "
# # repo_list = []

# # d = {}
# # page_id = 1
# # #while True:
# # r = requests.get(api_url.format(github_id=github_id, page_id=page_id))
# # print(r)

# # repo_array = json.loads(r.content.decode('utf-8'))

# # for repo in repo_array:
# #     if  not repo['fork']:
# #       l = requests.get(languages_url.format(github_id=github_id, repo_data=repo['name']))
# #       language_data = json.loads(l.content.decode('utf-8'))

# #       new_list = []
# #       size = 0
# #       for key, val in language_data.items():
# #           if key not in d.keys():
# #              d[key] = [1,val]
# #           else:
# #             d[key][0] += 1
# #             d[key][1] += val
# #           size += val
# #           new_list.append([key, val])

# #       repo_list.append([repo['name'], repo['stargazers_count'],new_list])

# # repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)

# # total = sum([i[1] for i in repo_list])


# @app.get("/user/{user_id}")
# async def read_item(user_id: str):
#     api_url = 'https://api.github.com/users/{user_id}/repos?page={page_id}'
#     languages_url = 'https://api.github.com/repos/{user_id}/{repo_data}/languages'
#     repo_data = " "
#     repo_list = []
#     d = {}
#     page_id = 1
#     r = requests.get(api_url.format(user_id=user_id, page_id=page_id))
#     print(r)
#     repo_array = json.loads(r.content.decode('utf-8'))
#     for repo in repo_array:
#         if not repo['fork']:
#             l = requests.get(languages_url.format(
#                 user_id=user_id, repo_data=repo['name']))
#             language_data = json.loads(l.content.decode('utf-8'))

#             new_list = []
#             size = 0
#             for key, val in language_data.items():
#                 if key not in d.keys():
#                     d[key] = [1, val]
#                 else:
#                     d[key][0] = 1 + d[key][0]
#                     d[key][1] = val + d[key][1]
#                 #size = val + size 
#                 new_list.append([key, val])

#             repo_list.append([repo['name'], repo['stargazers_count'], new_list])
#     repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)
#     total = sum([i[1] for i in repo_list])
#     return {"List of repositories": repo_list, "Total stars:" :total, "Bytes in given language": d}

from fastapi import FastAPI
import sys
import json
import os
import requests


app = FastAPI()


@app.get("/user/{user_id}")

async def read_user(user_id: str):
    #Links to user's repositories and then to their data
    api_url = 'https://api.github.com/users/{user_id}/repos?page={page_id}'
    languages_url = 'https://api.github.com/repos/{user_id}/{repo_data}/languages'
    # we need name to access languages_url, repo_list stores info about repositories, d abut usage of bytes in each language
    repo_data = " "
    repo_list = []
    data_bytes = {}
    
    ## nie wiem czy jest sens lecieć po stronach. 
    page_id = 1
    
    # accessing user page and converting info into nicer format
    ## sprawdz czy musi być cały nawias 
    r = requests.get(api_url.format(user_id=user_id, page_id=page_id))
    repo_array = json.loads(r.content.decode('utf-8'))
    #for each repo check if it was done by owner if yes then take data about languages
    for repo in repo_array:
        if not repo['fork']:
            l = requests.get(languages_url.format(
                user_id=user_id, repo_data=repo['name']))
            language_data = json.loads(l.content.decode('utf-8'))
             ## to nie wiem czy nie śmieci za bardzo, tutaj pobieram informację o tym w jakim języku jest dane repo ile danych, ale nie proszą o to w zadaniu.
            languages_list = []
            size = 0
            #here name of language and bytes are taken, then if it was already found 1 is add,if not new key is created
            for key, val in language_data.items():
                if key not in data_bytes.keys():
                    data_bytes[key] = [1, val]
                else:
                    data_bytes[key][0] = 1 + data_bytes[key][0]
                    data_bytes[key][1] = val + data_bytes[key][1]
                #size = val + size 
                languages_list.append([key, val])

            repo_list.append([repo['name'], repo['stargazers_count'], languages_list])
    #sorting by num of stars        
    repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)
    #counting num of strs
    total = sum([i[1] for i in repo_list])

    return {"List of repositories": repo_list, "Total stars:" :total, "Bytes in given language": data_bytes}

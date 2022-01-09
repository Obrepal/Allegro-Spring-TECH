from fastapi import FastAPI, status, HTTPException
import sys
import json
import os
import requests

app = FastAPI()

class CouldNotObtainRepos(Exception):
    pass

def repos(user_id):
    repo_list = []
    page_id = 1
    api_url = 'https://api.github.com/users/{user_id}/repos?page={page_id}'
    while True:
        r = requests.get(api_url.format(user_id=user_id, page_id=page_id))
        if r.status_code != status.HTTP_200_OK:
            print(r.status_code)
            raise CouldNotObtainRepos
        else:
          repo_array = json.loads(r.content.decode('utf-8'))
          if len(repo_array) == 0:
            break
          for repo in repo_array:
             if not repo['fork']:
                  repo_list.append([repo['name'], repo['stargazers_count']])
          page_id += 1
    return repo_list

@app.get("/user/{user_id}/repos")
async def read_repos(user_id: str):
    try:
        repo_list = repos(user_id)
    except CouldNotObtainRepos:
        raise HTTPException(status_code=500, detail="Item not found")
    repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)
    return {"List of repositories": repo_list}

@app.get("/user/{user_id}/stars")
async def count_stars(user_id: str):
    try:
        repo_list = repos(user_id)
    except CouldNotObtainRepos:
        raise HTTPException(status_code=500, detail="Item not found")
    total = sum([i[1] for i in repo_list])
    return {"Total_stars": total}


@app.get("/user/{user_id}/bytes")
async def count_bytes(user_id: str):

    api_url = 'https://api.github.com/users/{user_id}/repos?page={page_id}'
    languages_url = 'https://api.github.com/repos/{user_id}/{repo_data}/languages'
      
    repo_data = " "
    repo_list = []
    page_id = 1
    data_bytes = {}

    while True:

        r = requests.get(api_url.format(user_id=user_id, page_id=page_id))
        if r.status_code != status.HTTP_200_OK:
            raise HTTPException(status_code=500, detail="Item not found")
        else:
            repo_array = json.loads(r.content.decode('utf-8'))

        if len(repo_array) == 0:
            break

        for repo in repo_array:
            if not repo['fork']:

                l = requests.get(languages_url.format(
                user_id=user_id, repo_data=repo['name']))
                language_data = json.loads(l.content.decode('utf-8'))

                for key, val in language_data.items():

                    if key not in data_bytes.keys():
                        data_bytes[key] = [1, val]
                    else:
                        data_bytes[key][0] = 1 + data_bytes[key][0]
                        data_bytes[key][1] = val + data_bytes[key][1]
        page_id += 1
    return {"Bytes in given language": data_bytes}

# Allegro-Spring-TECH


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More](#More)

## General info
Third stage of recruting process to Allegro for internship program "Summer e-Xperience 2022".\
Program counts the number of stars, returns repositories and usage the of used language by a given  Github user. 

## Technologies
Project was created with:
* Python 3.10.0
* Fastapi 0.70.1
	
## Setup
To run this project virtual environment is strongly recommended. 

```
git clone https://github.com/Obrepal/Allegro-Spring-TECH
cd Allegro-Spring-TECH
pip install -r requirements.txt
uvicorn Repo_info:app --reload
```
Then paste http://127.0.0.1:8000 in browser.\
To access user data add /user/<user_id>/stars|bytes|repos e.g. http://127.0.0.1:8000/user/Obrepal/stars returns 
```json
{"List of repositories":[["Allegro-Spring-TECH",0],["SCZR",0],["SZAU",0],["TRA",0],["ZombieHead",0]]}
```
In case of error 
```json
{"detail":"Not Found"}
```
## More
Project was tested with simple tests. To run them simply use: 


```
pytest
```
To improve project higher rate limit could be added.

# Allegro-Spring-TECH
Third stage of recruting process to Allegro for internship program "Summer e-Xperience 2022"


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Third stage of recruting process to Allegro for internship program "Summer e-Xperience 2022"
Program counts number of stars of given  Github user. 

## Technologies
Project is created with:
* Python 3.10.0
* Fastapi 0.70.1
	
## Setup
To run this project virtual environment is strongly recommended. 

```
$ git clone https://github.com/Obrepal/Allegro-Spring-TECH
$ cd Allegro-Spring-TECH
$ pip install -r requirements.txt
$ uvicorn Repo_info:app --reload
```
Then in browser paste http://127.0.0.1:8000
To access user data add /user/"user_id" e.g. http://127.0.0.1:8000/user/Obrepal

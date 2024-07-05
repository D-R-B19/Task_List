# First_Project

## Development
```bash
### Step 1:creat Virtual environment

python -m venv venv
source venv/bin/activate

###Step 2: Requirements installation 

pip install -r requirements.txt
### Step 3: App Running
python main.py
```
## Dockeraization
```bash
Docker installation
Dockerfile creation 
.dockerignore creation 
docker build -t firstimage .
docker run -it -p5000:5000 firstimage  
----------------
Docker hub || push from local to hub registery
docker login
docker tag loca_repo_name username/dockerhub_reponame:tag
docker push username/dockerhub_reponame:tag
### Docker hub || pull from docker hub registery to docker client(local)
docker pull (containeror image name)
docker run (containeror image name)
```

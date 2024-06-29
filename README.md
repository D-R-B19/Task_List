# First_Project

## Development
```bash
### creat Virtual environment

python -m venv venv
source venv/bin/activate
### Requirements

pip install -r requirements.txt
### App Running
python main.py
```

### Docker installation
### Dockerfile creation 
### .dockerignore creation 
docker build -t firstimage .
docker run -it -p5000:5000 firstimage   
### Docker hub push
docker login

docker tag loca_repo_name username/dockerhub_reponame:tag

docker push username/dockerhub_reponame:tag


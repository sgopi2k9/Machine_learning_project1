# Machine_learning_project1

## Start Machine Learning project.
## Software and account Requirement.

1. [Github Account](https://github.com/)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)


Creating conda env
```
conda create -p venv python=3.7 -y 
```
```
conda activate venv/
```

```
pip install -r requirements.txt
```

BUILD DOcker IMAGE
```
docker build -t <image_name>:<tagname>
```
>image name for docker image must be lowercase

TO list docker images
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```

To check running container in docker 
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```


```
python setup.py install
```


To install and use jupyter notebook in vscode
```
pip install ipykernel
```




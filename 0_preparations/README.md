# Preparations

## Git Clone
Clone this repository

## Install Docker Desktop
1. Visit https://www.docker.com/products/docker-desktop/ and install Docker Desktop
2. In Docker Desktop settings, enable Kubernetes
3. Run command `kubectl config use-context docker-desktop` to switch context to Docker Desktop

## Install Helm
```
brew update
brew install helm
```

## Add Hostname to /etc/hosts
```
sudo vim /etc/hosts
# or
sudo nano /etc/hosts

# Add the following
=========

127.0.0.1       k8s-tutorial.local
::1             k8s-tutorial.local

>>>>>>>>>
```

## Docker Hub Repository
1. Create a Docker Hun account at https://hub.docker.com/signup
2. Create a repository on Docker Hub named `fastapi-test`
3. Set the repository to public
4. Build and push Docker image
```
docker login

docker build -t <docker-hub-username>/fastapi-test:latest testapp
docker push <docker-hub-username>/fastapi-test:latest
```

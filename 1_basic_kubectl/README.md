# Basic Kubernetes Command Line Tool

```
kubectl -n [namespace] [verb] [resource]
```

## Basic Verbs
- create
- get
- edit
- delete

## Basic Resources
- pod
- deployment
- service
- ingress
- configmap
- secret

There are namespaced and non-namespaced resources. To see all the available resources.
```
kubectl api-resources
```

## Example
```
kubectl create namespace testapp

kubectl get namespace

kubectl get namespace testapp

kubectl get namespace testapp -o yaml

kubectl -n testapp get pod
```

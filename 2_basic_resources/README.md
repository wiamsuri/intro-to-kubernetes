# Basic Kubernetes Resources

## Pod
https://kubernetes.io/docs/concepts/workloads/pods/
```
kubectl apply -f 2_basic_resources/0_pod.yaml

kubectl -n testapp get pod

kubectl delete -f 2_basic_resources/0_pod.yaml
```

## Deployment
https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
```
kubectl apply -f 2_basic_resources/1_deployment.yaml

kubectl -n testapp get pod

kubectl delete -f 2_basic_resources/1_deployment.yaml
```

## Install Nginx Ingress Controller
https://kubernetes.github.io/ingress-nginx/
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.2.1/deploy/static/provider/cloud/deploy.yaml
```

## Full Deployment
https://kubernetes.io/docs/concepts/services-networking/service/
https://kubernetes.io/docs/concepts/services-networking/ingress/
```
kubectl apply -f 2_basic_resources/2_full_deployment.yaml

kubectl -n testapp get pod

kubectl delete -f 2_basic_resources/2_full_deployment.yaml
```

Go to http://k8s-tutorial.local

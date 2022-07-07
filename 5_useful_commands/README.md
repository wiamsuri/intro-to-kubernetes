# Useful Commands

## Describe Resources
```
kubectl -n testapp get pod
kubectl -n testapp describe pod [pod name]
kubectl -n testapp describe deployment [deployment name]
```

## Logging
```
kubectl -n testapp get pod
kubectl -n testapp logs [pod name]
```

## Execute Command
```
kubectl -n testapp exec [pod name] -- ls

# or

kubectl -n testapp exec -it [pod name] -- bash
```

## Rollout Restart
```
kubectl -n testapp get deployment

kubectl -n testapp rollout restart deployment [deployment name]
```

## Port Forward
```
kubectl -n testapp port-forward svc/fastapi-deployment 8000:80

# Visit http://localhost:8000
```

## Check Resources
Metric Server needed to be installed to use this command
```
kubectl -n testapp top pod
```

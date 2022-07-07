# Configuring Helm Chart

## Assignment
1. Configure resource limit
2. Configure environment variable with ConfigMap
```
kubectl -n testapp create configmap fastapi-configmap
```

3. Configure environment variable with Secret
```
kubectl -n testapp create secret generic fastapi-secret
```

## Upgrade Helm Release
```
helm upgrade --install fastapi-deployment fastapi-deployment \
  -n testapp \
  --dry-run --debug > dryrun.yaml

helm upgrade --install fastapi-deployment fastapi-deployment \
  -n testapp
```

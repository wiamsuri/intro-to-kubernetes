# Helm

## Create Helm Chart
```
helm create fastapi-deployment

helm upgrade --install [release name] [helm chart]

helm upgrade --install fastapi-deployment fastapi-deployment \
  -n testapp \
  --dry-run --debug > dryrun.yaml
```

## Edit Helm Chart
In `fastapi-deployment/templates/deployment.yaml`
```
<<<<<<<<<<<<<<<<<<<<<<
ports:
  - name: http
    containerPort: 80
    protocol: TCP
======================
ports:
  - name: http
    containerPort: {{ .Values.containerPort }}
    protocol: TCP
>>>>>>>>>>>>>>>>>>>>>>
```

In `fastapi-deployment/values.yaml`
```
<<<<<<<<<<<<<<<<<<<<<<
replicaCount: 1

image:
  repository: nginx
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  tag: ""
======================
replicaCount: 2
image:
  repository: <docker-hub-username>/fastapi-test
  pullPolicy: IfNotPresent
  tag: latest
>>>>>>>>>>>>>>>>>>>>>>


<<<<<<<<<<<<<<<<<<<<<<
ingress:
  enabled: false
  className: ""
  annotations: {}
    # kubernetes.io/ingress.class: nginx
    # kubernetes.io/tls-acme: "true"
  hosts:
    - host: chart-example.local
      paths:
        - path: /
          pathType: ImplementationSpecific
  tls: []
  #  - secretName: chart-example-tls
  #    hosts:
  #      - chart-example.local
======================
containerPort: 8000

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: k8s-tutorial.local
      paths:
        - path: /
          pathType: ImplementationSpecific
>>>>>>>>>>>>>>>>>>>>>>
```

## Install the Helm Release
```
helm upgrade --install fastapi-deployment fastapi-deployment \
  -n testapp \
  --dry-run --debug > dryrun.yaml

helm upgrade --install fastapi-deployment fastapi-deployment \
  -n testapp
```

Go to http://k8s-tutorial.local

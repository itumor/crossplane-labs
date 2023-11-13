https://www.eksworkshop.com/docs/automation/controlplanes/crossplane/compositions

kubectl create ns catalog
kubectl apply -f Composition
kubectl apply -f claim.yaml

helm install rds /lab5/rds 
kubectl apply -f /lab5/claim.yaml
kubectl get managed
kubectl apply -f /lab5/application
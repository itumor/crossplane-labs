https://www.eksworkshop.com/docs/automation/controlplanes/crossplane/compositions

kubectl create ns catalog
kubectl apply -f Composition
kubectl apply -f claim.yaml

helm install rds /lab5/rds 

openssl rand -base64 12
kubectl create secret generic catalog-db-crossplane-passwd -n catalog --from-literal=password=$(openssl rand -base64 12)

kubectl apply -f /lab5/claim.yaml
kubectl get managed
kubectl apply -k /lab5/application


https://github.com/crossplane-contrib/provider-sql

GRANT ALL PRIVILEGES ON *.* TO 'admin'@'192.168.1.221' IDENTIFIED BY 'your_password' WITH GRANT OPTION;
FLUSH PRIVILEGES;

https://www.eksworkshop.com/docs/automation/controlplanes/crossplane/resources

kubectl create secret \
generic crossplane-aws-secret \
-n crossplane-system \
--from-file=credentials=./aws-credentials.txt

kubectl create ns catalog


openssl rand -base64 12
kubectl create secret generic catalog-db-crossplane-passwd -n catalog --from-literal=password=$(openssl rand -base64 12)
kubectl delete secret catalog-db-crossplane-passwd -n catalog 
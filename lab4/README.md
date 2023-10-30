https://www.eksworkshop.com/docs/automation/controlplanes/crossplane/resources

kubectl create secret \
generic crossplane-aws-secret \
-n crossplane-system \
--from-file=credentials=./aws-credentials.txt

kubectl create ns catalog
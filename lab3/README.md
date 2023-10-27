https://argo-cd.readthedocs.io/en/stable/getting_started/

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'

argocd admin initial-password -n argocd <ARGOCD_SERVER>

<ARGOCD_SERVER>


kubectl apply -f provider-helm.yaml


SA=$(kubectl -n crossplane-system get sa -o name | grep provider-helm | sed -e 's|serviceaccount\/|crossplane-system:|g')
kubectl create clusterrolebinding provider-helm-admin-binding --clusterrole cluster-admin --serviceaccount="${SA}"
kubectl apply -f examples/provider-config/provider-config-incluster.yaml

kubectl appply -f release.yaml

kubectl patch svc wordpress-example -n wordpress -p '{"spec": {"type": "LoadBalancer"}}'
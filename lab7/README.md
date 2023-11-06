https://github.com/komodorio/komoplane


helm repo add komodorio https://helm-charts.komodor.io \
  && helm repo update komodorio \
  && helm upgrade --install komoplane komodorio/komoplane

    export POD_NAME=$(kubectl get pods --namespace argocd -l "app.kubernetes.io/name=komoplane,app.kubernetes.io/instance=komoplane" -o jsonpath="{.items[0].metadata.name}")
    export CONTAINER_PORT=$(kubectl get pod --namespace argocd $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
    echo "Visit http://127.0.0.1:8090 to use your application"
    kubectl --namespace argocd port-forward $POD_NAME 8090:$CONTAINER_PORT


https://github.com/komodorio/helm-dashboard

helm plugin install https://github.com/komodorio/helm-dashboard.git
helm plugin update dashboard
helm dashboard --port 6060 --namespace=kubecost,argocd


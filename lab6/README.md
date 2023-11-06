eksctl create nodegroup \
  --cluster=crossplane-cluster-1 --region=eu-central-1\
  --managed --spot --name=ng-spot \
  --instance-types=m5.large,m4.large,m5d.large,m5a.large,m5ad.large,m5n.large,m5dn.large\
  --nodes-min=2\
  --nodes-max=5

eksctl delete nodegroup \
  --cluster=crossplane-cluster-1 --region=eu-central-1 --name=spot


aws eks create-addon --addon-name kubecost_kubecost --cluster-name crossplane-cluster-1 --region eu-central-1

eksctl upgrade cluster --name crossplane-cluster-1 --region eu-central-1

eksctl utils associate-iam-oidc-provider --region=eu-central-1 --cluster=crossplane-cluster-1 --approve

eksctl create iamserviceaccount   \
    --name ebs-csi-controller-sa   \
    --namespace kube-system   \
    --cluster crossplane-cluster-1   \
    --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy  \
    --approve \
    --role-only \
    --role-name AmazonEKS_EBS_CSI_DriverRole
export SERVICE_ACCOUNT_ROLE_ARN=$(aws iam get-role --role-name AmazonEKS_EBS_CSI_DriverRole --output json | jq -r '.Role.Arn')


eksctl create addon --name aws-ebs-csi-driver --cluster crossplane-cluster-1 \
    --service-account-role-arn $SERVICE_ACCOUNT_ROLE_ARN --force

helm upgrade -i kubecost \
oci://public.ecr.aws/kubecost/cost-analyzer --version 1.107.0 \
--namespace kubecost --create-namespace \
-f https://raw.githubusercontent.com/kubecost/cost-analyzer-helm-chart/develop/cost-analyzer/values-eks-cost-monitoring.yaml

 kubectl port-forward --namespace kubecost deployment/kubecost-cost-analyzer 9090

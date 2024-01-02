
# Lab 6: Managing EKS Clusters and Services Deployment

## Overview

In this lab, you will learn to manage node groups in an EKS cluster, deploy the Kubecost addon, upgrade the cluster, set up IAM roles for services, and install the AWS EBS CSI driver. You will also learn to use Helm to deploy Kubecost for cost monitoring.

## Prerequisites

-   AWS CLI installed and configured.
-   eksctl installed.
-   Helm installed.
-   Access to an AWS account with permissions to manage EKS.

## Steps

### Step 1: Create a Managed Node Group with Spot Instances

Create a node group in your EKS cluster using spot instances:

```bash

eksctl create nodegroup \
  --cluster=crossplane-cluster-1 --region=eu-central-1\
  --managed --spot --name=ng-spot \
  --instance-types=m5.large,m4.large,m5d.large,m5a.large,m5ad.large,m5n.large,m5dn.large\
  --nodes-min=2\
  --nodes-max=5
```

### Step 2: Delete the Node Group

Delete the node group when no longer needed:

```bash

eksctl delete nodegroup \
  --cluster=crossplane-cluster-1 --region=eu-central-1 --name=spot
```

### Step 3: Create Addon in EKS Cluster

Deploy the Kubecost addon to your EKS cluster:

```bash

aws eks create-addon --addon-name kubecost_kubecost --cluster-name crossplane-cluster-1 --region eu-central-1
```

### Step 4: Upgrade the EKS Cluster

Upgrade your EKS cluster to the latest version:

```bash

eksctl upgrade cluster --name crossplane-cluster-1 --region eu-central-1
```

### Step 5: Associate IAM OIDC Provider

Associate IAM OIDC provider with your EKS cluster:

```bash

eksctl utils associate-iam-oidc-provider --region=eu-central-1 --cluster=crossplane-cluster-1 --approve
```

### Step 6: Create IAM Service Account for EBS CSI Driver

Create an IAM service account for the AWS EBS CSI driver:

```bash

eksctl create iamserviceaccount   \
    --name ebs-csi-controller-sa   \
    --namespace kube-system   \
    --cluster crossplane-cluster-1   \
    --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy  \
    --approve \
    --role-only \
    --role-name AmazonEKS_EBS_CSI_DriverRole
```

Extract the ARN of the created role:

```bash

export SERVICE_ACCOUNT_ROLE_ARN=$(aws iam get-role --role-name AmazonEKS_EBS_CSI_DriverRole --output json | jq -r '.Role.Arn')
```

### Step 7: Deploy the AWS EBS CSI Driver

Deploy the AWS EBS CSI driver using the created service account:

```bash

eksctl create addon --name aws-ebs-csi-driver --cluster crossplane-cluster-1 \
    --service-account-role-arn $SERVICE_ACCOUNT_ROLE_ARN --force
```

### Step 8: Install Kubecost using Helm

Install Kubecost for cost monitoring:

```bash

helm upgrade -i kubecost \
oci://public.ecr.aws/kubecost/cost-analyzer --version 1.107.0 \
--namespace kubecost --create-namespace \
-f https://raw.githubusercontent.com/kubecost/cost-analyzer-helm-chart/develop/cost-analyzer/values-eks-cost-monitoring.yaml
``` 

### Step 9: Access Kubecost Dashboard

Forward the Kubecost port to access the dashboard:

```bash

kubectl port-forward --namespace kubecost deployment/kubecost-cost-analyzer 9090
```

## Conclusion

You have successfully managed node groups in your EKS cluster, set up IAM roles, deployed the AWS EBS CSI driver, and installed Kubecost for cost monitoring. These steps are crucial for efficient Kubernetes cluster management and cost optimization.
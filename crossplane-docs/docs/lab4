# Lab 4: Deploying AWS RDS and Kubernetes Application with Crossplane

## Overview

In this lab, you will learn how to use Crossplane to provision AWS RDS instances, DBSubnetGroups, and SecurityGroups. You'll also deploy a sample Kubernetes application that interacts with the provisioned RDS instance.

## Prerequisites

-   Access to an EKS cluster.
-   Crossplane installed on the EKS cluster.
-   AWS CLI installed and configured.

## Steps

### Step 1: Configure AWS Provider in Crossplane

Create a secret in Kubernetes to store your AWS credentials:

```bash
kubectl create secret generic crossplane-aws-secret \
-n crossplane-system \
--from-file=credentials=./aws-credentials.txt` 
```
### Step 2: Create Namespaces for the Application and Database

``` bash
kubectl create ns catalog
kubectl create ns ui
```
### Step 3: Configure Database Password

Generate a random password for the database and store it as a Kubernetes secret:

```bash
openssl rand -base64 12
kubectl create secret generic catalog-db-crossplane-passwd -n catalog --from-literal=password=$(openssl rand -base64 12)
```
### Step 4: Deploy AWS Resources using Crossplane

#### 4.1 Deploy a DBSubnetGroup

```yaml
# Source: chartlab4/templates/rds-dbgroup.yaml
apiVersion: database.aws.crossplane.io/v1beta1
kind: DBSubnetGroup
metadata:
  name: $(EKS_CLUSTER_NAME)-catalog-crossplane
  labels:
    app.kubernetes.io/created-by: eks-workshop
spec:
  forProvider:
    region: $(AWS_REGION)
    description: DBSubnet group
    subnetIds:
    - $(VPC_PRIVATE_SUBNET_ID_1)
    - $(VPC_PRIVATE_SUBNET_ID_2)
    - $(VPC_PRIVATE_SUBNET_ID_3)
    tags:
    - key: created-by
      value: eks-workshop-v2
    - key: env
      value: $(EKS_CLUSTER_NAME)
    - key: managed-by
      value: crossplane
  providerConfigRef:
    name: crossplane-default
```

#### 4.2 Deploy a SecurityGroup

```yaml
#Source: chartlab4/templates/rds-security-group.yaml
apiVersion: ec2.aws.crossplane.io/v1beta1
kind: SecurityGroup
metadata:
  name: $(EKS_CLUSTER_NAME)-catalog-crossplane
  labels:
    app.kubernetes.io/created-by: eks-workshop
spec:
  forProvider:
    region: $(AWS_REGION)
    description: SecurityGroup
    groupName: $(EKS_CLUSTER_NAME)-catalog-crossplane
    vpcId: $(VPC_ID)
    ingress:
      - fromPort: 3306
        toPort: 3306
        ipProtocol: tcp
        ipRanges:
          - cidrIp: "$(VPC_CIDR)"
    egress:
      # AWS will treat it as all ports any protocol
      - ipProtocol: '-1'
        ipRanges:
          - cidrIp: "0.0.0.0/0"
    tags:
    - key: created-by
      value: eks-workshop-v2
    - key: env
      value: $(EKS_CLUSTER_NAME)
    - key: managed-by
      value: crossplane
  providerConfigRef:
    name: crossplane-default
```

#### 4.3 Deploy a DBInstance

```yaml
#Source: chartlab4/templates/rds-instance.yaml
apiVersion: rds.aws.crossplane.io/v1alpha1
kind: DBInstance
metadata:
  name: $(EKS_CLUSTER_NAME)-catalog-crossplane
  labels:
    app.kubernetes.io/created-by: eks-workshop
spec:
  forProvider:
    region: $(AWS_REGION)
    allocatedStorage: 20
    dbInstanceClass: db.t4g.micro
    dbName: catalog
    engine: mysql
    engineVersion: "8.0"
    masterUsername: admin
    autogeneratePassword: true
    skipFinalSnapshot: true
    applyImmediately: true
    dbSubnetGroupNameRef:
      name: $(EKS_CLUSTER_NAME)-catalog-crossplane
    vpcSecurityGroupIDRefs:
      - name: $(EKS_CLUSTER_NAME)-catalog-crossplane
    masterUserPasswordSecretRef:
      key: password
      name: catalog-db-crossplane-passwd
      namespace: catalog
    tags:
    - key: created-by
      value: eks-workshop-v2
    - key: env
      value: $(EKS_CLUSTER_NAME)
    - key: managed-by
      value: crossplane
  writeConnectionSecretToRef:
    name: catalog-db-crossplane
    namespace: catalog
  providerConfigRef:
    name: crossplane-default
```

Apply these configurations with `kubectl apply`.

### Step 5: Deploy the Kubernetes Application

Deploy your application in the Kubernetes cluster:

```bash
kubectl apply -k https://github.com/itumor/crossplane-labs/tree/main/lab4/application
```
### Step 6: Verifying the Deployment

-   Check the status of AWS resources using AWS CLI or AWS Management Console.
-   Verify the application deployment in Kubernetes using `kubectl get pods -n ui`.

## Cleanup

Delete the resources once you're done with the lab:

```bash
kubectl delete -f [configuration-file]
kubectl delete secret catalog-db-crossplane-passwd -n catalog` 
```
## Conclusion

In this lab, you have successfully used Crossplane to provision AWS resources and deploy a Kubernetes application that interacts with these resources. This demonstrates the power of Crossplane in managing cloud-native applications and infrastructure as code.

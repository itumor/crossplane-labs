# Lab Document: Crossplane AWS S3 Provider Configuration

## Overview

This lab will guide you through the setup of a Crossplane AWS S3 provider using a secret for AWS credentials and creating an S3 bucket in the specified region.

## Prerequisites

-   Access to a Kubernetes cluster
-   Crossplane installed on the Kubernetes cluster
-   AWS account credentials

## Steps

### 1. Configure AWS Credentials

Edit the Crossplane ProviderConfig YAML to include your AWS credentials:


```yaml
`apiVersion: aws.upbound.io/v1beta1
kind: ProviderConfig
metadata:
  name: default
spec:
  credentials:
    source: Secret
    secretRef:
      namespace: crossplane-system
      name: aws-secret
      key: creds` 
```

Replace `<aws_access_key_id>` and `<aws_secret_access_key>` with your AWS access key ID and secret access key.

### 2. Create an S3 Bucket

Edit the S3 Bucket YAML to define your bucket configuration:

```yaml
apiVersion: s3.aws.upbound.io/v1beta1
kind: Bucket
metadata:
  name: crossplane-bucket-e017b4c8
spec:
  forProvider:
    region: eu-central-1
  providerConfigRef:
    name: default` 
```
Replace `eu-central-1` with your desired AWS region.

### 3. Configure the AWS S3 Provider

Edit the AWS S3 Provider YAML to specify the provider package:

```yaml
apiVersion: pkg.crossplane.io/v1
kind: Provider
metadata:
  name: provider-aws-s3
spec:
  package: xpkg.upbound.io/upbound/provider-aws-s3:v0.37.0` 
```
### 4. Apply Configurations

Apply the configurations to your Kubernetes cluster:

```bash
kubectl apply -f aws-credentials.yaml kubectl apply -f s3-bucket.yaml kubectl apply -f aws-s3-provider.yaml`
```

### 5. Verify

Check the status and logs to ensure the Crossplane AWS S3 provider and S3 bucket are successfully configured:
```bash
kubectl get provider,config,bucket
kubectl logs -l app=provider-aws-s3-controller -n crossplane-system` 
```

## Conclusion

You have successfully configured a Crossplane AWS S3 provider and created an S3 bucket. Refer to [Crossplane AWS Provider Documentation](https://docs.crossplane.io/v1.13/getting-started/provider-aws/) for more information.
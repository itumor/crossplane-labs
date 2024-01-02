# Lab Document: Crossplane Helm Release Configuration for Argo CD and Ingress NGINX

## Overview

This lab demonstrates configuring and deploying Argo CD and Ingress NGINX using Crossplane Helm releases in a Kubernetes environment. You'll learn how to create and apply Helm-based Crossplane configurations for efficient cluster management.

## Prerequisites

- Access to a Kubernetes cluster
- Crossplane installed on the Kubernetes cluster
- Basic understanding of Helm charts

### Checklist

- [ ] Define and Apply `ProviderConfig` for Helm
- [ ] Deploy Argo CD using Crossplane Helm Release
- [ ] Deploy Ingress NGINX using Crossplane Helm Release
- [ ] Verify the deployments

## Steps

### 1. Define and Apply ProviderConfig for Helm

Create a `ProviderConfig` for Helm to interact with your Kubernetes cluster:

<details> 
    <summary>provider-helm.yaml</summary>

```yaml
apiVersion: helm.crossplane.io/v1beta1
kind: ProviderConfig
metadata:
  name: helm-provider
spec:
  credentials:
    source: InjectedIdentity
```
</details>


Apply the ProviderConfig:
<details> 
    <summary>Apply the ProviderConfig:</summary>


``` bash

kubectl apply -f provider-helm.yaml

```
</details>

### 2. Deploy Argo CD using Crossplane Helm Release
Deploy Argo CD by defining a Release object:

<details> 
    <summary>argo-cd-release.yaml</summary>

```yaml
apiVersion: helm.crossplane.io/v1beta1
kind: Release
metadata:
  name: argo-cd
spec:
  forProvider:
    chart:
      name: argo-cd
      repository: https://argoproj.github.io/argo-helm
      version: 5.47.0
    namespace: argo-cd
  providerConfigRef:
    name: helm-provider
```
</details>
Apply the Argo CD release:

<details> 
    <summary>argo-cd-release.yaml</summary>

```bash
kubectl apply -f argo-cd-release.yaml
```

</details>

### 3. Deploy Ingress NGINX using Crossplane Helm Release
Similarly, deploy Ingress NGINX:

<details> 
    <summary>ingress-nginx-release.yaml</summary>

```yaml
apiVersion: helm.crossplane.io/v1beta1
kind: Release
metadata:
  name: ingress-nginx
spec:
  forProvider:
    chart:
      name: ingress-nginx
      repository: https://kubernetes.github.io/ingress-nginx
      version: 4.8.3
    namespace: ingress-nginx
  providerConfigRef:
    name: helm-provider
```
</details>

Apply the Ingress NGINX release:

<details> 
    <summary>Apply the Ingress NGINX release:</summary>

```bash
kubectl apply -f ingress-nginx-release.yaml
```
</details>

### 4. Verify the Deployments
After applying the configurations, verify that both Argo CD and Ingress NGINX are correctly deployed and running in your cluster.

### Conclusion
You have successfully configured and deployed Argo CD and Ingress NGINX using Crossplane Helm releases. This lab demonstrates the power of Crossplane in managing complex Kubernetes deployments with ease and efficiency.

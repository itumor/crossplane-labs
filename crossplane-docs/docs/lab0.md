# Lab-00 : Installing EKS, Crossplane, and Setting up the Development Environment

This lab is a step-by-step guide to install EKS, Crossplane, and set up the development environment. It is essential to complete this lab as it serves as the foundation for the subsequent steps.

## Prerequisites
Before starting this lab, ensure that you have the following:

- Access to an AWS account
- Basic knowledge of AWS services and Kubernetes

## Lab Instructions
Follow the instructions below to install EKS, Crossplane, and set up the development environment:

1. Install the AWS CLI by following the instructions in the [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

2. Install eksctl by running the following command: `choco install eksctl`. For more details, refer to the [eksctl installation guide](https://eksctl.io/installation/).

3. Install Helm by following the instructions in the [Helm documentation](https://helm.sh/docs/intro/install/).

4. Use AWS CloudShell for an integrated AWS CLI experience. For more information, refer to the [AWS CloudShell documentation](https://aws.amazon.com/cloudshell/).

5. Create a Kubernetes cluster using eksctl by running the following command: `eksctl create cluster -f cluster.yaml`. Make sure to provide the appropriate configuration in the `cluster.yaml` file. For more details, refer to the [eksctl documentation](https://eksctl.io/).


<details>
  <summary>cluster.yaml</summary>

```yaml
# A simple example of ClusterConfig object:
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: crossplane-cluster-1
  region: eu-central-1

#nodeGroups:
#  - name: ng-1
#    instanceType: m5.large
#    desiredCapacity: 1

managedNodeGroups:
- name: spot
  instanceTypes: ["t4g.medium","t4g.small"]
  spot: true
  minSize: 2
  maxSize: 4

managedNodeGroups:
- name: spot
  instanceTypes: ["t4g.medium","t4g.small"]
  spot: true
  minSize: 2
  maxSize: 4


#cloudWatch:
    #clusterLogging:
        # enable specific types of cluster control plane logs
        # enableTypes: []
        # all supported types: "api", "audit", "authenticator", "controllerManager", "scheduler"
        # supported special values: "*" and "all"

```
</details>

6. Follow the steps in the [Crossplane documentation](https://docs.crossplane.io/v1.13/getting-started/provider-aws/) to install Crossplane and the AWS provider. This includes installing the Crossplane Helm chart and configuring the AWS provider with the necessary credentials.

7. Set up your Kubeconfig file to connect to your Amazon EKS cluster. Follow the instructions in the [Amazon EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html) based on your operating system.

8. Additional Steps:
   - Install the AWS CLI MSI by downloading it from [here](https://awscli.amazonaws.com/AWSCLIV2.msi).
   - Configure the AWS CLI by running the `aws configure` command.

Please note that this lab is a prerequisite and serves as the base for installing EKS, Crossplane, and setting up the development environment. It is important to complete this lab before proceeding to the next steps.

Feel free to modify the content as needed to fit your specific requirements.
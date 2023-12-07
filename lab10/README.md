# Crossplane Lab: Ansible Integration

## Introduction
In this lab, you will learn how to integrate Ansible with Crossplane to manage infrastructure resources.

## Prerequisites
Before starting this lab, make sure you have the following:
- A working Crossplane installation
- Ansible installed on your local machine

## Lab Steps
1. Install the Crossplane Ansible Provider:
     ```bash
     $ kubectl crossplane install provider crossplane/provider-ansible:v0.18.0
     ```

2. Create a Crossplane ProviderConfig to connect to your Ansible control node:
     ```yaml
     apiVersion: ansible.crossplane.io/v1alpha1
     kind: ProviderConfig
     metadata:
         name: ansible-provider-config
     spec:
         connection:
             type: ansible
             config:
                 ansible:
                     host: <ansible-control-node-ip>
                     port: <ansible-control-node-port>
                     username: <ansible-username>
                     password: <ansible-password>
     ```

3. Create a Crossplane Provider to use the Ansible ProviderConfig:
     ```yaml
     apiVersion: ansible.crossplane.io/v1alpha1
     kind: Provider
     metadata:
         name: ansible-provider
     spec:
         providerConfigRef:
             name: ansible-provider-config
     ```

4. Create a Crossplane Composition that defines the desired infrastructure resources using Ansible playbooks:
     ```yaml
     apiVersion: ansible.crossplane.io/v1alpha1
     kind: Composition
     metadata:
         name: my-composition
     spec:
         playbook: |
             ---
             - name: Create EC2 instance
                 hosts: localhost
                 tasks:
                     - name: Create EC2 instance
                         ec2_instance:
                             instance_type: t2.micro
                             image: ami-0c94855ba95c71c99
                             key_name: my-key-pair
                             region: us-west-2
                             count: 1
                             state: present
     ```

5. Create a Crossplane ResourceClaim that references the Composition to provision the infrastructure resources:
     ```yaml
     apiVersion: ansible.crossplane.io/v1alpha1
     kind: ResourceClaim
     metadata:
         name: my-resource-claim
     spec:
         compositionRef:
             name: my-composition
     ```

6. Verify that the infrastructure resources are provisioned by checking the status of the ResourceClaim:
     ```bash
     $ kubectl get resourceclaim my-resource-claim -o yaml
     ```

## Conclusion
Congratulations! You have successfully integrated Ansible with Crossplane to manage infrastructure resources. You can now leverage the power of Ansible playbooks to provision and manage your infrastructure using Crossplane.

## Next Steps
- Explore more advanced use cases of Ansible integration with Crossplane.
- Learn how to manage infrastructure resources using other providers supported by Crossplane.

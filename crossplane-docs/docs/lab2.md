# Lab Document: Crossplane S3 Bucket CompositeResourceDefinition Configuration

## Overview

This lab guides you through the configuration of a CompositeResourceDefinition (CRD) for managing AWS S3 Buckets using Crossplane. The CRD allows you to provision S3 Buckets in a Kubernetes environment.

## Prerequisites

-   Access to a Kubernetes cluster
-   Crossplane installed on the Kubernetes cluster

### Checklist

 - [ ] Define and Apply the CompositeResourceDefinition
 - [ ] Create a Composition for S3Bucket
 - [ ] Instantiate an S3Bucket resource

## Steps

### 1. Define and Apply the CompositeResourceDefinition

Edit the CompositeResourceDefinition YAML to define the structure for managing S3 Buckets:

<details> 
	<summary>s3buckets-crd.yaml</summary>

```yaml
apiVersion: apiextensions.crossplane.io/v1
kind: CompositeResourceDefinition
metadata:
  name: s3buckets.example.org
spec:
  group: example.org
  names:
    kind: S3Bucket
    plural: s3buckets
  versions:
  - name: v1alpha1
    served: true
    referenceable: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              parameters:
                type: object
                properties:
                  region:
                    type: string
                required:
                - region
            required:
            - parameters` 
```
</details>

Apply the configuration to your Kubernetes cluster:

<details> 
	<summary>Apply s3buckets-crd </summary>

```bash
kubectl apply -f s3buckets-crd.yaml 
```
</details>

### 2. Create a Composition for S3Bucket

Edit the Composition YAML to specify how the S3Bucket resource maps to the underlying AWS S3 Bucket:

<details>
	 <summary>s3buckets-composition.yaml</summary>

```yaml
apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
  name: s3buckets
spec:
  compositeTypeRef:
    apiVersion: example.org/v1alpha1
    kind: S3Bucket
  resources:
    - name: bucket
      base:
        apiVersion: s3.aws.upbound.io/v1beta1
        kind: Bucket
        spec:
          forProvider:
            tags:
              Name: SampleBuckets
          publishConnectionDetailsTo:
            name: s3-kubernetes-secret
          writeConnectionSecretToRef:
            name: s3-secret
            namespace: default
      patches:
      - type: FromCompositeFieldPath
        fromFieldPath: metadata.name
        toFieldPath: spec.forProvider.name
      - type: FromCompositeFieldPath
        fromFieldPath: metadata.name
        toFieldPath: metadata.annotations.crossplane.io/external-name
      - type: FromCompositeFieldPath
        fromFieldPath: spec.parameters.region
        toFieldPath: spec.forProvider.region
```
</details>

Apply the Composition configuration:
<details> 
	<summary>Apply Composition </summary>

```bash
kubectl apply -f s3buckets-composition.yaml
```
</details>


### 3. Instantiate an S3Bucket resource

Create an instance of the S3Bucket resource to provision an AWS S3 Bucket:

<details>
	 <summary>my-s3-bucket.yaml</summary>

```yaml
apiVersion: example.org/v1alpha1
kind: S3Bucket
metadata:
  name: my-s3-bucket
spec:
  parameters:
    region: eu-central-1
 ```

</details>
Apply the S3Bucket resource configuration:

<details>
	 <summary>apply bucket</summary>

```bash
kubectl apply -f my-s3-bucket.yaml
```

</details>


## Conclusion

You have successfully defined a CompositeResourceDefinition for S3 Buckets, created a Composition for mapping to the AWS S3 Bucket resource, and instantiated an S3Bucket resource. This allows you to provision S3 Buckets in your Kubernetes environment using Crossplane. For more information, refer to [Crossplane AWS Provider Documentation](https://docs.crossplane.io/v1.13/getting-started/provider-aws/).
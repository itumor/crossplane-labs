https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
https://eksctl.io/installation/
https://helm.sh/docs/intro/install/

https://awscli.amazonaws.com/AWSCLIV2.msi
(choco install eksctl)

aws configure

eksctl create cluster -f cluster.yaml

https://docs.crossplane.io/v1.13/getting-started/provider-aws/


AWS CloudShell


https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html


eksctl create nodegroup \
  --cluster=crossplane-cluster-1 --region=eu-central-1\
  --managed --spot --name=ng-spot \
  --instance-types=m5.large,m4.large,m5d.large,m5a.large,m5ad.large,m5n.large,m5dn.large\
  --nodes-min=2\
  --nodes-max=5
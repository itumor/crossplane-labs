from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import InternetGateway, ELB
from diagrams.aws.compute import EKS
from diagrams.k8s.compute import Pod
from diagrams.aws.database import RDS

with Diagram("Lab23 EKS Architecture", show=False, direction="TB"):
    internet = InternetGateway("Internet")

    with Cluster("AWS Elastic Load Balancer"):
        elb = ELB("ELB")

    with Cluster("Amazon EKS Cluster"):
        eks_cluster = EKS("EKS Cluster")
        with Cluster("Pods"):
            pods = [Pod("Pod-1"), Pod("Pod-2")]



    rds = RDS("Amazon RDS")

    internet >> elb >> eks_cluster
    eks_cluster >> Edge(label="Traffic", color="firebrick") >> pods
    pods >>  rds

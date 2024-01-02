from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import InternetGateway, ELB, Route53
from diagrams.aws.compute import EKS
from diagrams.k8s.compute import Pod
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.storage import S3




with Diagram("Lab24 Web Application Complex Architecture", show=False, direction="TB"):
    internet = InternetGateway("Internet")

    with Cluster("Amazon Route 53"):
        route53 = Route53("Route 53")

    with Cluster("AWS Elastic Load Balancer"):
        elb = ELB("ELB")

    with Cluster("Amazon EKS Cluster"):
        eks_cluster = EKS("EKS Cluster")
        with Cluster("Pods"):
            pods = [Pod("Pod-1"), Pod("Pod-2")]



    rds_primary = RDS("Amazon RDS (Primary)")
    elasticache = ElastiCache("Amazon ElastiCache")
    s3 = S3("Amazon S3")

    internet >> route53 >> elb >> eks_cluster
    eks_cluster >> Edge(label="Traffic", color="firebrick") >> pods
  
    pods >> rds_primary
    pods >> elasticache
    pods >> s3
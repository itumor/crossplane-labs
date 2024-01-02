from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import InternetGateway
from diagrams.aws.network import ElasticLoadBalancing
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS

with Diagram("lab21 Web Application Architecture", show=False, direction="TB"):
    internet = InternetGateway("Internet")

    with Cluster("Auto Scaling Group"):
        elb = ElasticLoadBalancing("ELB")
        with Cluster("EC2 Instances"):
            instances = [EC2("EC2-1"), EC2("EC2-2")]

    db = RDS("Application Database")

    internet >> elb >> instances
    instances >> Edge(label="Traffic", color="firebrick") >> db

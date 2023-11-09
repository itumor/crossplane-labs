from diagrams import Diagram, Cluster
from diagrams.aws.network import InternetGateway, APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb

with Diagram("lab22 Web Serverless Architecture", show=False, direction="TB"):
    internet = InternetGateway("Internet")

    with Cluster("AWS API Gateway"):
        api_gateway = APIGateway("API Gateway")
        with Cluster("AWS Lambda Functions"):
            lambda_function = Lambda("Lambda Function")

    dynamodb = Dynamodb("DynamoDB Table")

    internet >> api_gateway >> lambda_function
    lambda_function >> dynamodb

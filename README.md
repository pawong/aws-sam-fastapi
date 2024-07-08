# AWS SAM FastAPI Demo

AWS + SAM + FastAPI + Amazon API Gateway + AWS Lambda + Cognito - Demo

## Prerequisites

### for Deployment:

- AWS Account
- AWS Command Line Tool (CLI) - `aws` [aws cli installation guide]
- AWS Serverless Application Model (SAM) with a command line tool AWS SAM CLI - `sam` [sam cli installation guide]

### for Development:

- Python
- Docker; if you don't have it yet, follow the [installation instructions];
- Docker Compose; refer to the official documentation for the [installation guide].
- Pre-commit; refer to the official documentation for the [pre-commit](https://pre-commit.com/#install).

## Run tests and type checking

Create isolated Python environment `python -m venv venv` and activate it `source venv/bin/activate`

Install all necessary dependencies: `pip install -r requirements-dev.txt`

Run tests:

    python -m pytest tests -v  # increase verbosity

with coverage report:

    python -m pytest --cov=app tests

Run type checking:

    mypy backend

## Build the Stack

For building the stack run:

    sam build -t sam-template.yaml

## Deploy the Stack

For deploying appropriate Stack (`dev`, `prod`) run (with guided prompts):

    sam deploy --guided --capabilities CAPABILITY_IAM --config-env {dev|prod}

For newly created API Gateway endpoint URL see CloudFormation outputs, ex.:

    CloudFormation outputs from deployed stack
    -------------------------------------------------------------------------------------------------------------------------------
    Outputs
    -------------------------------------------------------------------------------------------------------------------------------
    Key                 CognitoUserPoolId
    Description         Cognito User Pool ID
    Value               us-west-2_uDaOCj6M4

    Key                 FastAPI
    Description         API Gateway endpoint URL
    Value               https://ymixsvbpdj.execute-api.us-west-2.amazonaws.com/dev

    Key                 CognitoAppClientId
    Description         Cognito App Client ID
    Value               1elb5jor6uipquvagdbg5lng3t
    -------------------------------------------------------------------------------------------------------------------------------

Service will be available on the following routes:

    https://ymixsvbpdj.execute-api.us-west-2.amazonaws.com/dev
    https://ymixsvbpdj.execute-api.us-west-2.amazonaws.com/dev/docs
    https://ymixsvbpdj.execute-api.us-west-2.amazonaws.com/dev/openapi.json

## Delete the Stack

For deleting the Stack run:

    sam delete --stack-name your-stack-name

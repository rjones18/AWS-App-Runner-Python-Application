# AWS-Elasticbeanstalk-Application

In this project, I created a flask application using Python, HTML, and CSS. The application takes the information that a user puts into the field and pushes it to my DynamoDB table in AWS. Once the information is stored, I am sent a SNS notification via email that new user signed up. The application was deployed on to Elastic Beanstalk and the custom domain was created using Route 53. The EC2 instances are being managed using Systems Manager to perform patch management on the servers. The access logs on the application load balancer are being sent to Amazon S3 and where they are being encrypted at rest using KMS. To review the logs I query them using Athena. Also when information is added/modified in the DynamoDB table it will trigger a Lambda Function that captures the users inputs and puts it into CloudWatch Logs for monitoring. 

Link to Website: https://rjcloud.reggiestestdomain.com/ (VM Currently Turned Off)



## Application Breakdown

The application is broken down into the architecture below:

![elasticbeanstalkapp](https://github.com/rjones18/Images/blob/main/Elastic%20Beanstalk%20Site.10drawio.png)



### Frontend

- HTML
- CSS
- [Bootstrap via Bootswatch](https://bootswatch.com/)


### Backend 

- [Python](https://www.python.org/) 
- [Flask (Python Framework)](https://flask.palletsprojects.com/en/1.1.x/)

### Database 

- [DynamoDB](https://aws.amazon.com/dynamodb/)


### Deployment Platform

- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)





### DNS

- [Route 53](https://aws.amazon.com/route53/)


### SSL Certificate

- [Certificate Manager](https://aws.amazon.com/certificate-manager/)




### Notification Service

- [SNS](https://aws.amazon.com/sns/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)


### Serverless Function

- [Lambda](https://aws.amazon.com/lambda/)


### Management Tools

- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)


### Key Management Service

- [KMS](https://aws.amazon.com/kms/)


### Storage

- [S3 Bucket](https://aws.amazon.com/s3/)


### Query Service

- [Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)


### IDE

- [Visual Studio Code](https://code.visualstudio.com/)

### CLI

- [EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)


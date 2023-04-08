# AWS-Elasticbeanstalk-Application

In this project, I developed a robust Flask application using a combination of Python, HTML, and CSS. The application was designed to capture user data and store it in an Amazon DynamoDB table hosted on AWS. Once the user data is stored, the application triggers an AWS Simple Notification Service (SNS) notification that sends an email to alert me that a new user has signed up.

To facilitate deployment, I leveraged AWS Elastic Beanstalk, which automatically scales and manages the infrastructure needed to run the application. In addition, I created a custom domain using AWS Route 53 and configured a secure SSL/TLS encryption via Certificate Manager to protect the application.

By integrating this modern technology stack with AWS's powerful cloud computing infrastructure, I was able to build a highly scalable, reliable, and secure Flask application that can handle large amounts of user data while maintaining the highest level of data privacy and security.


Link to Website: https://rjcloud.reggiestestdomain.com/ (VM Currently Turned Off)



## Application Breakdown

The application is broken down into the architecture below:

![elasticbeanstalkapp](https://github.com/rjones18/Images/blob/main/Elastic%20Beanstalk%20Site2.drawio.png)

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


 ### IDE

 - [Visual Studio Code](https://code.visualstudio.com/)

 ### CLI

 - [EB CLI](https://docs.aws.amazon.com/)

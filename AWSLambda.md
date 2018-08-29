# AWS Lambda
## Intro to AWS Lambda
In this talk we will be going through feature and functions of AWS Lambda. We will be looking at how to get started , the use cases and some examples using Python 3.5 programming language.

## Goals of this Talk
1) Get to Know Lambda
2) Go through the Console
3) Know the the limitations
4) Look at some examples.

So by the end of the talk the take away would be that you know what and where to use Lambda and are able to write small functions to test and play with lambda.

## Lambda 101
AWS Lambda is an event driven purely compute resource that allows users to deploy code directly and not worry about infrastructure maintenance. Think of it as pushing just the python script as opposed to instantiating the EC2 and updating the OS, maintaining security patches, installing the language with dependant libraries and then running your code. Lambda does away with all of that. Just Fire and Forget.

You can find the Lambda service in the Compute section of the list of services in AWS console.

Lambda is pretty inexpensive, while you will get billed for a minimum of 100ms regardless of the actual runtime, you are only getting billed for the use time and not anything else. When comparing that with the traditional cost of running a piece of code on ec2, lambda fares well. The cost for running a Lambda function is low enough to make economic sense for the industry to explore and exploit the serverless option.

[Apache openwhisk](https://openwhisk.apache.org/)   is an open source example of the serverless application.

## Dashboard 
In this talk we will be using the Dahsboard to launch the Lambda function

## Event Trigger
One of the many advantages of Lambda is ease of wiring it with services like Cloudwatch, S3 and others which serve as the input for the function. So we are essentially putting lego pieces together. 

## Example 1
The main function with Lambda in python looks like this
<pre class="devsite-terminal devsite-click-to-copy">
def handler(event,context):
    return "What's Up!"
</pre>

Here *handler* is the name of the function, event and context are the default parameters passed to the function with return being the output

When running lambda you will need the name of the python file and the name of the function that you want to call defined in the console. 

By default, Lambda is going to log any function you run. You can customize the log if you need more details. 

## Things to Keep Note
*Cold Start* This is the phenomenon of the function taking a longer time when it initializes for the first run. Successive runs take much shorter time. Cold start times are different for various programming languages

## Limitations
1) Its important to note that AWS Lambda is not for managing underlying resources.
2) Retries happen when functions fail. Functions fail if it maxes out on provided time or if the input is wrong or unparseble and other contraints
3) scope of the functions should be self contained and stateless

## Use Cases
Now, where can lambda be used. One example of using Lambda is in ETL. A common and often necessary activity in entreprises is to be able to load data from databases to datawarehouses on a daily basis. This is done through the Extract Transform and Load routine. The code written to do this connects to the source database, takes all the records entered for that day , transforms the schema to match the target database and loads into the respective tables. AWS Redshift is a datawarehouse commonly used in cloud architectures to store data. Data is extracted from source databases like MongoDB and is stored in S3 as a flat file also called a text file which triggers a EC2 containing the ETL code to load the data into redshift. 

The new way of doing the routine would be to set a trigger for the moment new data is stored in S3 , the trigger launches the code deployed in a Lambda function that connects to S3 and redshift and transforms and loads data into the target tables. The advantage: Cost. With Lambda one does not have to deal with EC2 instance costs and maintenances. 


## Resources
1) [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
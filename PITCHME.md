# Intro to AWS Lambda

NoVaLUG Meetup

8th-Sept-2018

[@sidhu177](https://twitter.com/sidhu177?lang=en) 

[github.com/sidhu177](https://github.com/sidhu177)

---

## Goals of this Talk
 - Get to Know Lambda
 - Go through the Console
 - Know the limitations
 - Look at some examples
 - Resources

---

### Intro to AWS Lambda
In this talk we will be going through feature and functions of AWS Lambda. We will be looking at how to get started , the use cases and some examples using Python 3.5 programming language.

---

### Lambda 101
AWS Lambda is an event driven purely compute resource that allows users to deploy code directly and not worry about infrastructure maintenance. Think of it as pushing just the python script as opposed to instantiating the EC2 and updating the OS, maintaining security patches, installing the language with dependant libraries and then running your code. Lambda does away with all of that. Just Fire and Forget.

+++

### Departure from Previous Architectures

With on demand serverless compute, Lambda is replacing EC2s in traditional architectures and is demonstrating performance all the while reducing cost.

+++

### Cost Benefit
 - Billed in milli seconds 
 - steps in 100 milli seconds
 - On demand run and scale as you go
needless to say, lambda offers some impressive cost benefits that makes it hard to ignore
---

### Dashboard 
In this talk we will be using the Dahsboard to launch the Lambda function
![Dashboard](assets/image/Lambda_Dashboard.JPG)

+++ 

To launch a lambda function you have 3 options 
* start from scratch
* use a readymade blueprint
* use a repo that AWS offers

+++ 

Lets choose start from scratch for a quick example

you will need to 
 - name your function
 - choose the language 
 - choose a role

+++

Next is the Lambda console. Notice that you have an embedded code editor. 

Thats the cloud9 integration right in your browser that allows you to edit code and run realtime. 

*fun fact: its powered by linux*

---

### Go Run
When running lambda you will need the name of the python file and the name of the function that you want to call defined in the console. 

The main function with Lambda in python looks like this
```
def handler(event,context):
    return "What's Up!"
```

Here *handler* is the name of the function, event and context are the default parameters that have to be passed to the function with return being the output

+++

*event* is usually used to pass in triggers from other services

*context* is used to get the remaining time information

+++

By default, Lambda is going to log any function you run. You can customize the log if you need more details.

Logging and Exceptions are handled through cloud watch logs. You will see the exception used for the failure displayed on the console and on the log

+++

Now for a small example demonstrating the use of lambda console and the levers that we can use to make changes to lambda runtime.

+++


```
def lambda_handler(event,context):
    calc = 2**3**2
    print(calc)
    print("Remaining Time in MilliSeconds: " + str(context.get_remaining_time_in_millis()))
    print("This is the RequestID: " + str(context.aws_request_id))
    return "End of Lambda Function"
```
+++

Now lets look at the console, we have
 - the return value
 - the printed message
 - the duration it took to run
 - And max memory used

---

### Event Trigger
One of the many advantages of Lambda is ease of wiring it with services like Cloudwatch, S3 and others which serve as the input for the function. So we are essentially putting lego pieces together

+++

### Different Call Types
 - Asynchronous : Anytime you fire a function without an order and do not return an output
 - Synchronous : When order of recieving the request and returning an output matter
 - Push : Services connected to Lambda have the permission to input to Lambda
 - Pull : Lambda has the permission to ask for data from other services like S3, cloudwatch

+++

### Event Source Mapping
Adding a trigger from the given list to your lambda function is in AWS Lingo "Event Source Mapping"

---

### Limitations
 - Its important to note that AWS Lambda is not for managing underlying resources.
 - Retries happen when functions fail. Functions fail if it maxes out on provided time or if the input is wrong or unparseble and other contraints
 - scope of the functions should be self contained and stateless

+++

### Things to Keep Note
*Cold Start* This is the phenomenon of the function taking a longer time when it initializes for the first run. Successive runs take much shorter time. Cold start times are different for various programming languages

---
### Step Functions 

The SAM example goes here

+++

### Serverless Application Model

---

### Use Cases
Now, where can lambda be used. One example of using Lambda is in ETL.

---

### Resources
1) [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

**What is EC2 ?**



* EC2 (Elastic Compute Cloud) instances are virtual servers in the cloud that enable users to run applications.

* It is a powerful tool that can be used to run a variety of applications, including web servers, databases, and big data processing systems in a scalable, flexible, and cost-effective manner. 


* EC2 instances are used by individuals, small businesses, and large enterprises to host websites, run applications, and process data. 

* EC2 instances are a fundamental building block of the AWS cloud, and they provide users with complete control over their computing resources.

**How to create an EC2 instance on AWS**

To create an EC2 instance on AWS, you will need to follow these steps:

**Step 1 : Go to the AWS console and log in to your account.**

* To create an EC2 instance, you must first log in to the AWS console. If you don't have an AWS account yet, you can create one for free.

![alt text](img/AWS_FREETIER.png) 

To create your free tier account click [Here](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)


**Step 2: Navigate to EC2**

Once you're logged in to the AWS console, navigate to the EC2 dashboard by clicking on the Launch a virtual machine  link .

![alt text](img/aws_console.png) 



**Step 3: Launch an Instance**

Click the "Launch Instance" button to launch a new EC2 instance.

Add a name of your choice for your new instance as shown below.

![alt text](img/ec2_instance1.png) 


***Step 4: Choose an Instance Type***

In this step, you can choose the instance type that best suits your needs based on the CPU, memory, and storage requirements of your application.


Make chose Ubuntu for your EC2 Instance

![alt text](img/ec2_instance2.png)




![alt text](img/ec2_instance3.png)

> * Note <br>
 EC2 instances on AWS not in Free Tier will incur charges for usage, varying based on instance type, region, and usage time. Select Free Tier eligible types to avoid unexpected charges.

**Step 4: Create a Key Pair**

A Key pair is a set of security credentials used to authenticate a user's access to an EC2 instance. 

* Under  the Key Pair heading, click ```Create  new Key Pair```.

* In the "Create Key Pair" dialog box, enter a name for your new key pair in the ```Key pair name``` field. This name should be unique and easy to remember.

* Click ```Create  key pair```.



![alt text](img/KEY1.png)



> * ***The console will download a .pem file containing your private key. Save this file in a safe place.(your current working directory)***



 **Step 5: configure HTTP and HTTPS access**

  To enable  both  HTTP and HTTPS access in an EC2 instance on AWS,tick on both ```Allow HTTPS traffic from the internet```   and   ```Allow HTTP traffic from the internet```  
 

![alt text](img/ec2_instance4.png) 


 **Connecting to an EC2 instance**

 There are two ways to connect to an EC2 instance:

* Using SSH
* Using EC2 Instance Connect


In this tutorial we are going to use  ``` SSH``` 

 To use SSH, you will need to:

* Go to the Instances page, select the instance that you want to connect to   and  Click Connect.

![alt text](img/ec2_instance6.png) 


* On the Connect To Your Instance page, choose SSH Client    and copy the ssh command   and paste it in the cmd

> * make sure you are in the folder that you saved your ```.pem file containing your private key```

![alt text](img/ec2_instance7.png) 


* Use the ssh command to connect to your EC2 instance.


The syntax for the ssh command is:

```bash
ssh -i <key_file> <user>@<instance_ip_address> 
``` 

Explanation 

* ```ssh``` : This is the command to initiate an SSH connection to a remote host.

* ```-i  twitter_ec2_key.pem``` : This option specifies the private key file to use for authentication. In this case, the private key file is ```twitter_ec2_key.pem```.

* ```ubuntu``` : This is the username to use for the SSH connection. In this case, the username is ```ubuntu```.

* ```@ec2-54-165-148-57.compute-1.amazonaws.com``` : This is the hostname or IP address of the remote machine to connect to. In this case, the hostname is ```ec2-54-165-148-57.compute-1.amazonaws.com```.

> This SSH command is connecting to a remote EC2 instance with the IP address of "ec2-54-165-148-57.compute-1.amazonaws.com" using the "ubuntu" username and the private key file "twitter_ec2_key.pem" for authentication.


* Once you are connected to your EC2 instance, you will be able to run commands on the instance.If your cmd writes the as shown below then you have successfully connected to your ec2 instance.

![alt text](img/success.png)



**Installing packages on an EC2 instance running Ubuntu**

**Step 1: Update the Package List**

Before installing any packages, it's a good practice to update the package list on your EC2 instance. To do so, run the following command:

```
sudo apt-get update
```

**Step 2: Install Python3 and Pip**

To install Python3 and Pip, you can run the following command:

```bash
sudo apt install python3-pip
```

**Step 3: Install the Desired Packages**

Once Python3 and Pip are installed, you can install the desired packages using the pip command. For example, to install Apache Airflow, you can run the following command:

``` bash
sudo pip install apache-airflow
```

* To install Pandas, you can run the following command:

``` bash
sudo pip install pandas 
```


* To install S3fs, you can run the following command:


``` bash
sudo pip install s3fs
```

> * Note <br>  S3fs is a FUSE (Filesystem in Userspace) based file system that allows you to mount an Amazon S3 bucket as a local file system on your EC2 instance. This means that you can use S3fs to access and manipulate the files and objects stored in your S3 bucket as if they were local files on your EC2 instance.


* To install snsscrape, you can run the following command:

``` bash
sudo pip install snscrape
```

> * Snscrape is a Python package that allows you to scrape social media data from various platforms such as Twitter, Instagram, and TikTok.

> * Snscrape uses web scraping techniques to extract data from social media platforms, and it works by sending HTTP requests to the respective platform's API and parsing the response data. 


**Step 4: Verify the Installation**

After installing the packages, you can verify the installation by running the respective commands for each package. For example, to verify the installation of Apache Airflow, you can run the following command:

``` bash
airflow version
```


**Step 5 : Running Airflow  Server  in EC2 instance**



``` bash
airflow standalone
```

> * Note  <br>
Once Airflow is ready copy the Username and Password   and save it somewhere safe.

**Allow your Ip address to have access to your EC2 Instance**

* Select the instance that you want to allow access to


![alt text](img/security1.png)


* In the bottom panel, click on the "Security" tab  and click on the security group

![alt text](img/security2.png)


* Click the "Edit inbound rules" button and on the left

![alt text](img/security3.png)


* In the "Edit inbound rule" section, select the protocol and port you want to allow access to. For example, to allow SSH access, set the type to "SSH", the protocol to "All", and the port range to "All",  and Type to all traffic as shown below

* In the "Source" field, select "Anywhere" to automatically add your current IP address to the rule.


* Click the "Save" button to save your changes.

![alt text](img/security4.png)

> * This is done only in the development enviroment annd not recomended for the production enviroment due to security issues


**Accessing the airflow Ui**

* Select the instance that you want to connect to.

* Under Instance summary  look for the Public IPv4 DNS  and copy it 

![alt text](img/publicip.png)



* Open a new tab on your browser  and paste the Public IPv4 DNS   and add :8080 at the end since 8080   is the port being used by airflow


![alt text](img/airflow.png)


* Add the username and password  that you have previous saved and if its successful you will see the airflow ui as shown below

![alt text](img/airflow2.png)


**Creating an ETL pipeline on Airflow**

**ETL pipeline**

* An ETL pipeline is a process for extracting data from one source, transforming it, and loading it into another source.

* In this case the data is extracted from twitter and then transformed  and the loaded into Amazon Simple Storage Service (S3).

* Amazon Simple Storage Service (S3)  is  a a cloud storage service that provides a scalable, durable, and cost-effective way to store data. S3 buckets can be used to store a variety of data, including structured, semi-structured, and unstructured data.


**Step 1: Create a Python file for your ETL code**

* The first step is to create a new Python file to store your ETL code. 

* To do this, open your preferred text editor or IDE and create a new file.

* You can name the file ETL.py or choose a more descriptive name of your choice.

**Step 2: Import the necessary libraries**

* Once you have created the Python file, the next step is to import the necessary libraries for your ETL process.


```python
# Import the snscrape library for accessing Twitter data
import snscrape.modules.twitter as sntwitter

# Import the pandas library for data manipulation and analysis
import pandas as pd

# Import the json library for working with JSON data
import json

# Import the datetime library for working with dates and times
from datetime import datetime

# Import the s3fs library for accessing data stored in Amazon S3
import s3fs
```
**Step 3: Write the code  for the ETL**

* Now it's time to start writing the code to perform each step  of the ETL pipeline. 

* This will involve calling the appropriate functions and methods from the libraries that we  have  imported earlier.

```python
def  ETL_Datapipeline():
    # Creating list to append tweet data to
    attributes_container = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid since:2021-07-05 until:2022-07-06').get_items()):
        if i>150:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
        
    # Creating a dataframe to load the list
    tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    
    #exports the  contents  of   tweets_df  to a CSV file
    df = tweets_df.to_csv('covid_data.csv')
```


**Step 4: Create an Airflow DAG**

* The first step is to create a new DAG in Airflow. To do this, open your preferred text editor or IDE and create a new file. 


* You can name the file Airflow_DAG.py or choose a more descriptive name of your choice.

**Step 5: Import the necessary libraries  for the DAG**

```PYTHON
# Import timedelta for working with time intervals
from datetime import timedelta

# Import DAG for defining DAGs in Airflow
from airflow import DAG

# Import PythonOperator for defining Python tasks in DAGs
from airflow.operators.python_operator import PythonOperator

# Import days_ago for working with dates in Airflow
from airflow.utils.dates import days_ago

# Import datetime for working with dates and times
from datetime import datetime

# Import the ETL_Datapipeline function for running the Twitter ETL process
from ETL import ETL_Datapipeline
```

**Step 6: Define the DAG structure**


* Define DAG structure and default arguments for the DAG

```# Define default arguments for the DAG
default_args = {
    'owner': 'AJAY',
    'depends_on_past': False,
    'start_date': datetime(2022, 04, 8),
    'email': ['******@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Define the DAG
dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='First DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)
```
**Step 6: Define the Operator**

```
run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=ETL_Datapipeline,
    dag=dag, 
)

run_etl
```

**Adding data to   AWS s3 Buckets**

**What is an S3 bucket?**

* Amazon S3 (Simple Storage Service) is a highly scalable, durable, and secure object storage service that allows you to store and retrieve data from anywhere on the web. 

* S3 is designed to be highly available and fault-tolerant, with built-in redundancy and automatic data replication across multiple availability zones. 

* S3 buckets are essentially containers for storing data objects, which can be accessed using a unique URL or API endpoint.


**Who uses S3 buckets, and what are the benefits?**

* S3 buckets are used by a wide range of organizations, from startups to large enterprises, to store and manage data in the cloud.


**Advantages**

* Scalability: S3 is designed to scale horizontally, meaning you can store virtually unlimited amounts of data in an S3 bucket, without worrying about running out of storage space.

* Durability: S3 is designed to be highly durable, with built-in redundancy and data replication across multiple availability zones. This means your data is protected against hardware failures, natural disasters, and other types of disruptions.

* Security: S3 provides a variety of security features, including encryption, access control, and logging, to help you keep your data safe and secure.

* Cost-effectiveness: S3 is a cost-effective solution for storing and managing large amounts of data, with pay-as-you-go pricing and no upfront costs.



**How to create an S3 bucket on AWS**

* Now that you understand the benefits of using S3, let's walk you through the steps of creating an S3 bucket on AWS:


**Step 1**

Log in to the AWS Management Console and navigate to the S3 service.



**Step 2**

 Click on the "Create bucket" button to start creating a new S3 bucket.

![alt text](img/s3bucket1.png)

**Step 3**

 Choose a unique name for your bucket, and select the region where you want to store your data.

![alt text](img/s3bucket2.png)

***Leave  the rest   of the settings as they are and click on ```create bucket```***


![alt text](img/s3bucket3.png)


And boom the S3bucket has been sucessfully created


**Adding data to the s3 bucket**

The following code will  write the contents of a Pandas DataFrame df to a CSV file located in an S3 bucket named twitter-s3-bucket.

> Change the code for the ETL_Datapipeline  above add the code below

```python
def  ETL_Datapipeline():
    # Creating list to append tweet data to
    attributes_container = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid since:2021-07-05 until:2022-07-06').get_items()):
        if i>150:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
        
    # Creating a dataframe to load the list
    tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])
    
    #Add contents to s3 bucket
    df.to_csv("s3://twitter-s3-bucket/covid_twitter_data.csv")
```


**Adding permission to write tHE S3 BUCKET FROM THE EC2 MACHINE**

**Step 1 : Create an IAM role**


* Select the EC2 instance that you want to create the IAM role for.

* Click on the "Actions" button and select "Security".

* Click on "Modify IAM Role".



![alt text](img/permission1.png)


**Step 2 : Modify IAM role**

* In the "Create IAM Role" dialog box, click on Create new IAM role .


![alt text](img/permission2.png)


**Step 3 : Create  role**

* Click on Create Role

![alt text](img/permission3.png)


* Under Trusted Entity type selet AWS Service then under common use cases select EC2 as shown below.

* Click on Next


![alt text](img/permission4.png)


**Step 3 : Permission Policies**

* In the "Attach permissions policies" step, select the policies that you want to attach to the role  , in this case we will select AmazonS3FullAccess  



![alt text](img/permission5.png)


* Reapeat the step above and select and  AmazonEC2FullAccess  again

![alt text](img/permission6.png)

* Add the role name as shown below

![alt text](img/permission7.png)


* The new Role has been created 

![alt text](img/permission8.png)






* Once the role is created, in the "Select IAM Role" dialog box will show the name of the new role. Select the role and click on " Update IAM role".

![alt text](img/permission9.png)




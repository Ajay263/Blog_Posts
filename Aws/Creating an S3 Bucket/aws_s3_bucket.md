

![alt text](img/logo.png)

# What is Amazon Simple Storage Service (S3)



* Amazon Simple Storage Service (S3) is a highly scalable, secure, and durable object storage service offered by Amazon Web Services (AWS). 

* It enables you to store and retrieve any amount of data from anywhere on the web with high availability and low latency. S3 is a popular choice for storing and managing data in the cloud

* S3 is primarily used for storing data such as images, videos, log files, backups, and documents. 

* It provides a simple web services interface that can be used to store and retrieve data from anywhere on the web. 

* S3 also supports a wide range of data management and security features, including versioning, lifecycle policies, access controls, and encryption.


**Advantages of s3 buckets**

* S3 is a highly scalable service, which means that it can handle large amounts of data with ease. 

* It is also designed for high durability, meaning that your data is stored redundantly across multiple devices and facilities. 

* This makes S3 a reliable choice for storing critical data that must be available at all times.


**Uses**

* Organizations of all sizes and types are using S3 to store and manage their data in the cloud. 

* Small businesses use S3 for backups and archiving, while larger enterprises use S3 for data lakes, content delivery, and application hosting. 

* S3 is also used by developers and data scientists for storing and sharing datasets, model outputs, and other artifacts.


**When to use S3 Buckets**

1. **Data Storage**

*  If you need to store large amounts of data in the cloud, S3 is a great choice. It enables you to store and retrieve any amount of data with high availability and low latency.

2. **Backup and Disaster Recovery**

*  S3 is also a great choice for backups and disaster recovery. You can use S3 to store backup copies of your data and recover it in case of a disaster.

3. **Static Website Hosting**

* S3 can also be used to host static websites. You can upload your website content to S3 and configure it to serve as a static website.



**How to access an S3 bucket using the AWS Command Line Interface (CLI):**

**Step 1:** 

* Install the AWS CLI on your local machine if you haven't already. You can download the CLI from the AWS website and follow the installation instructions for your operating system.Click [here](https://aws.amazon.com/cli/)

**Step 2:** 

* Configure the AWS CLI with your AWS access key ID and secret access key. You can use the ```aws configure``` command to set up the CLI with your credentials and default region.

**Step 3: **

* Use the `aws s3 ls` command to list all the S3 buckets in your AWS account. This command will return a list of all the S3 buckets, along with their creation dates.


**Step 4:** 

Use the `aws s3 ls s3://bucket-name` command to list all the objects in a specific S3 bucket. Replace `bucket-name` with the name of the S3 bucket you want to access.


**Step 5:** 

* Use the `aws s3 cp` command to copy files from your local machine to an S3 bucket or vice versa. For example, use `aws s3 cp /local/file/path s3://bucket-name/object-key` to copy a file from your local machine to the S3 bucket.


**Step 6:** 

* Use the `aws s3 sync` command to synchronize the contents of a local directory with an S3 bucket. For example, use `aws s3 sync /local/directory/path s3://bucket-name` to upload all the files in the local directory to the S3 bucket.

**Step 7:**

* Use the "aws s3 rm" command to delete objects from an S3 bucket. For example, use "aws s3 rm s3://bucket-name/object-key" to delete a specific object from the S3 bucket.




# How to  create S3  buckets 

**Step 1: Log in to the AWS Management Console** 

* Log in to the AWS Management Console and navigate to the S3 service.



**Step 2: Create a new S3 Bucket** 

* Click on the "Create bucket" button to create a new S3 bucket.

![alt text](img/s3bucket1.png)




**Step 3: Add a Unique Name for your Bucket** 

* Enter a name for your bucket, making sure that the name is unique across all S3 buckets in the AWS region you have selected. 

> * Note <br> 
Bucket names must be between 3 and 63 characters long and can only contain lowercase letters, numbers, and hyphens.

> * the conventions for naming S3 buckets can vary among different companies and organizations. Below is an  example of common naming conventions used by some  companies:

![alt text](img/s3bucket3.png)



![alt text](img/s3bucket2.png)


**Step 4: Select Region** 

* Select the region where you want to create the S3 bucket. 

* The region you select will determine the physical location of the bucket and can affect data transfer speeds and costs.


Leave the rest as it as but just make sure 
that Server side encryption is enabled   and  then click on `Create bucket`

![alt text](img/s3bucket4.png)



**Uploading data to an S3 Bucket**

**Step 1:** 

* Open a command prompt or terminal on your local machine  and navigate to the directory with the data you  want to add to the s3 bucket


**Step 2:** 

* Use the `aws s3 cp` command to upload a file to an S3 bucket. For example, use the following command to upload a file named `myfile.txt` to an S3 bucket named `mybucket`:

```bash
aws s3 cp myfile.txt s3://mybucket/
```

**Step 3:** 

* If you want to upload a folder and its contents to an S3 bucket, use the `aws s3 cp` command with the `--recursive` option. 

* For example, use the following command to upload a folder named `myfolder` to an S3 bucket named `mybucket`:

```
aws s3 cp myfolder s3://mybucket/ --recursive

```

for this tutorial to add the data do the following


```
aws s3 cp covid s3://topdevs-raw-useast1-911576787844-dev/data --recursive
```

**What this means**

1. ``aws:`` This is the command to call the AWS CLI.

2. ``s3:`` This is the service name for Amazon S3, the object storage service provided by AWS.

3. ```cp:``` This is the command to copy files or objects from a source to a destination.

4. `covid:` This is the name of the file or directory you want to upload to the S3 bucket.

5. `s3://topdevs-raw-useast1-911576787844-dev/data:` This is the destination path of the S3 bucket where you want to upload the file or directory. In this case, the S3 bucket name is `topdevs-raw-useast1-911576787844-dev `and the subdirectory path within the bucket is `/data`.

6. `--recursive:` This option tells the AWS CLI to copy all files and subdirectories within the "covid" directory to the S3 bucket.

![alt text](img/s3bucket5.png)


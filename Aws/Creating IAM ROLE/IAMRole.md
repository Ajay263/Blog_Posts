# What is AWS Identity and Access Management (IAM)

AWS Identity and Access Management (IAM) is a web service that enables you to manage access to AWS services and resources securely. IAM allows you to create and manage AWS users and groups, and apply permissions to control their access to AWS resources.

IAM is primarily used for managing access to AWS resources such as EC2 instances, S3 buckets, RDS instances, and more. It enables you to control who can access your resources and what actions they can perform on those resources.

**When  to start using AWS Identity and Access Management (IAM)**

IAM is an essential part of AWS security, and it is important to understand when to use it. Here are some situations in which IAM is a great fit:

1. **Multiple Users** 

* If there are multiple users who need access to your AWS account, IAM is a great tool for managing their access. 

* You can create individual IAM users for each person who needs access and assign them permissions based on their role.


2. **Fine-Grained Access Control**

*  If you need to control access to specific AWS resources, IAM allows you to do so at a granular level. 

* You can specify which actions users can perform and which resources they can access.


3. **Compliance Requirements**

* If your organization has specific compliance requirements, IAM can help you meet those requirements by providing detailed logs of all user activity and access to your AWS resources.


# Creating Identity and Access Management (IAM)  user


**Step 1: Log in to the AWS Management Console and navigate to the IAM dashboard.**

![alt text](img/iam2.png)

**Step 2: Create an IAM user** 

 * Click on the "Users" link on the left-hand menu, then click the "Add user" button. 
 
 ![alt text](img/iam3.png)
 
 
 Enter a user name and select the ```Provide user access to the AWS Management Console``` option to create an access key and secret access key for the user  and then click on next.
 ![alt text](img/iam4.png)



 **Step 3: Set permissions for the IAM user** 
 
 * Set permissions for the IAM user by attaching policies to the user.
 
 * Policies define what actions the user can take and what AWS resources they can access. 
 
* Click on the "Attach policies" button and select the policies you want to attach to the user . You can also create custom policies if necessary.In this case select ```AdministratorAccess```    and then click on Next.


> * Note <br>
 ```Administrator access```,  grants the user full access to all AWS services and resources. This means that the user can perform any action on any AWS resource, including modifying access permissions, creating or deleting resources, and even deleting the entire AWS account.


 ![alt text](img/iam5.png)

 * click on Next.

 ![alt text](img/iam6.png)


 Review and create your IAM USER  and then Click On Create User

 ![alt text](img/iam7.png)


 **Step 4: Loggin with the newly created credentials** 

* Download the CSV file containing the access key ID and secret access key for the IAM user you just created. 

* To do this, click on the "Download .csv file" button in the IAM user creation confirmation screen.

* Open the downloaded CSV file and take note of the access key ID and secret access key.


* Click on the link provided in the CSV file to navigate to the AWS console login page.

 ![alt text](img/iam8.png)

 * Enter the Username and password from the CSV file when prompted to log in.

 


  You will now be logged in to the AWS console with the permissions granted to the IAM user you created



# Apache Airflow   ![alt text ](img/logo.png)   



Apache Airflow is an open-source workflow management platform that can be used to schedule and monitor data pipelines. It is a popular choice for data engineers because it is easy to use, flexible, and scalable.


![alt text](img/airflow1.jpg) 

**Tasks that can be automated by airflow**

* Extracting data from a variety of sources, such as databases, files, and APIs.

* Cleaning and transforming data.

* Loading data into a variety of destinations, such as databases, data warehouses, and data lakes.

* Running machine learning models.

* Visualizing data.

**Companies using Apache Airflow**

* Airbnb

* Spotify

* Netflix

* Uber

* The New York Times

These companies have benefited from using Airflow in a variety of ways, including:

* Increased efficiency: Airflow can help to automate and streamline data engineering tasks, which can free up data engineers to focus on more strategic work.

* Improved reliability: Airflow can help to ensure that data pipelines are executed reliably and consistently.

* Reduced costs: Airflow can help to reduce the costs associated with data engineering, by automating tasks and reducing the need for manual intervention.


 




**Advantages of Airflow**

* Airflow is a Python-based platform, which makes it easy to integrate with other Python-based tools and libraries.

* Airflow is highly scalable, and can be used to manage large and complex data pipelines.

* Airflow is open source, which means that it is free to use and there is a large community of users and developers who can provide support and help with troubleshooting.

*If you are looking for a powerful and flexible workflow management platform for data engineering, then Airflow is a good option.*


**Setting up Apache Airflow**

Airflow can be installed on your own infrastructure, or you can use a managed service like Astro.

Astro is a managed service from Google Cloud Platform.

It is a fully managed platform for Apache Airflow, which means that Google takes care of the underlying infrastructure, including provisioning servers, installing software, and managing updates. 

This frees you up to focus on developing your Airflow workflows.

**Why  use Astro??**

* **Ease of use** 

    Astro is a managed service, which means that Google takes care of the underlying infrastructure. 

    This makes it much easier to get started with Airflow, as you don't need to worry about setting up and managing your own servers.

* **Performance** 

    Astro is designed to scale to meet the needs of your Airflow workloads. 

    This means that you can easily add more resources as your needs grow, without having to worry about performance bottlenecks.

* **Security**

   Astro is a secure platform, with built-in features to protect your data and applications. 
   
   This includes things like role-based access control (RBAC), encryption, and auditing.

##### Prerequisites
* A terminal that accepts bash commands
* [Docker Desktop ](https://docs.docker.com/get-docker/) (v18.09 or higher).
* The [Astro CLI.](https://docs.astronomer.io/astro/cli/install-cli) 
* An integrated development environment (IDE) for Python development, such as [VSCode.](https://code.visualstudio.com/)
* Optional. A local installation of Python 3 to improve your Python developer experience.

> *For installing Astro cli in windows  click [here](https://gist.github.com/andriisoldatenko/e351f5310d14c0270fad681bfd7c49d3)*


**Step 1: Create an Astro project**

To run data pipelines on Astro, you first need to create an Astro project, which contains the set of files necessary to run Airflow locally.

> 1. Create a new directory for your Astro project:

```
mkdir <your-astro-project-name>
```

> 2. Open the directory:
```
cd <your-astro-project-name>
```
> 3. Run the following Astro CLI command to initialize an Astro project in the directory:

```
astro dev init
```

> ***The Astro project is built to run Airflow with Docker. Docker is a service to run software in virtualized containers within a machine. When you run Airflow on your machine with the Astro CLI, Docker creates a container for each Airflow component that is required to run DAGs. For this tutorial, you don't need an in-depth knowledge of Docker. All you need to know is that Airflow runs on the compute resources of your machine, and that all necessary files for running Airflow are included in your Astro project***


**Step 2: Start Airflow**

the next step is to actually start Airflow on your machine. In your terminal, open your Astro project directory and run the following command:


```
astro dev start

astro dev run
```
> *Starting Airflow for the first time can take 2 to 5 minutes. Once your local environment is ready, the CLI automatically opens a new tab or window in your default web browser to the Airflow UI at https://localhost:8080.*


> **Note**<br>
> If port 8080 or 5432 are in use on your machine, Airflow won't be able to start. To run Airflow on alternative ports, run:

```
astro config set webserver.port <available-port>

astro config set postgres.port <available-port>
```

**Step 3: Log in to the Airflow UI**

To access the Airflow UI, open http://localhost:8080/ in a browser and log in with admin for both your username and password.

The   following is a default page in the Airflow UI and is called the DAGs page, which shows an overview of all DAGs in your Airflow environment:

![alt text](img/airflowui1.png) 

**Architecture Overview**

![alt text](img/Airflow_Archtecture.png) 

The architecture of Apache Airflow can be divided into three main components:

1. **Webserver**

     * The webserver is the main entry point for Airflow.

     * It provides a user interface for creating, managing, and monitoring DAGs.

2. **Scheduler**

     * The scheduler is responsible for  scheduling and executing  DAGs. 

    *  It determines when a task should be executed based on its dependencies and the schedule interval defined in the DAG. 

     * The scheduler communicates with the database to retrieve information about DAGs and tasks and updates their status as they are executed.

3. **Workers**
    
    *  Workers are the machines that execute the tasks defined in DAGs.

    * They are launched by the scheduler and can be distributed across multiple machines.

    * They pull tasks from the task queue and execute them in parallel.

    * Each worker runs a single task at a time, but multiple workers can run concurrently to execute multiple tasks simultaneously.


4. **Metadata Database**
    
    * The metadata database stores information about DAGs, tasks, and their dependencies. 
     
    * It is used by the scheduler and workers to retrieve information about tasks and update their status as they are executed.


5. **DAG directory**

    * It is a directory that contains DAGs

    * Airflow uses DAG directories to organize DAGs. 
    
    * This makes it easy to find and manage DAGs.
    
    *  DAG directories can also be used to control access to DAGs. For example, you can create a DAG directory that only contains DAGs that are used by a specific team.

    

    ![alt text](img/Archtecture_detail.png) 
     

**Airflow Components**

To understand the architecture of Apache Airflow in more detail, let's take a closer look at the components that make up the system:


1. **Task**

    * A task is the smallest unit of work that can be executed.
   
    *  Tasks can be anything from running a SQL query,running a Python script, copying data from one location to another to sending an email notification 

    * Tasks are connected by dependencies. When a task is scheduled to run, Airflow will first check if all of its dependencies have been completed. If they have, Airflow will then execute the task.

    ***To create a task, you need to define the following:***

    > * The name of the task.

    > * The type of the task.

    > * The arguments that are passed to the task.


    **Example**

    ```python
    #create  new BashOperator task
    task = BashOperator(

    #set  ID of the task    
    task_id='task1',

    #set  bash command
    bash_command='echo "Hello, world!"',

    #specifies the DAG
    dag=dag)
    ```


    Explanation

    * ```BashOperator```  is an operator in Airflow that allows you to execute a Bash command as a task


    * ```task_id``` is a unique identifier i.e a name for the task.

    * ```bash_command```  specifies the Bash command that should be executed as part of the task

    * ```dag parameter``` specifies the DAG to which this task belongs

   > *This task will run the echo "Hello, world!" command every time the DAG is scheduled to run.*



2. **DAG in Airflow**

    * A DAG in Airflow is a Directed Acyclic Graph that represents a workflow. 
    
    * A DAG is a collection of tasks that are connected by dependencies.

    * Airflow uses DAGs to represent workflows because they are a simple and easy way to visualize and understand the dependencies between tasks.
    
    * DAGs can also be scheduled to run on a recurring basis, which makes them ideal for automating data pipelines.


    ***To create a DAG in Airflow, you need to define the following:***

     > * The name of the DAG.

     > * The start date of the DAG.

     > * The end date of the DAG.

     > * The tasks that are part of the DAG.

     > * The dependencies between the tasks.

     **Example**


      ```python
     
    dag = DAG(

    #specifies   name of the DAG 
    dag_id='my_dag',

    #specifies  the starting date of the DAG
    start_date=datetime.datetime(2023, 5, 26),
    
    #specifies  how often the DAG should run
    schedule_interval='0 10 * * *')


    task1 = BashOperator(

    task_id='task1',

    bash_command='echo "Hello, world!"',

    dag=dag)


    task2 = BashOperator(

    task_id='task2',

    bash_command='echo "Goodbye, world!"',

    dag=dag)

    task1 >> task2 
    ```

  ```>> ``` operator is used to define dependencies between tasks in the DAG. In this example, task2 is dependent on task1, which means that task1 must be completed before task2 can start.

The expression task1  ```>> ``` task2 specifies that the output of task1 is required input for task2, and that task2 should only be executed after task1 has successfully completed.


3. **Operators**

    * Operators are the building blocks of Airflow DAGs.
    
    *  They contain the logic of how data is processed in a pipeline.
    
    * Each task in a DAG is defined by instantiating an operator. There are many different types of operators available in Airflow.



    ***Airflow has a wide variety of operators that can be used to perform a variety of tasks. Some of the most common operators include:***

    * BashOperator: Executes a bash command.
 
    * PythonOperator: Executes a Python function.

    * HiveOperator: Executes a Hive query.

    * MySQLOperator: Executes a MySQL query.

    * EmailOperator - sends an email

   ***To create an operator, you need to define the following:***

   > * The name of the operator.

   > * The type of the operator.

   > * The arguments that are passed to the operator.

   **Examples of Operators**

    1. **BashOperator**
     
  ```
    task = BashOperator(

    task_id='task1',

    bash_command='echo "Hello, world!"',

    dag=dag)

  ```

ii. **PythonOperator**

 ```
task = PythonOperator(

    task_id='task1',

    python_callable='my_function',

    op_args=['arg1', 'arg2'],

    dag=dag)
     
```










     


















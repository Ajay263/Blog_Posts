# What is dbt?


- dbt stands for data build tool. It's a transformation tool: 

- It allows us to transform process raw data in our Data Warehouse to transformed data which can be later used by Business Intelligence tools and any other data consumers.

- dbt also allows us to introduce good software engineering practices by defining a deployment workflow:

    1. Develop models

    2. Test and document models

    3. Deploy models with version control and CI/CD.

# How does dbt work?

- dbt works by defining a modeling layer that sits on top of our Data Warehouse.

- The modeling layer in dbt is made up of models, which are essentially SQL queries .

- SQL queries  define how to transform raw data into derived data. 

- Each model is stored in a .sql file that contains a SELECT statement, and no DDL or DML is used.

- The modeling layer will turn tables into models which we will then transform into derived models, which can be then stored into the Data Warehouse for persistence.

- A model is a .sql file with a SELECT statement; no DDL or DML is used. dbt will compile the file and run it in our Data Warehouse.

- When you run dbt, it will compile the SQL files and run them in the Data Warehouse to create the derived models. 

- This means that you can easily transform and manipulate data in your Data Warehouse without having to write complex SQL queries.

# Benefit of using dbt 

1. It allows you to create a repeatable, scalable data pipeline. Because each model is stored in its own file, it's easy to version control and track changes over time. 

2. Since dbt compiles and runs the SQL files, you can be sure that your data pipeline is consistent and reproducible.

# Anatomy of a dbt model

dbt models are mostly written in SQL (remember that a dbt model is essentially a SELECT query) but they also make use of the Jinja templating language for templates.

**Example of a dbt Model**

```python
{{
    config(materialized='table')
}}

SELECT *
FROM staging.source_table
WHERE record_state = 'ACTIVE'
```

**Explanation**

1. **config(materialized='table')**  

    -  This line sets a configuration option for the dbt model that follows it. 
    In this case, it's setting the "materialized" property to `table`. This means that when the model is compiled and run, the result will be stored as a table in your Data Warehouse. 

    - Other options for the `materialized` property include `view` (which creates a view in the Data Warehouse) and `ephemeral` (which creates a temporary table that is dropped after the query is run).

    - The `incremental strategy` is essentially a table strategy but it allows us to add or update records incrementally rather than rebuilding the complete table on each run.

2.  `SELECT *
FROM staging.source_table
WHERE record_state = 'ACTIVE'`

    - This is a SQL query that selects all columns from a table called `source_table `in a schema called `staging`. It then applies a filter to only return rows where the `record_state` column is equal to the string `ACTIVE.`


dbt will compile this code into the following SQL query:

```python 
CREATE TABLE my_schema.my_model AS (
    SELECT *
    FROM staging.source_table
    WHERE record_state = 'ACTIVE'
)
```

After the code is compiled, dbt will run the compiled code in the Data Warehouse.

Additional model properties are stored in YAML files. Traditionally, these files were named schema.yml but later versions of dbt do not enforce this as it could lead to confusion.


# The FROM clause


The FROM clause within a SELECT statement defines the sources of the data to be used.

The following sources are available to dbt models:

1. **Sources:** 
    
    - In dbt, a `source` is a reference to external data that is used as input to your data pipeline.
    
    - Sources can include databases, files, APIs, and other data sources that you want to integrate into your data warehouse.

    - We can access this data with the source() function.

    - The sources key in our YAML file contains the details of the databases that the source() function can access and translate into proper SQL-valid names.

    - Additionally, we can define "source freshness" to each source so that we can check whether a source is "fresh" or "stale", which can be useful to check whether our data pipelines are working properly.
    More info about sources in this link.

2. **Seeds:** 

    - CSV files which can be stored in our repo under the seeds folder.

    - The repo gives us version controlling along with all of its benefits.

    -  Seeds are best suited to static data which changes infrequently.

#### Seed usage:

1. Add a CSV file to your seeds folder.

2. Run the dbt seed command to create a table in our Data Warehouse.

    > * If you update the content of a seed, running dbt seed will append the updated values to the table rather than substituing them. Running dbt seed --full-refresh instead will drop the old table and create a new one.

3. Refer to the seed in your model with the ref() function.

More info about seeds in this link.


***Here's an example of how you would declare a source in a .yml file:***

```python 

sources:
    - name: staging
      database: production
      schema: trips_data_all

      loaded_at_field: record_loaded_at
      tables:
        - name: green_tripdata
        - name: yellow_tripdata
          freshness:
            error_after: {count: 6, period: hour}
```

# Explanaton

```python

- name: staging  #Name of source
  database: production  #database name
  schema: trips_data_all    #Database schema

```
* This sets up a source named "staging" that connects to a database named "production" and a schema named "trips_data_all". This tells dbt where to look for the source data.



```python
loaded_at_field: record_loaded_at
```

* This line specifies the name of the field in the source data that indicates when the data was loaded into the source. This can be useful for tracking the freshness of the data and identifying when it needs to be updated.

```python 
tables:
  - name: green_tripdata
  - name: yellow_tripdata
    freshness:
      error_after: {count: 6, period: hour}
```

* This section lists the tables within the `trips_data_all` schema that are part of the `staging` source. In this case, there are two tables: `green_tripdata` and `yellow_tripdata`.

* The `freshness` parameter is used to specify how often the data in this table should be refreshed. In this case, the `yellow_tripdata` table has a freshness threshold of 6 hours. This means that if the data in the `yellow_tripdata` table is older than 6 hours, dbt will consider it stale and will raise an error. The `green_tripdata` table does not have a freshness threshold specified, so it will not trigger an error based on data freshness.


**And here's how you would reference a source in a FROM clause:**

```python 
FROM {{ source('staging','yellow_tripdata') }}
```

* The first argument of the source() function is the source name, and the second is the table name.

In the case of seeds, assuming you've got a `taxi_zone_lookup.csv` file in your seeds folder which contains `locationid`, `borough`, `zone` and `service_zone`:

```python 
SELECT
    locationid,
    borough,
    zone,
    replace(service_zone, 'Boro', 'Green') as service_zone
FROM {{ ref('taxi_zone_lookup) }}
```

The ref() function references underlying tables and views in the Data Warehouse. When compiled, it will automatically build the dependencies and resolve the correct schema for us. So, if BigQuery contains a schema/dataset called `dbt_dev` inside the `my_project` database which we're using for development and it contains a table called `stg_green_tripdata`, then the following code...

```python 
WITH green_data AS (
    SELECT *,
        'Green' AS service_type
    FROM {{ ref('stg_green_tripdata') }}
),
```

...will compile to this:


```python 

WITH green_data AS (
    SELECT *,
        'Green' AS service_type
    FROM "my_project"."dbt_dev"."stg_green_tripdata"
),
```

* The ref() function translates our references table into the full reference, using the database.schema.table structure.

* If we were to run this code in our production environment, dbt would automatically resolve the reference to make ir point to our production schema.

# Defining a source and creating a model

We will now create our first model.

We will begin by creating 2 new folders under our models folder:

1. `staging` will have the raw models.

2. `core` will have the models that we will expose at the end to the BI tool, stakeholders, etc.

Under staging we will add 2 new files: `sgt_green_tripdata.sql` and `schema.yml`:


```python
# schema.yml

version: 2

sources:
    - name: staging
      database: your_project
      schema: trips_data_all

      tables:
          - name: green_tripdata
          - name: yellow_tripdata
```
* We define our sources in the schema.yml model properties file.

* We are defining the 2 tables for yellow and green taxi data as our sources.

```python 

-- sgt_green_tripdata.sql

{{ config(materialized='view') }}

select * from {{ source('staging', 'green_tripdata') }}
limit 100
```

* This query will create a view in the staging dataset/schema in our database.

* We make use of the source() function to access the green taxi data table, which is defined inside the schema.yml file.

# Benefits of having the properties in a separate file

The advantage of having the properties in a separate file is that we can easily modify the schema.yml file to change the database details and write to different databases without having to modify our sgt_green_tripdata.sql file.

You may know run the model with the `dbt run` command, either locally or from dbt Cloud

# Macros

- Macros are pieces of code in Jinja that can be reused, similar to functions in other languages.

- dbt already includes a series of macros like `config()`, `source()` and `ref()`, but custom macros can also be defined.

Macros allow us to add features to SQL that aren't otherwise available, such as:

1. Use control structures such as` if `statements or `for` loops.

2. Use environment variables in our dbt project for production.

3. Operate on the results of one query to generate another query.

4. Abstract snippets of SQL into reusable macros.

> * Note ! <br>
Macros are defined in separate .sql files which are typically stored in a macros directory.

There are 3 kinds of Jinja delimiters:

1. `{% ... %}` for statements (control blocks, macro definitions)

2. `{{ ... }}` for expressions (literals, math, comparisons, logic, macro calls...)

3. `{# ... #}` for comments.

Here's a macro definition example:

```python 
{# This macro returns the description of the payment_type #}

{% macro get_payment_type_description(payment_type) %}

    case {{ payment_type }}
        when 1 then 'Credit card'
        when 2 then 'Cash'
        when 3 then 'No charge'
        when 4 then 'Dispute'
        when 5 then 'Unknown'
        when 6 then 'Voided trip'
    end

{% endmacro %}
```

* The macro keyword states that the line is a macro definition. It includes the name of the macro as well as the parameters.

* The code of the macro itself goes between 2 statement delimiters. The second statement delimiter contains an endmacro keyword.

* In the code, we can access the macro parameters using expression delimiters.

* The macro returns the code we've defined rather than a specific value.

Here's how we use the macro:

```python
select
    {{ get_payment_type_description('payment-type') }} as payment_type_description,
    congestion_surcharge::double precision
from {{ source('staging','green_tripdata') }}
where vendorid is not null
```
* We pass a payment-type variable which may be an integer from 1 to 6.

And this is what it would compile to:

```python
select
    case payment_type
        when 1 then 'Credit card'
        when 2 then 'Cash'
        when 3 then 'No charge'
        when 4 then 'Dispute'
        when 5 then 'Unknown'
        when 6 then 'Voided trip'
    end as payment_type_description,
    congestion_surcharge::double precision
from {{ source('staging','green_tripdata') }}
where vendorid is not null
```

The macro is replaced by the code contained within the macro definition as well as any variables that we may have passed to the macro parameters.

# Packages

Macros can be exported to packages, similarly to how classes and functions can be exported to libraries in other languages. Packages contain standalone dbt projects with models and macros that tackle a specific problem area.

When you add a package to your project, the package's models and macros become part of your own project. A list of useful packages can be found in the dbt package hub.

To use a package, you must first create a packages.yml file in the root of your work directory. Here's an example:

```python
packages:
  - package: dbt-labs/dbt_utils
    version: 0.8.0
```

After declaring your packages, you need to install them by running the `dbt deps` command either locally or on dbt Cloud.

You may access macros inside a package in a similar way to how Python access class methods:

```python
select
    {{ dbt_utils.surrogate_key(['vendorid', 'lpep_pickup_datetime']) }} as tripid,
    cast(vendorid as integer) as vendorid,
    -- ...
```

The surrogate_key() macro generates a hashed surrogate key with the specified fields in the arguments

# Variables

Like most other programming languages, variables can be defined and used across our project.

Variables can be defined in 2 different ways:

1. Under the vars keyword inside `dbt_project.yml`.

```python
vars:
    payment_type_values: [1, 2, 3, 4, 5, 6]
```

2. As arguments when building or running your project.

```python
dbt build --m <your-model.sql> --var 'is_test_run: false'

```

Variables can be used with the `var()` macro. For example:

```python
{% if var('is_test_run', default=true) %}

    limit 100

{% endif %}
```

- In this example, the default value for `is_test_run` is `true`; in the absence of a variable definition either on the `dbt_project.yml` file or when running the project, then `is_test_run` would be true.

- Since we passed the value `false `when runnning `dbt build`, then the if statement would evaluate to false and the code within would not run.


# Referencing older models in new models

> * Note: <br>
You will need the Taxi Zone Lookup Table seed, the staging models and schema and the macro files for this section.

The models we've created in the staging area are for normalizing the fields of both green and yellow taxis. With normalized field names we can now join the 2 together in more complex ways.

The `ref()` macro is used for referencing any undedrlying tables and views that we've created, so we can reference seeds as well as models using this macro:

```python
{{ config(materialized='table') }}

select
    locationid,
    borough,
    zone,
    replace(service_zone, 'Boro', 'Green') as service_zone
from {{ ref('taxi_zone_lookup') }}
```

* This model references the taxi_zone_lookup table created from the taxi zone lookup CSV seed.


```python 
with green_data as (
    select *, 
        'Green' as service_type 
    from {{ ref('stg_green_tripdata') }}
), 
```

* This snippet references the sgt_green_tripdata model that we've created before. Since a model outputs a table/view, we can use it in the FROM clause of any query.
You may check out these more complex "core" models in this link.

> * Note: <br>
 When running `dbt run` will run all models but NOT the seeds. The `dbt build` can be used instead to run all seeds and models as well as tests, which we will cover later. Additionally, running `dbt run --select my_model `will only run the model itself, but running `dbt run --select +my_model` will run the model as well as all of its dependencies.


 # Testing and documenting dbt models

Testing and documenting are not required steps to successfully run models, but they are expected in any professional setting.

**Testing**

Tests in dbt are assumptions that we make about our data.

In dbt, tests are essentially a `SELECT` query that will return the amount of records that fail because they do not follow the assumption defined by the test.

Tests are defined on a column in the model YAML files (like the `schema.yml` file we defined before). dbt provides a few predefined tests to check column values but custom tests can also be created as queries. Here's an example test:

```python
models:
  - name: stg_yellow_tripdata
    description: >
        Trips made by New York City's iconic yellow taxis. 
    columns:
        - name: tripid
        description: Primary key for this table, generated with a concatenation of vendorid+pickup_datetime
        tests:
            - unique:
                severity: warn
            - not_null:
                severrity: warn
```
* The tests are defined for a column in a specific table for a specific model.

* There are 2 tests in this YAML file: `unique` and `not_null` Both are predefined by dbt.

* `unique` checks whether all the values in the tripid column are unique.

* `not_null` checks whether all the values in the tripid column are not null.

Both tests will return a warning in the command line interface if they detect an error.

Here's wwhat the `not_null` will compile to in SQL query form:

```python
select *
from "my_project"."dbt_dev"."stg_yellow_tripdata"
```

You may run tests with the `dbt test` command.

# Documentation

* dbt also provides a way to generate documentation for your dbt project and render it as a website.

* You may have noticed in the previous code block that a description: field can be added to the YAML field. dbt will make use of these fields to gather info.

The dbt generated docs will include the following:

1. Information about the project:

    * Model code (both from the `.sql` files and compiled code)

    * Model dependencies

    * Sources

    * Auto generated DAGs from the `ref()` and `source()` macros

    * Descriptions from the `.yml` files and tests

2. Information about the Data Warehouse (information_schema):

    * Column names and data types

    * Table stats like size and rows

dbt docs can be generated on the cloud or locally with `dbt docs generate`, and can be hosted in dbt Cloud as well or on any other webserver with `dbt docs serve`.


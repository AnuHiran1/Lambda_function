# Lambda_function
Lambda_function which connects to rds and delete database with particular string

### Steps to follow to run Lambda function :

NOTE : This Lambda function depends on libraries other than the SDK for Python (Boto 3), install them to a local directory with pip, and include them in your deployment package.

#### To update a Python function with dependencies:

1.Install libraries in a new, project-local package directory with pip's --target option.
     
     pip install --target ./package pymysql,logging
     
2.Create a ZIP archive of the dependencies.

    ~/my-function$cd package
    ~/my-function/package$zip -r9 ${OLDPWD}/function.zip .

3.Add your function code to the archive. 

    ~/my-function/package$ cd $OLDPWD
    ~/my-function$ zip -g function.zip lambda_function.py
    
4.Update the function code.

    ~/my-function$ aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip
    
Note:Here function-name is name of the lambda function in aws.



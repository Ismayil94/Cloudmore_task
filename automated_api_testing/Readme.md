I am using Postman for API testing,
with Newman to run from CLI,
and newman-reporter.html for generating HTML reports


Step 1: Install Nodejs

Download it from official website https://nodejs.org/en/download/

Step 2: Install Postman

Download it from official website https://www.postman.com/

Step 3: Install Newman

Run npm install -g newman 

Step 4: Install newman-reporter.html

Run npm install -g newman-reporter-html

Step 5: Run API tests with newman 

Run newman run  C:\Users\I\Documents\GitHub\Cloudmore_task\automated_api_testing\API_Flow_Tests.postman_collection.json -r html 
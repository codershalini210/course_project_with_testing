## TC01 - course model
requirement: Every course stores its title and description 
scenario : Create a course with a title and des
expected result : the course is save and its fields contain the expected values

## TC02 - course list view
requirment: users can open the course list page.
scenario: rquest the course list url
Expected Result : HTTP 200 is returned and page displays the expected course

## TC-03 - course detail view 
req: Users can open an individual course.
Scenario : reuest the details of existing course 
Expected result : Http 200 is returned and the correct course details are displayed

## TC04  - Course Form 
requirment : A course must have a tile and des
Screnario : validate a form with complete data and another with the missing required fieds
Expected result : Complete data is valid : missing required data is invalid 

## TC05 : Dashboard while signed out
Requirment : Only authenticated users can access the dashboard
Scenario : Request the dashboard without loggin in .
Expected REsult : the user is redirected to the login page 

## TC06: Dashboard while signed in 
Requirment : Authenticated users can access the dashboard. 
Scenario : Sign in the test user and request the dashboard,
Expected result : http 200 and the dashboard is displayed
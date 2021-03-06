# Library-management
This is a library management project created with Django web framework.

This documentation will be helpful to understand the backend of the project.

Activate the Virtual env using "env\scripts\activate" command.

The backend for the project is divided into 4 parts-
1) CRUD operation
2) Admin registration and login
3) User registration and login
4) REST API


1) CRUD operation:

* In INDEX function, a context is created in which a dictionary is passed to show all the data in tables and further passed to a template.
* The Add function is created to add the information in the database which will be done by the admin.Generally
  we use two mehods POST and GET. The POST method is used to post the data and get for retriving or fetching the data.
* Here the POST method is used as we have to send the data to database.
* The Edit function allows us to edit the data in database.
* The Update function verifies the credentials entered by the admin and updates them with value and name.
* In case if the admin wants to delete the data, the Delete function will manipulate the database by deleting the data.
  Here the ORM queries play main roles like filter, delete and create the objects
 
2) Admin registration and login:

* Here multiple admins are allowed to register.
* In the signupadmin function the admin will register himself with the POST method as information is to be send.
* To register, admin have to manually enter a link which is not or anybody can register themselves as admin.(http://127.0.0.1:8000/signupadmin)
* All the credentials entered by the admin will be checked in if loop.Also the code for the authentication is
  done to check the length of the username, the match between password and confirm password.If these things are
  not as per the authentication, a error message will pop-up and the page will be redirected to the same sign up page.
* If all the credentials lies within the authentication rules, it will be saved in a variable 'user'.
  Also this function won't allow to generate the admin duplicate username or it will show an error message.
* After signing up successfully the admin will be redirected to the login page.During the login process the loginadmin
  function will fetch the username and password recently created by the admin. If the credentials matched,
  the admin will be redirected to the library management page. And if the username is not correct or password is not
  correct as per the database,an error will be displayed as "Incorrect username" and "Incorrect password" resp.or if 
  both fields are not correct the error message "Bad credentials" will be displayed.

3) User registration and login:

* The registration and signup process for the user is same as the admin. But here, the user can register by clicking on
  "Not registered yet? Signup here" link provided on the login page.

* The signin function is defined to render the signin page
* The signup function is defined to render the signup page for user.
* The signout function simply renders the login page as the user should to redirected to the login page.
* The loginadmin function renders the login page for admin.
* The signoutadmin function will redirect the admin to login page of admin after logout.

* The main objective of the project is to show the user only the data created by admin not to manipulate it. Hence it is necessary to create a function which will
  only show the data. So the function named "User" is defined. The data is stored in a variable "emp" and this variable is passed in a dictionary whose key is "emp".


*****************************************************************************************************************************************************************************


4) REST API:

The admin never wants to expose the unnecessary or whole database to the user. It may lead to mishandling or manipulation of data. Here the API comes to handy.
It only shows the the information requested by user.


For API a serializer.py file is created in which a class followed by the model class is created.
A Meta class is created having model which is the model class "Book" as the data in this class needed to display.
As we want to all the fields in response from this class, the "__all__" fields are selected. We can select the specific fields too.

In views, a class named BookList is created in which the APIView is passed. The APIView is used so tha the normal views can return an API data.
Here we use the GET and POST method. The GET method is used to return all the data in a model and the POST method is used to create new data.
The variable book1 stores all the objects. As furthe we need to serialize them which means that taking all the objects and coverting them into JSON
a serializer is defined.

To access the API enter "booklist" followed by the port number of development server eg."http://127.0.0.1:8000/booklist".



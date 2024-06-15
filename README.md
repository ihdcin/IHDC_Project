**User Vendor Management**
Description
User Vendor Management is a Django-based web application designed to streamline vendor management operations. 
It allows users to manage vendors efficiently, including adding, editing, and deleting vendor details. 
The application provides a user-friendly interface to view vendor information and download transaction 
reports associated with each vendor.

**Features**
Vendor Management:

Add new vendors with details like vendor name, account number, and IFSC code.
Edit existing vendor details.
Delete vendors securely with confirmation prompts.
Transaction Reports:

Generate Excel reports for vendor transactions.
Download transaction reports for each vendor.
Prerequisites
Before you start, ensure to activate the virtual environment called myenv inside the base project folder
for requirements check the requirements.txt
Django==5.0.3
Python 3.12.2

# How to use the project #
The user need to first register by providing the details like Name  , email and password through the register page.
Then the user can login through his entered email and password through the login page.
After authentication only the user can access the website services like , Add Vendors , View Vendors , Add Transactions like that.
The authenticated user can add new vendors through the service section there are 3 cards , Inorder to add the vendors the user need to click 
the first card called add vendors / (Create Vendors ) It will redirect the user to an another 'create vendor page' where the user can create a vendor by giving
details like vendor name , account number and ifsc code. 

# View vendors , CRUD Operations and Excel sheet Downloading #
Then after that the user can view his created vendors in an another page called view vendors / (vendor table). This page is accessed through the 3rd card in the service section called 'view cendor details'.
Where in that table there will two buttons called edit and delete  , which is linked with some javascript functions .
While performing the deleting , two confirmation prompts wil be asked for the confirmation after that it will auto update or refresh the table.
While performing the edit operation a javascript function will redirect the user to another editing page , where the vendor details like name , account number and ifsc code can be updated using a 
javascript function in the frontend itself.

There is aslo an another button in the vendor table called " Print Excel or view transcations ". Where the user can download each vendors entire transactions , this is implemented using a javacript function.
which will call a api ending to the rest backend where a serailized data will be sent in the jason format to the frontend. By using these datas an excel sheet is created with the vendors name and id as its file name.

# Note #
If the vendor has not transaction history a propmt will be shown like "no transactions yet done" will be poped out as an alert.

# Adding Transactions #
The authenticated user can add multiple transactions for each vendors through the service section there is a second card called "Add Transactions",
where the user is redirected to an another page where the user can select the vendor as a dropdown list from the existing vendors,  and can also related fields like description , amount , date.
After that you can download the excel sheet from the vendor table.





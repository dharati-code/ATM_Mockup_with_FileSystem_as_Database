# ATM_Mockup_with_FileSystem_as_Database

To wrap up our ATM project, we are going to be using python file system as our database.



The solution is implemented as  below:



1. Consistent User Account Balance: When user deposits, withdrawals and do other banking operations, their account balance should be saved in a file. You can create a seperate file for each user, or use the existing user file, or use the same file for all users.

2. When user login to the system, create a file in the auth_session folder to keep track of their login.

3. When user logout of the system, delete the file in auth_session to indicate that they have logged out of the system.


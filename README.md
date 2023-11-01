This is a course project for CyberSecurity2023. It is meant to be a simple application that has flaws from the [OWASP 2017](https://owasp.org/www-project-top-ten/).

##### FLAW 1: Broken Authentication 

[Link to the code](https://github.com/AapoTuulentie/CyberSecurity2023/blob/60c9e0a837f30fe1d93f42270db3ed507cc61168/mysite/cs_project/views.py#L14) 
The first flaw in this project is broken authentication. There are a few deficiencies in the user registration requirements. Firstly, the minimum length of a password is not defined. A user can have a password that is only one character, when best practice is at least 8 characters. Also, a user can have a password that contains only numbers or only letters. A password should be at least a mix of these two, and preferably also contain capital letters or special characters.  

A fix for this flaw is commented out below the register-function. Now it requires 8 characters and at least one number. This prevents attackers from using traditional brute force attacks with common password lists including passwords such as “123456” or “password”.  

 

##### FLAW 2: SQL Injection 
[Link to the code](https://github.com/AapoTuulentie/CyberSecurity2023/blob/60c9e0a837f30fe1d93f42270db3ed507cc61168/mysite/cs_project/views.py#L62) 

The second flaw is SQL injection. Django uses models to access the database, but it is also possible to write raw SQL queries with the raw() function. The flaw is in the viewnotes-function and more specifically in the search notes functionality. The raw SQL query is poorly written and directly places the user input into the query with the query parameter. For example, the user could write “NOTHING”’ UNION SELECT * FROM note --” as input and gain access to every user’s notes.  

For the fix, I used Django’s own models-functions that replace the raw SQL queries and are parametrized by default. Now the raw SQL query is replaced with Note.objects.filter() and the LIKE part of the query is replaced with text__contains=query. To prevent SQL injection, the user inputs need to be checked and validated before making the query. Luckily in Django the attacker cannot access the User-table with this injection because it is provided by django.contrib.auth and managed by Django Object-Relational Mapping system, which provides protection against SQL injection attacks.  

 

##### FLAW 3: Broken Access Control 
[Link to the code](https://github.com/AapoTuulentie/CyberSecurity2023/blob/60c9e0a837f30fe1d93f42270db3ed507cc61168/mysite/cs_project/views.py#L80) 

The third flaw in the application is broken access control, in the deletenote-function. Although the code authenticates the user with @login.required, it does not check if the user has the required permission to delete the note. The function is in the form of /delete/<noteid>, and by modifying the noteid, a malicious user could delete another user’s note.  

This flaw can be fixed quite easily. The application needs to check if the owner of the note is compatible with the current user. This can be done with ‘if n.user == request.user’ clause. Now the program compares the current user's information with the note’s owner field and if it matches, it will let the user delete the note. It is important for the application to ensure that user actions are authenticated properly.  

 

##### FLAW 4: Sensitive Data Exposure 

[Link to the code](https://github.com/AapoTuulentie/CyberSecurity2023/blob/60c9e0a837f30fe1d93f42270db3ed507cc61168/mysite/mysite/settings.py#L134) 
The fourth flaw is sensitive data exposure. Moving on from views.py to settings.py, there is a flaw in password hashing procedures. Django’s settings.py allows coders to modify the password hashers and use their own hashers. This application uses the outdated MD5 password hasher, which can be found in hashers.py file, that does not salt passwords. Salting means adding random data into a password string before hashing it and storing it into a database. Without salting, the hasher will always produce the same hash with the same password.  

The fix uses five different hashers that are all salted. By default, Django will use the hasher listed on the top of the list, which in this case is PBKDF2PasswordHasher. It will also be able to use the rest of the hashers to validate the password, depending on which of them the password is hashed with. These hashers will provide a salted password hash, that makes a password much more difficult for attackers to crack. By cracking a password, the attacker gains access to sensitive data, thus making it fall under the category of sensitive data exposure.  

 

##### FLAW 5: Insufficient Logging and Monitoring 

[Link to the code](https://github.com/AapoTuulentie/CyberSecurity2023/blob/60c9e0a837f30fe1d93f42270db3ed507cc61168/mysite/mysite/settings.py#L148) 
The fifth and final flaw in the application is insufficient logging and monitoring. In settings.py, logging is disabled with LOGGING_CONFIG = None. Now the application does not use any logging features. Without logging, the application does not leave any traces of security breach attempts and authentication errors. This will cause the administrators of the application to be unaware of the security risks. With logging disabled in this application, the administrators would not have any messages about the other flaws in the code, making them more difficult to notice. For example, if an attacker tried to do a brute force password spray attack, it would not leave any failed login-logs. 

The fix includes a basic logger for Django. Now logging messages are sent to console in the handler section. DJANGO_LOG_LEVEL is set to INFO, which is the second most detailed logging level. It gives detailed information about the program. For example, console gets information about database queries, user activity and sessions. The log level could also be set to DEBUG mode, where the logging messages would be very detailed.

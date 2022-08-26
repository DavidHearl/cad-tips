# Inventor Blog - [Live Website](https://cad-tips.herokuapp.com/)

https://github.com/DavidHearl/cad-tips

Multi Device Layout will go here
https://techsini.com/multi-mockup/index.php

## About
---

CAD Tips is a fully responsive blog where users can come to learn how to use Autodesk Inventor.
The user will find helpful posts and examples which they can complete to increase their skill!

## User Stories
---

### Admin

- As an Admin I want to create, read, update and delete posts so that I can manage my blog content.
- As an Admin I want to create draft posts so that I can take more time to create content.
- As an Admin I want to remove comments so that I can filter content on the website.

### User

- As a site User I want to view comments on the article so I can read the conversation and get more knowledge.
- As a Site User I want to register an account so that I can comment.
- As a Site User I want to leave a comment on a post so that I can be involved in a conversation.
- As a Site User I want to delete my comment so that I can remove any errors that I have made
- As a site User I want to be able to update my profile information so that my details stay correct.

### Visitor

- As a visitor I want to see a list of posts so that I can select the post I would like to read.
- As a visitor I want to click on a post so that I can read the full content as see all the information.
- As a visitor I want to be able to share a post so that I can share content with with friends & colleagues.

## Agile Development Tool
---

For the agile methodology I used the GitHub canban board, it was here where I created the user stories, first as a draft then progressed the items to issues in the to do column. You can see a snap shot below.
![Canban_Preview](./media/Readme/Canban%20Board%20In%20Progress.PNG)

When I wanted to start working on a feature, I moved the issue from the 'todo' list to the 'in progress' list. Once the task was completed it was moved in to the completed list.

Below is a snapshot of the completed canban board.

![Canban_Done](./media/Readme/Canban%20Board%20Completed.png)

## Code Validation

All Python files passed PEP8 validation through http://pep8online.com. See below the list of files that have been validated.
- blog/admin.py - Passed
- blog/apps.py - Passed
- blog/forms.py - Passed
- blog/models.py - Passed
- blog/urls.py - Passed
- blog/views.py - Passed
- cad_tips/urls.py - Passed

All HTML Templates passed HTML validation through






![Post Detail - Desktop](./media/Readme/Post%20Detail%20-%20Desktop.png)
![Post Detail - Tablet](./media/Readme/Post%20Detail%20-%20Tablet.png)
![Post Detail - iPhone](./media/Readme/Post%20Detail%20-%20iPhone.png)
![Post List - Desktop](./media/Readme/Post%20List%20-%20Desktop.png)
![Post List - Tablet](./media/Readme/Post%20List%20-%20Tablet.png)
![Post List - iPhone](./media/Readme/Post%20List%20-%20iPhone.png)

## Design



## Issues
---

As the emails are not sent using a local SMTP server but instead a google account there may be some issues. 
Google sometimes blocks the ability to log into google with a 3rd part application, as a fallback emails will be logged to the console.

## Pass Criteria

| Number | Marking Criteria | Met |
|:-:|:----------|:---:|
|1.1|Design a Front-End for a data-driven web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of user interactions.|x|
|1.2|Implement custom HTML and CSS code to create a responsive Full-Stack application consisting of one or more HTML pages with relevant responses to user actions and a set of data manipulation functions|x|
|1.3|Build a database-backed MVC web application that allows users to store and manipulate data records about a particular domain.|x|
|1.4|Design a database structure relevant for your domain, consisting of a minimum of one custom model.|x|
|1.5|Use an Agile tool to manage the planning and implementation of all significant functionality|x|
|1.6|Document and implement all User Stories and map them to the project within an Agile tool|x|
|1.7|Write Python code that is consistent in style and conforms to the PEP8 style guide and validated HTML and CSS code.||
|1.8|Include sufficient custom Python logic to demonstrate your proficiency in the language|x|
|1.9|Include functions with compound statements such as if conditions and/or loops in your Python code|x|
|1.10|Write code that meets minimum standards for readability (comments, indentation, consistent and meaningful naming conventions).||
|1.11|Name files consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatibility.|x|
|1.12|Document and implement all User Stories within the Agile tool and map them to the project goals||
|1.13|Document the UX design work undertaken for this project, including any wireframes, mockups, diagrams, etc.,created as part of the design process and its reasoning. Include diagrams created as part of the design process and demonstrate that these have been followed through to implementation||
|2.1|Develop the model into a usable database where data is stored in a consistent and well-organised manner.|x|
|2.2|Create functionality for users to create, locate, display, edit and delete records|x|
|2.3|All changes to the data should be notified to relevant user|x|
|2.4|Implement at least one form, with validation, that allows users to create and edit models in the backend|x|
|3.1|Apply role-based login and registration functionality|x|
|3.2|The current login state is reflected to the user|x|
|3.3|Users should not be permitted to access restricted content or functionality prior to role-based login.||
|4.1|Design and implement manual and/or automated Python test procedures to assess functionality, usability, responsiveness and data management within the entire web application||
|4.2|Design and implement manual and/or automated JavaScript test procedures to assess functionality,usability, responsiveness and data management within the entire web application||
|4.3|Document all implemented testing in the README.||
|5.1|Use Git & GitHub for version control of a Full-Stack web application up to deployment, using commit messages to document the development process.|x|
|5.2|Commit final code that is free of any passwords or security-sensitive information to the repository and the hosting platform||
|6.1|Deploy a final version of the Full-Stack application code to a cloud-based hosting platform and test to ensure it matches the development version||
|6.2|Ensure that the final deployed code is free of commented out code and has no broken internal links||
|6.3|Document the deployment process in a README file in English||
|6.4|Ensure the security of the deployed version, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off||
|7.1|Design a custom data model that fits the purpose of the project|x|


## Requirements

- pip3 install django
- pip3 install dj_database_url
- pip3 install psycopg2-binary
- pip3 install dj3-cloudinary-storage
- pip3 install gunicorn
- pip3 install Pillow
- pip3 install django-summernote
- pip3 install django-crispy-forms
- pip3 install django-allauth
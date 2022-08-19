## Requirements

- pip3 install django
- pip3 install dj_database_url
- pip3 install psycopg2-binary
- pip3 install dj3-cloudinary-storage
- pip3 install gunicorn

## Issues

As the emails are not sent using a local SMTP server but instead a google account there may be some issues. 
Google sometimes blocks the ability to log into google with a 3rd part application, as a fallback emails will be logged to the console.
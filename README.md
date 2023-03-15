## Rewardo - Earn points by downloading apps

Stack - Django, Postgres, DRF, JWT, Bootstrap, Swagger, uwsgi, Nginx, AWS EC2

URLs -
Homepage - [Rewardo](http://13.233.96.71/accounts/login/?next=/)
Admin - [Admin](http://13.233.96.71/admin/login/?next=/admin/)

BRIEF - A list of apps are available to user in home page after logging in.
user clicks on an app and can upload a screenshot of downloaded app.
He completes a task and earns points.

                              API 
-------------------------------------------------------------------
    URLS                                    METHODS
-------------------------------------------------------------------
    # homepage
    '/api/v1/'                              GET

    # apps URLS                           
    '/api/v1/apps/'                         GET
    '/api/v1/app/<int:app_id>/'             GET, POST

    # tasks and points URLS
    '/api/v1/completed-tasks/'              GET
    '/api/v1/total-points/'                 GET

    # user profile URLS
    '/api/v1/profile/'                      GET
    '/api/v1/profile/update/'               GET, POST

    # all-auth logout URL
    '/api/v1/accounts/logout/'              POST

    # JWT Tokens URLs
    '/api/v1/token/'                        GET
    '/api/v1/token/refresh/'                GET, POST
    '/api/v1/token/verify/'                 GET

##### [Deployed on AWS EC2](./DEPLOYMENT.md)
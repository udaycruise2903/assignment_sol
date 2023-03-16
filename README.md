## Rewardo - Earn points by downloading apps

Stack - Django, Postgres, DRF, JWT, Bootstrap, Swagger, uwsgi, Nginx, AWS EC2

Homepage - [Rewardo](http://13.233.96.71/accounts/login/?next=/)
Admin - [Admin](http://13.233.96.71/admin/login/?next=/admin/)

BRIEF - A list of apps are available to user in home page after logging in.
user clicks on an app and can upload a screenshot of downloaded app.
He completes a task and earns points.


                            API Urls

    | NAME                | URL                                       | METHODS   |
    | ------------------- | ----------------------------------------- | --------- |
    | home                | '127.0.0.0:8000/'                         | GET       |
    | home                | '127.0.0.0:8000/api/v1/'                  | GET       |
    | ------------------- | ----------------------------------------- | -------   |
    | apps                | '127.0.0.0:8000/api/v1/apps/'             | GET       |
    | single app          | '/127.0.0.0:8000api/v1/app/<int:app_id>/' | GET, POST |
    | ----                | ------------------------                  | -------   |
    | tasks               | '127.0.0.0:8000/api/v1/completed-tasks/'  | GET       |
    | ----                | ------------------------                  | -------   |
    | points              | '127.0.0.0:8000/api/v1/total-points/'     | GET       |
    | ----                | ------------------------                  | -------   |
    | user profile        | '127.0.0.0:8000/api/v1/profile/'          | GET       |
    | update user profile | '127.0.0.0:8000/api/v1/profile/update/'   | GET, POST |
    | ----                | ------------------------                  | -------   |
    | logout              | '127.0.0.0:8000/api/v1/accounts/logout/'  | POST      |
    | ----                | ------------------------                  | -------   |
    | JWT tokens          | '127.0.0.0:8000/api/v1/token/'            | GET       |
    | refresh token       | '127.0.0.0:8000/api/v1/token/refresh/'    | GET, POST |
    | verify token        | '127.0.0.0:8000/api/v1/token/verify/'     | GET       |
    | ----                | ------------------------                  | -------   |

                            Other Urls
    
    | NAME          | URL                                        |
    | ------------- | ------------------------------------------ |
    | jet           | '127.0.0.0:8000/jet/'                      |
    |               | '127.0.0.0:8000/jet/dashboard/'            |
    | ------------- | ------------------------------------------ |
    | rest-api-auth | '127.0.0.0:8000/api-auth/'                 |
    | ----          | ------------------------                   |
    | tasks         | '127.0.0.0:8000/api/v1/completed-tasks/'   |
    | ----          | ------------------------                   |
    | all-auth      | '127.0.0.0:8000/accounts/'                 |
    | ----          | ------------------------                   |
    | admin         | '127.0.0.0:8000/admin/'                    |
    | ----          | ------------------------                   |
    | swagger       | '127.0.0.0:8000/docs/'                     |
    |               | '127.0.0.0:8000/openapi/'                  |
    |               | '127.0.0.0:8000/swagger/'                  |
    |               | '127.0.0.0:8000/redoc/'                    |
    | ----          | ------------------------                   |
    | debug         | '127.0.0.0:8000/**debug**/'                |
    | ----------    | ------------------------                   |


### [Deployed on AWS EC2](./DEPLOYMENT.md)

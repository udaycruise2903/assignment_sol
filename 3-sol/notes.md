### Note on my choice on periodic task scheduling

My choice of system to schedule periodic tasks would be (Celery)[https://docs.celeryq.dev/en/stable/]. because it provides a simple interface for scheduling periodic tasks. Allows for the configuration of various options such as task priority, retry behavior, and timeouts. It also integrates with many  message brokers - RabbitMQ, Redis, and Apache Kafka, making it easy to scale and distribute tasks across multiple worker nodes.

FEATURES - task result caching, monitoring with flower and task chaining

PROBLEMS -  
1. It requires lotv of effort to set up and configure correctly, 
2. More difficult to use with large-scale distributed systems. 



#### FLASK versus DJANGO 

1. I choose Flask for light-weight small-sized projects, django for large projects.
2. Flask has Jinja compared to Django's builtin template engine is considerably better.
3. A certain level of expertise is required to use the level of customisation availble in Flask.
4. developers can implement exactly their needs using flask framework. 
5. Django has ready-to-use admin framework & other third-party admin libraries to choose from, compared to flask.
6. For enterprise-level applications, Django's built-in template loaders, middleware, sites, etc. save a lot of developer's time.
7. Django should be used in projects using RDBMS, as it has ORM support for different SQL dialects. 
8. for custom Class-based views instead of Django's defaults, flask can be used.
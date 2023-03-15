### Deployed on AWS EC2

1. create a EC2 instance and edit security groups.
2. generate ssh keys & add them in EC2 dashbaord(import at keypairs). 
ssh into EC2 instance
3. setup ubuntu with system dependencies.
4. create usergroups and add a user to it.
5. create /webapps/rewardo and chown the user
6. install postgresql, setup database.
7. switch to user1 with command `sudo su - user1`
8. clone repo from gitlab
9. create venv and install requirements.
10. run migrate, createsuperuser, collectstatic
11. add domain to .env file
12. create uwsgi.ini file and configuration
13. create log,run,conf folders in the `user1`
14. run chmod on log and run folders.
15. to start server, run `uwsgi --ini /webapps/rewardo/conf/uwsgi.ini`
16. switch back to sudo user and create a systemd unit file for uwsgi
17. run `sudo nano /etc/systemd/system/uwsgi.service` and add configurations
18. run `sudo systemctl daemon-reload` to reload systemd manager config.
19. run `sudo systemctl enable uwsgi` to enable uwssgi service
20. run `sudo service uwsgi start` to start uwsgi service
21. install nginx
22. remove default folders in sites-available and sites-enabled directories.
    run `sudo rm -rf /etc/nginx/sites-available/default`
    run `sudo rm -rf /etc/nginx/sites-enabled/default`
23. run `sudo nano /etc/nginx/sites-available/nginx-uwsgi.conf` to create nginx config file
24. update the `nginx-uwsgi.conf` file
25. Create symbolic link into sites-enabled directory for same
    `sudo ln -s /etc/nginx/sites-available/nginx-uwsgi.conf /etc/nginx/sites-enabled/nginx-uwsgi.conf`
26. run `sudo systemctl daemon-reload` to reload systemctl daemon
27. enable and start nginx service again.
28. run `sudo nginx -t` to check if nginx config is successful
29. visit [my domain](http://13.233.96.71/accounts/login/?next=/) to find the website.


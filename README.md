
# Activity Tracking System
The Activity Tracking System is designed to manage and track various elements of organizational projects and activities. It includes modules for managing funders, projects, planning sheets, funds allocation, and activities. The system is equipped with workflows to streamline processes related to activities, planning sheets, and fund allocations.
### Features:
    1. Activity Tracking
    2. Planning Sheet 
    3. Funds Allocation
    4. Tracking Project Details
    5. Tracking Funder Details
    6. Senior Management Page
    7. Current Month Details View
    8. Activity Tracking Dashboard
    9. Reports based on Roles
    10. Role based Access - City Manager, State Manager, 
        Deputy Director, Department Heads, Executive Director.

### Dependencies
To setup Activity Tracking System, you'll need Frappe Framework.
Frappe Framework: A full-stack web application framework built with Python and JavaScript. It provides the foundation for building and customizing web applications.
### Prerequisites for Installing Frappe Framework on VM
Before installing Frappe Framework on your virtual machine (VM), ensure that you have the following prerequisites:
- Operating System: Ubuntu 22.04 LTS
- Python: Version 3.10
- Node.js: Version 21.0 or higher.
- MariaDB: Version 10.6
- Redis: Version 5.x or higher.
# Installation
Installing Frappe Framework: Frappe Version 16

    1. Install Prerequisites
    - sudo apt update
    - sudo apt install git python-dev python-pip redis-server
    - sudo apt install software-properties-common
    - sudo apt-get update
    - sudo apt install -y mariadb-server mariadb-client
    - mysql_secure_installation
        - Enter current password for root: (Enter your SSH root user password)
        - Switch to unix_socket authentication [Y/n]: Y
        - Change the root password? [Y/n]: Y
        - Remove anonymous users? [Y/n] Y
        - Disallow root login remotely? [Y/n]: N
        - Remove test database and access to it? [Y/n]: Y
        - Reload privilege tables now? [Y/n]: Y

    - sudo apt install curl
    - sudo curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
    - nvm install 21
    - node -v
    - sudo apt-get install npm
    - npm install -g yarn
    - apt-get install xvfb libfontconfig wkhtmltopdf
    - sudo pip3 install frappe-bench
    2. Creating Site and Installing the applications:
    - bench new-site [site_name]
    - bench get-app 'URL for Activity Tracking System'
    - bench --site [site_name] install-app activity_tracking_system


### Contact
For any inquiries or feedback, please contact us at hello@tech4goodcommunity.com.

Creating Python virtualenv in Windows
If python is installed in your system, then pip comes in handy. So simple steps are: 1) Install virtualenv using

 > pip install virtualenv 

2)Now in which ever directory you are, this line below will create a virtualenv there

 > python -m venv myenv

And here also you can name it anything. 3) Now if you are same directory then type,

 > myenv\Scripts\activate

You can explicitly specify your path too. Similarly like Linux you can deactivate it like

$ deactivate

Install Flask on Windows or Linux
Step 1: Make sure that Python PIP should be installed on your OS. You can check using the below command.

pip -V
or
pip --version

Step 2: At first, open the command prompt in administrator mode. Then the following command should be run. This command will help to install Flask using Pip in Python and will take very less time to install. According to the machine configuration, a proper Flask version should be installed. Wait for some time till the process is completed. After completion of the process, Flask is completed successfully, the message will be displayed. Hence Installation is successful.

pip install flask

Step-1: Install MySQL workbench. Link to install : https://dev.mysql.com/downloads/workbench/ 

Know more about it : 

https://www.mysql.com/products/workbench/ 

Step-2: Install ‘mysqlbd’ module in your venv.

pip install flask-mysqldb
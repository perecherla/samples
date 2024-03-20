<code>
python -m venv venv
</code>

# For windows
<code>
venv\Scripts\activate
</code>

# For Mac/Linux
<code>
source venv/bin/activate
</code>

If successful, (venv)will appear in your cmd/terminal prompt. (ps. if you want to deactivate the virtual environment, run deactivate on the terminal)

After you have activated the virtual environment, you will need to install Locust with pip by running:

<code>
pip install locust
</code>


You could run the program with this command (note that I’ll be using the command for CLI or without the browser’s interface as it’s more likely to be used this way in servers that don’t have access to web browsers):

<code>
locust -f locust.py --headless -u 10000 -r 50 -t 1h --html report.html
</code>

With the parameter — headless , locust will start immediately without the web interface. This is preferable especially if you’re doing this on a server (with ssh) and not on your local computer with browsers available. Then for the other parameters, the -u parameter is the maximum number of consecutive users that will do the requests, the -r parameter is the rate to spawn users at users per second, the -t parameter which is the time of the test, and lastly — html parameter which will store a HTML report to the file path specified


Three Types of Load Tests in Python

To do the three types of load tests, we can just play around with the parameters that we can set (and of course the locust file itself if it’s needed).

# <b>Load Testing:</b>

To do the usual load testing, you just need to determine every parameter as you need it. For example, you want to know if your server can take 100 consecutive users in a span of 30 minutes, you would write this command:

<code>
locust -f locust.py --headless -u 100 -r 10 -t 30m --html report.html
</code>

# <b>Stress Testing:</b>

For stress testing, you would want to write a really 
big number for parameter -u. This is because we want to 
try the maximum number of users and try to break the 
application. This is to find out our website’s 
limit and how it reacts to it. So you could put 
a ridiculous number like 1 million for the parameter -u, 
and parameter -r that is somewhat large too
so it doesn’t take too long. The -t parameter can 
be whatever you want as long as you can see the result
of the stress testing.

<code>
locust -f locust.py --headless -u 1000000 -r 50 -t 30m --html report.html
</code>

# <b>Endurance Testing:</b>

For endurance testing, the most important thing is to set the parameter -t to a long time, for example for 3 days or 1 week. This is to test if your website can handle these constant requests for a prolonged amount of time. The number of users can be set to a normal/expected load for your website.

<code>
locust -f locust.py --headless -u 100 -r 10 -t 3d --html report.html
</code>

<b>Reference Link:</b>

https://medium.com/@rico098098/load-testing-with-python-fea13369af43
https://www.jetbrains.com/help/pycharm/markdown.html#preview

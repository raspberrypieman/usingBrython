# usingBrython
Examples of using Brython to create web pages

canvasJSexample.html - This, together with its companion, canvasJSexample.py, is an example of using 
Brython together with Canvas.js (https://canvasjs.com) to produce some simple charts.
Ideally, I would have liked to do everything in Brython, however, this is as compact as I have been able make the Javascript part. If anyone can suggest a way to minimise it further or to fully do without the Javascript I would be appreciate any suggestions.

Web pages with calls to Brython cannot be run using the file:// protocol, so if you want to view the canvasJSexample.html file, first download it and its companion, canvasJSexample.py together with pythonWebserver.py, all to the same folder.

Then run pythonWebserver.py using IDLE or some other Python IDE, in that same folder and then launch a browser and point it to the ip address displayed by pythonWebserver.py. It wil be something like: 192.168.0.11:8081
The browser should display a directory listing of the folder. Click on canvasJSexample.html and you should see the chart. In canvasJSexample.py I use radio buttons to change the chart type and you could also change the theme of the chart in a similar way to 'light2', 'dark1', 'dark2' etc.

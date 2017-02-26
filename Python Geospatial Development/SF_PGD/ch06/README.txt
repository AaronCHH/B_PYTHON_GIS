ABOUT THE CODE EXAMPLES
-----------------------

The Python scripts in this directory are taken from Chapter Nine of the Python
Geospatial Development book.  These consist of the following three files:

  cgi-bin/greatCircleDistance.py

    This example CGI script implements an example web service that calculates
    and returns the great-circle distance, in meters, between two points.

  webServer.py

    A simple HTTP web server that can be used to run the greatCircleDistance.py
    CGI script.

  callWebService.py

    A simple test script to call the greatCircleDistance.py web service and
    display the result.

There are also two HTML files which you can use to test out the OpenLayers and
Leaflet slippy map interfaces.  Simply open these two files ("openlayers.html"
and "leaflet.html") in a web browser to see the results.

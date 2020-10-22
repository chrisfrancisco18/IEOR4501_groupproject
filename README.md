# IEOR4501_groupproject

# A Brief Description
This is a set of Django codes which is to import a csv format file of stored squirrel data, consisting of 31 columns/attributes, and each row representing a single instance of squirrel sighting.

# Project Group
Fall 2020, Group 13 (Peeratach Ritthikarn: chrisfrancisco18, Doohyung Yun: dy2423)

# Primary Functions and Methods
Import Management Command: Located in the /adopt/management/commands directory, custom command importer_test.py enables the transformation of csv data into a dbsqlite-form data set, stored in the environment.
  
Export Management Command: Also located in the /adopt/management/commands directory, sqdata_export.py transforms the SQL-form query data in the Django environment into a csv file with corresponding column names.  
  
Map View: Being the first view method in the /adopt/views.py, this map view makes use of the leafletjs website. When directed to /map url address, this view can display 100 dots on the Google map from the 100 randomly sampled squirrel instances from the imported data queryset, and referencing from each instance's (x,y) coordinates.  
  
List of Sightings View: The second view method is enabled when the user directs herself to /sightings via url. This view provides the full list of all registered squirrel instances with some of the representative attributes such as Unique Squirrel ID being displayed. This view also reflects changes of the squirrel database whenever there has been an adding or update, whenever the /sightings html is refreshed.  
  
Detail of Sightings View: Named squirrel_detail, the view supports a clickable button to redirect the user into a url /sightings/"unique_squirrel_id" which displays the detailed attributes of that particular squirrel instance, and also supports a form that could be used by the user to update the attributes of the particular squirrel. When provided with a valid update, the squirrel data is modified and the user will receive a message of gratitude.  
  
Add View: Named sights_add, the view can be reached by the user via a button located at the top of the /sightings url, and directs the user to /sightings/add where the user is given with a form that can be filled to "add" a new instance of squirrel.
  
General Statistics View: Named stats_act, the view provides the user with

# A disclaimer on  contributions
At the early stage of our project, we faced frequent variable differences and errors followed by them. Fortunately we were able to manage to meet in-person and resolve the issues, mainly via Peeratch's personal computer, being the reason for the large gap of commit number differences.  
  
Another issue is regarding the username: while Doohyung Yun uses the GitHub ID dy2423, many of the push commits are not name dy2423, but as Doohyung Yun, thus dy2423's commit number is a misrepresentation of the actual contributions.  
  
To clarify the work load division, Peeratch Ritthikarn primarily worked on map, listing of sightings, detail of sightings, and general statistics view. Doohyung Yun worked on the construnction of import/export commands, with dbsqlite3 management, detail-update view, and the add-sighting view. In addition, 15+ hours of offline cooperations for debugging and test runs must be included.  

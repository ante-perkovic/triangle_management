# Welcome to Triangle Management App!

Triangle Managment is a desktop application using Python 3 that supports CRUD operations for managing triangles. Tkinter is used for visualisation and SQLite3 for database.

## Requirements

1. Have Python 3 installed on your machine (for reference I used 3.11)
2. That's it, enjoy!

## How to start the app?

1. Clone git repo to a folder of your choosing
2. Position yourself with the terminal inside the repository folder
3. Start the app with the following command: `python main.py` (might be `python3 main.py` depending on your environment

## How to use the app?

1. Choose from the following options: `Create New Triangle` , `Stored Triangles`
   ### Create New Triangle
   1. Choose one way to create a triangle
   2. Fill the fields with the wanted triangle data (make sure to give it a creative name)
   3. Click on `Submit` if you want to view the triangle and save it
   4. You will be provided with the visual representation and calculations of perimiter, area size and type of triangle for your particular triangle
   ### Stored Triangles
   5. You can use the Search bar to search for existing triangles in the database and clicking on the `Search` button. (you don't have to type the whole name)
   6. Under the search bar there will be a list of existing triangles stored in the database labeled with their ID and Name
   7. Next to each label there are three options for the triangles: `View`, `Edit` and `Delete`
   8. View will provide you with the visual representation and calculations of perimiter, area size and type of triangle for your particular triangle
   9. Edit will open a window in which you can change the points of the triangle and its name, after you are satisfied with your edit, you can press `Submit` to save your changes which will update the triangle list with new data
   10. Delete will permanently delete the triangle from database

## Improvements?

If I were to spend more time on this project I would make the editing feature more intuitive by enabling editing of triangle side sizes and angles.
I would also add unit tests and further clean up the code

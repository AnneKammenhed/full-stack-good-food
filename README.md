## Gitpod Reminders

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.
To migrate changes to the database: `python3 manage.py migrate` (`python3 manage.py makemigrations --dry-run`)
To run the project `python3 manage.py runserver`

python3 manage.py migrate --run-syncdb

<h1>Welcome to Good Food!</h1>

<h2>Background</h2>
This project is the fourth in my full stack developer course at Code Institute that I will be completing in october 2022. 

It is a restaurant booking app with a website to promote Good Food.

<h2>Development</h2>
I installed Django and the supporting libraries. Since I will deploy the project to Heroku I also installed gunicorn as the server that I will use to run Django on Heroku. 

The supporting libraries are postreql and psycopg2. 

The images will be on Cloudinary. 

I called the project "goodfood" in Django and the app is called "food". 

I went back and fourt during development between one or several models. There has been models for guest and TimeDateFields too but in this one there is one model called Booking. 

The guest-model has also been based on either ForeignKey User or a CharField. Since the requirement is to be able to erase bookings, I went with the User solution. It is a one to many relationship since Good Food likes its guests to come back but it is not possible for the same guest to book twice on the same time.

This app was created using three different repositories. In troubleshooting the first repository, I found that many changes to the models can make the latest changes clash with the first ones. After removing the migrations files and migrating again there is still an issue of unapplied migrations and programming error in the admin panel wher the admin form is visible for each model, but its not possible to see the list of bookings or menu items or to add anything to the database. 

The second repository was not connected to Heroku and there I succeeded in getting a model working to book times. To be sure not to run in to the same problem as in the first repository, I also created a third repository (not connected to Heroku) where I tried to connect the model to djangos TimeDateField without any success. I also connected the User function since this is the solution that I found for the guest to be able to erase his or her booking (requirement for the project).  


<h2>Deployment</h2>
Cloudinary
Heroku

<h2>Tests</h2>


------

<h2>Credits</h2>

This site is built on the Code Institute student template for Gitpod with preinstalled tools to get started. I reused the templates from the Django Blog walkthrough project for the html in this project.  

Django


---

Enjoy!

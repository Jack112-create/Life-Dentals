# Life Dentals

## Introduction

Life Dentals is a full stack web application built for the purpose of allowing users to book in for a dental service with the fictional organization. Life Dentals is my fourth portfolio project with Code Institute.

![Screenshot of responsive site](./docs/images/responsive-screenshot.png)

The link to the live version of this project can be found [here](https://life-dentals.herokuapp.com/).

## Table of Contents

* [User Experience](#Introduction)
    * [Site Goals](#Site-Goals)
    * [User Stories](#User-Stories)
    * [Strategy Plane](#Strategy)
    * [Scope Plane](#Scope)
    * [Structure Plane](#Structure)
    * [Surface Plane](#Surface)
        * [Design](#Design)
    * [Features](#Features)
    * [Testing](#Testing)
    * [Bugs](#Bugs)
    * [Deployment](#Deployment)
    * [Credits](#Credits)


## UX

### User Stories

* As a user, I want to a clear form of navigation so that I can navigate through the site more easily.

* As a user, I want to be able to book an appointment so that I can have the required treatment.

* As a user, I want to update or cancel my bookings so that I can reschedule for a later date.

* As a user, I want to be able to register and log in so that I can view my bookings.

* As a user, I want to view all available treatments so that I can choose the appropriate booking.

* As a user, I want to read any testimonials so that I can read people's opinions and experiences of the provided service.

* As a user, I want to have access to contact information, so that I can get in touch with the clinic.

* As an admin user, I want access to all patient bookings so that I can delete or update any bookings (incomplete).

### Site Goals

* As a site owner, I want to provide a service to people looking to receive oral care so that they can improve their oral health.

* As a site owner, I want to provide users with a visually appealing website so that they have a positive user experience when browsing the site.

### Strategy

* Life Dentals is a dental service web application that provides both regular users, and users that have created an account, with information about the services that are available at Life Dentals. Users that have created an account gain access to the booking feature, allowing them to book in with Life Dentals for anytime, for any treatment, for any date.

* The overall design is quite simple, reducing the barrier that users sometime face when visiting their favourite sites.

### Scope

Features to be included:

* Responsive Design - The site should function correctly on all screen sizes. The design should allow users to have a good experience when visiting the site no matter what device they use when visiting.

* Navigation -  Navigation elements should be clear to the user. The main site navigation should be clear to the user that the links will bring them to other pages on the site.

* Users should be able to create, update and delete a booking if they have created an account. This feature should not be available to users who do not have an account.

### Structure


### Surface

*  #### Design

  * Colours
    - ![Colour Palette](/docs/images/colour-palette-1.png)
    - ![Colour Palette](/docs/images/colour-palette-2.png)

  * Icons:
    - Font Awesome was used to add icons to multiple sections throughout the site, such as the employee section on the homepage and the footer.

  * Typography:
    - Google Fonts was used to add the "Assistant" font to the project. The "Assistant" font family was chosen as I felt it added to the simple yet visual aesthetic.

#### Wireframes
* Balsamiq was used for this project. Balsamiq allowed me to create mockup designs for each feature and layout for this project.

![Homepage Desktop Wireframe](/docs/wireframes/Homepage-Desktop.png)

![Homepage Desktop Wireframe](/docs/wireframes/Homepage-Tablet.png)

![Homepage Mobile Wireframe](/docs/wireframes/Homepage-Mobile.png)

![Treatments Page Desktop Wireframe](/docs/wireframes/Treatments-Desktop.png)

![Treatments Page Tablet Wireframe](/docs/wireframes/Treatments-Tablet.png)

![Treatments Page Mobile Wireframe](/docs/wireframes/Treatments-Mobile.png)

![Contact Page Desktop Wireframe](/docs/wireframes/Contact-Desktop.png)

![Contact Page Tablet Wireframe](/docs/wireframes/Contact-Tablet.png)

![Contact Page Mobile Wireframe](/docs/wireframes/Contact-Mobile.png)

![Login Page Desktop Wireframe](/docs/wireframes/Login-Desktop.png)

![Login Page Tablet Wireframe](/docs/wireframes/Login-Tablet.png)

![Login Page Mobile Wireframe](/docs/wireframes/Login-Mobile.png)

![Booking Page Desktop Wireframe](/docs/wireframes/Booking-Desktop.png)

![Booking Page Tablet Wireframe](/docs/wireframes/Booking-Tablet.png)

![Booking Page Mobile Wireframe](/docs/wireframes/Booking-Mobile.png)

![Booking Form Desktop Wireframe](/docs/wireframes/BookingForm-Desktop.png)

![Booking Form Tablet Wireframe](/docs/wireframes/BookingForm-Tablet.png)

![Booking Form Mobile Wireframe](/docs/wireframes/BookingForm-Mobile.png)

#### Database Schema

![Database Schema](/docs/images/database-schema.png)

* The Life Dentals project makes use of 3 custom models - Booking, Treatment and User. The screenshot displays an extra custom model - Testimonials - which I was unable to implement due to time restraints. A user profile is required in order to create a booking. The treatments model is then also linked to the booking model so that when users create a booking, they can choose from all available bookings that are stored within the database.

### Features

#### Homepage

![Homepage Live Screenshot](/docs/images/homepage-live.png)

- The homepage is the first page the user is directed to when visiting Life Dentals. The homepage provides users with basic details about Life Dentals, such as - details about the members of staff, the Life Dentals vision and a link for the user to create their first booking.

**Site Owner Goal related to this feature:**

* As a site owner, I want to provide users with a visually appealing website so that they have a positive user experience when browsing the site.

#### Navigation

![Navbar Live Screenshot](/docs/images/navbar-live.png)

- The navbar is fully responsive and correctly links to the appropriate pages provided within the navigation. The responsiveness of the navbar provides users to be able to navigate throughout the site no matter what device they use.

**User stories related to this feature:**

* As a user, I want to a clear form of navigation so that I can navigate through the site more easily.

#### Treatments Page

![Treatments Live Screenshot](/docs/images/treatments-live.png)

- The treatments page provides users with information about the available treatments at Life Dentals. Information includes: treatment name, price and procedure duration. Patient testimonials are also present at the bottom of the page so that users can read about some of the patient experiences.

**User stories related to this feature:**

* As a user, I want to view all available treatments so that I can choose the appropriate booking.

* As a user, I want to read any testimonials so that I can read people's opinions and experiences of the provided service.

#### Contact Page

![Contact Live Screenshot](/docs/images/contact-live.png)

- The contact page allows users to get in contact with the Life Dentals staff by sending them a message through the contact form. Once a user has filled in the required fields, they can send their query which will be received by the Life Dental email.

**User stories related to this feature:**

* As a user, I want to have access to contact information, so that I can get in touch with the clinic.

#### Register & Login

![Register Live Screenshot](/docs/images/register-live.png)

![Login Live Screenshot](/docs/images/login-live.png)

- Depending on if a user has created an account or not - they will be shown different links within the sites main navigation. If a user is signed in, the "booking" navigation link will appear, and the "login" navigation link changes to "logout".

- The register page provides the user with a form to register for an account. The form requires to fill in multiple fields - which upon a successful completion - will grant the user access to create a booking.

**User stories related to this feature:**

* As a user, I want to be able to register and log in so that I can view my bookings.

#### Booking

![Create Booking Live Screenshot](/docs/images/create-booking-live.png)

- The create booking page provides the user with a form to create their own booking by selecting a time, date and treatment. Each time the user selects a different date the available time slots for the date they have chosen will be displayed to them.

![Edit Booking Live screenshot](/docs/images/edit-booking-live.png)

- The edit booking page allows the user to update/edit their booking. This allows the user to change the date, time or treatment of their pre-existing booking.

![Delete Booking Live Screenshot](/docs/images/delete-booking-live.png)

- The delete booking page gives the user the ability to delete their booking. When the user clicks the "delete button", they are prompted with a message that asks if they would like to continue with the deletion.

### Future features


### Technologies


### Testing


#### Manual Testing
Test Cases:


### Bugs


#### Fixed Bugs


### Deployment

#### Creating a clone of the repository

  1. Navigate to the Life Dentals Repository (https://github.com/Jack112-create/Life-Dentals).
  2. Click on the "Code" dropdown.
  3. Copy either the HTTPS or SSH clink.
  4. Navigate to the directory on your local machine where you would like the project to be cloned into.
  5. Type "git clone", and paste the link that you copied from the remote repository.
  6. To run the project locally, you must install the requirements.txt file. This can be done by typing "pip3 install -r requirements.txt".

#### Workspace setup & Deployment onto Heroku

  **Workspace Setup:**

  1. Navigate to the Code Institue Template - https://github.com/Code-Institute-Org/gitpod-full-template
  2. Click the "Use this template" button.
  3. Enter your repository name and click the "Create repository from template" button.
  4. Once you are redirected to your new repository, click the green "Gitpod" button.
  5. Open up the terminal in your new Gitpod workspace and run the following commands:
    - pip3 install django == 3.2
    - pip3 install gunicorn
    - pip3 install dj_database_url 
    - pip3 install psycopg2
    - pip3 install dj3-cloudinary-storage
    - pip3 freeze --local > requirements.txt
  6. Create your Django project by entering the following command:
    - django-admin startproject < YOUR PROJECT NAME >
  7. Create a Django app by entering the following command:
    - python manage.py startapp < YOUR APP NAME >
  8. Add the newly created app to the "INSTALLED_APPS" list in settings.py
  9. Migrate the changes by entering the following command:
    - python manage.py migrate
  10. Run local server by entering the following command:
    - python manage.py runserver

  **Creating Heroku App:**

  1. Sign in or log in to Heroku
  2. Click the "New" button on the dashboard
  3. Select "Create new app" from the dropdown menu
  4. Enter your app name and select your region
  5. Navigate to the "Resources" tab on the dashboard.
  6. Under the heading "Add ons," enter "Heroku Postgres" into the search field.
  7. Select the "Heroku Postgress" database option. and click on it when it appears
  8. Select "Hobby Dev - Free" from the "plan name" drop-down menu and click "Submit Order Form." 
  9. Navigate back to your Gitpod workspace into settings.py and copy the SECRET_KEY variable
  10. Navigate back to your Heroku app and into the settings tab.
  11. Create a new config variable by clicking the "Reveal Config Vars" button
  12. Enter "SECRET_KEY" into the key field and enter the SECRET_KEY variable value copied from your Django project into the value field.

  **Local Environment Setup:**

  1. Navigate to your Gitpod workspace
  2. Create a file named "env.py"
  3. Import the os module
  4. Create a variable inside the env.py file and name it "DATABASE_URL"
  5. Navigate to Heroku and into your app. Click the settings tab and then the "Reveal Config Vars" button. Copy the value from the "DATABASE_URL" key on Heroku and paste it into the "DATABASE_URL" variable in your Django project.
  6. Navigate to your settings.py file and copy the value from the "SECRET_KEY" variable. Create a new variable in your env.py file and name it "SECRET_KEY". Paste the value from the "SECRET_KEY" variable in settings.py into the new "SECRET_KEY" variable in env.py
  7. Create another variable inside of env.py and name it "CLOUDINARY_URL". Copy the API key from your cloudinary account and paste it into the new variable.
  8. Navigate to settings.py and add the following lines from the screenshots below:

  - ![Import settings screenshot](/docs/images/imports-settings.png)
  - ![Apps settings screenshot](/docs/images/apps-settings.png)
  - ![Database settings screenshot](/docs/images/database-settings.png)
  - ![Static fiels settings screenshot](/docs/images/static-files-settings.png)

  **Heroku CLI Setup:**
  1. Navigate to your terminal in your Django project
  2. Enter the following command:
    - "heroku login -i"
  3. Enter your login credentials for Heroku
  4. Enter the following command:
    - "heroku apps" and locate your app name
  5. Enter the following command:
    - "heroku git:remote -a < YOUR HEROKU APP NAME >"
  6. Enter the following commands:
    - "git add ."
    - "git commit ."
  7. Push your changes to Heroku by entering the following commands:
    - "git push origin main"
    - "git push heroku main"

### Credits

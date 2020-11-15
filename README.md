
![Responsive](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Responsive.JPG)

# Althea's Bookshelf

The purpose of this project is to create a website for fellow parents or guardians to share 
the most recommended books by their young ones. These could be the books that they always read to
their toddlers before bedtime or during story times. This will be an interesting place for parents
to share their recommendations as well as their experiences when reading for their young ones.  

My inspiration for this project is our 2 years old daughter who continuously amazed us everyday.
One of her favorite times of the day is when we read her story books. She has couple of favorite books
that she always chose especially before bedtime. She loves these books to the point that she has memorized
the lines from the characters.  

For this project, I will be using python, flask and MongoDB as my primary programming language and
html, CSS, JavaScript and materialize for the front end.

To view the live version of the website please click [Alteha's Bookshelf](https://althea-bookshelf.herokuapp.com/)

# UX

## Project Goals:

#### My goals for this project are:

*  Create an interactive website where parents/guardians and/or childminders can use it as a source of information
    on what books they should get for their young ones

* The website should give the site visitor ability to suggest a book they think their toddler loves,
    add a comment or feedback to other books posted by other users at the same time it should give
    them the ability to delete or remove their account if they wish to.

#### Site Owner's Goals:

* To provide a platform for the user to share books best fit for the young ones

* Create an interactive community working towards the goal of sharing the best books for the little ones.

## User Stories:

#### Target Audience:

Our target audiences are parents/guardians and childminders who are searching for a quality books to read to their kids.

* As a parent/guardian and childminder, I should be able identify the purpose of the website 
* As a parent/guardian and childminder, I should be able get an idea of what books I should get my little ones
    based on the recommendations from fellow parents.
* As a parent/guardian and childminder, I should be able to contribute with the community by sharing
    the book/s that my kids love.
* As a parent/guardian and childminder,I should be able to view the list of books I have recommended to the community.
* As a parent/guardian and childminder,I should have the ability to edit or remove the books that I shared.
* As a parent/guardian and childminder, I should be able to add my feedback or comments to the recommended books
* As a parent/guardian and childminder, I should be able to delete my profile if I wish to do so. 
* As a parent/guardian and childminder, I should be able to view the site using my mobile phone or tablet

#### As an admin User or site owner:

* I should be able to moderate properly the page by filtering comments/feedback that are harmful to the target audience.
* I should be able to remove/delete an account or books shared if this are not appropriate to the site's purpose.

## Design:

The aim of the site design is to ensure the focus is on the book reviews.
Icons used on the site are easy to understand and read and therefore text use is avoided where possible.

#### Fonts

I chose easy to read and light fonts for this app. I am keeping it simple and will only use one type of font, Abreeze. 

#### Color Fonts

I opted for this color pallete since as per research this works better for toddlers.

![Color Pallete](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/color%20palette.JPG)

#### Icons

On this project I have used easily identifiable Font Awesome icons.

## Wireframes

I designed my site moc-ups using [balsamiq](https://balsamiq.com/) wireframes.
The idea was to create a basic layout structure of the site and identify how it will display on different screen sizes.

For more details please click [wireframe]

# Technologies used

## Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

## Libraries and Technologies
* [jQuery](https://jquery.com/)
* [Materialize](https://materializecss.com/)
* [MongoDB Atlas](https://account.mongodb.com/account/login)
* [PyMongo](https://pypi.org/project/pymongo/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com/)
* [Git](https://git-scm.com/)
* [Github](https://github.com/)
* [Heroku](https://dashboard.heroku.com/)
* [Trello](https://trello.com/b/a3dsnJ58/ms2-project)
* [Cloudinary](https://cloudinary.com)
* [Favicon](https://favicon.io/)

# Features
* Users can create an account and log in
* Users can add a book 
* Users can edit and delete book they've added
* Users can upload a photo of the book/s they've added
* Users can comment to the other books already added
* Users can update and delete each comments added

## Existing Features
There are 2 user views currently for the website, unregistered Users and Registered Users.

### Unregistered Users
* Home 
- As an unregistered users, they can search for a specific books from search area. 
- They can see the list of books added on the database

* The logo 
- Allows the users to go back to the home page

* Register 
- Allows users to create a new profile. Once created, they will be entitled to additional functionality.
- They would need to create a username, password, their toddler's name and age.
- Upon successful registration they will be redirected to the Profile Page

* Log in
- Allow users to login to their profile for complete functionality

### Registered Users
* Home 
- The users can search for a specific books from the search area.
- The users can see the list of added on the database
- The users can add a review of the books already added 
- The users can update and/or delete the reviews they've added
- If the users have already added a book, they would have the ability to delete and/or update it

* The logo 
- Allows the users to go back to the home page

* profile
- Allows users to view the list of books they've added and their profile details
- Users will have the ability to delete added books from their profile
- Users will have the ability to delete their account when they wish to.

* Add Book
- Allows the users to add book by filling out the add book form.

## Features Left to Implement
* Contact form
- This will allow the users to contact the site owner for any feedback and recommendations

* Store Link
- Add a link where the users can suggest how to purchase the books they've added 

* Admin User
- This will allow the site owner to delete in-appropriate books added or reviews

* Category
- Add a category based on age group and part of the day the books are best to be read

# Testing
For testing procedure please click [Testing.md](https://github.com/gideongannaban/althea-bookshelf/blob/master/testing.md)

# Deployment

## Deploying to Heroku
The project was deployed in Heroku by following below procedure:

1. Create requirements.txt. This can be done by runnnig the following command into the terminal.
> pip3 freeze --local > requirements.txt.
2. Once done, I created a Procfile ( capital "P" ) by running the following command into the terminal.
> echo web:python app.py > Procfile
3. Commit and push both requirements.txt and Procfile
4. Login to Heroku, click on "New" then on the dropdown choose "Create App".

![Heroku New](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Heroku.JPG)

5. Give the app a unique name and choose the region closest to your location then click "Create App"

![Heroku Name](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Heroku2.png)

6. From the deploy tab, select the Deployment method 'Github'.

![connect to Github](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Heroku3.png)

7. After clicking the "Connect to Github", make sure Github profile name is displayed then type in your repository name then click "Search". Once repo is found click on "Connect".

![connect to repo](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Heroku4.JPG)

8. Go to the Settings Tab, scroll to the "Config Vars" then click on "Reveal Config Vars".

![reveal Config](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Heroku5.JPG)

9. Enter variables(key and value) from your env.py file. Example of which are below:

![key and value](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Heroku6.JPG)

10. Once these are added in Heroku make sure you commit and push requirements.txt and Procfile from the terminal.
11. Go to the Deploy Tab in Heroku and under the Automatic Deployment section click on "Enable Automatic Deploys". 

![Automatic deploy](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Heroku7.JPG)

12. Under the Manual Deploy, click on the "Deploy Branch".

![Deploy branch](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Heroku8.JPG)

13. Heroku will now build the app using the required package. 
14. Once done, you will receive the message "Your app was successfully deployed" and click "View" to launch the app. 

## Making a Github clone
1. In the [repository page](https://github.com/gideongannaban/althea-bookshelf), click on the Clone or Download button ( right beside the Gitpod button).
2. To clone the repository using HTTPS, copy the link in the "Clone with HTTPS".
3. Open Git Bash.
* Make sure Git Bash App is downloaded in your laptop/desktop
* Paste the Cloned link using the "Git Bash here" option.

![gitbash](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/gitbash.png)

4. Type "git clone" in the Git Bash command page, then paste the URL you copied.

![gitclone](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/gitclone.JPG)

5. Press Enter to create the local clone. 

![local clone](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/localclone.JPG)

Click [Here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for additional details and more detailed explanation of the process.

# Credits

## Content 
* [Materialize 1.0.0:](https://materializecss.com/)Materialize Library used throughout the project, components used include the grid System, forms, buttons, modals, navbar, dropdown, side nav, tabs, carousel, cards, toasts, and tooltips.

* These websites contain great source of inspiration and solution whenever I encounter an error or just looking for a better way of presenting my idea:
> [W3schools](https://www.w3schools.com/)
> [Youtube](https://www.youtube.com/)
> [stackoverflow](https://stackoverflow.com/)

* Favicon logo was create from [canva](https://www.canva.com/)
* All text are written by myself

## Acknowledgement
Main source of inspiration for all my projects is our 2 years old daughter and my ever supportive wife. 

Thanks to my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for guidance on the project and for
providing online literature.

Thanks to [Tim](https://github.com/TravelTimN) for letting me preview the updated videos of the mini project Task Manager. Large parts project functionality were picked up from these videos.
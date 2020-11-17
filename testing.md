# Testing

## Manual Function Testing
Manual testing was carried out in different browsers and screen sizes to ensure site is not just responsive but also the apprearance and functionality is consisnte to all viewing platforms. The primary tool used for this was [Google Developer Tool](https://developers.google.com/web/tools/chrome-devtools) and the tests were done using the following screen sizes:
* Samsung Note 10
* Samsung S9+
* Iphone 5/SE
* Iphone 6/7/8
* Ipad/Ipad Pro
* Laptop 1024px

Summary of the testing result can be found [here](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Responsiveness.JPG). 
 
#### Browser Compatibility Testing
Browser testing was done using below browsers to ensure website can be viewed for all users. The website is responsive on all browsers except for the IE, the adding an image button overlaps in small screen. 

* Chrome
* Firefox
* Edge
* Safari
* IE

## Code Validation

### Validation of Python Code:

#### app.py 

- Checked Gitpod Python Linter
  - The Gitpod editor is clear of all PEP8 errors, except for the env which is not applicable.

- Used [pep8online.com](http://pep8online.com/checkresult)
  - The online PEP8 check returned 0 errors or warnings


### Validation for jQuerry

- jQuerry code was validated using [jshint](https://jshint.com/) with 0 error.

### Validation for CSS

- CSS was validated using [W3C](https://jigsaw.w3.org/css-validator/)


![Css](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/CSS%20Validation.JPG)


### Validation for HTML

- HTML was validated using [validator](https://validator.w3.org/). 
  - I did "CTRL + U" in Google Chrome then copied the codes. 


![HTML](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/HTML%20Validation.JPG)


## Testing User Stories

* As a parent/guardian and childminder, I should be able identify the purpose of the website 
  - When the user visits the website, they will notice immediately right below the navbar the theme of the site. As supporting note,they will see additional detail at the footer below the website's name. 

* As a parent/guardian and childminder, I should be able get an idea of what books I should get my little ones based on the recommendations from fellow parents.
  - In the middle of page, the users will see the books that have been added by other users which they believe are best to be read to their young ones. 

* As a parent/guardian and childminder, I should be able to contribute with the community by sharing the book/s that my kids love.
   - This can be achieved once the user has registered and created their profile. Upon registration they will be directed to their profile page and the Add Book tab in navbar will show which then give them the ability to share their recommended book/s.

* As a parent/guardian and childminder,I should be able to view the list of books I have recommended to the community.
  - Once the user added a book, they view the list of books they've recommended in 2 ways. First, click on Home and go over the books that have been added. They'll see the username of the person who added each book. Second and better way is for the user to click on Profile Tab and they'll see right away the list of books that they've added/ 

* As a parent/guardian and childminder,I should have the ability to edit or remove the books that I shared.
  - The user can only edit or delete books that he/she has added in the website. They can do this either through the Profile page or on the Home Page. Once the user click on Delete, they will get a modal message to confirm their action. 

* As a parent/guardian and childminder, I should be able to add my feedback or comments to the recommended books
  - The user can be able to do this provided they are still logged in on the site. When they click on a book they will see the option to add/edit or delete their own review. They wouldn't be able to do the same to the other's comments. 

* As a parent/guardian and childminder, I should be able to delete my profile if I wish to do so.  
  - The user can do this by going to the Profile Page then click on "DELETE". This will eventually delete their profile, all books added and comments posted. Once user clicks on Delete Profile, they will get a modal message to confirm their action.

* As a parent/guardian and childminder, I should be able to view the site using my mobile phone or tablet
  - Website responsiveness has been throroughly tested so the user can be able to view the website on all types of viewing platform.

### Additional Testing
 Manual testing was done using Samsung Note 10, Sony Z5 and Iphone 5 by family members and friends. The responsive design was tested using [Responsinator](https://www.responsinator.com/) and [ami.responsivedesign.](http://ami.responsivedesign.is/)websites.

### Google Chrome Dev Lighthouse
[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the quality of the web pages. 


![lighthouse](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/Lighthouse.JPG)


# Bugs:

The journey of this website is not with-out bugs either minor or major ones. These are some of the ones that took me sometime to debug. 

* I created a function to remove a book in the database however every time I do so only the 1st item in the list is being removed instead of the specific item I wanted. The function was working fine initially, I was able to remove any item from the list. I encounter the "problem" when I added the modal boilerplate for the delete button. 

 Resolution: 
   - I tried my best to resolve this by going over my codes but I was having a difficult time pinpointing the error. When I raised it over in Slack, Igor pointed what I was missing. Apparently I was missing the {{ loop.index }} which should have been added in the ID of the modal. I went over to the Thorin Project Module to refresh my memory and lo and behold it was actually discussed on that module. Everything was working fine after I added {{ loop.index }} to the modal ID and trigger. 

* I created a function that will display the user's list of added books to the database however when I try to register a new profile I was getting below error message from werkzeug-debugger. I went over my code testing every bit of it by deleting and changing however I hit a wall then reached out to the Tutors. 

Resolution:
  - With Tim's guidance, I modified my code to just find the username from my mongo db instead of the session user. 


![profile error](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/profile%20error.JPG)


* I wanted to add an option for the user to include a photo of the books that they are adding in the database. I am trying to user Cloudinary to convert the images to url so that it will be stored in the database. But everytime I do so it was giving me the error below.

Resolution:
  - I added "enctype="multipart/form-data"" in my form classes but the images were still not loading on the website. I then realized that the album name in Cloudinary should match my key in the app.py. I created a new album in cloudinary and named it "Photo" and this successfully loaded the images. 

![cloudinary](https://github.com/gideongannaban/althea-bookshelf/blob/master/Readme/Images/cloudinary.JPG)

* Before submitting the project, I did a final check and lo and behold the modal and collapsible was not working properly. Nothing is happening when I click it and I don't see any error message on my command line. 

Resolution:
  - Checked Chrome Dev Tool and its giving me an error with jQuerry "Uncaught TypeError: $(...).sidenav is not a function". Checked on my Heroku Deployed page with the help of Tutor Igor and it was working fine. Igor suggested to stop and start the workspace and this fixed the bug. 
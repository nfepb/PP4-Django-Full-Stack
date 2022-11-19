![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## **Introduction**

Welcome to WatchIt!,

WatchiIt is my fourth portfolio project that I have been working on in the Full Stack Developer Programme, as a student of the Code Institute. 

The purpose of this project was a build a full-stack website based around a business logic used to control a centrally-owned dataset. The technologies used for this project are HTML, CSS, Python, and Django. Heroku Postgres is used as a relational database.

WatchIt! is a website where anyone that enjoys watching a movie can look up movies they think is interesting to see what other website's user think of the said movie and how they grade it. WatchIt! also allows logged in users to add movies to their watchlist and add reviews on movies they have watched. 

WhatchIt! is a fictional brand. This project is for educational purposes only.
---

## **User Experience Design - UXD** 

A large part of the inspiration behind the planning for this project came from Jason James Garretts’s, “The Elements of User-Experience”.

By keeping the user in mind throughout the design and development of the project, it would be easier to make the user experience a satisfying and cohesive.

The planning of the project is broken into 5 planes,

* [The Strategy Plane](#the-strategy-pane)
* [The Scope Plane](#the-scope-plane)
* [The Structure Plane](#the-structure-plane)
* [The Skeleton Plane](#the-skeleton-plane)
* [The Surface Plane](#the-surface-plane)

---

## **The Strategy Pane**

### **App Creator's Goals**

### User Stories

To help in defining the most important benefits of the app and the features required to deliver this value, I created a flowchat that goes through the different stages of the app user. It starts with the visitor (as the user), and evolves into a connected user, which is also identified as a regular user. 

[User Flowchart](./planning-docs/user-stories/images/user-flowchart.png)

#### **Admin User Stories**

#### **Site User Stories**

#### **Logged-In User Stories**

My user stories were obtained by doing research into other apps/websites and analyzing how the user was accompanied through their journey. The [IMDb](https://www.imdb.com/) and [AlloCiné](https://www.allocine.fr/) helped me define what were some of the critical features to get to a MVP, and which features were considered 'nice to have' for later development. 

---

## **The Scope Plane**

In order to achieve the desired user & business goals, the following features will be included in this release:

* Responsive navbar that will navigate to the various pages throughout the site
* Home landing page with brief information about the movie review platform and links to the movie page 
    * Movie page, with the latest posted movie content 
    * Movie detail page, where logged-in users can post a review of the movie and grade it based on their experience watching it. 
* Movie page, with a booking form to enquire with the cycling gym
* Watchlist page, where logged-in users can add/remove movies from the list
* Register/login feature using Django allauth

Too many ideas, not enought time. Too much ambition for the defined deadline. This is the reason why. opted for a phased approach to help digest and define what I would work on in an initial deployment, and what would come in the later stage. 

**Phase 1**
- Define the critical features to satisfy the user stories:
    - A Home Page with an introduction,
    - A Navigation Bar accessible on all pages,
    - A 'Catalogue' Page to view all the movies referenced,
    - A Movie Detail Page.
    - A watchlist page

---

## **The Structure Plane**

### **Color Palette**

### **Fonts**

### **Images**

### **Database Design**

SQLite was used throughout the development of the WatchIt! app. During deployment to a production environment, Heroku PostgreSQL was used.

In order to support the functionalities defined in the user stories for each Epic, mapping the architecture became crucial. This helped foresee how we could get to an MVP.

#### **Key Models**

[Database Diagram](./documentation/schema/database-architecture.png)

**User**

* The User is created based on the User model, which is created by Allauth on registration.

**Movie**

* The Movie holds information about each movie entry in the database. Each product has a unique ID.
* The Movie model is connected to the WatchlistItem model. This allows the user to add multiple movies to a single watchlist.
* The movie includes the average_rating, which will hold the logic to calculate the average movie rating based on the reviews of the movie.  

**Review**

* Reviews can be posted by the users on the movies with this model
* The Review model has a one-to-many relationship to the User model to obtain the username. One user can post multiple reviews. 
* The Review model also is linked to the Movie model based on a one-to-many relationship. This allows one movie to have multiple reviews. 

**WatchListItem**

* The WatchListItem is used to allow the many-to-many relationship between the users and the movies. 
* One user can have multiple movies in their watchlist through the movie lookup in the Movie model. 
* One movie can be added to multiple users' watchlist through the user ID in the User model.

---

## **The Skeleton Plane**

**Navbar Wireframes**

**Homepage Wireframes**

**Movie Detail Wireframes**

**Register Wireframes**

**Login Wireframes**

---

## **The Surface Plane**

### **Features**

---

## **Technologies Used**

| Technology | Comment |
| :---: | --- |
| [dbdiagram](https://dbdiagram.io/home) | Used to design the ERD for WatchIt! |
| [Grammarly](https://www.grammarly.com/) |	Used to fix the grammar errors across the project. |
| [Canva](https://www.canva.com/)	| Used to create the wireframes for the website for the different supports. |
| [Coolors](https://coolors.co/) | Used to define the color palette for the website. |
| [Github](https://github.com/) | Used as the development environment. |
| [Pep8](https://peps.python.org/pep-0008/)	| Used to test my code for any issues or errors. |
| [Django](https://www.djangoproject.com/) | Framework used to build the project and its apps. |
| [Python](https://www.python.org/) | Python is the core programming language used to write all of the code in this application to make it fully functional. |
| [Heroku](https://dashboard.heroku.com/login) | Used to deploy the WatchIt! application. |
| [Google Fonts](https://fonts.google.com/) | |
| [Cloudinary](https://cloudinary.com/) | Used to store all of my static files and images. |


---

## **Testing**

## ** Issues encountered**

### Navbar

Bootstrap was not allowing the items to be centered. What were looking to do:
- Have the search bar centered at the top of the navbar on larger screens
- Have the other navigation items displayed inline underneath the search function

Instead, all the items were displayed on the 2 lines (as wanted), but on the right hand side of the screen. 

### Footer
Footer did not allow to center the content.

---

## **Deployment**

The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institute student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

- Click the *Use This Template* button.
- Give your repository a name, and description if you wish.
- Click the *Create Repository from Template* to create your repository. 
- Click the *Gitpod* button to create a gitpod workspace, this can take a few minutes.
- When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
Use the following commands to commit your work, 
- `git add . ` - adds all modified files to a staging area.
- `git commit -m "A short message exlaining your commit"` - commits all changes to a local repository.
- `git push` - pushes all your commited changes to your Github repository.

**Requirements**

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

## Credits

[Willem Van Onsem](https://stackoverflow.com/users/67579/willem-van-onsem) for his answer in Stackoverflow for [How to make an average from values of a foreign key in Django?](https://stackoverflow.com/questions/59479908/how-to-make-an-average-from-values-of-a-foreign-key-in-django)

---

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

## **Credits**

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!

# Testing

[Return to README.md](README.md)

- [Manual Testing](#manual-testing)
  - [Bugs and Fixes During the Development Process](#bugs-and-fixes-during-the-development-process)
- [Wave Aim Accessibility checker:](#wave-aim-accessibility-checker)
- [Lighthouse](#lighthouse)
  - [Mobile](#mobile)
  - [Desktop](#desktop)
- [Validators](#validators)
  - [HTML](#html)
  - [CSS](#css)
  - [Javascript](#javascript)
  - [Python](#python)
- [User Stories](#user-stories)
  - [As an **Admin** I can...](#as-an-admin-i-can)
  - [As an **Unregistered User** I can...](#as-an-unregistered-user-i-can)
  - [As a **Registered User** I can...](#as-a-registered-user-i-can)

## Bugs and Fixes During the Development Process

- Issue - Bookings app would not load at all.
- Cause - Django could not find the 'cloundinary bookings' app
- Solution - [Fix Commit](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/5335cba884d78564406acd379ba420e64b5548be) Seperate the apps with a comma.
  css
- Issue - The deployed site on Heroku would not build properly as it couldn't install all dependencies
- Cause - backports.zoneinfo had been set in the requirements.txt file which Heroku couldn't build wheels for, and was therefore not completeling the build.
- Solution - [Fix](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/c0f9003a72c683865e5b214b964072c33f5f6f1a) Remove backports.zoneinfo library from requirements.txt as it wasn't necessary. Details on what this library does can be found [HERE](https://pypi.org/project/backports.zoneinfo/)

- Issue - Development server would not load the local host
- Cause - 'localhost' was set as an allowed host rather than 127.0.0.1.
- Solution - [Fix Commit](c8b15cfddd30dbd47d483891d8db87a3cd76181b) Change the allowed host so that the dev environment can load properly.

- Issue - All Questions in FAQs were showing/hiding whenever a single question was clicked on
- Cause - Becuase questions were being populated by a for loop, the same classes were being added to every question, making them behave in the same way.
- Solution - [Fix Commit](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/f28a6bbd7b59645e7c67e237bfdce814e07dcdc8) Added dynamic IDs to the cards and data target attributes to control the collapse class per question.

- Issue - FAQs page title was not displaying, which meant that the container class in base.html was also not loading the black background.
- Cause - QuestionList class was loading the listview before the pagetitle mixin
- Solution - [Fix Commit](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/c42ab8f86b1a6accca7b95ec0aaf020e4f0526ab) Swap them around.

- Issue - bookings url was displaying as bookings/bookings
- Cause - url path in bookings.url had 'bookings/' as the path, while tomsdrumlessons urls.py did too.
- Solution - [Fix Commit](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/ed05bcc947961ab23a3124561fb295c12e2a602d?diff=split)

- Issue - Navbar not changing active link colour
- Cause - Styling the active state of an anchor tag, rather than the active class in css
- Solution - [Fix Commit](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/ed05bcc947961ab23a3124561fb295c12e2a602d) Styling .active rather than .nav-link:active

- Issue - Navbar burger icon not displaying on small screens
- Cause - Styling issue. I hadn't specified a colour for the icon. It functioned as expected, but wasn't visible to the user.
- Solution - [Fix Commit](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/1f2b2e650aa3878ebb8465e8699ca4fc43883813) Added the navbar-dark class to the nav element.

- Issue - Reviews displaying with html tags around them
- Cause - Content was being loaded as html rather than plain text.
- Solution - [Fix Commit](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/0fae7ed6a55966a7c1c65574dfff8b4261ba6c0a) Added the 'safe' filer to the review body.

- Issue - Heroku build failure
- Cause - Heroku could not find django-summernote==0.8.20.0π
- Solution - [Fix Commit](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/92f8cba4712ac7fd0e260b6a4497870dce527830) Typo in requirements.txt on the end of the line. Proof that the smallest thing can have a big effect!

- Issue - Any authenticated user can update or delete any review.
- Cause - There were no checks in place to see whether the logged in user had access to individual entities. This allowed anyone with the specific update or delete url to manipulate the whole database.
- Solution - [Fix Commit](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/6dbb1a38e486d175ab6bc8fd66024382ccb5ce0c) Added an if statement to check whether the current user was the same as the user for a given review object. I made the same change for the update view as well in the next commit.

- Issue -
- Cause -
- Solution -

## Wave Aim Accessibility Checker

## Lighthouse

### Mobile

### Desktop

## Validators

### HTML

No errors were found

### CSS

There were numerous errors caused by Bootstraps classes, but when pasting in my custom css, no errors or warnings were found were found.

### JavaScript

There is only 1 function in the script.js file, for closing messages after 3 seconds. I removed the alert variable as it wasn't necessary, and came up with a warning as the variable'bootstrap' wasn't defined. I retested the messages with this line removed and it still worked as expected.

### Python

![Pep8online Testing](readmecontent/images/testing-python.png)

[Pep8online.com](http://pep8online.com) was used to test all python files. All efforts were made to make all code pep8 compliant, with the exception of the settings.py file, which Django state in their docs is okay to ignore should it make the code ugglier or harder to read, which in these cases it does.

## User Stories

### As a **New Student** I can...

| Checked | ...**find a teacher online** so that **I can learn more about that person.**                                                                        |
| :-----: | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | With an SEO score of 100, I have made it as likely as possible to be found on search engine, and the home page is clear about what the site offers. |

| Checked | ...**see who I am taking lessons with** so that **I can feel comfortable meeting a new teacher.** |
| :-----: | :------------------------------------------------------------------------------------------------ |
| &check; | Video of myself playing drums on the home page, and a detailed 'about me' section                 |

| Checked | ... **see whether the teacher teaches children** so that **I know I am safe to leave my child during the lessons.** |
| :-----: | :------------------------------------------------------------------------------------------------------------------ |
| &check; | In the FAQs section this question has been covered direclty.                                                        |

| Checked | ...**find out if I am too old to start taking lessons** so that **I can avoid wasting my time** |
| :-----: | :---------------------------------------------------------------------------------------------- |
| &check; | Also covered in FAQs                                                                            |

| Checked | ...**Approve new job posts offered by the community for the community** so that **I can ensure that posts are not malicious, false, misleading, or incomplete.** |
| :-----: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | Can approve a job individually from within the job post                                                                                                          |
| &check; | Can approve jobs on mass from the main jobs list page                                                                                                            |
| &check; | Change in the approved field is reflected in the database table for the specific job                                                                             |

| Checked | ...**Delete a Job post** so that **I can remove jobs that are no longer relevant or available.** |
| :-----: | :----------------------------------------------------------------------------------------------- |
| &check; | Can delete from the front end                                                                    |
| &check; | Delete button only visible on the front end for admin staff                                      |
| &check; | Warning to check if the user has the post pinned before deletion from the front end              |
| &check; | Can hide from the admin panel so post still visible on users pinboard                            |
| &check; | hidden post still visible on users pinboard when set to hidden                                   |
| &check; | Deletion is reflected in the database                                                            |

| Checked | ...**Edit a job post without using the admin panel** to that **if I spot a mistake or update a job post, I can do so quickly and easily without issue.** |
| :-----: | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | Can edit from the front end                                                                                                                              |
| &check; | Edit button only visible on the front end for admin staff                                                                                                |
| &check; | Can cancel the edit                                                                                                                                      |
| &check; | Can save the edit                                                                                                                                        |
| &check; | Edit is reflected in the database                                                                                                                        |

## As an **Unregistered User** I can...

| Checked | ...**quickly determine the subject of the site** so that **from the landing page, I can see if I want to continue spending my time on this site and register** |
| :-----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | Can see the theme of the site from the landing page                                                                                                            |
| &check; | Can access the instructions to understand better what I can do if I register                                                                                   |

| Checked | ...**register for an account** so that **I can enjoy a personalized experience as a job seeker** |
| :-----: | :----------------------------------------------------------------------------------------------- |
| &check; | Can sign up for a new account with email                                                         |
| &check; | Can sign up for a new account without email                                                      |
| &check; | Logged in and get redirected to the landing page upon successful signup                          |
| &check; | Able to start using the site features immediately                                                |
| &check; | New user entry visible from the database after registration                                      |
| &check; | Unable to register with a duplicate email or username                                            |

| Checked | ...**browse the available jobs (brief description only)** so that **I can see if I wish to register with the site or not** |
| :-----: | :------------------------------------------------------------------------------------------------------------------------- |
| &check; | Can see the preview cards for available jobs                                                                               |
| &check; | Can see I need to sign up/log in to see more info                                                                          |

## As a **Registered User** I can...

| Checked | ...**Pin jobs to a board** so that **I can refer back to them later with minimal effort**         |
| :-----: | :------------------------------------------------------------------------------------------------ |
| &check; | Can pin a job post from the job opening page                                                      |
| &check; | Once pinned, they are visible on the saved jobs page                                              |
| &check; | Pinned jobs are visible only to the user who pinned them                                          |
| &check; | Once pinned, they are visible on the saved jobs page                                              |
| &check; | Can unpin a job post from the job saved jobs page, and it disappears from this view               |
| &check; | The unpinning of the job is reflected when returning to the job openings page                     |
| &check; | The unpinning of the job is reflected when returning to the full job spec of that job             |
| &check; | Only user-specific Notes are deleted when unpinned                                                |
| &check; | When unpinned a job, the insights remain                                                          |
| &check; | When unpinning a job, a warning appears warning the user notes will be lost                       |
| &check; | When clicking cancel on the above warning, the toggle switch goes back to the pinned position     |
| &check; | When clicking cancel on the above warning, the toggle switch goes back to the pinned position     |
| &check; | When is pinned value is changed, the database value is updated                                    |
| &check; | When logged out, the user sees a custom error page                                                |
| &check; | If deleting all items on page 2 or higher the user is redirected to the previous page             |
| &check; | If deleting all entries, the view is not paginated; the user sees a space where pinned posts were |

| Checked | ...**browse the full details of the available jobs** so that **I can see the full job spec and how to apply** |
| :-----: | :------------------------------------------------------------------------------------------------------------ |
| &check; | Access full job spec from the job openings page                                                               |
| &check; | Access full job spec from the saved jobs page                                                                 |
| &check; | Can see an apply now button which takes me back to an external site where I can apply                         |
| &check; | Can see a button which takes me back to all job openings                                                      |
| &check; | If a user is not logged in, they see a custom error page                                                      |

| Checked | ...**leave notes specific to the job on my pinboard** so that **I can keep track of specific milestones in the application process** |
| :-----: | :----------------------------------------------------------------------------------------------------------------------------------- |
| &check; | When job pinned Notes form and accordion are visible                                                                                 |
| &check; | No notes section from full spec page when job unpinned                                                                               |
| &check; | The notes section display can be toggled with the toggle switch                                                                      |
| &check; | When on smaller screen sizes, there is a button to direct the user to the notes section below the full spec                          |
| &check; | Can successfully leave a note from the full job spec                                                                                 |
| &check; | Can mark Note as insight and background color of related accordion-item changes to yellow with an icon in the heading                |
| &check; | Can see each note/item heading in the accordion                                                                                      |
| &check; | When expanding one section of the accordion, any previous one closes                                                                 |
| &check; | Notes/insights can only be seen by the user who left them                                                                            |
| &check; | Notes/insights left are reflected in the database                                                                                    |
| &check; | If a user is not logged in and tries to use the URL to access the edit note form, they see a custom error page                       |

| Checked | ...**turn a note into an insight** so that **it can be seen on a separate page showing learnings from the entire process of the job-hunting process** |
| :-----: | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | Edit button visible on the accordion item                                                                                                             |
| &check; | Take the user to a form where they can update the is insight field                                                                                    |
| &check; | Ticking is insight checkbox and clicking save updates the record. The updated record reflects in the database and the accordion                       |
| &check; | Clicking save without editing any details will return the user to the originating job spec                                                            |
| &check; | When a user changes note to insight, the entry displays on their insights page                                                                        |
| &check; | Edit is reflected in the database                                                                                                                     |
| &check; | If a user is not logged in, they see a custom error page from the forms URL                                                                           |

| Checked | ...**delete previous notes and insights** so that **I can delete notes or insights that are no longer relevant to me.** |
| :-----: | :---------------------------------------------------------------------------------------------------------------------- |
| &check; | Delete button visible from the notes accordion and the insight page entry                                               |
| &check; | Warning is displayed when clicking delete                                                                               |
| &check; | Warning is closed when clicking cancel                                                                                  |
| &check; | Entry disappears from notes accordion/ insights page upon deletion confirmation                                         |
| &check; | Deletion is reflected in the database                                                                                   |

| Checked | ...**see a timeline of insights** so that **I can track them over time**                     |
| :-----: | :------------------------------------------------------------------------------------------- |
| &check; | Timeline display staggered on larger screens                                                 |
| &check; | Timeline display stacked on smaller screens                                                  |
| &check; | Paginated by 3                                                                               |
| &check; | When deleting all items on page 2 (or above), the page redirects to the previous page        |
| &check; | When deleting all entries and if not paginated, the user sees a space where the timeline was |
| &check; | If a user is not logged in, they see a custom error page                                     |

| Checked | ...**Add my job posts** so that **I may make notes and insights to track my progress.** |
| :-----: | :-------------------------------------------------------------------------------------- |
| &check; | Can see add job button on job opening page when logged in                               |
| &check; | Can add job from the drop-down in the nav bar when logged in                            |
| &check; | If a user is not logged in, they see a custom error page from the forms URL             |
| &check; | Placeholders visible in URL fields                                                      |
| &check; | Alert shown on successful form submission                                               |
| &check; | Job post is reflected in the database upon submission                                   |
| &check; | Approved shows false in the database upon submission                                    |
| &check; | Does not show on job openings page until approved by the admin                          |
| &check; | If canceling the add job form, the user returns to the landing page.                    |

| Checked | ...**Edit previously made notes and insights** so that **I may correct mistakes or further elaborate on an existing comment/insights.** |
| :-----: | :-------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | Edit button visible on the accordion item                                                                                               |
| &check; | Edit buttons take the user to a form to edit the insight/note entry                                                                     |
| &check; | Edit button visible on the insight page entry                                                                                           |
| &check; | Ticking is an insight checkbox, and clicking save, the record updates, which is visible from the database and the accordion             |
| &check; | Clicking save without editing any details will return the user to the originating job spec                                              |
| &check; | Any notes marked as insight display on the user personal insights page                                                                  |
| &check; | Edited fields reflected in the database                                                                                                 |
| &check; | If a user is not logged in, they see a custom error page from the form's URL                                                            |

| Checked | ...**See balanced forms with an included text editor for the main field** so that **I can have a pleasant visual experience across the site, and my job post and notes/insight look visually appealing in the style and layout when the submitted data is displayed.** |
| :-----: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | Note Form formatted and styled with widget tweaks and summer note editor replaces for text area entry                                                                                                                                                                  |
| &check; | Add Job Form formatted and styled with widget tweaks, and summer note editor replaces for text area entry                                                                                                                                                              |
| &check; | Insights Form formatted and styled with widget tweaks, and summer note editor replaces for text area entry                                                                                                                                                             |
| &check; | Edit Note Form formatted and styled with widget tweaks and summer note editor replaces for text area entry                                                                                                                                                             |

| Checked | ...**Delete or edit insights from the insights page** so that **I can update or delete insights without job posts no longer visible.** |
| :-----: | :------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | Delete button visible from the insight entry                                                                                           |
| &check; | Edit button visible from the insight entry                                                                                             |
| &check; | Warning is displayed when clicking delete                                                                                              |
| &check; | Warning is closed when clicking cancel                                                                                                 |
| &check; | Entry disappears from insights page upon deletion                                                                                      |
| &check; | Deletion is reflected in the database                                                                                                  |
| &check; | Edit is reflected in the database                                                                                                      |
| &check; | If all items on page 2 or above are deleted page redirects to the previous page                                                        |
| &check; | If all entries are deleted and the page is not paginated, the user sees a space where the timeline was                                 |

| Checked | ...**Create insights directly from the insights page** so that **I can document my general learning along my career path that may not be specific to a job role advertised on the site.** |
| :-----: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | Can see add insight button on insights page when logged in                                                                                                                                |
| &check; | If a user is not logged in, they see a custom error page from the forms URL                                                                                                               |
| &check; | Alert shown on successful form submission                                                                                                                                                 |
| &check; | Insight related_job field is reflected in the database as null upon submission                                                                                                            |
| &check; | If canceling the add insight form, the user returns to the insights page.                                                                                                                 |

| Checked | ...**See appealing colors and uniform style themes** |
| :-----: | :--------------------------------------------------- |
| &check; | Colors pass contrast test                            |
| &check; | Colors and styles are consistent across the site     |

| Checked | ...**Access the site from any size screen and still have a pleasant experience on the site** so that **I am not restricted to which devices I can use on the site** |
| :-----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| &check; | Landing page is responsive from 320px up                                                                                                                            |
| &check; | Add Job form is responsive from 320px up                                                                                                                            |
| &check; | Tracking instructions is responsive from 320px up                                                                                                                   |
| &check; | Saved jobs page is responsive from 320px up                                                                                                                         |
| &check; | Insight page is responsive from 320px up                                                                                                                            |
| &check; | Contact page is responsive from 320px up                                                                                                                            |
| &check; | Navbar is responsive from 320px up                                                                                                                                  |
| &check; | Footer page is responsive from 320px up                                                                                                                             |
| &check; | Edit form is responsive from 320px up                                                                                                                               |
| &check; | Add insight form is responsive from 320px up                                                                                                                        |
| &check; | Sign in page is responsive from 320px up                                                                                                                            |
| &check; | Sign in page is responsive from 320px up                                                                                                                            |
| &check; | Sign out page is responsive from 320px up                                                                                                                           |
| &check; | Sign up page is responsive from 320px up                                                                                                                            |
| &check; | Not signed in message page is responsive from 320px up                                                                                                              |
| &check; | 404 page is responsive from 320px up                                                                                                                                |
| &check; | 500 page is responsive from 320px up                                                                                                                                |
| &check; | full job spec page is responsive from 320px up                                                                                                                      |
| &check; | pagination bar is responsive from 320px up                                                                                                                          |

| Checked | ...**type a URL into the web browser** so that **I can access the site's various pages**                  |
| :-----: | :-------------------------------------------------------------------------------------------------------- |
| &check; | All pages can be accessed by their URL when logged in                                                     |
| &check; | When logged out, only the landing page, contact page, and all auth pages are visible                      |
| &check; | Appropriate message displayed if a user is logged out and tries to access a URL which is for members only |

| Checked | ...**see uniformity on each page and clearly distinguish the content subject** so that **I can quickly and familiarly navigate the page.** |
| :-----: | :----------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | Navbar on all pages the same                                                                                                               |
| &check; | Footer on all pages the same                                                                                                               |
| &check; | Styling of all pages follow a theme                                                                                                        |

| Checked | ... **Find relevant contact details** so that **I can contact the site admin via email** |
| :-----: | :--------------------------------------------------------------------------------------- |
| &check; | Contact page accessible from navbar                                                      |
| &check; | email address provided on the contact page                                               |

## As a **Site User** I can...

| Checked | ...**see appropriate responses upon specific interactions with the site** so that **I know my edit, deletion, submission has been successful.** |
| :-----: | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | When unpinning a post the is an HTTP response of 200 in the console                                                                             |
| &check; | When unpinning a post, it disappears from the pinboard                                                                                          |
| &check; | Prior to unpinning a post, a warning model is advising that associated notes will be deleted                                                    |
| &check; | Only the relevant user's notes are deleted when unpinning a job                                                                                 |
| &check; | Pin status is correctly updated and reflected in the database                                                                                   |
| &check; | Notes appear in the accordion when left                                                                                                         |
| &check; | Banner appears when making a note to advise it was left successfully                                                                            |
| &check; | Prior to deleting an element, a warning modal is displayed                                                                                      |
| &check; | Deletion logs HTTP response of 200 to the console                                                                                               |
| &check; | Elements being deleted are removed from the DOM                                                                                                 |
| &check; | Deletions of jobs and notes are correctly reflected in the database.                                                                            |
| &check; | When adding a job, the default status is hidden and not visible to the user                                                                     |
| &check; | Banner stating the job sent for approval                                                                                                        |
| &check; | New job shows in the database                                                                                                                   |
| &check; | Form errors show when jobs form is incorrectly filled in upon submission                                                                        |
| &check; | Banner stating the note/insight has successfully been updated from full details page                                                            |
| &check; | Note/insight update reflects in the database                                                                                                    |
| &check; | Form errors show when edit notes/insights form is incorrectly filled in upon submission                                                         |
| &check; | When editing a note from the full details page, the user is redirected back to the full details page                                            |
| &check; | Banner stating the insight has successfully been updated from insights page                                                                     |
| &check; | Insight update reflects in the database                                                                                                         |
| &check; | Form errors show when add insights form is incorrectly filled in upon submission                                                                |
| &check; | When editing an insight from the insights page, they user is redirected back to the insights page                                               |

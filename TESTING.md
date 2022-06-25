# Testing

[Return to README.md](README.md)

- [Manual Testing](#manual-testing)
  - [Bugs and Fixes During the Development Process](#bugs-and-fixes-during-the-development-process)
- [Wave Aim Accessibility checker:](#wave-aim-accessibility-checker)
- [Lighthouse](#lighthouse)
  - [Job Openings](#job-openings)
    - [Logged out:](#logged-out)
      - [_Desktop_:](#desktop)
      - [_Mobile_:](#mobile)
    - [Logged in:](#logged-in)
      - [_Desktop_:](#desktop-1)
      - [_Mobile_:](#mobile-1)
  - [Full Job Spec](#full-job-spec)
    - [With Notes Displayed:](#with-notes-displayed)
      - [_Desktop_:](#desktop-2)
      - [_Mobile_:](#mobile-2)
    - [No Notes Displayed:](#no-notes-displayed)
      - [_Desktop_:](#desktop-3)
      - [_Mobile_:](#mobile-3)
  - [Saved Jobs](#saved-jobs)
    - [_Desktop_:](#desktop-4)
    - [_Mobile_:](#mobile-4)
  - [Tracking Instructions Page](#tracking-instructions-page)
    - [_Desktop_:](#desktop-5)
    - [_Mobile_:](#mobile-5)
  - [Contact Page](#contact-page)
    - [_Desktop_:](#desktop-6)
    - [_Mobile_:](#mobile-6)
  - [Insights Page](#insights-page)
    - [_Desktop_:](#desktop-7)
    - [_Mobile_:](#mobile-7)
  - [Add Insights Page](#add-insights-page)
    - [_Desktop_:](#desktop-8)
    - [_Mobile_:](#mobile-8)
  - [Edit Notes Page](#edit-notes-page)
    - [_Desktop_:](#desktop-9)
    - [_Mobile_:](#mobile-9)
  - [Add Job Page](#add-job-page)
    - [_Desktop_:](#desktop-10)
    - [_Mobile_:](#mobile-10)
  - [Sign Out Page](#sign-out-page)
    - [_Desktop_:](#desktop-11)
    - [_Mobile_:](#mobile-11)
  - [Sign in Page](#sign-in-page)
    - [_Desktop_:](#desktop-12)
    - [_Mobile_:](#mobile-12)
  - [Sign up Page](#sign-up-page)
    - [_Desktop_:](#desktop-13)
    - [_Mobile_:](#mobile-13)
- [Validators](#validators)
  - [HTML:](#html)
  - [CSS:](#css)
  - [JS:](#js)
  - [PEP8:](#pep8)
- [Manual testing](#manual-testing)
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

## Lighthouse

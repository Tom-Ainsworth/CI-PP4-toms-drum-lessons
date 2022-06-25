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

- Issue - The deployed site on Heroku would not build properly as it couldn't install all dependencies
- Cause - backports.zoneinfo had been set in the requirements.txt file which Heroku couldn't build wheels for, and was therefore not completeling the build.
- Solution - [Fix](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/commit/c0f9003a72c683865e5b214b964072c33f5f6f1a) Remove backports.zoneinfo library from requirements.txt as it wasn't necessary. Details on what this library does can be found [HERE](https://pypi.org/project/backports.zoneinfo/)

- Issue - Development server would not load the local host
- Cause - 'localhost' was set as an allowed host rather than 127.0.0.1.
- Solution - [Fix Commit](c8b15cfddd30dbd47d483891d8db87a3cd76181b) Change the allowed host so that the dev environment can load properly.

# Toms Drum Lessons

## Code Institute Portfolio Project 4

Although I am in the process of changing careers, I currently teach 1-1 drum lessons in person. One of the primary reasons I became interested in web development was to build my own website to advertise my business, and host lessons online. This website is aimed at people of all ages who are interested in taking drum lessons with me at my studio, and want to find out a bit more about me and what I can offer, before booking a lesson.

![Multi Screen Image](#)

[Live Site](https://toms-drum-lessons.herokuapp.com/)

## Contents

- [Toms Drum Lessons](#toms-drum-lessons)
- [UX Design](#ux-design)
  - [Strategy Plane](#strategy-plane)
  - [Scope Plane](#scope-plane)
  - [Structure Plane](#structure-plane)
    - [User Stories](#user-stories)
  - [Skeleton Plane](#skeleton-plane)
    - [Site Flow](#site-flow)
    - [Database Schema](#database-schema)
    - [Wireframes](#wireframes)
  - [Surface Plane](#surface-plane)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
- [Agile Development Process](#agile-development-process)
- [Current Features](#current-features)
  - [Site Navigation](#site-navigation)
    - [Logged Out](#logged-out)
    - [Logged In](#logged-in)
    - [Mobile Navigation](#mobile-navigation)
  - [Home Page](#home-page)
  - [About Page](#about-page)
  - [Bookings Page](#bookings-page)
  - [Reviews Page Logged Out](#reviews-page-logged-out)
  - [Reviews Page Logged In](#reviews-page-logged-in)
  - [Create a Review](#create-a-review)
  - [Update a Review](#update-a-review)
  - [Delete a Review](#delete-a-review)
  - [FAQs Page](#faqs-page)
  - [Footer](#footer)

## UX Design

### Strategy Plane

- Site Goal

  - As mentioned above, the site goal is to attract potential customers to take drum lessons.

- Target Audience

  - As lessons are in person, the target audience is primarily people living nearby the studio, as they will need to be physically present during the lessons. As of 2021, there are around 329,000 people living in Wandsworth, London (The borough in which the studio is located). Giving a huge amount of potential customers. This is excluding other adjacent boroughs where current students are happy to travel from, so the actual scale of potential customers is far greater.

- Is there a need for this?

  - As one of the only drum teachers in the surrounding area, the demand for drum teachers far outways the demand. There are currently 4 other teachers in the area, 3 of which do not have a website or significant online presence.

- Is the content relevant?

  - Drumming has been proven to have several health benefits, such as improving problem solving skills, relieving stress and tension, boosting creativity, increasing focus and goal setting through practice, along with generally being a very fun and accessible instrument to learn.

- Customer Needs:

  - At the very least, the customer should know who I am, how to contact me, and where the lessons take place.
  - Further needs can be seen below, with the level of importance and feasability scored.

| Opportunity                                            | Importance | Viability/Feasibility |
| ------------------------------------------------------ | ---------- | --------------------- |
| Landing page with site overview                        | 5          | 5                     |
| About Section                                          | 5          | 5                     |
| Location Section                                       | 5          | 5                     |
| Enquiries Section                                      | 5          | 4                     |
| Lesson Info Section                                    | 5          | 5                     |
| Availability Form to book a lesson                     | 4          | 3                     |
| Google maps APIintegration to show studio location     | 3          | 2                     |
| Song Transcriptions Section with downloadable material | 3          | 1                     |
| Tips/resources                                         | 2          | 5                     |
| Current Student reviews                                | 4          | 4                     |
| New User submitted reviews                             | 3          | 3                     |
| User log in                                            | 5          | 5                     |
| Transcription requests                                 | 2          | 3                     |
| Blog style lessons                                     | 2          | 5                     |
| Video Lessons                                          | 2          | 2                     |
| User profile                                           | 5          | 3                     |
| ----------------------------------------               | ----       | ----                  |
| Totals: 16                                             | 60         | 60                    |

As the viability score matches the importance score, I should in theory be able to implement all of the above features. This may well change as I begin the work, due to distractions and unforseen difficulties. The scores above have been based on my own skill levels currently. I may have estimated incorrectly for some, therefore changing the time needed. Between sprints I will reassess each opportunity to see what is more feasable.

### Scope Plane

In order to manage the workload for each sprint, I have divided the above opportunities into three categories, depending on their overall importance to reaching a minimum viable product (MVP).

- Must Have

  - Landing Page
  - About Section
  - Enquiries Section
  - User Log In
  - Location Section
  - Lesson Info Section

- Should Have

  - Availability Form
  - Tips/Resources
  - Current Student Reviews
  - New User Reviews
  - Transcription Section

- Could Have
  - Google Maps API Integration
  - Transcription Requests
  - Blog style lessons
  - Video Lessons
  - User Profile

### Structure Plane

#### User Stories

- New Students

  - As someone interested in learning drums, I want to find a teacher online, so that I can learn more about that person.
  - As a new drummer, I want to see who I am taking lessons with, so that I can feel comfortable meeting a new teacher.
  - As a parent, I want to know whether the teacher teaches children, so that I know I am safe to leave my child during the lessons.
  - As an adult, I want to know if I am too old to start taking lessons, so that I can avoid wasting my time
  - As someone with a tight schedule, I want to book exact time slots, so that I can plan the lessons around my life.
  - I want to contact Tom before booking, to ask him questions about the lessons, so that I can make an informed decision about whether to take lessons.
  - As a visual learner, I want to see and hear what is being played, so that I can play along and watch what is happening.
  - As a visual learner, I want to see music written down, so that I can read and learn it at my own pace.
  - As a kinesthetic learner, I want to get stuck in and play along at the same time as Tom, rather than starting and stopping.
  - As a new user, I want to see reviews from real people, so that I can find out if Tom is a good teacher for me.

- Current Students
  - As a current student, I want to have a profile, so that I can don't have to enter my details everytime I use the site.
  - As a drum student, I want to request new songs to have the sheet music for
  - As a satisfied customer, I want to submit a review on Tom's site to share my experience.
  - As a reading drummer, I want to download transcriptions of new songs to learn between lessons.

These were the initial user stories I had, however once I began entering them on github as issues, I realised that they were much more tailored the actual business I do, rather than what the website can offer users. As such please see the [project board](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/projects/1) to see actual user stories and tasks carried out that can be directly related to the site features.

### Skeleton Plane

#### Site Flow

Below is a flow chart using [Lucid Charts](https://www.lucidchart.com/) of how I envisage the flow of the site to look. For an unregistered user, they will have read only access to the site, with prompts to create an account to see extra features.

<img src="readme-content/images/tdl-site-flow-chart.png" alt="toms drum lessons site flow chart"  width="70%"/>

#### Database Schema

Here is the initial idea for how the backend will look should all of the features be implemented. I used [Lucid Charts](https://www.lucidchart.com/) once again to create the mockup.

<img src="readme-content/images/data-schema.png" alt="data schema for tom's drum lessons" width="70%"/>

The Transcriptions and Lessons entities will only be writtable from an admin, so that I can maintain the quality of the material. Reviews will require a login to post, and will be subject to admin approval. They will be connected to the user so that each user can be identified in their review.

#### Wireframes

- [Homepage](readme-content/wireframes/homepage.png)
- [About Page](readme-content/wireframes/about-page.png)
- [Lessons Page](readme-content/wireframes/lessons-page.png)
- [Bookings Page](readme-content/wireframes/bookings-page.png)
- [Find Us Page](readme-content/wireframes/find-us-page.png)
- [Transcriptions Page](readme-content/wireframes/transcriptions-page.png)
- [Reviews Page](readme-content/wireframes/reviews-page.png)
- [FAQ Page](readme-content/wireframes/faq-page.png)
- [Login/Sign Up Page](readme-content/wireframes/login-signup-page.png)

After doing the mockups for each page I realised there is a lot to do in a short space, so I will be really narrowing things down to begin with. The homepage is vital, as are the login/sign up, about, bookings and find us pages. I will start with these first to ensure the core functionality of the site is working, and then go through the others as time permits.

### Surface Plane

#### Colour Scheme

The site features a minimalistic colour scheme, allowing text ot contrast well against both the background, and images.

<img src="readme-content/images/colour-palette.png" alt="colour palette" width="50%" />

#### Typography

The main font of the entire site is Nanum Gothic from [Google Fonts](https://fonts.google.com/specimen/Nanum+Gothic?query=gothic). I used sans-serif as a backup as they use the same typeface.

## Agile Development Process

I used Github's issues and projects to keep track of the progress throughout the project. The main project board can be found [here](https://github.com/Tom-Ainsworth/CI-PP4-toms-drum-lessons/projects/5)
Notes on individual sprints, including tasks completed and problems encountered can be found in a the [AGILE.md](AGILE.md) file.

## **Current Features**

### **Navbar**

#### Logged Out

![Navbar Logged Out](readme-content/images/navbar-logged-out.png)

When the user is logged out, both the Login and Sign Up buttons appear, linked to the relevant pages

#### Logged In

![Navbar Logged In](readme-content/images/navbar-logged-in.png)

When the user is logged in, a Logout button appears, allowing them to log out

#### Mobile Navigation

![Navbar Mobile](readme-content/images/navbar-mobile.png)

The authentication functionality is the same as above, however on smaller screens a burger menu appears, which drops down to reveal the navbar links.

### **Home Page**

![Home Page](readme-content/images/homepage.png)

The home/landing page of the site features a Title with subheading outlining exactly what the site is. There is also an embedded video of myself playing drums, so users can see my abilities. The background image is the studio where the lessons take place, which can also be seen throughout the site, and in the video.

### **About Page**

![About Page](readme-content/images/aboutpage.png)

The about sections features some more images of myself, from both my drum kit and where the students sit to give users an idea of what to expect. The text here is about my journey on the drums and what I currently do. On smaller screens the page shrinks to a single column to maintain the text and image size.

### **Bookings Page**

![Bookings Page](readme-content/images/bookingpage.png)

The bookings page is very simple so not to distract from it's purpose. There is some text explaining how to book a lesson, followed by a button connected to my Calendly calendar for users to book a lesson. Should users want to know more, I added a link to the FAQs section (see below).

### **Reviews Page Logged Out**

![Reviews Page Logged Out](readme-content/images/reviewspageout.png)

When logged out, users can view all reviews on the page, but are unable to do any further actions. The reviews are paginated to display 3 reviews per page, with forward and backward buttons when necessary. On smaller screens, reviews are displayed in a single column to maintain the text size.

### **Reviews Page Logged In**

![Reviews Page Logged In](readme-content/images/reviewspagein.png)

When authenticated, users are able to create a new review via the 'write a review' button. Should the already have a review, they can update and delete that review via the buttons that appear on the corresponding cards.

### **Reviews Page No Access**

![Reviews Page No Access](readme-content/images/review-no-access.png)

If a logged in user manually enters a url to create, update or delete another user's review, they are met with an error message asking them to log in to the correct account.

### Create a review

![Create a Review](readme-content/images/review-create.png)

A blank form page shows for users to create a new review. Both fields are required and will notify the user should either be blank. All reviews are pending admin approval.

### Update a review

![Update a Review](readme-content/images/review-update.png)

The update view will prefill the necessary fields with existing data, and the user can edit either or both fields as they wish.

### Delete a review

![Delete a Review](readme-content/images/review-delete.png)

This view loads an extra page for users to confirm that they want to delete their review, and an option to go back to the reviews page should they change their mind.

### FAQs Page

![FAQs](readme-content/images/faqpage.png)

The Frequently asked questions section features an accordion layout. This is read only for all users, and each question is dynamically added to the page from the Questions model, so that I can add or remove questions without touching the code.

### Footer

![Footer](readme-content/images/footer.png)

The footer features a more subtle grey text colour than the rest of the site to differentiate it. I split it into 3 columns: Opening hours, contact links, Studio Address.

## **Future Development**

- User profiles section to add personal info, see reviews, book lessons
- Online community to discuss lessons and share progress
- SaaS business model with different access tiers for different content through monthly recurring subscriptions
- Internal booking system rather than Calendly link
- Payment system so users can fully book a lesson
- Review replies so users can see that I've responded to them

## Testing

A full breakdown of testing can be seen in the [TESTING.md](TESTING.md) document.

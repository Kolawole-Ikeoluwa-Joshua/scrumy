# Django Project

### Note to self: should have added comments throughout this code base

## First App
=====

kolawoleikeoluwa2018scrumy

=====

This is a project management application built with the SCRUM framework in mind.

It serves as a a digital tool used by the Scrum team to manage their projects.

Quick Start
-----------

1. Add "kolawoleikeoluwa2018scrumy" to your INSTALLED_APPS settings like this ::

INSTALLED_APPS = [
    ...
    'kolawoleikeoluwa2018scrumy',
]

2. Include the app URLconf in your project urls.py like this::

    path('kolawoleikeoluwa2018scrumy/', include('kolawoleikeoluwa2018scrumy.urls')),

3. Run 'python manage.py migrate' to create the app models.

4. Start the development server 

## Second App
=====

websocket chat application with AWS API gateway

=====


WebSockets enable seamless two-way communication between a client and server. 

In other words they allow websites to send and receive data in real time. 

This WebSockets chat applications expose events in real-time, allowing users to talk to each other.

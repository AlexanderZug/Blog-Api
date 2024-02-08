# Blog API Project

This is a Django-based RESTful API project for managing blogs, posts, subscriptions, and user notifications.

## Features

- User management: Users can register, login, update their profiles, and manage their subscriptions.
- Blog creation: Each user has a personal blog upon registration.
- Post management: Users can create posts within their blogs.
- Subscription system: Users can subscribe to other users' blogs to receive updates.
- Personalized news feed: Users have a personalized news feed showing posts from blogs they are subscribed to.
- Read status tracking: Users can mark posts in their feed as read.
- Daily email notifications: Users receive a daily email containing the latest posts from their subscriptions.

## Installation

1. Clone the repository:
```
    git clone https://github.com/AlexanderZug/Blog-Api.git
```

2. Navigate to the Project Directory:
```
    cd Blog-Api
```
3. Run Docker Compose to start the API, Redis, and Postgres:

```
    sudo docker-compose up --build
```
This will create and start the necessary containers.
It will also create a superuser with the credentials admin/admin and fixtures for testing.
4. Navigate to the API documentation at http://localhost:8000/api/swagger/

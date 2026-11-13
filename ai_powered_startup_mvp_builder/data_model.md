# Data Model - SmartAdvisor

## Overview

The SmartAdvisor data model describes how application information is organized and stored.

## Entities

### 1. User

Stores basic information about application users.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique user identifier |
| name | String | User's name |
| email | String | User's email address |
| created_at | DateTime | Account creation date |

### 2. Request

Stores requests submitted by users.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique request identifier |
| user_id | Integer | ID of the user who submitted the request |
| title | String | Request title |
| description | Text | Request details |
| status | String | Current request status |
| created_at | DateTime | Request creation date |

### 3. Task

Stores tasks created by users.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique task identifier |
| user_id | Integer | ID of the task owner |
| title | String | Task title |
| description | Text | Task details |
| status | String | Pending or completed |
| due_date | DateTime | Task deadline |

### 4. ChatMessage

Stores messages exchanged in the AI chat.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique message identifier |
| user_id | Integer | ID of the user |
| role | String | User or assistant |
| content | Text | Message content |
| created_at | DateTime | Message timestamp |

## Relationships

- One User can create many Requests.
- One User can create many Tasks.
- One User can have many ChatMessages.
- Each Request belongs to one User.
- Each Task belongs to one User.
- Each ChatMessage belongs to one User.

## Notes

- The id field is the primary key in each entity.
- user_id is a foreign key in Request, Task, and ChatMessage.
- Authentication is outside the initial MVP scope, but the User entity is included for future development.

# Content Service

The Content Service is responsible for managing user contents. It is part of the FastAPI app.

## Tech Stack

- **FastAPI** – Web framework
- **PostgreSQL** – Relational database
- **Docker** – Containerization
- **GitHub Actions** – Continuous Integration and Continuous Delivery

## API Endpoints

- `POST /content/posts` – Retrieves the post associated with the authenticated user.
> The endpoint above require a valid JWT token generated by the `auth_service`.
- `GET /content/posts/{post_id}` – Retrieves the post associated with the authenticated user.
- `GET /content/users/{user_id}/posts` – Retrieves the posts created by a specific user.

## Getting Started

> This service depends on the `auth_service`. It's recommended to run the full system using [`fast-deployment`](https://github.com/labtst-online/fast-deployment).

### 1. Clone repository

```bash
git clone https://github.com/labtst-online/fast-content_service.git
cd fast-content_service
```

### 2. Configure

```bash
cp .env.sample .env
```
> Change variables before `docker-compose up`

### 3. Run with Docker

```bash
docker-compose up --build
```

## GitHub Actions (CI, CD)

* Continuous Integration workflow runs tests and ruff formater check on every push and pull request to the main and develop branches.
* Continuous Delivery workflow build and push image to GHCR.

## License

This repository is licensed under the terms of the MIT license.

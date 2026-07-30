# Voting Application

## Project Title and Description

The Voting Application is a simple web application that allows users to vote for their favorite candidates. Every time a user visits the voting URL for a candidate, that candidate receives one vote. The application also displays the current vote count for all candidates. All votes are stored in memory while the application is running.

---

## Installation and Setup Steps

### Prerequisites

- Python 3.x
- Flask

### Steps

1. Clone the repository

```bash
git clone https://github.com/bishwa1991/Assignment_HeroVired.git
```

2. Navigate to the project folder

```bash
cd Assignment_HeroVired
```

3. Install Flask

```bash
pip install flask
```

4. Run the application

```bash
python app.py
```

5. Open your browser and visit

```
http://127.0.0.1:5000
```

---

## API Endpoint Reference

| Endpoint | Method | Description | Example Response |
|----------|--------|-------------|------------------|
| `/vote/<name>` | GET | Records one vote for the specified candidate. Creates the candidate if they do not already exist. | `{"message":"Vote recorded for Alice","total_votes":2}` |
| `/results` | GET | Returns the current vote count for all candidates. | `{"Alice":2,"Bob":1}` |

---

## Git Workflow

I followed a simple Git branching strategy using **main** and **dev** branches.

- The **main** branch contains the stable version of the application.
- The **dev** branch was used to develop and test new features.
- After testing the changes in the **dev** branch, they were merged into the **main** branch.
- Version tags were created after completing major milestones.

### Workflow

```
main
  │
  ├─────────────── Version 1
  │
  └───────────────┐
                  │
                 dev
                  │
      Added new features
                  │
                  ▼
          Merge into main
                  │
                  ▼
             Version 2
```

---

## Version History

| Version | Description |
|---------|-------------|
| Version 1 | Created the Flask application with the `/vote/<name>` endpoint to record votes. |
| Version 2 | Added the `/results` endpoint, improved the application, merged changes from `dev` into `main`, and updated the documentation. |

---

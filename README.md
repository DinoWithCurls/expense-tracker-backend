# Expense Tracker Backend

This is the backend code for the **Expense Tracker** app that I create with **React** and **Bootstrap** in the frontend.


## Tech Stack
The following tech has been used to create this part:

 1. Django - For API
 2. PostgreSQL - For DBMS
 3. Docker - For containerizing the application

## Database Schema

### User
| Column | Data Type | Options
|--|--|--|
| ID | UUID | Primary Key |
| Name | Text | |
| Email | Text | With Email Validitors |

### Transaction
| Column | Data Type | Options |
|--|--|--|
| ID | Integer | Primary Key |
| User_ID | UUID | Foreign Key to User |
| Type | Text | income, expense |
| Date | Date | |
| Reason | Text | Uber, Grocery Stores Food, Water Can, Other |
| Other_Reason | Text | |
| Amount | Integer | |

## How to Run the Code

1. Install Docker in your local system.
2. Clone the Project.
3. Execute the following commands:
`chmod +x initialise.sh`
`chmod +x migrate.sh`
4. Execute the following commands:
`./initialise.sh`
`./migrate.sh`

The code is set up.
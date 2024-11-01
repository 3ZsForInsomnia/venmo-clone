# Simple Venmo

## Backend

Accounts
- Associated with a user
- Create an account

Users API
- Get user, users, search users, create users (automatically populates one account)
- Can have multiple accounts, one account is "main"

Transactions API
- Get transaction, transactions
- Create transaction between accounts, _not_  between users
- Transaction is created and set to pending if to another user
  - Goes to their "main" account
  - If going to another account of yours, instantly approved

General
- Get transaction history for user

## Frontend

Show current user and their accounts
Search users
Create transaction
View your transaction history

## Not doing yet

Deleting/updating/searching/creating accounts
- Api is there to create accounts, but no UI for it

Deleting/updating users
No real auth
Canceling, filtering transactions
Viewing other people's transaction history
Approvals? Maybe just auto-approve for simplicity for now

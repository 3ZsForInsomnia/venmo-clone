export interface User {
  username: string;
  id: number;
}

export interface NewUserRequest {
  username: string;
  password: string;
  starting_balance: number;
  first_account_name: string;
}

export interface Account {
  balance: number;
  is_primary: boolean;
  name: string;
  id: number;
}

export interface Transaction {
  id: number;
  amount: number;
  sender: string;
  receiver: string;
  created_by: number;
  created_on: string;
  approved: boolean;
  approved_on?: string;
}

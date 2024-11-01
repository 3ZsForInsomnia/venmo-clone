import { Account, NewUserRequest, User } from "./types";
import { createUrl } from "./utils";

const headers = {
  "Content-Type": "application/json",
};

interface LoginResponse {
  user: User;
  accounts: Account[];
}

export interface HttpError {
  detail: string;
}

const handleResponse = async <TData>(response: Response) => {
  if (!response.ok) {
    const data = await response.json();
    throw new Error(data.detail);
  }
  return response.json() as Promise<TData>;
};

export const UsersService = {
  login: async (username: string, password: string) =>
    fetch(createUrl("login"), {
      method: "POST",
      body: JSON.stringify({ username, password }),
      headers,
    })
      .then(handleResponse<LoginResponse>)
      .catch((error) => {
        throw new Error(error.message);
      }),

  createUser: async (user: NewUserRequest) =>
    fetch(createUrl("users"), {
      method: "POST",
      body: JSON.stringify(user),
      headers,
    })
      .then(handleResponse<User>)
      .catch((error) => {
        throw new Error(error.message);
      }),
};

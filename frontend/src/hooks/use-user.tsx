import { UsersService } from "@/lib/users-service";
import { useToast } from "./use-toast";
import { useState } from "react";
import { Account, NewUserRequest, User } from "@/lib/types";
import { useRouter } from "next/navigation";

export const useUser = () => {
  const [user, setUser] = useState<User | null>(null);
  const [accounts, setAccounts] = useState<Account[] | null>(null);
  const { toast } = useToast();
  const router = useRouter();

  const { login: handleLogin } = UsersService;

  const login = async (username: string, password: string) => {
    try {
      const response = await handleLogin(username, password);
      toast({ title: `Welcome back, ${response.user.username}!` });

      setUser(response.user);
      setAccounts({ ...response.accounts });
    } catch (error) {
      toast({ title: (error as Error).message });
      console.error(error);
    }
  };

  const sendUserToLoginPage = () => {
    router.push("/login");

    return (
      <div>
        <p>Redirecting to login...</p>
      </div>
    );
  };

  const createNewUser = async (user: NewUserRequest) => {
    try {
      const response = await UsersService.createUser(user);

      toast({ title: `Welcome, ${response.username}!` });
      setUser(response);
    } catch (error) {
      console.log("error", error);
      toast({ title: (error as Error).message });
      console.error(error);
    }
  };

  return {
    login,
    user,
    accounts,
    sendUserToLoginPage,
    createNewUser,
  };
};

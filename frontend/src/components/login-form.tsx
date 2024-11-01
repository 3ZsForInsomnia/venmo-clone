import { useUser } from "@/hooks/use-user";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { useCallback, useState } from "react";

export const LoginForm = () => {
  const { login, createNewUser } = useUser();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [creatingUser, setCreatingUser] = useState(false);
  const [nameOfAccount, setNameOfAccount] = useState("");
  const [initialBalance, setInitialBalance] = useState(0);

  const handleSubmit = useCallback(
    async () => login(username, password),
    [username, password, login],
  );

  const handleCreateUser = useCallback(
    async () =>
      createNewUser({
        username,
        password,
        first_account_name: nameOfAccount,
        starting_balance: initialBalance,
      }),
    [createNewUser, username, password, nameOfAccount, initialBalance],
  );

  return (
    <section className="m-auto w-1/2">
      <Input
        type="text"
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
        className="mb-4 w-72"
      />
      <Input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
        className="mb-4 w-72"
      />
      {!creatingUser && (
        <section className="flex flex-col">
          <Button
            onClick={handleSubmit}
            variant="outline"
            className="mb-4 w-72"
          >
            Login
          </Button>
          <Button
            onClick={() => setCreatingUser(!creatingUser)}
            variant="outline"
            className="w-72"
          >
            Sign up
          </Button>
        </section>
      )}
      {creatingUser && (
        <section className="mt-4">
          <Input
            type="text"
            placeholder="Name of account"
            className="mb-4 w-72"
            onChange={(e) => setNameOfAccount(e.target.value)}
          />
          <Input
            type="number"
            placeholder="Initial balance"
            className="mb-4 w-72"
            onChange={(e) => setInitialBalance(Number(e.target.value))}
          />
          <Button onClick={handleCreateUser} className="w-72">
            Create user
          </Button>
        </section>
      )}
    </section>
  );
};

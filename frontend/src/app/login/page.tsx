"use client";

import { useUser } from "@/hooks/use-user";
import { useRouter } from "next/navigation";
import { LoginForm } from "@/components/login-form";

export default function Login() {
  const { user } = useUser();
  const router = useRouter();

  if (user) {
    router.push("/dashboard");

    return (
      <div>
        <p>Redirecting to dashboard...</p>
      </div>
    );
  }

  return (
    <section>
      <h1>Welcome to Totally-Not-Venmo!</h1>
      <main>
        <LoginForm />
      </main>
    </section>
  );
}

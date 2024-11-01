"use client";

import { useUser } from "@/hooks/use-user";

export default function Home() {
  const { user, sendUserToLoginPage } = useUser();

  if (!user) return sendUserToLoginPage();

  return <section></section>;
}

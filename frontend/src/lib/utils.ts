import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

const baseUrl = "http://localhost:8000";
export const createUrl = (endpoint: string) => `${baseUrl}/${endpoint}`;

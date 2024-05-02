import Image from "next/image";
import { Inter } from "next/font/google";
import Login from "@/login";
import { UserProvider } from "@auth0/nextjs-auth0/client";
const inter = Inter({ subsets: ["latin"] });

export default function dashboard() {
  return (
    <main
      className={`flex min-h-screen flex-col items-center justify-between p-24 ${inter.className}`}
    >
      <h1 className="text-4xl font-bold">Welcome to Our Application</h1>
      <p className="text-2xl">This is the Getting Started page</p>
      <Login className="p-4 mt-4 bg-blue-500 text-white rounded-lg" />
      <p className="text-xl">Your journey begins here</p>
    </main>
  );
}

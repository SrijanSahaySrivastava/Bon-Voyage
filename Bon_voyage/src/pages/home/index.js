"use client";
import { Inter } from "next/font/google";
import { useState } from "react";
import TagInput from "@/components/Taginput";
import "./index.css";
import { useUser } from "@auth0/nextjs-auth0/client";
const inter = Inter({ subsets: ["latin"] });
import { getSession } from "@auth0/nextjs-auth0";
export default async function Home() {
  // const { user, error, isLoading } = useUser();
  const [interests, setInterests] = useState([]);
  const [healthIssues, setHealthIssues] = useState([]);
  const [foodPreferences, setFoodPreferences] = useState([]);
  const handleSubmit = async (e) => {
    e.preventDefault();
    // console.log(e.target[0].value);
    // console.log(e.target[1].value);
    // console.log(e.target[2].value);
    // console.log(healthIssues);
    // console.log(interests);
    // console.log(foodPreferences);
    //     {
    //     "Place": "Lucknow",
    //     "Food": "local",
    //     "Interests": "Adventure, Religion",
    //     "Health": "None",
    //     "Days": 5,
    //     "email": "abc@gmail.com",
    //     "in_date": "06-04-2024",
    //     "out_date": "06-04-2024"
    // }
    // const response = await fetch("https://8dd2-103-231-47-210.ngrok-free.app", {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json",
    //   },
    //   body: {
    //     Place: e.target[0].value,
    //     Food: foodPreferences.join(", "),
    //     Interests: interests.join(", "),
    //     Health: healthIssues.join(", "),
    //     Days: 5,
    //   },
    // // });
    // console.log(yah);
    // console.log(user);
    // if (!response.ok) {
    //   // handle error
    //   console.error("An error occurred while making the POST request");
    //   return;
    // }

    // const data = await response.json();
  };
  return (
    <main className="main">
      <h1 className="title">Welcome to Bon Voyage</h1>
      <form className="form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Where are you going?"
          className="input location"
        />
        <div className="dates">
          <input
            type="date"
            placeholder="When are you going?"
            className="input date-go"
          />
          <input
            type="date"
            placeholder="When are you coming back?"
            className="input date-back"
          />
        </div>
        <TagInput
          _placeholder="Health Issues"
          tags={healthIssues}
          setTags={setHealthIssues}
          className="tag-input HealthIssues"
        />
        <TagInput
          _placeholder="Interest"
          tags={interests}
          setTags={setInterests}
          className="tag-input Interests"
        />
        <TagInput
          _placeholder="Food Preferences"
          tags={foodPreferences}
          setTags={setFoodPreferences}
          className="tag-input Preferences"
        />
        <button type="submit" className="submit-button">
          Plan my trip
        </button>
      </form>
      <p className="description">Your one-stop shop for travel planning</p>
    </main>
  );
}

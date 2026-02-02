
"use client";
import { useRouter } from "next/navigation";
import { IkigaiSliders } from "@/components/onboarding/IkigaiSliders";
import { useUserStore } from "@/store/userStore";

export default function OnboardingPage() {
  const router = useRouter();
  // In a real app, we would send these values to the backend to create the user
  // For this demo, we just simulate the step
  
  const handleSubmit = () => {
    // Logic to save to backend would go here
    router.push("/dashboard");
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
      <div className="bg-white p-8 rounded-2xl shadow-xl max-w-md w-full space-y-6">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900">Define Your Ikigai</h2>
          <p className="text-gray-500 text-sm mt-1">
            Rate yourself on a scale of 0-10 to help our AI find your perfect IT domain.
          </p>
        </div>

        <IkigaiSliders onChange={(val) => console.log(val)} />

        <button
          onClick={handleSubmit}
          className="w-full py-3 bg-indigo-600 text-white font-bold rounded-xl hover:bg-indigo-700 transition-colors"
        >
          Generate My Path
        </button>
      </div>
    </div>
  );
}

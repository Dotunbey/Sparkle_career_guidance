
import Link from "next/link";
import { APP_NAME, TAGLINE } from "@/lib/constants";

export default function LandingPage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-6 text-center bg-white">
      <div className="max-w-2xl space-y-8">
        <div className="space-y-4">
          <h1 className="text-6xl font-extrabold tracking-tight text-gray-900">
            {APP_NAME} <span className="text-indigo-600">.</span>
          </h1>
          <p className="text-2xl text-gray-600 font-medium">{TAGLINE}</p>
          <p className="text-gray-500 max-w-lg mx-auto leading-relaxed">
            Stop guessing your career. We combine <strong>Ikigai Philosophy</strong> with 
            <strong> Real-time Course Tracking</strong> to guide you through the 
            "Valley of Despair" in learning.
          </p>
        </div>

        <div className="flex justify-center gap-4">
          <Link 
            href="/onboarding"
            className="px-8 py-4 bg-indigo-600 text-white font-bold rounded-full hover:bg-indigo-700 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-1"
          >
            Find My Spark &rarr;
          </Link>
          <Link 
            href="/dashboard"
            className="px-8 py-4 bg-gray-100 text-gray-700 font-bold rounded-full hover:bg-gray-200 transition-all"
          >
            Demo Dashboard
          </Link>
        </div>
      </div>
    </main>
  );
}

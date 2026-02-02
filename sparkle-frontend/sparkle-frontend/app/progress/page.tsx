
"use client";
import { EmotionalTrendChart } from "@/components/charts/EmotionalTrendChart";
import { Button } from "@/components/ui/Button";
import Link from "next/link";

// Mock data for the chart (Connect this to backend history later)
const MOCK_HISTORY = [
  { week: "Week 1", emotionScore: 80, label: "Optimism" },
  { week: "Week 2", emotionScore: 40, label: "Pessimism" },
  { week: "Week 3", emotionScore: 20, label: "Despair" },
  { week: "Week 4", emotionScore: 55, label: "Informed" },
];

export default function ProgressPage() {
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto space-y-8">
        <header className="flex justify-between items-center">
            <h1 className="text-3xl font-bold text-gray-900">Your Emotional Journey</h1>
            <Link href="/dashboard">
                <Button variant="outline">Back to Dashboard</Button>
            </Link>
        </header>

        <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
            <h2 className="text-lg font-semibold mb-4">The Cycle of Change</h2>
            <div className="h-[400px]">
                <EmotionalTrendChart data={MOCK_HISTORY} />
            </div>
            <p className="text-sm text-gray-500 mt-4 text-center">
                This chart tracks your emotional state as you complete courses. 
                Dips are normal—keep going!
            </p>
        </div>
      </div>
    </div>
  );
}




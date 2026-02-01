
"use client";
import { useQuery } from "@tanstack/react-query";
import { fetchRecommendations } from "@/lib/api";
import { RecommendationCard } from "@/components/dashboard/RecommendationCard";

// Mock User ID (In real app, get this from Auth Context)
const USER_ID = "12345678-1234-5678-1234-567812345678";

export default function DashboardPage() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["recommendations", USER_ID], // Cache key includes ID
    queryFn: () => fetchRecommendations(USER_ID),
  });

  if (isLoading) return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="animate-pulse text-indigo-600 font-medium">Loading your path...</div>
    </div>
  );

  if (error) return (
    <div className="p-8 text-red-500">
      Error loading data. Is the backend running?
    </div>
  );

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-8">
      <header className="space-y-2">
        <h1 className="text-3xl font-bold text-gray-900">Your Career Path</h1>
        <div className="bg-indigo-50 p-4 rounded-xl border border-indigo-100 text-indigo-800 text-sm">
          💡 <strong>AI Insight:</strong> {data?.reasoning}
        </div>
      </header>

      <div className="grid gap-6">
        {data?.courses.map((course) => (
          <RecommendationCard key={course.id} course={course} />
        ))}
      </div>
    </div>
  );
}

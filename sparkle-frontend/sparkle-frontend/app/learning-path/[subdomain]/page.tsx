
"use client";
import { useParams } from "next/navigation";
import { useCourses } from "@/hooks/useCourses";
import { RecommendationCard } from "@/components/dashboard/RecommendationCard";
import { Button } from "@/components/ui/Button";
import Link from "next/link";

export default function SubdomainPage() {
  const params = useParams();
  const subdomain = params.subdomain as string; // e.g., "frontend"
  const { data: courses, isLoading } = useCourses(subdomain);

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto space-y-6">
        <header className="flex items-center justify-between">
            <div>
                <h1 className="text-3xl font-bold capitalize text-gray-900">
                {subdomain.replace("-", " ")} Path
                </h1>
                <p className="text-gray-500">Curated modules for this specialization</p>
            </div>
            <Link href="/dashboard">
                <Button variant="outline">Back to Dashboard</Button>
            </Link>
        </header>

        {isLoading ? (
            <div>Loading modules...</div>
        ) : (
          <div className="grid gap-4">
            {courses?.map((course) => (
              <RecommendationCard key={course.id} course={course} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

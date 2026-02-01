
"use client";
import { useState } from "react";
import { Course } from "@/lib/types";
import { updateProgress } from "@/lib/api";
import { EmotionalBadge } from "../ui/EmotionalBadge";

// Mock User ID for demo (Replace with Auth ID later)
const USER_ID = "12345678-1234-5678-1234-567812345678";

export function RecommendationCard({ course }: { course: Course }) {
  // Local state for immediate UI updates (Optimistic UI)
  const [progress, setProgress] = useState(course.progress);
  const [emotion, setEmotion] = useState(course.emotional_stage);
  const [isLoading, setIsLoading] = useState(false);

  const handleCheckbox = async () => {
    setIsLoading(true);
    
    // Logic: Toggle between 0 and 100, or increment by 20%
    const newProgress = progress >= 100 ? 0 : Math.min(progress + 20, 100); 
    
    try {
      // 1. Send update to Backend
      const newEmotion = await updateProgress(USER_ID, course.id, newProgress);
      
      // 2. Update Local State with Backend Response
      setProgress(newProgress);
      setEmotion(newEmotion);

      // 3. Trigger User Feedback if in "Valley of Despair"
      if (newEmotion === "Valley of Despair") {
        alert("Hold on! You are in the Valley of Despair. This is the hardest part, don't quit!");
      }
    } catch (error) {
      console.error("Failed to sync progress", error);
      alert("Failed to save progress. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-2xl p-5 shadow-sm space-y-3 border border-gray-100 transition-all hover:shadow-md">
      <div className="flex justify-between items-start">
        <div>
          <h3 className="font-semibold text-lg text-gray-900">{course.title}</h3>
          <span className="text-xs text-gray-500 uppercase tracking-wide font-medium">
            {course.platform} • {course.duration_hours} Hours
          </span>
        </div>
        <EmotionalBadge stage={emotion} />
      </div>

      {/* Dynamic Progress Bar */}
      <div className="w-full bg-gray-100 rounded-full h-2 mt-2 overflow-hidden">
        <div 
          className={`h-2 rounded-full transition-all duration-500 ease-out ${
            progress === 100 ? 'bg-green-500' : 'bg-indigo-600'
          }`} 
          style={{ width: `${progress}%` }} 
        />
      </div>

      <div className="flex justify-between items-center pt-2">
        <button
          onClick={handleCheckbox}
          disabled={isLoading}
          className={`text-sm font-medium transition-colors ${
            progress >= 100 
              ? "text-green-600 hover:text-green-700" 
              : "text-indigo-600 hover:text-indigo-800"
          } disabled:opacity-50`}
        >
          {isLoading ? "Syncing..." : progress >= 100 ? "✓ Completed" : "Mark Progress (+20%)"}
        </button>
        
        <a 
          href={course.url} 
          target="_blank" 
          rel="noopener noreferrer"
          className="px-4 py-2 bg-gray-900 text-white text-sm font-medium rounded-lg hover:bg-black transition-colors"
        >
          Go to Course
        </a>
      </div>
    </div>
  );
}


export type EmotionalStage = 
  | "Uninformed Optimism" 
  | "Informed Pessimism" 
  | "Valley of Despair" 
  | "Informed Optimism" 
  | "Success";

export interface Course {
  id: string;
  title: string;
  platform: "Coursera" | "Udemy" | "YouTube";
  url: string;
  level: string;
  duration_hours: number;
  // These are now guaranteed by the backend's CourseResponse
  emotional_stage: EmotionalStage;
  progress: number;
}

export interface RecommendationResponse {
  user_id: string;
  domains: string[];
  reasoning: string;
  confidence_score: number;
  courses: Course[];
}

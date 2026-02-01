
import axios from "axios";
import { RecommendationResponse, EmotionalStage } from "./types";

// Setup Axios Client
const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
  headers: { "Content-Type": "application/json" }
});

export const fetchRecommendations = async (userId: string): Promise<RecommendationResponse> => {
  const { data } = await api.get<RecommendationResponse>(`/recommendations/${userId}`);
  return data;
};

// Now returns the EmotionalStage for immediate UI feedback
export const updateProgress = async (
  userId: string,
  courseId: string, 
  progress: number
): Promise<EmotionalStage> => {
  const { data } = await api.post<EmotionalStage>("/progress", { 
    user_id: userId, 
    course_id: courseId, 
    progress 
  });
  return data;
};

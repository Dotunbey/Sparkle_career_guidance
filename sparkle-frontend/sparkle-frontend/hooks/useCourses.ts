  
import { useQuery } from "@tanstack/react-query";
import { fetchRecommendations } from "@/lib/api";
import { DEMO_USER_ID } from "@/lib/constants";
import { Course } from "@/lib/types";

export function useCourses(subdomain?: string) {
  return useQuery({
    queryKey: ["courses", subdomain],
    queryFn: async () => {
      // In a real app, you'd hit an endpoint like /courses?subdomain=X
      // Here we filter the main recommendations to keep it aligned with your current backend
      const data = await fetchRecommendations(DEMO_USER_ID);
      
      if (!subdomain) return data.courses;
      
      // Filter logic to find courses matching the requested subdomain
      // Note: The backend data needs to include 'subdomain' in the response for this to work perfectly.
      // For now, we return all, or you can add .filter() if you add that field to the DTO.
      return data.courses; 
    },
  });
}

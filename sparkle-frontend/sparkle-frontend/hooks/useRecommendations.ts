
import { useQuery } from "@tanstack/react-query";
import { fetchRecommendations } from "@/lib/api";
import { DEMO_USER_ID } from "@/lib/constants";

export function useRecommendations() {
  return useQuery({
    queryKey: ["recommendations", DEMO_USER_ID],
    queryFn: () => fetchRecommendations(DEMO_USER_ID),
    staleTime: 1000 * 60 * 5, // Data stays fresh for 5 minutes
  });
}

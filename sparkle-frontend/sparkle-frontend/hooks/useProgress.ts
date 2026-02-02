#!filepath hooks/useProgress.ts
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { updateProgress } from "@/lib/api";
import { DEMO_USER_ID } from "@/lib/constants";
import { EmotionalStage } from "@/lib/types";

export function useUpdateProgress() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ courseId, progress }: { courseId: string; progress: number }) =>
      updateProgress(DEMO_USER_ID, courseId, progress),
      
    onSuccess: (newEmotion, variables) => {
      // 1. Immediately update the cache so the UI reflects the change without a refetch
      queryClient.setQueryData(
        ["recommendations", DEMO_USER_ID], 
        (oldData: any) => {
          if (!oldData) return oldData;
          return {
            ...oldData,
            courses: oldData.courses.map((c: any) =>
              c.id === variables.courseId
                ? { ...c, progress: variables.progress, emotional_stage: newEmotion }
                : c
            ),
          };
        }
      );
    },
  });
}

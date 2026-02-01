
#!filepath store/userStore.ts
import { create } from "zustand";
import { EmotionalStage } from "@/lib/types";

interface UserState {
  name: string;
  // We store the user's overall current stage here
  currentEmotionalStage: EmotionalStage; 
  
  // Actions to update the state
  setName: (name: string) => void;
  setEmotionalStage: (stage: EmotionalStage) => void;
}

export const useUserStore = create<UserState>((set) => ({
  name: "Guest", // Default value
  currentEmotionalStage: "Uninformed Optimism", // Default start
  
  setName: (name) => set({ name }),
  setEmotionalStage: (stage) => set({ currentEmotionalStage: stage }),
}));

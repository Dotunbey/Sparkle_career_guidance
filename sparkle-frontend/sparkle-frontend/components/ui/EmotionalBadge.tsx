
import { EmotionalStage } from "@/lib/types";

const colorMap: Record<EmotionalStage, string> = {
  "Uninformed Optimism": "bg-blue-100 text-blue-800 border-blue-200",
  "Informed Pessimism": "bg-yellow-100 text-yellow-800 border-yellow-200",
  "Valley of Despair": "bg-red-100 text-red-800 border-red-200",
  "Informed Optimism": "bg-green-100 text-green-800 border-green-200",
  "Success": "bg-emerald-100 text-emerald-800 border-emerald-200",
};

export function EmotionalBadge({ stage }: { stage: EmotionalStage }) {
  return (
    <span className={`px-3 py-1 rounded-full text-xs font-medium border ${colorMap[stage]}`}>
      {stage}
    </span>
  );
}

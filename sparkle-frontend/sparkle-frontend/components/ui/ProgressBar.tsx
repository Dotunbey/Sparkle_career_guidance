
interface ProgressBarProps {
  progress: number;
  className?: string;
}

export function ProgressBar({ progress, className = "" }: ProgressBarProps) {
  // Clamp value between 0 and 100
  const clamped = Math.min(Math.max(progress, 0), 100);
  
  return (
    <div className={`h-2 w-full overflow-hidden rounded-full bg-gray-100 ${className}`}>
      <div
        className="h-full bg-indigo-600 transition-all duration-500 ease-in-out"
        style={{ width: `${clamped}%` }}
      />
    </div>
  );
}

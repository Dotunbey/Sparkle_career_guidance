
"use client";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

interface ChartData {
  week: string;
  emotionScore: number;
  label?: string;
}

export function EmotionalTrendChart({ data }: { data: ChartData[] }) {
  return (
    <ResponsiveContainer width="100%" height="100%">
      <LineChart data={data} margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e7eb" />
        <XAxis 
          dataKey="week" 
          tick={{ fontSize: 12, fill: "#6b7280" }} 
          axisLine={false}
          tickLine={false}
        />
        {/* YAxis hidden for cleaner look, tooltip handles values */}
        <YAxis hide domain={[0, 100]} />
        <Tooltip 
          contentStyle={{ 
            backgroundColor: "#fff", 
            borderRadius: "12px", 
            border: "1px solid #e5e7eb",
            boxShadow: "0 4px 6px -1px rgb(0 0 0 / 0.1)" 
          }}
          itemStyle={{ color: "#4f46e5", fontWeight: 600 }}
        />
        <Line 
          type="monotone" 
          dataKey="emotionScore" 
          stroke="#4f46e5" 
          strokeWidth={4}
          dot={{ r: 6, fill: "#fff", stroke: "#4f46e5", strokeWidth: 3 }}
          activeDot={{ r: 8, fill: "#4f46e5" }}
          animationDuration={1500}
        />
      </LineChart>
    </ResponsiveContainer>
  );
}

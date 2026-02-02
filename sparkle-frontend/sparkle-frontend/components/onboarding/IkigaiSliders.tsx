
"use client";
import { useState } from "react";

interface IkigaiState {
  love: number;
  good_at: number;
  world_needs: number;
  paid_for: number;
}

interface Props {
  onChange: (values: IkigaiState) => void;
}

export function IkigaiSliders({ onChange }: Props) {
  const [values, setValues] = useState<IkigaiState>({
    love: 5,
    good_at: 5,
    world_needs: 5,
    paid_for: 5,
  });

  const handleSlider = (key: keyof IkigaiState, val: string) => {
    const newValues = { ...values, [key]: parseInt(val) };
    setValues(newValues);
    onChange(newValues);
  };

  return (
    <div className="grid gap-8 py-6">
      {Object.keys(values).map((key) => (
        <div key={key} className="space-y-2">
          <div className="flex justify-between items-center">
            <label className="capitalize font-semibold text-gray-700">
              {key.replace("_", " ")}
            </label>
            <span className="text-indigo-600 font-bold text-lg">{values[key as keyof IkigaiState]}</span>
          </div>
          <input
            type="range"
            min="0"
            max="10"
            value={values[key as keyof IkigaiState]}
            onChange={(e) => handleSlider(key as keyof IkigaiState, e.target.value)}
            className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-indigo-600"
          />
          <p className="text-xs text-gray-400">
            {key === "love" && "How much do you enjoy doing this?"}
            {key === "good_at" && "How skilled are you naturally?"}
            {key === "world_needs" && "Is there a demand for this?"}
            {key === "paid_for" && "Can you earn a living from this?"}
          </p>
        </div>
      ))}
    </div>
  );
}

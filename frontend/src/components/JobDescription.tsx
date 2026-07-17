"use client";

interface JobDescriptionProps {
    value: string;
    onChange: (value: string) => void;
}

export default function JobDescription({
    value,
    onChange,
}: JobDescriptionProps) {
    const MAX_CHARS = 10000;

    return (
        <div className="space-y-2">
            <div className="flex items-center justify-between">
                <label className="text-sm font-semibold text-zinc-300">
                    📋 Job Description
                </label>
                <span
                    className={`text-xs ${value.length > MAX_CHARS * 0.9
                            ? "text-amber-400"
                            : "text-zinc-600"
                        }`}
                >
                    {value.length.toLocaleString()} / {MAX_CHARS.toLocaleString()}
                </span>
            </div>
            <textarea
                value={value}
                onChange={(e) => {
                    if (e.target.value.length <= MAX_CHARS) onChange(e.target.value);
                }}
                placeholder="Paste the full job description here..."
                rows={8}
                className="w-full resize-none rounded-2xl border border-zinc-700/60 bg-zinc-900/40 p-4 text-sm text-zinc-200 placeholder-zinc-600 outline-none transition-all duration-300 focus:border-indigo-500/50 focus:ring-2 focus:ring-indigo-500/10 sm:text-[0.92rem]"
            />
        </div>
    );
}

"use client";

import { useEffect, useState } from "react";
import type { AnalysisResult } from "@/lib/api";
import { TrendingUp, TrendingDown, Lightbulb, PartyPopper } from "lucide-react";
import SkillAnalysis from "./SkillAnalysis";

interface ResultsCardProps {
    result: AnalysisResult;
}

export default function ResultsCard({ result }: ResultsCardProps) {
    const [animatedScore, setAnimatedScore] = useState(0);

    useEffect(() => {
        setAnimatedScore(0);
        const target = result.score;
        const duration = 1500;
        const startTime = Date.now();

        const animate = () => {
            const elapsed = Date.now() - startTime;
            const progress = Math.min(elapsed / duration, 1);
            // Ease out cubic
            const eased = 1 - Math.pow(1 - progress, 3);
            setAnimatedScore(Math.round(eased * target * 10) / 10);
            if (progress < 1) requestAnimationFrame(animate);
        };
        requestAnimationFrame(animate);
    }, [result.score]);

    const getIcon = () => {
        if (result.score < 40)
            return <TrendingDown className="h-5 w-5" />;
        if (result.score < 70) return <Lightbulb className="h-5 w-5" />;
        return <PartyPopper className="h-5 w-5" />;
    };

    return (
        <div className="animate-fadeIn space-y-5">
            {/* Score Card */}
            <div
                className="relative overflow-hidden rounded-2xl border p-6 text-center sm:p-8"
                style={{
                    borderColor: `${result.color_start}30`,
                    background: `linear-gradient(135deg, ${result.color_start}0A, ${result.color_end}06)`,
                }}
            >
                {/* Subtle glow */}
                <div
                    className="pointer-events-none absolute inset-0 opacity-20 blur-[80px]"
                    style={{
                        background: `radial-gradient(circle at center, ${result.color_start}, transparent 70%)`,
                    }}
                />

                <p className="relative text-xs font-semibold uppercase tracking-[0.2em] text-zinc-500">
                    Match Score
                </p>
                <p
                    className="relative mt-2 text-5xl font-extrabold tabular-nums sm:text-6xl"
                    style={{
                        background: `linear-gradient(135deg, ${result.color_start}, ${result.color_end})`,
                        WebkitBackgroundClip: "text",
                        WebkitTextFillColor: "transparent",
                    }}
                >
                    {animatedScore.toFixed(1)}%
                </p>
                <p
                    className="relative mt-1 text-sm font-semibold"
                    style={{ color: result.color_start }}
                >
                    {result.label}
                </p>
            </div>

            {/* Gauge Bar */}
            <div>
                <div className="mb-2 flex items-center justify-between text-xs">
                    <span className="font-medium text-zinc-500">Match Percentage</span>
                    <span className="font-bold" style={{ color: result.color_start }}>
                        {result.label}
                    </span>
                </div>
                <div className="h-3 overflow-hidden rounded-full bg-zinc-800/80 shadow-inner">
                    <div
                        className="h-full rounded-full transition-all duration-[1500ms] ease-out"
                        style={{
                            width: `${result.score}%`,
                            background: `linear-gradient(90deg, ${result.color_start}, ${result.color_end})`,
                            boxShadow: `0 0 16px ${result.color_start}44`,
                        }}
                    />
                </div>
            </div>

            {/* Feedback */}
            <div
                className="rounded-xl border-l-4 p-4 sm:p-5"
                style={{
                    borderLeftColor: result.color_start,
                    background: `${result.color_start}0A`,
                }}
            >
                <div className="flex items-start gap-3">
                    <div
                        className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg"
                        style={{ background: `${result.color_start}18`, color: result.color_start }}
                    >
                        {getIcon()}
                    </div>
                    <div>
                        <p className="text-sm font-semibold" style={{ color: result.color_end }}>
                            {result.icon} {result.label}
                        </p>
                        <p className="mt-1 text-sm leading-relaxed text-zinc-400">
                            {result.feedback}
                        </p>
                    </div>
                </div>
            </div>

            <SkillAnalysis result={result} />
        </div>
    );
}

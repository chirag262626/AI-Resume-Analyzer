"use client";

import type { AnalysisResult } from "@/lib/api";
import { CheckCircle2, XCircle, AlertCircle, Lightbulb } from "lucide-react";

export default function SkillAnalysis({ result }: { result: AnalysisResult }) {
    // Group skills by category for better visualization mapping
    const groupByCategory = (skills: { category: string; skill: string }[]) => {
        return skills.reduce((acc, curr) => {
            if (!acc[curr.category]) acc[curr.category] = [];
            acc[curr.category].push(curr.skill);
            return acc;
        }, {} as Record<string, string[]>);
    };

    const matchedGroups = groupByCategory(result.matched_skills || []);
    const missingGroups = groupByCategory(result.missing_skills || []);

    const hasMatches = result.matched_skills?.length > 0;
    const hasMissing = result.missing_skills?.length > 0;
    const hasRecommendations = result.recommendations?.length > 0;

    return (
        <div className="mt-8 animate-fadeIn space-y-6 border-t border-white/[0.06] pt-8">
            {/* Overview Head */}
            <div className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
                <div>
                    <h3 className="text-lg font-bold text-zinc-200">
                        Keyword & Skill Gap Analysis
                    </h3>
                    <p className="text-sm text-zinc-500">
                        Detected {result.total_jd_skills_found || 0} trackable skills in the
                        job description.
                    </p>
                </div>
                <div className="inline-flex items-center gap-2 rounded-xl border border-indigo-500/20 bg-indigo-500/[0.05] px-4 py-2 text-sm font-semibold text-indigo-400">
                    <AlertCircle className="h-4 w-4" />
                    Skill Match: {result.skill_match_percentage || 0}%
                </div>
            </div>

            {/* Matched Skills */}
            {hasMatches && (
                <div className="rounded-xl border border-emerald-500/10 bg-emerald-500/[0.02] p-4 sm:p-6">
                    <div className="mb-4 flex items-center gap-2 text-emerald-400">
                        <CheckCircle2 className="h-5 w-5" />
                        <h4 className="font-semibold">Matched Skills</h4>
                    </div>
                    <div className="space-y-4">
                        {Object.entries(matchedGroups).map(([category, skills]) => (
                            <div key={category}>
                                <span className="mb-2 block text-xs font-semibold uppercase tracking-wider text-emerald-500/70">
                                    {category}
                                </span>
                                <div className="flex flex-wrap gap-2">
                                    {skills.map((skill) => (
                                        <span
                                            key={skill}
                                            className="rounded-lg bg-emerald-500/10 px-2.5 py-1 text-xs font-medium text-emerald-300"
                                        >
                                            {skill}
                                        </span>
                                    ))}
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Missing Skills */}
            {hasMissing && (
                <div className="rounded-xl border border-amber-500/10 bg-amber-500/[0.02] p-4 sm:p-6">
                    <div className="mb-4 flex items-center gap-2 text-amber-500">
                        <XCircle className="h-5 w-5" />
                        <h4 className="font-semibold">Missing Keywords found in JD</h4>
                    </div>
                    <div className="space-y-4">
                        {Object.entries(missingGroups).map(([category, skills]) => (
                            <div key={category}>
                                <span className="mb-2 block text-xs font-semibold uppercase tracking-wider text-amber-500/70">
                                    {category}
                                </span>
                                <div className="flex flex-wrap gap-2">
                                    {skills.map((skill) => (
                                        <span
                                            key={skill}
                                            className="rounded-lg bg-amber-500/10 px-2.5 py-1 text-xs font-medium text-amber-500/90"
                                        >
                                            {skill}
                                        </span>
                                    ))}
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Recommendations */}
            {hasRecommendations && (
                <div className="rounded-xl border border-cyan-500/10 bg-cyan-500/[0.02] p-4 sm:p-6">
                    <div className="mb-3 flex items-center gap-2 text-cyan-400">
                        <Lightbulb className="h-5 w-5" />
                        <h4 className="font-semibold">Priority Recommendations</h4>
                    </div>
                    <ul className="space-y-3">
                        {result.recommendations.map((rec, i) => (
                            <li
                                key={i}
                                className="flex items-start gap-3 rounded-lg bg-black/20 p-3 text-sm text-cyan-100"
                            >
                                <span className="mt-0.5 flex h-4 w-4 shrink-0 justify-center text-cyan-500">
                                    •
                                </span>
                                {rec}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

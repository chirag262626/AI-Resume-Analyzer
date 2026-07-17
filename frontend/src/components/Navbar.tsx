"use client";

import { Sparkles } from "lucide-react";

export default function Navbar() {
    return (
        <nav className="fixed top-0 left-0 right-0 z-50 border-b border-white/[0.06] bg-[#0a0b0f]/80 backdrop-blur-xl">
            <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
                <div className="flex items-center gap-2.5">
                    <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-indigo-500 to-cyan-400 shadow-lg shadow-indigo-500/25">
                        <Sparkles className="h-5 w-5 text-white" />
                    </div>
                    <span className="bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-xl font-bold tracking-tight text-transparent">
                        ATS Analyzer
                    </span>
                </div>

                <div className="hidden items-center gap-6 sm:flex">
                    <span className="text-xs font-medium uppercase tracking-widest text-zinc-500">
                        Powered by TF-IDF
                    </span>
                    <a
                        href="https://github.com"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="rounded-lg border border-white/[0.08] bg-white/[0.03] px-4 py-2 text-sm font-medium text-zinc-300 transition-all hover:border-indigo-500/30 hover:bg-indigo-500/5 hover:text-white"
                    >
                        GitHub
                    </a>
                </div>
            </div>
        </nav>
    );
}

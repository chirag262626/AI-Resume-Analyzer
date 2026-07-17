"use client";

export default function Hero() {
    return (
        <section className="relative overflow-hidden pb-8 pt-28 sm:pb-12 sm:pt-32">
            {/* Background glow effects */}
            <div className="pointer-events-none absolute inset-0">
                <div className="absolute left-1/2 top-0 h-[500px] w-[800px] -translate-x-1/2 rounded-full bg-indigo-500/[0.07] blur-[120px]" />
                <div className="absolute right-0 top-32 h-[300px] w-[400px] rounded-full bg-cyan-500/[0.05] blur-[100px]" />
            </div>

            <div className="relative mx-auto max-w-4xl px-4 text-center sm:px-6">
                <div className="mb-4 inline-flex items-center gap-2 rounded-full border border-indigo-500/20 bg-indigo-500/10 px-4 py-1.5 text-xs font-medium text-indigo-300">
                    <span className="h-1.5 w-1.5 rounded-full bg-indigo-400 animate-pulse" />
                    AI-Powered Resume Analysis
                </div>

                <h1 className="text-4xl font-extrabold leading-tight tracking-tight sm:text-5xl lg:text-6xl">
                    <span className="bg-gradient-to-r from-indigo-400 via-cyan-400 to-indigo-400 bg-[length:200%_auto] bg-clip-text text-transparent animate-[gradientShift_4s_ease-in-out_infinite]">
                        AI Resume Reviewer
                    </span>
                </h1>

                <p className="mx-auto mt-4 max-w-2xl text-base text-zinc-400 sm:text-lg">
                    Upload your resume & paste a job description to see how well they
                    match. Get instant ATS compatibility insights.
                </p>

                <div className="mt-6 flex items-center justify-center gap-4 text-xs text-zinc-500 sm:gap-6 sm:text-sm">
                    <span className="flex items-center gap-1.5">
                        <span className="h-2 w-2 rounded-full bg-indigo-500" />
                        TF-IDF Vectorization
                    </span>
                    <span className="flex items-center gap-1.5">
                        <span className="h-2 w-2 rounded-full bg-cyan-500" />
                        Cosine Similarity
                    </span>
                    <span className="flex items-center gap-1.5">
                        <span className="h-2 w-2 rounded-full bg-emerald-500" />
                        PDF & DOCX Support
                    </span>
                </div>
            </div>
        </section>
    );
}

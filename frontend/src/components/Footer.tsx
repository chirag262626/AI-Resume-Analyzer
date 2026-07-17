export default function Footer() {
    return (
        <footer className="border-t border-white/[0.04] bg-[#0a0b0f]/60 py-8">
            <div className="mx-auto max-w-7xl px-4 text-center sm:px-6 lg:px-8">
                <p className="text-xs text-zinc-600">
                    Powered by{" "}
                    <span className="font-semibold text-indigo-400/60">TF-IDF</span>
                    {" + "}
                    <span className="font-semibold text-cyan-400/60">
                        Cosine Similarity
                    </span>
                </p>
                <p className="mt-1 text-xs text-zinc-700">
                    © {new Date().getFullYear()} ATS Resume Analyzer. Built with Next.js &
                    FastAPI.
                </p>
            </div>
        </footer>
    );
}

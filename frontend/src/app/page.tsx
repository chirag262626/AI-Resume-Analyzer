"use client";

import { useState } from "react";
import toast from "react-hot-toast";
import { Search, Loader2 } from "lucide-react";

import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import FileUpload from "@/components/FileUpload";
import JobDescription from "@/components/JobDescription";
import ResultsCard from "@/components/ResultsCard";
import Footer from "@/components/Footer";
import { analyzeResume, type AnalysisResult } from "@/lib/api";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState<AnalysisResult | null>(null);

  const handleAnalyze = async () => {
    // Validation
    if (!file) {
      toast.error("Please upload your resume first.");
      return;
    }
    if (!jobDescription.trim()) {
      toast.error("Please paste the job description.");
      return;
    }

    setIsLoading(true);
    setResult(null);

    try {
      const data = await analyzeResume(file, jobDescription);
      setResult(data);
      toast.success(`Analysis complete! Match score: ${data.score}%`);
    } catch (error) {
      const message =
        error instanceof Error
          ? error.message
          : "An unexpected error occurred.";
      toast.error(message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex min-h-screen flex-col">
      <Navbar />

      <main className="flex-1">
        <Hero />

        {/* ─── Input Section ─── */}
        <section className="mx-auto max-w-5xl px-4 pb-6 sm:px-6 lg:px-8">
          <div className="rounded-3xl border border-white/[0.06] bg-[#0e1017]/70 p-5 shadow-2xl shadow-black/20 backdrop-blur-xl sm:p-8">
            <div className="grid gap-6 md:grid-cols-2">
              <FileUpload file={file} onFileChange={setFile} />
              <JobDescription
                value={jobDescription}
                onChange={setJobDescription}
              />
            </div>

            {/* Analyze Button */}
            <div className="mt-6 flex justify-center">
              <button
                onClick={handleAnalyze}
                disabled={isLoading}
                className="group relative flex items-center gap-2.5 rounded-2xl bg-gradient-to-r from-indigo-500 to-indigo-600 px-8 py-3.5 text-sm font-semibold text-white shadow-lg shadow-indigo-500/25 transition-all duration-300 hover:from-indigo-400 hover:to-indigo-500 hover:shadow-xl hover:shadow-indigo-500/30 disabled:cursor-not-allowed disabled:opacity-60 sm:px-10"
              >
                {isLoading ? (
                  <>
                    <Loader2 className="h-4 w-4 animate-spin" />
                    Analyzing...
                  </>
                ) : (
                  <>
                    <Search className="h-4 w-4 transition-transform group-hover:scale-110" />
                    Analyze Match
                  </>
                )}
              </button>
            </div>
          </div>
        </section>

        {/* ─── Results Section ─── */}
        {result && (
          <section className="mx-auto max-w-3xl px-4 pb-16 pt-4 sm:px-6 lg:px-8">
            <ResultsCard result={result} />
          </section>
        )}

        {/* ─── How It Works ─── */}
        {!result && (
          <section className="mx-auto max-w-5xl px-4 pb-16 pt-8 sm:px-6 lg:px-8">
            <h2 className="mb-6 text-center text-lg font-bold text-zinc-300">
              How It Works
            </h2>
            <div className="grid gap-4 sm:grid-cols-3">
              {[
                {
                  step: "01",
                  title: "Upload Resume",
                  desc: "Drop your PDF or DOCX resume file into the upload area.",
                  color: "from-indigo-500 to-indigo-600",
                },
                {
                  step: "02",
                  title: "Paste Job Description",
                  desc: "Copy and paste the full job description you want to target.",
                  color: "from-cyan-500 to-cyan-600",
                },
                {
                  step: "03",
                  title: "Get Insights",
                  desc: "Receive an instant ATS compatibility score with actionable feedback.",
                  color: "from-emerald-500 to-emerald-600",
                },
              ].map((item) => (
                <div
                  key={item.step}
                  className="group rounded-2xl border border-white/[0.05] bg-[#0e1017]/50 p-5 transition-all hover:border-white/[0.1] hover:bg-[#0e1017]/80"
                >
                  <div
                    className={`mb-3 inline-flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br ${item.color} text-sm font-bold text-white shadow-lg`}
                  >
                    {item.step}
                  </div>
                  <h3 className="text-sm font-semibold text-zinc-200">
                    {item.title}
                  </h3>
                  <p className="mt-1 text-xs leading-relaxed text-zinc-500">
                    {item.desc}
                  </p>
                </div>
              ))}
            </div>
          </section>
        )}
      </main>

      <Footer />
    </div>
  );
}

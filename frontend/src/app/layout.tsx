import type { Metadata } from "next";
import { Toaster } from "react-hot-toast";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Resume Reviewer · ATS Analyzer",
  description:
    "Upload your resume and paste a job description to see how well they match. AI-powered ATS compatibility analysis using TF-IDF and Cosine Similarity.",
  keywords: [
    "ATS",
    "Resume Analyzer",
    "Resume Reviewer",
    "TF-IDF",
    "Cosine Similarity",
    "Job Match",
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="min-h-screen bg-[#08090d] font-sans text-zinc-200 antialiased">
        <Toaster
          position="top-center"
          toastOptions={{
            duration: 4000,
            style: {
              background: "#1a1d27",
              color: "#e4e4e7",
              border: "1px solid rgba(108, 99, 255, 0.2)",
              borderRadius: "12px",
              fontSize: "0.875rem",
            },
          }}
        />
        {children}
      </body>
    </html>
  );
}

"use client";

import { useCallback, useState, useRef } from "react";
import { Upload, FileText, X } from "lucide-react";

interface FileUploadProps {
    file: File | null;
    onFileChange: (file: File | null) => void;
}

export default function FileUpload({ file, onFileChange }: FileUploadProps) {
    const [isDragging, setIsDragging] = useState(false);
    const inputRef = useRef<HTMLInputElement>(null);

    const ACCEPTED_TYPES = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ];

    const handleFile = useCallback(
        (f: File) => {
            if (
                ACCEPTED_TYPES.includes(f.type) ||
                f.name.endsWith(".pdf") ||
                f.name.endsWith(".docx")
            ) {
                onFileChange(f);
            }
        },
        [onFileChange]
    );

    const handleDrop = useCallback(
        (e: React.DragEvent) => {
            e.preventDefault();
            setIsDragging(false);
            if (e.dataTransfer.files[0]) handleFile(e.dataTransfer.files[0]);
        },
        [handleFile]
    );

    const handleDragOver = useCallback((e: React.DragEvent) => {
        e.preventDefault();
        setIsDragging(true);
    }, []);

    const handleDragLeave = useCallback((e: React.DragEvent) => {
        e.preventDefault();
        setIsDragging(false);
    }, []);

    const formatSize = (bytes: number) => {
        if (bytes < 1024) return `${bytes} B`;
        if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
        return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
    };

    return (
        <div className="space-y-2">
            <label className="text-sm font-semibold text-zinc-300">
                📄 Resume Upload
            </label>

            {!file ? (
                <div
                    onDrop={handleDrop}
                    onDragOver={handleDragOver}
                    onDragLeave={handleDragLeave}
                    onClick={() => inputRef.current?.click()}
                    className={`group relative flex cursor-pointer flex-col items-center justify-center rounded-2xl border-2 border-dashed p-8 transition-all duration-300 sm:p-10 ${isDragging
                            ? "border-indigo-400 bg-indigo-500/10"
                            : "border-zinc-700/60 bg-zinc-900/40 hover:border-indigo-500/40 hover:bg-indigo-500/[0.03]"
                        }`}
                >
                    <div
                        className={`mb-3 flex h-14 w-14 items-center justify-center rounded-2xl transition-all duration-300 ${isDragging
                                ? "bg-indigo-500/20 text-indigo-400"
                                : "bg-zinc-800 text-zinc-500 group-hover:bg-indigo-500/10 group-hover:text-indigo-400"
                            }`}
                    >
                        <Upload className="h-6 w-6" />
                    </div>
                    <p className="text-sm font-medium text-zinc-300">
                        Drop your resume here or{" "}
                        <span className="text-indigo-400">browse</span>
                    </p>
                    <p className="mt-1 text-xs text-zinc-500">
                        PDF or DOCX — Max 10 MB
                    </p>
                    <input
                        ref={inputRef}
                        type="file"
                        accept=".pdf,.docx"
                        onChange={(e) => {
                            if (e.target.files?.[0]) handleFile(e.target.files[0]);
                        }}
                        className="hidden"
                    />
                </div>
            ) : (
                <div className="flex items-center gap-3 rounded-2xl border border-indigo-500/20 bg-indigo-500/[0.05] p-4">
                    <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-indigo-500/15 text-indigo-400">
                        <FileText className="h-5 w-5" />
                    </div>
                    <div className="min-w-0 flex-1">
                        <p className="truncate text-sm font-medium text-zinc-200">
                            {file.name}
                        </p>
                        <p className="text-xs text-zinc-500">{formatSize(file.size)}</p>
                    </div>
                    <button
                        onClick={(e) => {
                            e.stopPropagation();
                            onFileChange(null);
                            if (inputRef.current) inputRef.current.value = "";
                        }}
                        className="flex h-8 w-8 items-center justify-center rounded-lg text-zinc-500 transition-colors hover:bg-white/5 hover:text-zinc-300"
                    >
                        <X className="h-4 w-4" />
                    </button>
                </div>
            )}
        </div>
    );
}

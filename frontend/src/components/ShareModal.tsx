import { X, Download, Copy, Check } from 'lucide-react'
import { useState } from 'react'

interface ShareModalProps {
    imageSrc: string
    onClose: () => void
}

export default function ShareModal({ imageSrc, onClose }: ShareModalProps) {
    const [copied, setCopied] = useState(false)

    const handleCopy = async () => {
        try {
            const response = await fetch(imageSrc)
            const blob = await response.blob()
            await navigator.clipboard.write([
                new ClipboardItem({ 'image/png': blob })
            ])
            setCopied(true)
            setTimeout(() => setCopied(false), 2000)
        } catch (err) {
            console.error('Failed to copy', err)
            alert('Failed to copy to clipboard. Please try downloading instead.')
        }
    }

    const handleDownload = () => {
        const link = document.createElement('a')
        link.download = 'vinylo-matchup.png'
        link.href = imageSrc
        link.click()
    }

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4" onClick={onClose}>
            <div className="bg-gray-900 border border-gray-800 rounded-2xl max-w-2xl w-full p-6 shadow-2xl relative" onClick={e => e.stopPropagation()}>
                <button onClick={onClose} className="absolute top-4 right-4 text-gray-400 hover:text-white transition-colors">
                    <X size={24} />
                </button>

                <h3 className="text-2xl font-bold text-white mb-6 text-center">Share Matchup</h3>

                <div className="bg-black/50 rounded-xl overflow-hidden mb-6 border border-gray-800 p-4 flex justify-center">
                    <img src={imageSrc} alt="Matchup Preview" className="max-h-[60vh] w-auto rounded-lg shadow-lg" />
                </div>

                <div className="flex gap-4 justify-center">
                    <button
                        onClick={handleCopy}
                        className="flex items-center gap-2 px-6 py-3 bg-gray-800 hover:bg-gray-700 text-black rounded-full font-bold transition-all border border-gray-700 hover:border-purple-500"
                    >
                        {copied ? <Check size={20} className="text-green-500" /> : <Copy size={20} />}
                        {copied ? 'Copied!' : 'Copy Image'}
                    </button>
                    <button
                        onClick={handleDownload}
                        className="flex items-center gap-2 px-6 py-3 bg-white hover:bg-gray-200 text-black rounded-full font-bold transition-all shadow-lg hover:scale-105"
                    >
                        <Download size={20} />
                        Download
                    </button>
                </div>
            </div>
        </div>
    )
}

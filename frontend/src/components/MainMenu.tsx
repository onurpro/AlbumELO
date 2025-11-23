import { motion } from 'framer-motion'
import { Play, Trophy, LogOut, Ban } from 'lucide-react'
import logo from '../assets/logo.svg'

interface MainMenuProps {
    username: string
    onPlay: () => void
    onStats: () => void
    onIgnored: () => void
    onLogout: () => void
}

export default function MainMenu({ username, onPlay, onStats, onIgnored, onLogout }: MainMenuProps) {
    return (
        <div className="flex flex-col items-center justify-center h-full w-full z-10 relative">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-center mb-12 flex flex-col items-center gap-4"
            >
                <img src={logo} alt="Vinylo Logo" className="w-24 h-24" />
                <h1 className="text-7xl font-bold tracking-tighter text-black">
                    Vinylo
                </h1>
                <p className="text-gray-500 tracking-widest uppercase text-sm font-bold">
                    Welcome back, <span className="text-black">{username}</span>
                </p>
            </motion.div>

            <div className="flex flex-col gap-4 w-full max-w-sm px-8">
                <MenuButton
                    onClick={onPlay}
                    icon={<Play size={20} fill="currentColor" />}
                    label="START RANKING"
                    primary
                />
                <MenuButton
                    onClick={onStats}
                    icon={<Trophy size={20} />}
                    label="LEADERBOARD"
                />
                <MenuButton
                    onClick={onIgnored}
                    icon={<Ban size={20} />}
                    label="MANAGE IGNORED"
                />

                <div className="h-4" /> {/* Spacer */}

                <button
                    onClick={onLogout}
                    className="flex items-center justify-center gap-2 text-gray-400 hover:text-red-500 transition-colors text-sm font-bold tracking-widest uppercase"
                >
                    <LogOut size={16} />
                    Log Out
                </button>
            </div>
        </div>
    )
}

function MenuButton({ onClick, icon, label, primary = false, disabled = false }: { onClick: () => void, icon: React.ReactNode, label: string, primary?: boolean, disabled?: boolean }) {
    return (
        <button
            onClick={onClick}
            disabled={disabled}
            className={`
        btn w-full flex items-center justify-center gap-3 text-lg
        ${primary ? 'btn-primary' : 'btn-secondary'}
        ${disabled ? 'opacity-50 cursor-not-allowed' : ''}
      `}
        >
            {icon}
            <span>{label}</span>
        </button>
    )
}

export interface Album {
    id: number
    name: string
    artist_name: string
    image_url: string
    elo_score: number
    playcount: number
    username: string
    ignored: boolean
}

export interface VoteResponse {
    success: boolean
    new_scores: {
        album1: number
        album2: number
    }
}

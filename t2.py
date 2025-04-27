import subprocess
from concurrent.futures import ThreadPoolExecutor
import yt_dlp
ids = ["Vi9bxu-M-ag", "aRUhd1Wd3Sw", "ofHYRdWQESo", "0gU-qrq3gjU", "KdWPGqT5GwE", "e1X3WPoETsk", "VjCHupej12U", "dYrwawDa92U", "GmHC1oaK9Ts", "uNcMKFkAKuw", "fb4rgYbi84c", "0ZGAKHoVFs0", "tU4xz1r_aE8", "XLLluxLg_Xc", "xN8DPjcybpM", "YjWktudqGN4", "9BlNJFIMUrY", "APhPNDikwRE", "eMrjjsnQUDw", "tN12g5QUIqg", "tcgXPI6Nxsw", "D0vA_R8lVLw", "n8cTHW_VxBw", "1Yfn7lH_8uA", "remZuJHeI7s", "ILxYkSVU9-k", "koEnfJfRr6g", "byCsxHUuOrk", "mGw_BvyovgE", "Bq58-o8mji0", "VETRVLw7vz8", "DrWjRwC1kYw", "wn-dseKsdQw", "8TUMa9PPdP0", "29Mg76KoW8U", "qvbtM03bx70", "BPftiMM8mgI", "_zoJ34wPIJA", "1dFqthtouqU", "u3v2H5mwixY", "7k6oEConqLA", "UXxwO_U_gXI", "nqC-UlGTssg", "XK8loB2jYDE", "eK4gqHb7P7w", "7NA3hX3IfVg", "SslpdF_HlFc", "cmgpJxt1q6k", "9KBadAcKVrU", "u2xLcx3sC_k", "uoII7VSDF3k", "5Udw0F6DIhA", "x2gl4KwUIV8", "kqFauVbe-1M", "FqaCRrxiS_A", "Bgf2bXr6psI", "EL3PKEHggrE", "ThJOl1gqIjs", "5dDkw_yCSgw", "kRwmnQDiRWk", "HKX__TQ9ff0", "Aib88vl6gDA", "6a8CNTk9yo4", "BBgSB2bLy60", "Z4hN0WZbASk", "OjF-OwLOKYE", "xWYjtDbfkXA", "_NZ5kb68IpA", "Z7VSgQ_y0dg", "VeWdk4D_xYs", "wB3Jf7yyvfU", "DnRY5yG67u8", "gtHKKZJ9W-Q", "MXs2qqWcGHo", "pZjm9rX5GdU", "SPkDA2lWtWE", "b2bIdtSwDhc", "fn9oKI9-TEs", "y4MOo-9fNyk", "he5PnMFwVSE", "gHyZnLZDnWI", "TtjqEe-ktHY", "wnoC68eTCtw", "3MCOhN--bfM"]
playlist_url = "https://www.youtube.com/watch?v=mEsleV16qdo"


def get_playlist_links(playlist_url):
    options = {
        "quiet": True,  # Suppress output
        "extract_flat": True,  # Do not download; just list information
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)

    if "entries" in playlist_info:
        video_links = [video["url"] for video in playlist_info["entries"]]
        return video_links
    else:
        return []



def download_video(url):
    command = [
        'yt-dlp',
        '-f',"bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", 
        '--concurrent-fragments', '5',
        url
    ]
    
    # Run yt-dlp command to download the video
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error downloading video: {url}\n{result.stderr}")
    else:
        print(f"Successfully downloaded: {url}")


def main():
    get_url = get_playlist_links(playlist_url)
    max_parallel_downloads = 10
    
    # Use ThreadPoolExecutor to download videos in parallel
    with ThreadPoolExecutor(max_workers=max_parallel_downloads) as executor:
        executor.map(download_video, get_url)

if __name__ == "__main__":
    main()
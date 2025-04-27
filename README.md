# youtube-playlist-downloader

A Python script to download all videos from a YouTube playlist using **yt-dlp** with parallel downloads.

## Features

- Fetches all video links from a YouTube playlist.
- Downloads videos at the best available quality.
- Downloads videos **in parallel** (multi-threaded).
- Displays success and error messages.
- Uses `yt-dlp` and `subprocess` for robust downloading.

## Requirements

- Python 3.7 or higher
- yt-dlp installed globally

## Install yt-dlp

```bash
pip install yt-dlp
```

## How to Use

1. Clone or download this repository.
2. Open the script and set your `playlist_url` variable.
3. Run the script:

```bash
python your_script_name.py
```

(Replace `your_script_name.py` with your actual filename.)

## Script Explanation

### get_playlist_links(playlist_url)

- Fetches all video URLs from a given playlist using yt-dlp.
- Does not download; only extracts URLs.

### download_video(url)

- Downloads a single video at the best available quality.
- Format preference:
  - `bestvideo[ext=mp4]+bestaudio[ext=m4a]`
  - If unavailable, falls back to `best[ext=mp4]`
  - If still unavailable, uses `best`.

### main()

- Fetches all playlist video URLs.
- Downloads videos using a ThreadPoolExecutor with 10 concurrent downloads.

## Customization

- **Change the number of parallel downloads**:  
  Modify `max_parallel_downloads` in the `main()` function.

- **Change output folder**:  
  Modify the `command` list inside `download_video` to add `-o "folder/%(title)s.%(ext)s"`.

Example:

```python
command = [
    'yt-dlp',
    '-f', "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    '--concurrent-fragments', '5',
    '-o', 'Downloads/%(title)s.%(ext)s',
    url
]
```

## Notes

- The script uses `subprocess.run` to call `yt-dlp`.
- The `ids` list at the top of the script is unused. You can remove it unless you need it for something else.
- Make sure your Python terminal can recognize the `yt-dlp` command (installed properly).

## Troubleshooting

- **yt-dlp: command not found**:  
  Ensure yt-dlp is installed and added to PATH.

- **Download errors**:  
  Some videos may be private or region-locked. yt-dlp will throw errors in those cases.

- **Slow downloads**:  
  Increase the `--concurrent-fragments` or `max_parallel_downloads` value.

## License

This project is free for personal and educational use.

## Author

Created by **Anubhav Maurya**

# light-fantasy

Automated TikTok video pipeline for @spongebob_prime_ (15k followers, rebranding from "Pick One Quiz"). Posts photorealistic light-fantasy / knight-and-summer scenes (with occasional dark-fantasy night scenes mixed in), 10-second clips, first-person POV or dynamic tracking camera motion -- no locked-off static shots.

## How it works

Two-phase GitHub Actions pipeline, same pattern as the other niche repos (pallowyn, creepvale, dark-fantasy):

1. `generate` -- picks the next scenes from `scripts/scene_bank.py`, generates a still image (Higgsfield Soul v2), animates it into a 10s video (Minimax Hailuo 2.3 image-to-video), muxes in music, commits the finished clips to `output/light_fantasy/`.
2. `schedule` -- creates Buffer posts for the generated clips, updates `state/light_fantasy_state.json`, commits the new state.

Runs daily via `.github/workflows/daily-post.yml` (cron `0 11 * * *`), and can also be triggered manually from the Actions tab.

## Setup checklist

- [x] Repo created, pipeline code committed (`scripts/`, `requirements.txt`)
- [x] `scripts/scene_bank.py` -- 20 scenes, photorealistic, POV/dynamic camera prompts
- [x] `.github/workflows/daily-post.yml` committed
- [x] `state/light_fantasy_state.json` committed
- [x] GitHub secret `HIGGSFIELD_API_KEY` set (new key created for this niche)
- [x] GitHub secret `BUFFER_ACCESS_TOKEN_LIGHTFANTASY` set
- [ ] GitHub secret `MUSIC_TRACK_URL` -- not set yet. dez is sending a music track separately; once you send it, I'll host it somewhere fetchable and set this secret.
- [ ] Confirm the Buffer channel name for @spongebob_prime_ once it's connected in the new Buffer account -- `scripts/main.py` currently expects the channel name `spongebob_prime_`. If Buffer shows a different name/handle for the connected account, `CHANNELS` in `scripts/main.py` needs to match it exactly.
- [ ] First test run -- `posts_per_day` is set to 1 in the state file for the first test run (same process the other niches went through). Once a run succeeds end-to-end, bump it to 2 (your requested rate).
- [ ] After a successful test, the daily cron will keep it running automatically at 2 posts/day.

## Notes

- Clips are 10 seconds (Hailuo 2.3 `duration=10`), not 6s like the other niches.
- Posting cadence: 2/day once confirmed working, spaced 12 hours apart.
- Hashtags: `#lightfantasy #fantasy #knight #fantasyart #aiart`
- TikTok only -- no Instagram or YouTube cross-posting for this account.

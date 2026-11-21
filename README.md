# gta6-meme-x

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/yogiekw/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/yogiekw/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for make.fun's **Post a GTA 6 meme on X** (gta6-meme-x-01).

The joke: everyone waited **13 years** for GTA 6 (GTA V came out in 2013) —
and while we waited, my AI agent was out there making money on make.fun.
The picture is an original Vice City-style illustration: a laughing outlaw
couple speeding down a neon boulevard in a pink convertible, with make.fun's
white ghost mascot riding along in the back seat, magenta star coin in hand.

- Top caption: **WAITED 13 YEARS FOR GTA 6**
- Bottom caption: **MY AI AGENT MADE MONEY ON MAKE.FUN**

An AI judge compares the posts two at a time; the top 50 share $500 in USDC.
Likes, reposts, replies and views never count.

## The meme

- `meme.png` — the meme itself (1080×1080, PNG), as posted on X.
- `compose_meme.py` — the script that built it (PIL): base scene generated
  in-session, official make.fun press-kit ghost pasted into the back seat,
  captions in DejaVu Sans Bold with a black stroke.
- `assets/` — the generated base scene and the official ghost mark.
- `CREATIVE.md` — the creative decision: the moment, the hook, the joke and
  the pitch, as decided in the session that made the meme.
- `POSTING.md` — the exact post text and steps to publish it on X.

## The post

Posted on X from a public account, with the meme as its first picture. The
post's text carries the bounty link, the play code and @makefunai, and tells
readers that people and their AI agents earn money on make.fun. `POST.json`
names the post's address; `main.ts` (Node 22, standard library only) copies
`POST.json` to `/output/POST.json`, which is all the program has to do.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>

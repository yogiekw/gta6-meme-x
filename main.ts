// GTA 6 meme entry for make.fun's gta6-meme-x-01 (Node 22, standard library only).
//
// The entry is the X post itself: the agent makes a GTA 6 meme with make.fun's
// ghost in the picture, it is posted on X from a public account with make.fun
// (a link or written out) and/or @makefunai plus the play code in its text,
// POST.json names the post, and the house reads the post from X (its first
// picture and its text) and hands it to the AI judge. Nothing this program
// writes about the post is judged.
//
// The program copies POST.json from the repository root to /output/POST.json,
// where the gate reads it. That is all it has to do. Before copying it reads
// the file and checks it is a JSON object naming a post address, so a broken
// or placeholder POST.json fails loudly here instead of silently handing the
// gate an unusable file. It is deterministic: two runs write the same bytes.
// Run it locally with:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const postPath = join(BOT_DIR, 'POST.json');
let post;
try {
  post = JSON.parse(readFileSync(postPath, 'utf8'));
} catch (err) {
  console.error(`POST.json could not be read from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
if (typeof post !== 'object' || post === null || typeof post.url !== 'string' || !post.url.startsWith('https://')) {
  console.error('POST.json must be a JSON object with a url string, e.g. {"url": "https://x.com/<handle>/status/<id>"}');
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(postPath, join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}

# TrexMemes — Project Notes

## Concept
A static page exploring the eternal question: **"How many <small animal> would it take to kill a <big animal>?"**
Ten matchups spanning living, extinct, and mythical animals. Each matchup gets:
1. A title
2. A detailed (pseudo-)scientific analysis with a final number
3. An AI-generated battle image (OpenAI `gpt-image-2`, medium quality, landscape 1536x1024)

## The Matchups (original ten)
1. House Cats vs. Tyrannosaurus rex
2. Honey Badgers vs. Woolly Mammoth
3. Chickens vs. Velociraptor
4. Brown Rats vs. Smilodon (Saber-Toothed Cat)
5. Red-Bellied Piranhas vs. Megalodon
6. Army Ants vs. Fire-Breathing Dragon
7. Corgis vs. Griffin
8. Grey Squirrels vs. Lernaean Hydra
9. Emperor Penguins vs. Kraken
10. Mallard Ducks vs. Paraceratherium

## Technical Plan
- `generate_images.py` — calls OpenAI Images API (`gpt-image-2`, quality=medium, size=1536x1024), saves to `images/`
- `index.html` — self-contained static page: title, analysis, image per matchup
- Work happens directly on `main`, committing at each milestone

## Log
- Created repo skeleton and this notes file; picked the ten matchups.
- Smoke-tested the OpenAI Images API: `gpt-image-2` accepted, returns b64 PNG at 1536x1024.
- Wrote `generate_images.py` (3 concurrent workers, retries, skip-if-exists) and ran it:
  all 10 images generated successfully, ~3 MB each, 1536x1024 landscape, medium quality.
- Wrote `index.html`: dark parchment-style theme, one card per matchup with title,
  "tale of the tape" stat line, verdict badge, three-paragraph analysis, and the image.
- Added a lightbox: clicking any battle image opens it in a modal (dimmed overlay,
  caption, close button). On mobile (<=700px) the modal is true full-screen with an
  opaque background and `object-fit: contain`. Closes via backdrop click, the X
  button, or Escape; images are keyboard-focusable and body scroll is locked while
  open. Verified with Playwright at desktop (1280x800) and mobile (390x844) sizes.
- Added five more matchups (11-15: geese/Cyclops, hedgehogs/Basilisk, otters/Mosasaurus,
  guinea pigs/Titanoboa, hummingbirds/Roc). Per request these use a briefer, bulleted
  analysis format instead of the three-paragraph essays; same card layout and images
  (gpt-image-2, medium, 1536x1024). Lightbox picks them up automatically since it
  binds to all `figure img` elements.

## Final Verdicts
| # | Matchup | Verdict |
|---|---------|---------|
| 1 | House cats vs. T. rex | ~2,500 cats |
| 2 | Honey badgers vs. Woolly mammoth | ~120 badgers |
| 3 | Chickens vs. Velociraptor | ~5 chickens |
| 4 | Brown rats vs. Smilodon | ~1,000 rats |
| 5 | Piranhas vs. Megalodon | ~15,000 piranhas |
| 6 | Army ants vs. Dragon | ~2,500,000 ants |
| 7 | Corgis vs. Griffin | ~40 corgis |
| 8 | Squirrels vs. Lernaean Hydra | ~800 squirrels |
| 9 | Emperor penguins vs. Kraken | ~5,000 penguins |
| 10 | Mallard ducks vs. Paraceratherium | ~50,000 ducks |
| 11 | Canada geese vs. Cyclops | ~30 geese |
| 12 | Hedgehogs vs. Basilisk | ~200 hedgehogs |
| 13 | Sea otters vs. Mosasaurus | ~350 otters |
| 14 | Guinea pigs vs. Titanoboa | ~3,000 guinea pigs |
| 15 | Hummingbirds vs. Roc | ~1,500 hummingbirds |

## Analysis Methodology (loosely)
Each verdict weighs: mass ratio, the giant's kill rate against swarming attackers,
the small animal's ability to reach a genuine vulnerability (eyes, gills, tendons,
airways, or logistics like food/water/sleep), stamina asymmetry between an
individual and a rotating swarm, and expected casualty rates with a reserve margin.

# TrexMemes — Project Notes

## Concept
A static page exploring the eternal question: **"How many <small animal> would it take to kill a <big animal>?"**
Ten matchups spanning living, extinct, and mythical animals. Each matchup gets:
1. A title
2. A detailed (pseudo-)scientific analysis with a final number
3. An AI-generated battle image (OpenAI `gpt-image-2`, medium quality, landscape 1536x1024)

## The Ten Matchups
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

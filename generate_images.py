#!/usr/bin/env python3
"""Generate battle images for all ten matchups via the OpenAI Images API.

Uses gpt-image-2, medium quality, landscape (1536x1024). Reads the API key
from the OPENAI_API_KEY environment variable and writes PNGs into images/.
Skips images that already exist, so it can be re-run safely.
"""
import base64
import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

API_URL = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-2"
SIZE = "1536x1024"
QUALITY = "medium"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

STYLE = (
    "Epic dramatic wide-angle battle scene, painterly digital art with rich "
    "lighting and dust, motion and chaos, slightly humorous tone. "
)

PROMPTS = {
    "cats_vs_trex": STYLE + (
        "A furious Tyrannosaurus rex in a prehistoric valley being swarmed by "
        "hundreds of ordinary house cats of many colors, cats climbing its tail "
        "and back and leaping from rocks, the T. rex roaring."
    ),
    "honeybadgers_vs_mammoth": STYLE + (
        "A giant woolly mammoth on a snowy ice-age tundra surrounded by a pack "
        "of fearless honey badgers charging from all sides, some latched onto "
        "its legs and trunk, snow flying."
    ),
    "chickens_vs_velociraptor": STYLE + (
        "A single turkey-sized feathered Velociraptor in a desert cornered by a "
        "small angry mob of farm chickens flapping and pecking, feathers "
        "everywhere, barnyard fence in the background."
    ),
    "rats_vs_smilodon": STYLE + (
        "A snarling saber-toothed cat (Smilodon) in a rocky ice-age landscape "
        "engulfed by a huge swarming tide of brown rats pouring over rocks "
        "toward it from every direction."
    ),
    "piranhas_vs_megalodon": STYLE + (
        "Underwater scene: an enormous Megalodon shark surrounded by a "
        "glittering storm of thousands of red-bellied piranhas attacking in a "
        "spiraling school, rays of light from the surface."
    ),
    "ants_vs_dragon": STYLE + (
        "A huge fire-breathing dragon on a scorched volcanic plain covered by "
        "endless dark rivers of army ants climbing its legs, wings and tail, "
        "the dragon blasting flames at the ground."
    ),
    "corgis_vs_griffin": STYLE + (
        "A majestic griffin with eagle head and lion body on a castle "
        "courtyard, mobbed by dozens of determined corgis jumping and barking, "
        "some in tiny knight helmets, banners flying."
    ),
    "squirrels_vs_hydra": STYLE + (
        "A many-headed serpentine Lernaean Hydra rising from a misty swamp, "
        "attacked by an army of grey squirrels leaping between its heads from "
        "overhanging trees, acorns raining down."
    ),
    "penguins_vs_kraken": STYLE + (
        "A colossal kraken with massive tentacles erupting from icy Antarctic "
        "waters, battled by a huge colony of emperor penguins sliding on ice "
        "floes and diving in coordinated waves."
    ),
    "ducks_vs_paraceratherium": STYLE + (
        "A towering Paraceratherium, the largest land mammal ever, standing in "
        "an ancient floodplain while an immense flock of mallard ducks mobs it "
        "from the air and water, quacking chaos."
    ),
}


def generate(name: str, prompt: str) -> str:
    out_path = os.path.join(OUT_DIR, f"{name}.png")
    if os.path.exists(out_path):
        return f"skip {name} (exists)"
    body = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "size": SIZE,
        "quality": QUALITY,
        "n": 1,
    }).encode()
    req = urllib.request.Request(API_URL, data=body, headers={
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json",
    })
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                data = json.load(resp)
            raw = base64.b64decode(data["data"][0]["b64_json"])
            with open(out_path, "wb") as f:
                f.write(raw)
            return f"ok   {name} ({len(raw)} bytes)"
        except Exception as e:  # noqa: BLE001 - retry any transient failure
            last_err = e
    return f"FAIL {name}: {last_err}"


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    failures = 0
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(generate, n, p): n for n, p in PROMPTS.items()}
        for fut in as_completed(futures):
            result = fut.result()
            print(result, flush=True)
            if result.startswith("FAIL"):
                failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

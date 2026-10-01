"""
Scene bank for the light-fantasy video pipeline (@spongebob_prime_).

v4 -- second reset. v3 (intimate knight moments -- reading, feeding
animals, etc.) was closer but dez still called it "typical standard AI
slop" against the reference
(https://www.tiktok.com/@clawenai/video/7499162427452296490). Two test
stills were generated to isolate the fix: (1) a grimy, worn-armor
knight in a WIDE zoomed-out village square (full figure + surrounding
environment, not a tight medium shot), (2) a beautiful quiet hillside
town with no knight at all. dez picked #1 ("first one") and confirmed
the animated test of it (same grimy knight, camera zooming OUT to
reveal more of the square, verified sharp with no blur throughout).

v4 formula for every scene, no exceptions:

1. ZOOMED OUT / WIDE COMPOSITION. Full figure (when there is one) plus
   a real sense of the surrounding place -- buildings, streets, a
   landscape, weather, texture -- never a tight medium/close shot.
   This is the #1 fix from v3: dez explicitly said "more zoomed out."
2. USED, WORN, IMPERFECT DETAIL. When a knight appears, the armor is
   grimy, scratched, dented, dusty, with rust streaks -- never
   pristine or polished. Buildings are weathered, mossy, imperfect.
   Nothing reads as too clean/glossy/CGI-smooth.
3. VARIETY OF SUBJECT. Not every scene needs a knight. Quiet towns,
   villages, landscapes, and architecture on their own are just as
   valid as a knight doing something small and human -- dez explicitly
   said "it dont just have to be with a knight in it. it could be a
   beautiful town."
4. WARM, HAZY, NOSTALGIC LIGHT. Golden hour, soft diffused sunbeams,
   lantern glow, soft mist -- warm and dreamy, muted/desaturated film-
   like color grade, never a vivid HDR/glossy look.
5. SOFT VISIBLE MAGIC woven in lightly where it fits -- drifting
   butterflies or fireflies, floating petals, faint light particles,
   gentle mist -- understated, never a dramatic spell-effect.
6. Photorealistic documentary-style photography (not painted, not
   overly polished), shot on a full-frame DSLR, natural imperfect
   lighting, 9:16 vertical, no text, no watermark.
7. Animation: a fair amount of real movement every time -- camera
   zooming/drifting to reveal more of the environment, PLUS
   environmental motion (leaves, butterflies, smoke, water, foliage)
   and small natural action. The entire clip stays in crisp sharp
   focus throughout -- no motion blur, no soft frames (this is also
   enforced centrally in higgsfield_client.py for every scene).

16 scenes, mixing grimy-knight scenes with knight-free town/landscape
scenes, roughly 12 light / 4 quieter dark-leaning.
"""

SCENES = [
    {
        "title": "grimy knight at the village well",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "weary knight in heavily worn, dented, scratched plate "
            "armor with dried mud and grime caked into the joints and "
            "rust streaks along the edges, sitting on a low stone wall "
            "at the edge of a quiet moss-covered village square, "
            "reading a tattered old book, the full figure visible with "
            "plenty of surrounding environment -- cobblestone ground, "
            "an old stone well, a leaning wooden cart, ivy-covered "
            "walls -- warm hazy late-afternoon sunlight, soft dust "
            "motes and a few drifting leaves in the air, muted "
            "nostalgic film-like color grade, slightly desaturated, "
            "photorealistic documentary photography style, not overly "
            "polished or glossy, natural imperfect lighting, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "The knight slowly turns a page in the "
            "tattered book, his grimy scratched armor catching the "
            "warm light. A few leaves drift down across the cobblestone "
            "square. Distant butterflies flutter near the ivy-covered "
            "wall. Faint dust motes drift through the air. The camera "
            "slowly zooms out and drifts backward, revealing more of "
            "the quiet village square around him -- the stone well, "
            "the wooden cart, the ivy wall. A fair amount of movement "
            "throughout, calm and nostalgic, no text",
    },
    {
        "title": "hillside village at golden hour",
        "has_people": False,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "beautiful small medieval hillside town at golden hour, "
            "stone cottages with thatched and mossy slate roofs "
            "climbing a gentle hill, narrow cobblestone streets, warm "
            "lantern light glowing in a few windows, soft smoke rising "
            "from chimneys, wildflowers growing between the stones, a "
            "few butterflies and birds drifting through the warm hazy "
            "light, distant rolling green hills fading into soft mist, "
            "muted nostalgic film-like color grade, slightly "
            "desaturated, photorealistic documentary photography "
            "style, not overly polished or glossy, natural imperfect "
            "lighting, no people prominent in frame, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "Smoke drifts slowly up from the chimneys "
            "and dissipates into the golden haze. Birds glide slowly "
            "across the sky above the rooftops. A butterfly drifts "
            "past in the foreground. Window lantern light flickers "
            "faintly. The camera slowly drifts forward and down toward "
            "the town, revealing more streets and rooftops. A fair "
            "amount of movement throughout, calm and nostalgic, no "
            "text",
    },
    {
        "title": "grimy knight feeding the fox",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "knight in battered, scratched plate armor with mud and "
            "rust stains kneels at the edge of a misty forest "
            "clearing, full figure visible with the wide clearing and "
            "tall trees around him, a small red fox cautiously eating "
            "from his outstretched gauntlet, soft early-morning light "
            "filtering through the canopy in warm hazy beams, mist "
            "pooling low across the ferns and moss, muted nostalgic "
            "film-like color grade, slightly desaturated, "
            "photorealistic documentary photography style, not overly "
            "polished or glossy, natural imperfect lighting, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "The fox nibbles from the knight's palm then "
            "looks up, ears twitching. Mist drifts and curls slowly "
            "across the clearing floor. Light shafts shift faintly "
            "through the moving canopy above. The camera slowly zooms "
            "out and rises, revealing the full misty clearing and "
            "surrounding trees. A fair amount of movement throughout, "
            "calm and nostalgic, no text",
    },
    {
        "title": "misty harbor town at dawn",
        "has_people": False,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "quiet stone harbor town at dawn, weathered fishing boats "
            "moored along a worn stone quay, narrow buildings with "
            "peeling paint and mossy roofs lining the waterfront, soft "
            "morning mist drifting low over the still water, pale "
            "golden light breaking through, a few gulls in the sky, "
            "muted nostalgic film-like color grade, slightly "
            "desaturated, photorealistic documentary photography "
            "style, not overly polished or glossy, natural imperfect "
            "lighting, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Mist drifts slowly across the still water "
            "and along the quay. Small ripples move across the harbor "
            "surface as the moored boats sway gently. Gulls glide "
            "slowly through the pale sky. The camera slowly drifts "
            "sideways along the waterfront, revealing more of the "
            "harbor. A fair amount of movement throughout, calm and "
            "nostalgic, no text",
    },
    {
        "title": "grimy knight leading his horse through the meadow",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "knight in dented, mud-streaked armor walks slowly through "
            "a vast wildflower meadow at sunset, leading a tired brown "
            "horse by the reins, both small-to-medium in frame against "
            "the huge warm sky and rolling fields, long grass and "
            "wildflowers swaying around them, soft golden light, "
            "muted nostalgic film-like color grade, slightly "
            "desaturated, photorealistic documentary photography "
            "style, not overly polished or glossy, natural imperfect "
            "lighting, 9:16 vertical, no text, no watermark",
        "animate_prompt": "The knight and horse continue walking slowly "
            "through the meadow, grass and wildflowers swaying and "
            "parting around their legs. The horse's mane shifts in the "
            "breeze. Golden light shifts gently as thin clouds drift "
            "overhead. The camera drifts slowly alongside them at a "
            "calm walking pace, wide enough to keep the full landscape "
            "in frame. A fair amount of movement throughout, calm and "
            "nostalgic, no text",
    },
    {
        "title": "mountain village street at twilight",
        "has_people": False,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "narrow cobblestone street in a small stone mountain "
            "village at twilight, a string of small lanterns hung "
            "between weathered buildings, warm light glowing from a "
            "few windows, moss and ivy growing on old stone walls, "
            "distant mountains fading into deep blue dusk behind the "
            "rooftops, muted nostalgic film-like color grade, slightly "
            "desaturated, photorealistic documentary photography "
            "style, not overly polished or glossy, natural imperfect "
            "lighting, no people prominent in frame, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "The hanging lanterns sway gently in the "
            "evening breeze, their light flickering softly across the "
            "cobblestones. Window light flickers faintly. Thin clouds "
            "drift slowly behind the mountains in the deepening dusk. "
            "The camera drifts slowly forward down the street. A fair "
            "amount of movement throughout, calm and nostalgic, no "
            "text",
    },
    {
        "title": "grimy knight resting above the valley",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "knight in scratched, weathered armor sits resting against "
            "an old gnarled tree on a hillside, full figure small in "
            "frame against a vast view of a quiet valley town below, "
            "warm late-afternoon light, soft haze over the distant "
            "rooftops and fields, loose grass and wildflowers around "
            "him, muted nostalgic film-like color grade, slightly "
            "desaturated, photorealistic documentary photography "
            "style, not overly polished or glossy, natural imperfect "
            "lighting, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Grass and loose branches sway gently in the "
            "breeze around the knight as he sits still, looking out "
            "over the valley. Haze drifts slowly over the distant "
            "rooftops below. A few birds cross the sky in the "
            "distance. The camera slowly drifts and zooms out, "
            "revealing more of the valley and town below. A fair "
            "amount of movement throughout, calm and nostalgic, no "
            "text",
    },
    {
        "title": "sunlit orchard town",
        "has_people": False,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "quiet stone town bordered by a sunlit apple orchard in "
            "full bloom, weathered rooftops visible through the "
            "blossoming trees, petals drifting on the breeze, a "
            "narrow dirt path winding between the orchard and the "
            "town wall, warm midday light, muted nostalgic film-like "
            "color grade, slightly desaturated, photorealistic "
            "documentary photography style, not overly polished or "
            "glossy, natural imperfect lighting, no people prominent "
            "in frame, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Blossom petals drift steadily through the "
            "air across the orchard, branches swaying gently in the "
            "breeze. Light shifts and dapples through the moving "
            "leaves. Distant smoke rises faintly from a chimney in the "
            "town. The camera drifts slowly forward along the path "
            "toward the town. A fair amount of movement throughout, "
            "calm and nostalgic, no text",
    },
    {
        "title": "grimy knight at the stable",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "knight in worn, dusty armor stands in an open wooden "
            "stable at the edge of a village, brushing down a horse, "
            "full figure visible with the rustic stable interior and "
            "a view of the village beyond the open doors, warm hazy "
            "late-afternoon light spilling in, straw and dust drifting "
            "in the sunbeams, muted nostalgic film-like color grade, "
            "slightly desaturated, photorealistic documentary "
            "photography style, not overly polished or glossy, "
            "natural imperfect lighting, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "The knight's brush moves slowly along the "
            "horse's flank, the horse shifting its weight and flicking "
            "its tail. Dust and straw drift through the warm sunbeams "
            "spilling through the stable doors. Distant village life "
            "is faintly visible through the opening. The camera slowly "
            "zooms out, revealing more of the stable and the village "
            "beyond. A fair amount of movement throughout, calm and "
            "nostalgic, no text",
    },
    {
        "title": "snow-dusted mountain village",
        "has_people": False,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "small stone mountain village dusted with fresh snow at "
            "dusk, warm light glowing from cottage windows, smoke "
            "rising from chimneys, a narrow snow-covered path winding "
            "between the buildings, steep snowy peaks rising behind "
            "the rooftops, muted nostalgic film-like color grade, "
            "slightly desaturated, photorealistic documentary "
            "photography style, not overly polished or glossy, "
            "natural imperfect lighting, no people prominent in "
            "frame, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Snow falls gently over the village, "
            "settling on the rooftops and path. Smoke drifts slowly "
            "from the chimneys into the cold air. Window light "
            "flickers softly. The camera drifts slowly forward and "
            "down toward the village, revealing more of the snowy "
            "street. A fair amount of movement throughout, calm and "
            "nostalgic, no text",
    },
    {
        "title": "grimy knight on the battlements",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "knight in dented, weathered armor sits on an old stone "
            "town wall at sunset, legs hanging over the edge, full "
            "figure visible with a wide view of the town's rooftops "
            "and distant hills spread out below him, warm orange "
            "light, loose dust and a few birds drifting past, muted "
            "nostalgic film-like color grade, slightly desaturated, "
            "photorealistic documentary photography style, not overly "
            "polished or glossy, natural imperfect lighting, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "The knight's cloak shifts gently in the "
            "evening breeze as he looks out over the town. Birds drift "
            "slowly across the sunset sky below him. Smoke rises "
            "faintly from distant chimneys. The camera slowly zooms "
            "out and drifts sideways along the wall, revealing more of "
            "the town and hills. A fair amount of movement throughout, "
            "calm and nostalgic, no text",
    },
    {
        "title": "river village at golden hour",
        "has_people": False,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "quiet stone village straddling a slow river at golden "
            "hour, an old arched stone bridge connecting both banks, "
            "weathered buildings with mossy roofs along the water, "
            "small wooden boats tied up at the bank, soft warm light "
            "reflecting on the water, a few fireflies beginning to "
            "glow in the shadows, muted nostalgic film-like color "
            "grade, slightly desaturated, photorealistic documentary "
            "photography style, not overly polished or glossy, "
            "natural imperfect lighting, no people prominent in "
            "frame, 9:16 vertical, no text, no watermark",
        "animate_prompt": "The river flows gently beneath the stone "
            "bridge, the boats swaying slightly at their moorings. "
            "Fireflies drift and pulse softly in the shadows along the "
            "bank. Light reflects and shifts on the moving water "
            "surface. The camera drifts slowly across the bridge, "
            "revealing more of the village along the river. A fair "
            "amount of movement throughout, calm and nostalgic, no "
            "text",
    },
    {
        "title": "grimy knight at the forest shrine",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "knight in battered, grime-streaked armor kneels before a "
            "small moss-covered stone shrine deep in a misty forest, "
            "full figure visible with the wide clearing, ancient trees "
            "and tangled roots around him, soft cool blue-grey light "
            "filtering through the canopy, faint mist pooling low "
            "across the ground, somber but tender mood, not graphic, "
            "muted nostalgic film-like color grade, slightly "
            "desaturated, photorealistic documentary photography "
            "style, not overly polished or glossy, natural imperfect "
            "lighting, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Mist drifts slowly across the clearing "
            "around the shrine and the kneeling knight. Light shifts "
            "faintly through the moving canopy above. A few leaves "
            "drift down from the ancient trees. The camera slowly "
            "zooms out, revealing the full clearing and the tangled "
            "roots and trees around the shrine. A fair amount of "
            "movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "abandoned watchtower at dusk",
        "has_people": False,
        "mood": "dark",
        "still_prompt": "Wide cinematic photograph, zoomed out: a "
            "crumbling stone watchtower standing alone on a windswept "
            "hillside at dusk, moss and ivy climbing its weathered "
            "walls, a few birds circling above, distant rolling hills "
            "fading into deep blue twilight, a faint warm glow from a "
            "single lit window near the top, somber but peaceful mood, "
            "not graphic, muted nostalgic film-like color grade, "
            "slightly desaturated, photorealistic documentary "
            "photography style, not overly polished or glossy, "
            "natural imperfect lighting, no people prominent in "
            "frame, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Tall grass sways steadily around the base "
            "of the tower in the wind. Birds circle slowly above the "
            "tower. The lit window flickers faintly. Thin clouds drift "
            "across the darkening sky. The camera slowly drifts "
            "forward and rises toward the tower, revealing more of the "
            "windswept hillside. A fair amount of movement throughout, "
            "somber and nostalgic, no text",
    },
    {
        "title": "grimy knight crossing the old bridge",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Wide cinematic photograph, zoomed out: a lone "
            "knight in dented, rust-streaked armor walks slowly across "
            "a long weathered stone bridge over a misty river at dusk, "
            "small-to-medium in frame against the wide river valley "
            "and fading blue light, a sheathed sword at his hip, mist "
            "rising off the water below, somber but tender mood, not "
            "graphic, muted nostalgic film-like color grade, slightly "
            "desaturated, photorealistic documentary photography "
            "style, not overly polished or glossy, natural imperfect "
            "lighting, 9:16 vertical, no text, no watermark",
        "animate_prompt": "The knight walks slowly across the bridge, "
            "cloak shifting gently in the breeze. Mist drifts and "
            "rises steadily off the river below. Thin clouds pass "
            "overhead in the fading light. The camera tracks slowly "
            "alongside him at a calm walking pace, wide enough to keep "
            "the full bridge and valley in frame. A fair amount of "
            "movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "quiet ruins overlooking the coast",
        "has_people": False,
        "mood": "dark",
        "still_prompt": "Wide cinematic photograph, zoomed out: the "
            "crumbling stone ruins of an old coastal fortress on a "
            "windswept cliff at dusk, moss and wildflowers growing "
            "through the broken walls, the sea stretching out far "
            "below under a soft fading sky, a few birds gliding on the "
            "wind, somber but peaceful mood, not graphic, muted "
            "nostalgic film-like color grade, slightly desaturated, "
            "photorealistic documentary photography style, not overly "
            "polished or glossy, natural imperfect lighting, no "
            "people prominent in frame, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "Wildflowers and grass sway steadily in the "
            "sea wind around the broken walls. Birds glide slowly "
            "along the cliff edge. Waves move faintly far below. Thin "
            "clouds drift across the fading sky. The camera slowly "
            "drifts forward toward the cliff edge, revealing more of "
            "the ruins and the sea beyond. A fair amount of movement "
            "throughout, somber and nostalgic, no text",
    },
]

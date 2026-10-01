"""
Scene bank for the light-fantasy video pipeline (@spongebob_prime_).

v3 -- complete reset based on dez's reference
(https://www.tiktok.com/@clawenai/video/7499162427452296490,
hashtags #lightfantasy #brightfantasy #dreamcore #nostalgic). The v2
bank (wide epic landscapes, dramatic skies, knights fighting/charging)
was the wrong genre entirely -- dez called it "AI slop" and said the
real "light fantasy" trend is the opposite: quiet, intimate, nostalgic
moments. A lone knight in full armor doing something small and tender
(reading, resting, tending an animal) under warm hazy golden light,
with soft nature magic -- butterflies, fireflies, drifting petals --
rather than loud dramatic effects. Confirmed against a test
still+animation (knight reading under a tree, butterflies drifting)
before this full rebuild: "yes stuff like that is the right way. just
animated with a fair amount of movement."

v3 formula for every scene, no exceptions:

1. INTIMATE MEDIUM-SHOT COMPOSITION. The knight (or occasional second
   figure/animal companion) fills a meaningful part of the frame --
   not a tiny speck in a vast landscape, not a tight face close-up.
   Think "quiet portrait of a moment," not "movie poster."
2. WARM, HAZY, NOSTALGIC LIGHT. Golden hour, soft diffused sunbeams
   through leaves/mist, firelight, lantern glow, or soft moonlight --
   always warm and dreamy, never harsh or cold, never a stormy/epic sky.
3. A SMALL TENDER HUMAN MOMENT, not action or combat. Resting, reading,
   feeding or petting an animal, tending flowers, playing music,
   watching a sunset, warming hands by a fire -- the charm is the
   contrast between the hardened armor and the gentle, vulnerable act.
4. SOFT VISIBLE MAGIC woven in lightly -- drifting butterflies or
   fireflies, floating petals or embers, faint glowing pollen or light
   particles, gentle mist -- never a dramatic spell-effect or sky event.
5. Photorealistic (not painted/illustrated), shot on a full-frame DSLR
   with a soft/shallow depth of field, warm film-like color grade,
   9:16 vertical, no text, no watermark.
6. Animation: a fair amount of real movement every time -- a slow
   cinematic camera push-in or gentle drift, PLUS lots of environmental
   motion (butterflies/fireflies swirling, embers or petals drifting,
   grass or leaves stirring in a breeze, water rippling, fire
   flickering) and a small character action (turning a page, a hand
   reaching out, a head turning). Never fully locked-off/static, never
   a fast dramatic action-tracking shot -- calm but clearly alive.

17 scenes, 13 light / 4 quieter dark-leaning (still tender and
nostalgic, never graphic -- per dez's original light-mostly-with-dark-
breaks direction), covering a range of settings and small moments so
the daily rotation doesn't repeat.
"""

SCENES = [
    {
        "title": "reading under the blossom tree",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a lone "
            "knight in full ornate plate armor sits peacefully beneath "
            "a large tree, gently reading an old leather-bound book "
            "held in his gauntleted hands, warm golden-hour sunlight "
            "streaming through the leaves above in soft hazy diffused "
            "rays, dozens of small orange butterflies drifting through "
            "the air around him, some landing near the pages, soft "
            "bokeh, fallen leaves and wildflowers on the ground, "
            "tender and quiet mood, shot on a full-frame DSLR with a "
            "shallow depth of field, warm dreamy nostalgic color "
            "grade, medium shot centered on the knight under the tree "
            "canopy, 9:16 vertical, no text, no watermark",
        "animate_prompt": "The knight slowly turns a page in the book. "
            "Butterflies swirl and flutter in flowing paths around him, "
            "some landing on his shoulder or the book then taking "
            "flight again. Warm sunlight shifts and flickers through "
            "the moving leaves as a gentle breeze stirs the branches "
            "and scatters loose petals through the air. The camera "
            "slowly pushes in and drifts slightly to the side. A fair "
            "amount of movement throughout, calm and dreamy, no text",
    },
    {
        "title": "feeding the fox",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight in "
            "weathered plate armor kneels in a misty forest clearing, "
            "gauntlet held out flat with a piece of bread as a small "
            "red fox cautiously eats from his palm, soft early-morning "
            "light filtering through the trees in warm hazy beams, "
            "fireflies glowing faintly in the shadows nearby, dew on "
            "the ferns and moss, tender and gentle mood, shot on a "
            "full-frame DSLR with a shallow depth of field, warm "
            "nostalgic color grade, medium shot, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "The fox nibbles from the knight's palm then "
            "looks up at him, ears twitching, tail flicking gently. "
            "Fireflies drift and pulse softly in the misty shadows "
            "behind them, mist curling slowly along the forest floor. "
            "The camera drifts slowly closer and tilts slightly down "
            "toward the fox. A fair amount of movement throughout, "
            "calm and dreamy, no text",
    },
    {
        "title": "campfire embers",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight in "
            "dented plate armor sits cross-legged beside a small "
            "crackling campfire at dusk, firelight warmly lighting his "
            "armor and the ground around him, glowing embers rising "
            "into the darkening sky, a faint first star visible above, "
            "soft smoke drifting, tender and peaceful mood, shot on a "
            "full-frame DSLR with a shallow depth of field, warm "
            "nostalgic color grade, medium shot, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "The campfire flickers and crackles, flames "
            "dancing and casting shifting warm light across the "
            "knight's armor. Embers rise steadily into the dusk sky, "
            "swirling gently in the rising heat. The knight slowly "
            "leans forward and warms his gauntlets over the flame. The "
            "camera drifts slowly in a slight arc around the fire. A "
            "fair amount of movement throughout, calm and dreamy, no "
            "text",
    },
    {
        "title": "stream at dawn",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "kneels beside a gentle forest stream at dawn, having "
            "removed one gauntlet to cup clear water in his bare hand, "
            "dappled golden sunlight breaking through the canopy above "
            "onto the water, dragonflies hovering over the surface, "
            "soft mist rising off the stream, moss-covered stones, "
            "tender and quiet mood, shot on a full-frame DSLR with a "
            "shallow depth of field, warm nostalgic color grade, "
            "medium shot, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Water ripples gently as it flows past the "
            "knight's cupped hand, catching the dappled sunlight in "
            "small sparkles. Dragonflies dart and hover over the "
            "stream's surface. Mist curls slowly upward. The camera "
            "slowly pushes in toward the knight's hand and the water. "
            "A fair amount of movement throughout, calm and dreamy, no "
            "text",
    },
    {
        "title": "lanterns on the lake",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight in "
            "full armor crouches at the edge of a still lake at "
            "twilight, gently setting a small glowing paper lantern "
            "onto the water, dozens of lanterns already drifting out "
            "across the lake reflecting warm golden light, soft purple "
            "dusk sky above, fireflies mixing with the lantern glow, "
            "tender and peaceful mood, shot on a full-frame DSLR with "
            "a shallow depth of field, warm nostalgic color grade, "
            "medium shot, 9:16 vertical, no text, no watermark",
        "animate_prompt": "The lantern drifts gently away from the "
            "knight's hand onto the water's rippling surface, joining "
            "the others already floating across the lake. Fireflies "
            "drift lazily through the air. The warm lantern light "
            "flickers and reflects on the gently rippling water. The "
            "camera drifts slowly backward and up, revealing more "
            "lanterns on the lake. A fair amount of movement "
            "throughout, calm and dreamy, no text",
    },
    {
        "title": "flowers in the horse's mane",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight in "
            "polished armor stands beside a white horse in a sunlit "
            "wildflower field, gently braiding small wildflowers into "
            "the horse's mane, warm golden light, petals and seed-fluff "
            "drifting on the breeze, the horse's eyes soft and calm, "
            "tender and warm mood, shot on a full-frame DSLR with a "
            "shallow depth of field, warm nostalgic color grade, "
            "medium shot, 9:16 vertical, no text, no watermark",
        "animate_prompt": "The knight's hands continue gently weaving "
            "flowers into the horse's mane as it swishes its tail and "
            "shifts its weight. Wildflowers and grass sway in the "
            "breeze, petals and fluff drifting past. The horse turns "
            "its head slightly toward the knight. The camera drifts "
            "slowly to the side in a gentle arc. A fair amount of "
            "movement throughout, calm and dreamy, no text",
    },
    {
        "title": "sunset with the wolf",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight in "
            "weathered armor sits on a grassy hillside at sunset, one "
            "hand resting on the back of a large grey wolf lying beside "
            "him, both facing the warm orange horizon, soft golden-"
            "pink sky, tall grass swaying gently, tender and quiet "
            "mood, shot on a full-frame DSLR with a shallow depth of "
            "field, warm nostalgic color grade, medium shot, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "The wolf's fur and ears shift slightly as it "
            "breathes, tail giving a slow gentle sweep. The knight's "
            "hand strokes the wolf's back once. Tall grass sways "
            "steadily in the breeze as the sunset colors shift and "
            "deepen slightly. The camera drifts slowly in from behind "
            "them toward the horizon. A fair amount of movement "
            "throughout, calm and dreamy, no text",
    },
    {
        "title": "flute by the waterfall",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "sits on a moss-covered rock beside a small waterfall, "
            "playing a simple wooden flute, fine mist drifting from "
            "the falling water, soft sunbeams piercing the mist, moss "
            "and ferns around him, tender and peaceful mood, shot on a "
            "full-frame DSLR with a shallow depth of field, warm "
            "nostalgic color grade, medium shot, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "The waterfall flows continuously behind the "
            "knight, mist drifting and catching the sunbeams in soft "
            "shifting shafts of light. The knight's fingers move gently "
            "over the flute as he plays. The camera slowly pushes in "
            "and drifts slightly upward through the mist. A fair "
            "amount of movement throughout, calm and dreamy, no text",
    },
    {
        "title": "tending the glowing garden",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "kneels in a small cottage garden at dusk, carefully "
            "watering a bed of softly glowing bioluminescent flowers "
            "with a clay jug, warm lantern light spilling from a "
            "nearby window, fireflies and drifting pollen catching the "
            "light, tender and cozy mood, shot on a full-frame DSLR "
            "with a shallow depth of field, warm nostalgic color "
            "grade, medium shot, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Water pours gently from the jug onto the "
            "glowing flowers, which pulse softly brighter as droplets "
            "land on them. Fireflies and pollen drift lazily through "
            "the warm lantern light. The knight's hand adjusts a "
            "drooping stem. The camera drifts slowly closer to the "
            "flowerbed. A fair amount of movement throughout, calm and "
            "dreamy, no text",
    },
    {
        "title": "releasing the dove",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "stands on a sunlit hilltop at sunrise, arms raised gently "
            "as a white dove lifts off from his open gauntlets into "
            "the golden morning sky, soft warm light, loose feathers "
            "drifting on the breeze, mist in the valley below, tender "
            "and hopeful mood, shot on a full-frame DSLR with a "
            "shallow depth of field, warm nostalgic color grade, "
            "medium shot, 9:16 vertical, no text, no watermark",
        "animate_prompt": "The dove's wings beat as it lifts off the "
            "knight's gauntlets and rises into the sky, feathers "
            "drifting slowly down past him. Morning mist shifts gently "
            "in the valley below. The knight tilts his head up to "
            "watch the dove go. The camera tilts and drifts slowly "
            "upward following the dove. A fair amount of movement "
            "throughout, calm and dreamy, no text",
    },
    {
        "title": "snowfall by the lantern",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "leans against a tree in a snow-dusted pine forest at "
            "dusk, a small lit lantern resting beside him in the snow, "
            "soft snow falling gently, warm lantern glow contrasting "
            "the cool blue twilight, his breath faintly visible, "
            "tender and cozy mood, shot on a full-frame DSLR with a "
            "shallow depth of field, warm nostalgic color grade, "
            "medium shot, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Snow falls steadily and gently around the "
            "knight, flakes catching the warm lantern light as they "
            "drift down. His breath fogs faintly in the cold air. The "
            "lantern flame flickers softly. The camera drifts slowly "
            "in and slightly to the side. A fair amount of movement "
            "throughout, calm and dreamy, no text",
    },
    {
        "title": "fireflies over the valley",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "sits cross-legged on a cliff edge at dusk, watching "
            "thousands of fireflies swarm and glow softly in the "
            "valley below like a sea of warm light, deep blue twilight "
            "sky above, soft wind in his hair where his helmet rests "
            "beside him, tender and awestruck mood, shot on a full-"
            "frame DSLR with a shallow depth of field, warm nostalgic "
            "color grade, medium shot, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "Fireflies pulse and drift in slow glowing "
            "waves through the valley below, shifting brightness. The "
            "knight's hair and cloak stir gently in the breeze as he "
            "watches, still. The camera drifts slowly forward toward "
            "the cliff edge, taking in more of the glowing valley. A "
            "fair amount of movement throughout, calm and dreamy, no "
            "text",
    },
    {
        "title": "apples in the wheat field",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "stands in a golden wheat field at sunset, feeding an "
            "apple to a white horse from his open palm, the wheat "
            "swaying in long warm light, soft dust catching the sun, "
            "tender and warm mood, shot on a full-frame DSLR with a "
            "shallow depth of field, warm nostalgic color grade, "
            "medium shot, 9:16 vertical, no text, no watermark",
        "animate_prompt": "The horse leans forward and takes the apple "
            "gently from the knight's palm, chewing as its ears flick. "
            "Golden wheat sways steadily in the breeze all around "
            "them, dust motes drifting through the low sunlight. The "
            "camera drifts slowly sideways past them. A fair amount of "
            "movement throughout, calm and dreamy, no text",
    },
    {
        "title": "quiet watch at the fallen sword",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Intimate photorealistic portrait: a lone "
            "knight kneels in a misty moonlit clearing beside a sword "
            "planted upright in the ground as a marker, head bowed, "
            "one gauntlet resting on the pommel, soft cold blue "
            "moonlight through thin mist, a few fireflies glowing "
            "faintly nearby, somber but tender mood, not graphic, shot "
            "on a full-frame DSLR with a shallow depth of field, "
            "muted nostalgic color grade, medium shot, 9:16 vertical, "
            "no text, no watermark",
        "animate_prompt": "Mist drifts slowly across the clearing "
            "around the knight, fireflies pulsing faintly in the "
            "shadows. The knight's hand tightens gently on the sword's "
            "pommel, head still bowed. Moonlight shifts faintly as "
            "thin clouds pass overhead. The camera drifts slowly and "
            "quietly closer. A fair amount of movement throughout, "
            "somber and dreamy, no text",
    },
    {
        "title": "blue flame in the snow",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "crouches in a snowy twilight clearing, warming his bare "
            "hands over a small magical blue flame cupped in his "
            "palms, a deer watching quietly from the treeline, cool "
            "blue-toned snow contrasted with the warm flame glow, "
            "somber but tender mood, not graphic, shot on a full-"
            "frame DSLR with a shallow depth of field, muted nostalgic "
            "color grade, medium shot, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "The small blue flame flickers and dances in "
            "the knight's cupped hands, casting a soft shifting glow "
            "on his face. Snow falls gently around him. The deer shifts "
            "its weight at the treeline, ears turning. The camera "
            "drifts slowly in toward the flame. A fair amount of "
            "movement throughout, somber and dreamy, no text",
    },
    {
        "title": "ruins by firelight",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "sits inside a crumbling stone ruin at night, carefully "
            "polishing his sword by the light of a small fire, warm "
            "firelight flickering against moss-covered broken walls, "
            "embers drifting upward through a gap in the roof toward "
            "a starry sky, somber but peaceful mood, not graphic, shot "
            "on a full-frame DSLR with a shallow depth of field, muted "
            "nostalgic color grade, medium shot, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "The fire flickers and crackles, casting "
            "shifting warm light across the ruin's broken walls. "
            "Embers rise steadily through the gap in the roof toward "
            "the stars. The knight's cloth moves slowly along the "
            "blade as he polishes it. The camera drifts slowly upward "
            "following the embers. A fair amount of movement "
            "throughout, somber and dreamy, no text",
    },
    {
        "title": "cherry blossom walk",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Intimate photorealistic portrait: a knight "
            "walks slowly through a quiet cherry blossom grove at "
            "dusk, petals swirling thickly around him in the soft "
            "wind, faint cool blue-pink twilight light, a hand resting "
            "on the pommel of a sheathed sword at his side, somber but "
            "tender mood, not graphic, shot on a full-frame DSLR with "
            "a shallow depth of field, muted nostalgic color grade, "
            "medium shot, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Cherry blossom petals swirl thickly through "
            "the air around the knight as he walks slowly forward, "
            "cloak stirring in the breeze. Branches sway gently "
            "overhead, releasing more petals. The camera tracks slowly "
            "alongside him at a calm walking pace. A fair amount of "
            "movement throughout, somber and dreamy, no text",
    },
]

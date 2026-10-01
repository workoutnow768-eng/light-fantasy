"""
Scene bank for the light-fantasy video pipeline (@spongebob_prime_).

Mainly bright, warm light-fantasy (sunlit meadows, villages, knights,
golden fields) with occasional dark-fantasy breaks (a lantern-lit town
at night, people drinking, torchlit streets) for contrast and variety,
per dez's direction. 20 scenes, roughly 15 light / 5 dark-leaning.

Two things this bank does differently from pallowyn/creepvale/dark-fantasy:

1. Images are PHOTOREALISTIC, not painterly illustration -- shot-on-camera
   detail, real lighting, real texture, not concept art. Every still_prompt
   below is written with specific, concrete detail (named props, exact
   lighting conditions, particular actions mid-motion) rather than a
   generic template, because this account already has 15k followers and
   needs to look considerably better than a cold-start test account.

2. Animation is NOT the "camera locked, only ambient elements drift"
   style used elsewhere. dez was explicit: no more "someone standing
   still holding a torch with a flame" or "birds slowly moving in the
   background." Every animate_prompt here asks for real, sustained
   camera motion -- many written as true first-person POV (walking,
   running, riding, climbing, as if you are the knight looking through
   their own eyes, with natural handheld sway), others as dynamic
   third-person tracking shots moving alongside or around the subject.
   Nothing in this bank is a static tripod shot.
"""

SCENES = [
    {
        "title": "river crossing at dawn",
        "has_people": True,
        "mood": "light",
        "still_prompt": "First-person point of view: a young armoured "
            "knight's own gauntleted hands and the top of his breastplate "
            "visible at the bottom of frame, wading through a shallow "
            "sunlit river at dawn, clear water parting around his legs "
            "and catching the low golden morning light, smooth river "
            "stones visible beneath the surface, mist rising faintly off "
            "the water, a dense green forest lining the far bank, soft "
            "early sunlight breaking through the tree canopy, photorealistic, "
            "cinematic photography, shot on a DSLR, shallow depth of "
            "field, natural lighting, highly detailed water and fabric "
            "textures, 9:16 vertical, no text, no watermark",
        "animate_prompt": "True first-person POV: the camera moves "
            "forward through the water at walking pace exactly as if "
            "worn on the knight's own head, with a natural handheld bob "
            "and sway on each step, water visibly rippling and parting "
            "around his legs as he wades deeper, mist drifting past, "
            "sunlight flickering through the canopy overhead. Real "
            "sustained forward motion the entire clip, not a static or "
            "locked shot, grounded realistic documentary handheld feel, "
            "no text",
    },
    {
        "title": "market street weave",
        "has_people": True,
        "mood": "light",
        "still_prompt": "First-person point of view walking into a "
            "sunlit cobblestone market street, the knight's own armoured "
            "forearm brushing past a stall of ripe oranges at the edge of "
            "frame, colorful fabric awnings strung overhead casting "
            "dappled shade, a baker pulling bread from an open oven, "
            "children darting between legs, chickens scattering, warm "
            "midday sun flooding the narrow street, photorealistic, "
            "cinematic photography, shot on a DSLR, natural lighting, "
            "highly detailed textures on stone, fabric and produce, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "True first-person POV walking briskly through "
            "the crowded market at a natural human pace, weaving slightly "
            "left and right to pass between stalls and people exactly as "
            "a person would, vendors and shoppers passing close on both "
            "sides, a chicken fluttering out of the way, awning shadows "
            "sweeping across the view as the camera moves beneath them. "
            "Continuous real walking motion with natural handheld sway "
            "the whole clip, no text",
    },
    {
        "title": "cliffside gallop",
        "has_people": True,
        "mood": "light",
        "still_prompt": "A knight in bright polished armor riding a "
            "powerful brown warhorse at a full gallop along a grassy "
            "coastal cliff path, his cloak snapping straight out behind "
            "him in the wind, the horse's mane flying and dust kicking up "
            "from its hooves, a sparkling turquoise sea far below the "
            "cliff edge, bright midday sun, tall blue sky with scattered "
            "clouds, photorealistic, cinematic action photography, shot "
            "on a DSLR with a fast shutter freezing the horse's motion, "
            "natural lighting, highly detailed, 9:16 vertical, no text, "
            "no watermark",
        "animate_prompt": "Dynamic third-person tracking shot running "
            "alongside the galloping horse at matching speed, camera "
            "slightly low and close as if filmed from a horse riding "
            "beside it, the horse's legs pounding the ground, dust and "
            "loose turf kicking up toward the lens, cloak whipping in the "
            "wind, the sea sweeping past in the background the entire "
            "clip. Sustained high-energy tracking motion, not a locked or "
            "static shot, no text",
    },
    {
        "title": "tavern threshold at dusk",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "First-person point of view pushing open a heavy "
            "wooden tavern door from the darkening street outside, one "
            "armoured hand braced against the door, warm orange firelight "
            "and lantern glow spilling out through the widening gap, "
            "silhouettes of patrons visible inside around a long table, "
            "the first few stars appearing in a deep blue dusk sky behind, "
            "a wooden tavern sign creaking on an iron bracket overhead, "
            "photorealistic, cinematic photography, shot on a DSLR, "
            "natural lighting with strong warm/cool contrast, highly "
            "detailed, 9:16 vertical, no text, no watermark",
        "animate_prompt": "True first-person POV: the door swings open "
            "under the knight's own push, camera moving forward through "
            "the doorway from the cool dusk exterior into the warm firelit "
            "interior, the light growing brighter and warmer as the "
            "camera crosses the threshold, sound-suggesting motion like "
            "laughter and clinking mugs implied by the shifting light and "
            "movement inside. Continuous forward motion through the "
            "doorway, not static, no text",
    },
    {
        "title": "night street lanterns",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "First-person point of view walking down a "
            "narrow cobblestone street at night, iron lanterns hanging "
            "from building fronts casting warm pools of light between "
            "deep shadow, a tavern window glowing gold up ahead with "
            "silhouettes of people raising mugs and singing, laundry "
            "lines strung overhead between buildings, a cat slipping "
            "along a doorstep, puddles reflecting the lantern light, "
            "photorealistic, cinematic night photography, shot on a "
            "DSLR, natural low light, highly detailed, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "True first-person POV walking at a relaxed "
            "pace down the lantern-lit street, camera passing through "
            "alternating pools of warm lantern light and shadow with "
            "natural handheld sway, the glowing tavern window growing "
            "larger and the muffled sound of singing implied by figures "
            "swaying inside as the camera approaches. Continuous forward "
            "walking motion the entire clip, no text",
    },
    {
        "title": "waterfall bridge",
        "has_people": True,
        "mood": "light",
        "still_prompt": "First-person point of view crossing a narrow "
            "rope and plank bridge over a roaring waterfall, the "
            "knight's own boots and the edge of the swaying bridge "
            "visible at the bottom of frame, fine mist drifting up from "
            "the falls and catching bright sunlight in a faint rainbow, "
            "lush green cliffs on either side, spray beading on nearby "
            "leaves, bright midday sun, photorealistic, cinematic "
            "photography, shot on a DSLR, natural lighting, highly "
            "detailed water spray and wood grain, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "True first-person POV walking across the "
            "bridge, the planks visibly flexing and the rope bridge "
            "swaying slightly underfoot with each step, mist drifting "
            "past the camera and catching the light, a faint rainbow "
            "shifting in the spray, the waterfall's motion continuous "
            "below. Real sustained forward walking motion with natural "
            "sway the entire clip, not static, no text",
    },
    {
        "title": "forge sparks",
        "has_people": True,
        "mood": "light",
        "still_prompt": "A bare-armed blacksmith mid-swing with a heavy "
            "hammer striking a glowing orange blade on an anvil in an "
            "open-air smithy, a bright shower of sparks frozen in the "
            "air around the point of impact, bright midday sun "
            "streaming through the open sides of the forge shed, a young "
            "armoured knight and two villagers watching from just "
            "outside, tools and horseshoes hanging on the walls, "
            "photorealistic, cinematic action photography, shot on a "
            "DSLR with a fast shutter, natural lighting, highly detailed, "
            "9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic third-person tracking shot circling "
            "quickly around the anvil as the hammer rises and falls, "
            "sparks bursting outward with each strike and scattering "
            "toward the camera, the smith's muscles flexing with the "
            "swing, onlookers shifting to watch. Continuous orbiting "
            "camera motion around the forge the entire clip, energetic "
            "and handheld, not static, no text",
    },
    {
        "title": "wheat field pursuit",
        "has_people": True,
        "mood": "light",
        "still_prompt": "First-person point of view running through a "
            "vast field of tall golden wheat under bright summer sun, "
            "stalks brushing past on either side of frame and parting "
            "ahead, a distant small figure glimpsed ducking between the "
            "stalks further into the field, tall blue sky with a few "
            "wisps of cloud, dust and loose chaff catching the light, "
            "photorealistic, cinematic action photography, shot on a "
            "DSLR, natural lighting, highly detailed wheat texture, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "True first-person POV running at full pace "
            "through the wheat, camera bouncing with each stride in a "
            "natural handheld running rhythm, stalks whipping past and "
            "parting directly in front of the lens, the distant figure "
            "ahead ducking further out of sight, dust kicked up catching "
            "the sunlight. Continuous fast running motion the entire "
            "clip, high energy, not static, no text",
    },
    {
        "title": "lake dive",
        "has_people": True,
        "mood": "light",
        "still_prompt": "A young man mid-dive off a sun-warmed rock into "
            "a crystal-clear mountain lake, body stretched in the air "
            "just above the water's surface, droplets frozen mid-splash "
            "catching bright sunlight, his light armor and tunic left "
            "folded neatly on the rock behind him, pine-covered hills "
            "reflected in the still water, bright midday sun, "
            "photorealistic, cinematic action photography, shot on a "
            "DSLR with a fast shutter, natural lighting, highly detailed "
            "water droplets, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic third-person tracking shot following "
            "the dive down into the water and back up as he surfaces, "
            "camera moving with the motion from the rock through the air "
            "and into the splash, water droplets flying past the lens, "
            "sunlight glinting off the breaking surface as he emerges "
            "gasping and grinning. Continuous following motion the "
            "entire clip, not a static shot, no text",
    },
    {
        "title": "tavern brawl brewing",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "First-person point of view seated at a crowded "
            "wooden tavern table at night, tankards of ale raised in a "
            "toast close to the camera, firelight from a roaring hearth "
            "flickering warmly across weathered wooden beams, a rowdy "
            "crowd singing and laughing in the background, one patron "
            "leaning back on his stool about to tip over, spilled ale "
            "glistening on the table, photorealistic, cinematic night "
            "photography, shot on a DSLR, warm low light, highly "
            "detailed, 9:16 vertical, no text, no watermark",
        "animate_prompt": "True first-person POV: a tankard rises into "
            "frame as if raised by the knight's own hand for a toast, "
            "clinking against others entering frame from the sides, "
            "firelight flickering and figures swaying and laughing all "
            "around in continuous motion, the leaning stool wobbling "
            "further before frame ends. Sustained lively handheld motion "
            "the entire clip, not static, no text",
    },
    {
        "title": "orchard gallop",
        "has_people": True,
        "mood": "light",
        "still_prompt": "A knight on a pale grey horse galloping through "
            "a blossoming apple orchard in full bloom, white and pink "
            "petals shaken loose from the branches swirling in the air "
            "around horse and rider, dappled bright sunlight breaking "
            "through the blossom canopy, rows of trees stretching into "
            "the distance, bright blue sky, photorealistic, cinematic "
            "action photography, shot on a DSLR with a fast shutter, "
            "natural lighting, highly detailed petals and fur texture, "
            "9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic third-person tracking shot moving "
            "alongside the galloping horse through the orchard rows, "
            "petals shaking loose from branches overhead and swirling "
            "thickly through the air as horse and rider pass beneath "
            "them, dappled light flickering rapidly across the scene. "
            "Continuous fast tracking motion the entire clip, high "
            "energy, not static, no text",
    },
    {
        "title": "archery contest",
        "has_people": True,
        "mood": "light",
        "still_prompt": "The exact moment an arrow is released from a "
            "longbow at a sunlit village fairground, the arrow frozen "
            "mid-flight just leaving the string, a row of straw target "
            "butts downrange with colorful painted rings, a cheering "
            "crowd gathered behind a rope barrier in their best bright "
            "summer clothes, bunting strung between poles, bright midday "
            "sun, photorealistic, cinematic action photography, shot on "
            "a DSLR with a fast shutter, natural lighting, highly "
            "detailed, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic third-person tracking shot following "
            "the arrow's flight from the string toward the target, "
            "camera whipping alongside its path at speed before arriving "
            "at the target just as it strikes with a visible shudder, "
            "the crowd behind erupting into motion and cheering. "
            "Continuous fast whip-tracking motion the entire clip, not "
            "static, no text",
    },
    {
        "title": "cliff climb",
        "has_people": True,
        "mood": "light",
        "still_prompt": "First-person point of view climbing a knotted "
            "rope up a sunlit sandstone cliff face, the knight's own "
            "gauntleted hands gripping the rope at the bottom of frame, "
            "looking up toward a ruined hilltop tower silhouetted "
            "against bright blue sky, loose pebbles and dust visible on "
            "the rock face, warm golden afternoon light raking across "
            "the stone, photorealistic, cinematic photography, shot on a "
            "DSLR, natural lighting, highly detailed rock texture, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "True first-person POV climbing hand over "
            "hand up the rope, camera rising steadily with natural "
            "effortful sway and the occasional small slip and recatch, "
            "the tower above growing slowly closer, loose pebbles "
            "dislodging and falling past the lens toward the ground far "
            "below. Continuous upward climbing motion the entire clip, "
            "not static, no text",
    },
    {
        "title": "night market fortune teller",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "First-person point of view walking through a "
            "lantern-lit night market, strings of paper lanterns glowing "
            "warm orange overhead, passing a fortune teller's dim tent "
            "with tarot cards laid out on a small table and candlelight "
            "flickering across a hooded figure's hands, stalls of "
            "trinkets and dried herbs to either side, faint smoke from "
            "incense curling upward, photorealistic, cinematic night "
            "photography, shot on a DSLR, warm low light with deep "
            "shadow, highly detailed, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "True first-person POV walking slowly past the "
            "market stalls, camera passing the fortune teller's tent with "
            "a natural curious half-turn toward it, candlelight flickering "
            "and the hooded figure's hands shifting the cards, incense "
            "smoke curling and drifting past the lens. Continuous slow "
            "walking motion with a natural look-turn the entire clip, not "
            "static, no text",
    },
    {
        "title": "sunflower windmill",
        "has_people": True,
        "mood": "light",
        "still_prompt": "First-person point of view walking through a "
            "vast field of tall sunflowers all turned toward the late "
            "afternoon sun, golden light flooding the field, a wooden "
            "windmill with turning sails standing at the far edge of the "
            "field, bees drifting between blooms close to the camera, "
            "warm golden hour color, photorealistic, cinematic "
            "photography, shot on a DSLR, natural lighting, highly "
            "detailed petal texture, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "True first-person POV walking steadily toward "
            "the windmill, sunflower heads brushing past close to the "
            "lens on either side, the windmill's sails visibly turning "
            "in the distance and growing closer, a bee drifting across "
            "frame near the camera. Continuous forward walking motion "
            "the entire clip with natural handheld sway, not static, no "
            "text",
    },
    {
        "title": "festival square sparring",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Two young knights sparring with wooden practice "
            "swords in a sunlit village square during a festival, a "
            "lively crowd in bright summer clothes gathered in a loose "
            "circle cheering, colorful bunting and ribbons strung between "
            "the surrounding buildings, a stall of meat pies smoking "
            "nearby, bright midday sun, photorealistic, cinematic action "
            "photography, shot on a DSLR with a fast shutter, natural "
            "lighting, highly detailed, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "Dynamic third-person tracking shot circling "
            "quickly around the two sparring knights as their wooden "
            "swords clash, the crowd around them shifting and cheering, "
            "bunting rippling overhead in the breeze. Continuous "
            "energetic orbiting camera motion the entire clip, not "
            "static, no text",
    },
    {
        "title": "river boat village",
        "has_people": True,
        "mood": "light",
        "still_prompt": "First-person point of view drifting down a "
            "gentle sunlit river on a small wooden boat through the "
            "middle of a riverside village, timber houses with flower "
            "boxes lining both banks, villagers waving from doorways and "
            "little stone bridges overhead, dragonflies skimming the "
            "water's surface near the boat, warm afternoon light, "
            "photorealistic, cinematic photography, shot on a DSLR, "
            "natural lighting, highly detailed water reflections, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "True first-person POV: the boat drifts "
            "steadily forward with a gentle natural rocking motion, "
            "houses and waving villagers sliding past on both sides, "
            "passing beneath a low stone bridge with a brief shift in "
            "light, water rippling and catching the sun the whole way. "
            "Continuous smooth forward drifting motion the entire clip, "
            "not static, no text",
    },
    {
        "title": "bonfire night dance",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "A large bonfire blazing at night in a clearing "
            "just outside a town's wooden walls, sparks spiraling up into "
            "the dark sky, silhouetted figures mid-dance around the fire "
            "with arms raised, a small group playing drums and pipes off "
            "to one side, the town's torchlit gate visible in the "
            "background, warm orange firelight against deep blue night, "
            "photorealistic, cinematic night photography, shot on a "
            "DSLR with a slower shutter to show motion blur in the "
            "dancers, natural lighting, highly detailed, 9:16 vertical, "
            "no text, no watermark",
        "animate_prompt": "Dynamic third-person tracking shot circling "
            "the bonfire at a jogging pace, dancers whirling past close "
            "to the camera with firelight flickering across them, sparks "
            "rising continuously into the night sky, drummers' arms "
            "moving in rhythm. Continuous fast orbiting camera motion the "
            "entire clip, energetic and handheld, not static, no text",
    },
    {
        "title": "country lane companion",
        "has_people": True,
        "mood": "light",
        "still_prompt": "A young armoured knight walking down a sunlit "
            "dirt country lane lined with wildflowers and low stone "
            "walls, a scruffy brown dog trotting happily alongside him, "
            "rolling green hills and a distant farmhouse in the "
            "background, warm late-afternoon light, a few puffy clouds "
            "in a blue sky, photorealistic, cinematic photography, shot "
            "on a DSLR, natural lighting, highly detailed fur and fabric "
            "texture, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic third-person tracking shot moving "
            "alongside the knight and dog at walking pace, the dog "
            "bounding slightly ahead then circling back, wildflowers "
            "swaying at the lane's edge as the camera passes, the "
            "farmhouse growing slowly closer in the background. "
            "Continuous smooth lateral tracking motion the entire clip, "
            "not static, no text",
    },
    {
        "title": "harvest feast table",
        "has_people": True,
        "mood": "light",
        "still_prompt": "First-person point of view seated at a long "
            "wooden outdoor feast table during a harvest celebration, "
            "platters of roasted vegetables, bread and fruit being passed "
            "hand to hand close to the camera, warm late-afternoon "
            "sunlight slanting across the table, strings of lanterns not "
            "yet lit overhead, villagers laughing and talking on either "
            "side, hay bales and pumpkins decorating the scene, "
            "photorealistic, cinematic photography, shot on a DSLR, "
            "natural lighting, highly detailed food textures, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "True first-person POV: a platter of bread is "
            "passed into frame from one side as if handed to the knight "
            "himself, hands reaching across the table, people on either "
            "side turning to talk and laugh, warm light shifting slightly "
            "as the sun lowers. Continuous lively handheld motion at the "
            "table the entire clip, not static, no text",
    },
]

"""
Scene bank for the light-fantasy video pipeline (@spongebob_prime_).

v2 -- rebuilt from dez's feedback on the first preview batch. The v1
bank (close-up POV shots: market stalls, tavern doors, forge interiors)
read as "realistic medieval photography," not "fantasy," and several
scenes were too calm/static in composition even with camera motion
added. dez's reference was a wide epic landscape shot (tiny knight,
dramatic sunset sky, distant castle) -- epic scale, dramatic light,
something clearly happening, not a mundane close-up.

v2 formula for every scene, no exceptions:

1. WIDE EPIC LANDSCAPE COMPOSITION. The subject(s) are small-to-medium
   in frame against a vast, dramatic landscape (sky dominates much of
   the frame), not a tight close-up. Think "epic fantasy movie poster /
   location still," not "person standing in a room."
2. DRAMATIC, VIVID SKY. Golden-hour, storm-lit clouds, sunbeams,
   aurora-like glow, meteor showers, eclipses, or a vivid star field --
   the sky is doing something, every time.
3. REAL ACTION HAPPENING. A sword fight, a charge, a joust, a chase, a
   hunt, a siege -- dez was explicit: "stuff needs to be happening."
   Nothing posed or passive.
4. VISIBLE MAGICAL ELEMENTS woven into an otherwise photoreal scene --
   glowing mist, enchanted light on a blade, floating embers, aurora,
   an impossible sky event -- so it reads as FANTASY, not just
   "realistic medieval photo." This is what v1 was missing entirely.
5. Still photorealistic (not painted/illustrated -- dez confirmed they
   want to stay photoreal, just push the epic/magical scale further),
   shot on a full-frame DSLR with a wide lens, highly detailed, vivid
   color grade, 9:16 vertical, no text, no watermark.
6. Animation is real sustained camera motion matched to the action --
   tracking, circling, pushing in -- never a static or locked shot.

20 scenes, roughly 14 light / 6 dark-leaning, per dez's original
light-mostly-with-dark-breaks direction, now rebuilt to this bar.
"""

SCENES = [
    {
        "title": "meadow duel",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: two "
            "armoured knights locked in a dramatic sword fight in the "
            "foreground of a sunlit wildflower meadow, blades clashing "
            "mid-swing, small in frame against the vast landscape, an "
            "enormous ancient stone castle perched on a misty mountain "
            "peak in the far distance, dramatic sky with golden sunbeams "
            "breaking through scattered clouds like magical light, "
            "rolling fields of wildflowers catching the breeze around "
            "the fighters, faint glowing atmospheric haze in the valley "
            "between meadow and mountain, photorealistic landscape "
            "photography, shot on a full-frame DSLR with a wide lens, "
            "epic scale, highly detailed, vivid magical color grade, "
            "9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic cinematic tracking shot of two "
            "armoured knights in a full sword fight in the wildflower "
            "meadow, blades clashing and ringing, footwork shifting back "
            "and forth as they parry and strike, wildflowers flattened "
            "and kicked up around their feet, camera circling and "
            "pushing in slightly to follow the action, the distant "
            "mountain castle and dramatic golden-lit sky visible behind "
            "them the whole time, sunbeams shifting through the clouds. "
            "Continuous high-energy fight choreography motion the "
            "entire clip, not static, no text",
    },
    {
        "title": "cliffside gallop",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "knight in bright polished armor riding a powerful brown "
            "warhorse at a full gallop along a grassy coastal cliff "
            "path, small-to-medium in frame against the huge sky, cloak "
            "snapping straight out behind him in the wind, dust kicking "
            "up from the horse's hooves, a sparkling turquoise sea far "
            "below the cliff edge, an enormous dramatic sky filling most "
            "of the frame with towering sunlit clouds and scattered "
            "golden light, photorealistic landscape action photography, "
            "shot on a full-frame DSLR with a fast shutter freezing the "
            "horse's motion, epic scale, highly detailed, vivid color "
            "grade, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic third-person tracking shot running "
            "alongside the galloping horse at matching speed, camera "
            "slightly low and wide to keep the huge dramatic sky in "
            "frame, the horse's legs pounding the ground, dust and loose "
            "turf kicking up, cloak whipping in the wind, the sea and "
            "towering clouds sweeping past in the background the entire "
            "clip. Sustained high-energy tracking motion, not a locked "
            "or static shot, no text",
    },
    {
        "title": "storm cliff rider",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "knight on horseback, small in frame for scale, silhouetted "
            "atop a windswept cliff edge overlooking a vast turquoise "
            "sea, the horse rearing up on its hind legs, an enormous "
            "dramatic sky above filled with towering golden storm-lit "
            "clouds and shafts of sunlight breaking through like magic, "
            "seabirds scattering in the distance, bright vivid light "
            "with an otherworldly glowing quality where the sunbeams hit "
            "the water, photorealistic landscape photography, shot on a "
            "full-frame DSLR with a wide lens, epic scale, highly "
            "detailed, vivid color grade, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "Dynamic wide tracking shot as the horse rears "
            "and comes back down, the knight steadying it at the cliff "
            "edge, mane and cloak whipping violently in the wind, the "
            "camera sweeping slightly around to reveal more of the storm-"
            "lit sky and sea, sunbeams shifting and breaking through the "
            "clouds in real time, waves crashing against the cliff far "
            "below. Continuous dramatic motion the entire clip, not "
            "static, no text",
    },
    {
        "title": "mountain castle approach",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "lone armoured knight, small in frame for scale, striding "
            "fast along a grassy hilltop ridge toward a distant castle "
            "silhouetted on a far hill, vivid dramatic orange and pink "
            "sunset sky filling most of the frame with towering golden-"
            "lit clouds, rolling green hills stretching to the horizon, "
            "warm magical golden-hour light raking across the grass, a "
            "faint glowing mist in the valley below catching the last "
            "light, photorealistic landscape photography, shot on a "
            "full-frame DSLR with a wide lens, epic scale, highly "
            "detailed, vivid color grade, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "Dynamic low wide tracking shot moving "
            "alongside the knight at a fast determined stride, cloak "
            "snapping in the wind, camera gliding smoothly across the "
            "ridge to keep both the striding figure and the huge sunset "
            "sky in frame, the glowing valley mist drifting below, the "
            "castle on the distant hill growing slowly larger. "
            "Continuous forward tracking motion the entire clip, not "
            "static, no text",
    },
    {
        "title": "dragon-shadow over the wheat",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "knight in a vast golden wheat field looking up and sprinting "
            "as an enormous dark winged shadow sweeps rapidly across the "
            "field ahead of him, cast by something huge and unseen flying "
            "just out of frame overhead, wheat flattening in a sudden "
            "gust, a dramatic bright blue sky with towering clouds and a "
            "strange shimmering heat-haze where the shadow passes, "
            "photorealistic landscape action photography, shot on a full-"
            "frame DSLR with a fast shutter, epic scale, highly detailed, "
            "vivid magical color grade, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "Dynamic low wide tracking shot running "
            "alongside the knight as he sprints through the wheat, the "
            "huge shadow racing across the field ahead of and around "
            "him, wheat whipping and flattening violently in its wake, "
            "camera glancing upward briefly to the empty sky where the "
            "shadow's source stays just out of frame, dust and loose "
            "chaff thrown into the air. Continuous fast sprinting motion "
            "the entire clip, high energy, not static, no text",
    },
    {
        "title": "waterfall bridge crossing",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "knight crossing a long narrow rope and plank bridge strung "
            "high over a massive roaring waterfall deep in an enchanted "
            "valley, small in frame against the huge scale of the falls "
            "and cliffs, glowing turquoise magical motes and drifting "
            "light-wisps swirling in the rising mist, a vivid magical "
            "rainbow-aurora shimmering unnaturally bright in the spray, "
            "towering lush cliffs on either side, bright enchanted "
            "midday sun with a magical golden-teal color grade, "
            "photorealistic landscape photography, shot on a full-frame "
            "DSLR with a wide lens, epic scale, highly detailed, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "Dynamic wide tracking shot following the "
            "knight across the swaying bridge from the side, the bridge "
            "visibly flexing underfoot with each step, the glowing "
            "magical motes and mist swirling and drifting past in the "
            "foreground, the rainbow-aurora shifting in the spray, the "
            "massive waterfall thundering continuously below. Real "
            "sustained forward motion with the bridge swaying the entire "
            "clip, not static, no text",
    },
    {
        "title": "enchanted forge",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide cinematic photograph: a bare-armed "
            "blacksmith mid-swing with a heavy hammer striking a "
            "magically enchanted blade glowing bright blue-white with "
            "runic light on an anvil in an open-air hilltop smithy, "
            "framed wide to show the dramatic valley and huge golden-lit "
            "sky behind the forge, a shower of sparks that glow like "
            "tiny stars and drift upward instead of falling, faint "
            "magical energy crackling along the blade's edge, a young "
            "armoured knight watching in awe nearby, photorealistic "
            "fantasy photography, cinematic action shot, shot on a full-"
            "frame DSLR with a fast shutter, epic scale, highly detailed, "
            "vivid magical color grade, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "Dynamic third-person tracking shot circling "
            "quickly around the anvil as the hammer rises and falls, "
            "star-like sparks bursting outward and drifting upward with "
            "each strike, magical energy crackling visibly along the "
            "blade, the dramatic sky and valley sweeping past behind the "
            "forge as the camera orbits, the knight shifting to watch in "
            "awe. Continuous orbiting camera motion the entire clip, "
            "energetic, not static, no text",
    },
    {
        "title": "dawn arrow volley",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "line of archers on a hilltop releasing a volley of flaming "
            "arrows that arc high across a vast dawn sky toward a "
            "distant hilltop fort, the arrows' fire trails glowing "
            "against streaks of pink and orange dawn cloud, the archers "
            "small in frame against the huge sky, morning mist pooling "
            "in the valley below, photorealistic landscape action "
            "photography, shot on a full-frame DSLR with a fast shutter "
            "freezing the arrows mid-flight, epic scale, highly "
            "detailed, vivid color grade, 9:16 vertical, no text, no "
            "watermark",
        "animate_prompt": "Dynamic wide tracking shot following the "
            "flaming arrows' arc across the huge dawn sky from release "
            "to impact near the distant fort, camera whipping along "
            "their flight path at speed, fire trails streaking against "
            "the clouds, the archers' silhouettes small on the hilltop "
            "behind, morning mist drifting in the valley. Continuous "
            "fast whip-tracking motion the entire clip, not static, no "
            "text",
    },
    {
        "title": "valley cavalry charge",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "full line of mounted knights charging at a full gallop "
            "across a vast green valley, banners snapping in the wind "
            "above them, a huge storm of dust rising behind the charge, "
            "dramatic sky with towering sunlit clouds filling most of "
            "the frame, the riders small against the epic scale of the "
            "landscape, photorealistic landscape action photography, "
            "shot on a full-frame DSLR with a fast shutter, epic scale, "
            "highly detailed, vivid color grade, 9:16 vertical, no text, "
            "no watermark",
        "animate_prompt": "Dynamic low wide tracking shot running "
            "alongside the charging cavalry line at full gallop speed, "
            "dust and turf kicking up thickly around the camera, banners "
            "whipping overhead, hooves pounding in a continuous "
            "thunderous rhythm, the dramatic sky sweeping past above the "
            "charge. Sustained high-energy tracking motion the entire "
            "clip, not static, no text",
    },
    {
        "title": "bonfire magic dance",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Wide cinematic night photograph: a large "
            "bonfire blazing in a clearing just outside a town's wooden "
            "walls, framed wide to show the huge night sky above, "
            "sparks spiraling up and transforming into glowing magical "
            "embers that drift and swirl like fireflies with a life of "
            "their own, silhouetted figures mid-dance around the fire "
            "with arms raised, faint ethereal blue-green magical lights "
            "floating above the distant treeline, the town's torchlit "
            "gate visible in the background, vivid warm orange firelight "
            "against a deep magical purple-blue night sky with unusually "
            "bright stars, photorealistic fantasy night photography, "
            "shot on a full-frame DSLR with a slower shutter to show "
            "motion blur in the dancers and embers, epic scale, highly "
            "detailed, vivid magical color grade, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "Dynamic wide tracking shot circling the "
            "bonfire at a jogging pace, dancers whirling past close to "
            "the camera with firelight flickering across them, the "
            "magical embers rising and swirling unnaturally into the "
            "night sky, the ethereal lights above the treeline pulsing "
            "faintly, drummers' arms moving in rhythm. Continuous fast "
            "orbiting camera motion the entire clip, energetic, not "
            "static, no text",
    },
    {
        "title": "meteor camp",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Wide epic cinematic night photograph: a small "
            "group of knights standing around a campfire on a hilltop, "
            "all looking up in awe as a dramatic meteor shower streaks "
            "across a vast star-filled night sky above them, dozens of "
            "bright meteor trails crossing the huge dark sky, firelight "
            "flickering warm against the cold blue night, the camp small "
            "in frame against the epic scale of the sky, photorealistic "
            "fantasy night photography, shot on a full-frame DSLR with a "
            "long exposure to catch the meteor trails, epic scale, "
            "highly detailed, vivid magical color grade, 9:16 vertical, "
            "no text, no watermark",
        "animate_prompt": "Dynamic slow upward-tilting camera move from "
            "the firelit camp up into the star field as meteors streak "
            "continuously across the sky in real time, the knights' "
            "silhouettes shifting and pointing up at the brightest ones, "
            "firelight flickering across them, the camera settling into "
            "a slow drifting pan across the meteor shower. Continuous "
            "smooth motion the entire clip, not static, no text",
    },
    {
        "title": "grand tournament joust",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: two "
            "knights on horseback charging directly at each other down a "
            "jousting lane at full speed, lances leveled, the moment "
            "just before impact, a huge cheering crowd and colorful "
            "fluttering banners lining the field, a dramatic bright sky "
            "with scattered clouds filling the upper half of the frame, "
            "the whole tournament field shown at epic scale, "
            "photorealistic landscape action photography, shot on a "
            "full-frame DSLR with a fast shutter freezing the charge, "
            "highly detailed, vivid color grade, 9:16 vertical, no text, "
            "no watermark",
        "animate_prompt": "Dynamic low wide tracking shot running "
            "alongside the jousting lane as both knights charge toward "
            "each other at full gallop, dust kicking up from the "
            "hooves, lances lowering into position, banners snapping "
            "overhead, the crowd's roar implied by their surging motion "
            "as the two riders close the distance. Continuous fast "
            "tracking motion building to the moment of impact, not "
            "static, no text",
    },
    {
        "title": "the giant's footprint",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "small armoured knight walking through the bottom of an "
            "impossibly enormous ancient footprint-shaped valley, sheer "
            "mossy walls rising on either side far overhead, faint "
            "magical glowing moss and luminous blue flowers growing in "
            "the cracks of the stone, a sliver of dramatic golden sky "
            "visible far above between the towering walls, "
            "photorealistic landscape photography, shot on a full-frame "
            "DSLR with a wide lens, epic scale, highly detailed, vivid "
            "magical color grade, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic wide tracking shot following the "
            "knight as he walks deeper through the vast footprint-shaped "
            "valley, the glowing moss and flowers pulsing faintly as he "
            "passes, camera slowly craning upward to reveal more of the "
            "towering mossy walls and the sliver of golden sky above, "
            "dust and loose stone crumbling occasionally from the "
            "heights. Continuous forward and upward sweeping motion the "
            "entire clip, not static, no text",
    },
    {
        "title": "northern lights over the keep",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Wide epic cinematic night photograph: an "
            "ancient stone castle keep on a hilltop silhouetted against "
            "a vivid, unnaturally bright aurora rippling in waves of "
            "green, purple and teal across the entire night sky, a "
            "knight standing small on the battlements looking up, "
            "torchlight glowing warm along the castle walls below the "
            "cold magical light above, photorealistic fantasy night "
            "photography, shot on a full-frame DSLR with a long "
            "exposure, epic scale, highly detailed, vivid magical color "
            "grade, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic slow wide tracking shot drifting "
            "past the castle silhouette as the aurora ripples and shifts "
            "continuously overhead in real time, waves of color rolling "
            "across the sky, torchlight flickering along the battlements, "
            "the knight's silhouette turning slowly to take in the "
            "display. Continuous smooth drifting motion the entire clip, "
            "not static, no text",
    },
    {
        "title": "river rapids chase",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "knight riding a horse at a full sprint alongside a roaring "
            "white-water river, leaping a fallen log mid-stride, spray "
            "and mist rising off the rapids beside him, dramatic bright "
            "sky with scattered clouds above a steep forested valley, "
            "the rider small against the huge scale of the river and "
            "canyon, photorealistic landscape action photography, shot "
            "on a full-frame DSLR with a fast shutter, epic scale, "
            "highly detailed, vivid color grade, 9:16 vertical, no text, "
            "no watermark",
        "animate_prompt": "Dynamic low wide tracking shot running "
            "alongside the horse as it sprints beside the rapids and "
            "leaps the fallen log in one fluid motion, spray and mist "
            "kicking up from the river beside the camera, the canyon "
            "walls and dramatic sky sweeping past. Continuous high-"
            "energy tracking motion the entire clip, not static, no "
            "text",
    },
    {
        "title": "eclipse duel",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Wide epic cinematic landscape photograph: two "
            "knights in a tense sword fight on a hilltop during a total "
            "solar eclipse, the darkened sky showing a brilliant glowing "
            "corona ring around the black sun, an eerie magical twilight "
            "cast over the whole landscape, the fighters small against "
            "the dramatic sky, birds scattering in the distance, "
            "photorealistic landscape action photography, shot on a "
            "full-frame DSLR, epic scale, highly detailed, vivid magical "
            "color grade, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic wide tracking shot circling the two "
            "fighting knights as their blades clash under the eclipse, "
            "the glowing corona holding steady overhead, the eerie "
            "twilight light shifting subtly, footwork and strikes "
            "continuous and fast, birds flickering past in the distance. "
            "Continuous orbiting fight motion the entire clip, not "
            "static, no text",
    },
    {
        "title": "the great hunt",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "knight on horseback at a full gallop chasing a huge "
            "majestic glowing-antlered stag through a golden autumn "
            "forest, dappled sunbeams breaking through the canopy and "
            "catching the stag's faintly luminous antlers, leaves kicked "
            "up in the chase, the riders small against the vast forest "
            "and dramatic shafts of light, photorealistic landscape "
            "action photography, shot on a full-frame DSLR with a fast "
            "shutter, epic scale, highly detailed, vivid magical color "
            "grade, 9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic low wide tracking shot galloping "
            "alongside the chase through the forest, the glowing stag "
            "weaving between trees ahead, leaves and dust kicked up "
            "around the horse, sunbeams flickering rapidly through the "
            "canopy as the camera moves, the stag's antlers pulsing "
            "faintly with light. Continuous fast chase motion the entire "
            "clip, high energy, not static, no text",
    },
    {
        "title": "storming the gate",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "huge siege at a castle gate at dusk, a line of knights "
            "charging toward the burning gatehouse with a massive "
            "battering ram, catapults mid-launch flinging flaming "
            "projectiles in high arcs against a dramatic smoke-streaked "
            "orange sky, the whole battle shown at epic scale with "
            "figures small against the castle and sky, photorealistic "
            "landscape action photography, shot on a full-frame DSLR "
            "with a fast shutter, highly detailed, vivid color grade, "
            "9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic wide tracking shot running alongside "
            "the charging line toward the gate, flaming projectiles "
            "arcing overhead and impacting the walls in bursts of fire "
            "and debris, smoke rolling across the dramatic sky, the "
            "battering ram swinging into the gate. Continuous high-"
            "energy battle motion the entire clip, not static, no text",
    },
    {
        "title": "beneath the blossom tree",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Wide epic cinematic photograph: a wounded "
            "knight lying beneath a magnificent blooming pink Japanese "
            "cherry blossom tree in full bloom, his fallen sword resting "
            "near his side, a dark stain on the armor at his side where "
            "a blade struck him, countless petals drifting down and "
            "catching in his hair and on his breastplate, his hand "
            "reaching weakly toward the fallen blade, soft magical "
            "golden-pink light filtering through the blossoms above, a "
            "dramatic yet beautiful sunset sky glimpsed through the "
            "branches, his expression peaceful rather than pained, "
            "photorealistic cinematic photography, shot on a full-frame "
            "DSLR, epic scale, highly detailed, vivid soft magical color "
            "grade, poignant and beautiful rather than graphic, 9:16 "
            "vertical, no text, no watermark",
        "animate_prompt": "Dynamic slow push-in camera move toward the "
            "fallen knight beneath the blossom tree, countless petals "
            "drifting and swirling continuously in the breeze around "
            "him, his chest rising faintly, his hand trembling slightly "
            "as it reaches toward the fallen blade, the soft golden-pink "
            "light shifting through the branches above, the dramatic sky "
            "glimpsed beyond the blossoms. Continuous slow emotional "
            "motion the entire clip, not static, no text",
    },
    {
        "title": "twilight falconer",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "small figure standing at a cliff's edge releasing a "
            "faintly glowing magical falcon into a vast dramatic twilight "
            "sky, the bird's wings trailing soft golden light as it "
            "launches into flight, deep purple and orange twilight "
            "clouds filling most of the frame, a sweeping valley far "
            "below catching the last light, photorealistic landscape "
            "photography, shot on a full-frame DSLR with a wide lens, "
            "epic scale, highly detailed, vivid magical color grade, "
            "9:16 vertical, no text, no watermark",
        "animate_prompt": "Dynamic wide tracking shot following the "
            "glowing falcon as it launches from the figure's arm and "
            "climbs rapidly into the huge twilight sky, its light-trail "
            "streaking behind it, camera tilting and pushing to follow "
            "its flight against the dramatic clouds, the figure's cloak "
            "snapping in the wind at the cliff edge below. Continuous "
            "upward-following motion the entire clip, not static, no "
            "text",
    },
    {
        "title": "flooded ruins crossing",
        "has_people": True,
        "mood": "light",
        "still_prompt": "Wide epic cinematic landscape photograph: a "
            "knight riding a horse at a determined canter through the "
            "flooded ruins of an ancient temple, water splashing high "
            "around the horse's legs, broken glowing-runed pillars "
            "rising out of the water on either side, a dramatic sky with "
            "shafts of golden light breaking through drifting clouds "
            "above the ruins, the rider small against the epic scale of "
            "the temple, photorealistic landscape action photography, "
            "shot on a full-frame DSLR with a fast shutter, highly "
            "detailed, vivid magical color grade, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "Dynamic low wide tracking shot following the "
            "horse as it canters through the flooded ruins, water "
            "splashing high and catching the light with each stride, the "
            "glowing runes on the pillars pulsing faintly as the camera "
            "passes, shafts of sunlight sweeping across the scene. "
            "Continuous splashing forward motion the entire clip, not "
            "static, no text",
    },
    {
        "title": "the burning sky duel",
        "has_people": True,
        "mood": "dark",
        "still_prompt": "Wide epic cinematic landscape photograph: two "
            "knights in a fierce sword fight silhouetted on a ridge "
            "against an enormous, violently vivid red-and-orange sunset "
            "sky that looks almost like it is burning, towering storm "
            "clouds lit from within by the sunset, the fighters small "
            "against the overwhelming scale of the sky, a dark valley "
            "stretching below, photorealistic landscape action "
            "photography, shot on a full-frame DSLR, epic scale, highly "
            "detailed, vivid dramatic color grade, 9:16 vertical, no "
            "text, no watermark",
        "animate_prompt": "Dynamic wide tracking shot circling the "
            "dueling knights as their silhouettes clash against the "
            "blazing sky, blades flashing in the intense backlight, "
            "footwork fast and continuous, the towering clouds shifting "
            "and glowing behind them the entire time. Continuous "
            "orbiting fight motion the entire clip, high energy, not "
            "static, no text",
    },
]

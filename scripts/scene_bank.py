"""
Scene bank for the light-fantasy video pipeline (@spongebob_prime_).

v5 -- curated stills. Instead of generating a fresh still via the Soul
API on every run, each scene now points at one of 50 images dez
generated and hand-picked through Higgsfield's web app (Seedream 5.0
lite, Unlimited mode -- free, outside the per-generation API credit
cost) on 2026-10-02, after approving the v4 direction (grimy worn
armor, wide zoomed-out shots, town/landscape variety, warm nostalgic
light, matching https://www.tiktok.com/@clawenai/video/7499162427452296490).
dez said: "i like them. we will use them all."

image_url points at Higgsfield's own CDN (d8j0ntlcm91z4.cloudfront.net)
where these stills already live -- generate_one_post() in
higgsfield_client.py downloads straight from there and skips the Soul
still-generation call entirely for scenes that carry image_url. Only
the Hailuo image-to-video animation step still costs API credits.

50 scenes, 34 light / 16 dark, mixing grimy-knight moments with
knight-free towns and landscapes, same wide-zoomed-out warm/nostalgic
(or cool dusk for the dark ones) formula as v4.
"""

SCENES = [
    {
        "title": "grimy knight at the village well",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_084831_445d7aee-1a21-462c-82c3-bdcb62bf6090.png",
        "animate_prompt": "The knight slowly turns a page in the tattered book, his grimy scratched armor catching the warm light. A few leaves drift down across the cobblestone square. Distant butterflies flutter near the ivy-covered wall. Faint dust motes drift through the air. The camera slowly zooms out and drifts backward, revealing more of the quiet village square around him. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "hillside village at golden hour",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_084925_3e70bf77-5fe0-4702-8228-297c43ba3ae9.png",
        "animate_prompt": "Smoke drifts slowly up from the chimneys and dissipates into the golden haze. Birds glide slowly across the sky above the rooftops. A butterfly drifts past in the foreground. Window lantern light flickers faintly. The camera slowly drifts forward and down toward the town, revealing more streets and rooftops. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight feeding the fox",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_084950_9deda584-79d7-4b61-9a80-bc6dddad7f7f.png",
        "animate_prompt": "The fox nibbles from the knight's palm then looks up, ears twitching. Mist drifts and curls slowly across the clearing floor. Light shafts shift faintly through the moving canopy above. The camera slowly zooms out and rises, revealing the full misty clearing and surrounding trees. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "misty harbor town at dawn",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085015_d562dd60-8d9b-432f-8722-851495581bc9.png",
        "animate_prompt": "Mist drifts slowly across the still water and along the quay. Small ripples move across the harbor surface as the moored boats sway gently. Gulls glide slowly through the pale sky. The camera slowly drifts sideways along the waterfront, revealing more of the harbor. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight leading his horse through the meadow",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085034_3a370373-d4c9-4594-9ea7-8257f57e5cff.png",
        "animate_prompt": "The knight and horse continue walking slowly through the meadow, grass and wildflowers swaying and parting around their legs. The horse's mane shifts in the breeze. Golden light shifts gently as thin clouds drift overhead. The camera drifts slowly alongside them at a calm walking pace, wide enough to keep the full landscape in frame. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "mountain village street at twilight",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085055_65e57246-f86e-433e-8dda-d8374ce86dc0.png",
        "animate_prompt": "The hanging lanterns sway gently in the evening breeze, their light flickering softly across the cobblestones. Window light flickers faintly. Thin clouds drift slowly behind the mountains in the deepening dusk. The camera drifts slowly forward down the street. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight resting above the valley",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085119_949e599b-cf6a-4cd5-bdc8-15405dc7b231.png",
        "animate_prompt": "Grass and loose branches sway gently in the breeze around the knight as he sits still, looking out over the valley. Haze drifts slowly over the distant rooftops below. A few birds cross the sky in the distance. The camera slowly drifts and zooms out, revealing more of the valley and town below. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "sunlit orchard town",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085137_cec77ac8-613d-4fcc-8a14-02a4cc886d23.png",
        "animate_prompt": "Blossom petals drift steadily through the air across the orchard, branches swaying gently in the breeze. Light shifts and dapples through the moving leaves. Distant smoke rises faintly from a chimney in the town. The camera drifts slowly forward along the path toward the town. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight at the stable",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085200_1b8c33a9-c379-4dba-a3de-289ca96cb2cd.png",
        "animate_prompt": "The knight's brush moves slowly along the horse's flank, the horse shifting its weight and flicking its tail. Dust and straw drift through the warm sunbeams spilling through the stable doors. Distant village life is faintly visible through the opening. The camera slowly zooms out, revealing more of the stable and the village beyond. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "snow-dusted mountain village",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085216_ad389c32-cdfe-48f6-b9c1-485edce8186a.png",
        "animate_prompt": "Snow falls gently over the village, settling on the rooftops and path. Smoke drifts slowly from the chimneys into the cold air. Window light flickers softly. The camera drifts slowly forward and down toward the village, revealing more of the snowy street. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight on the battlements",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085232_0ef5f027-01fa-4b87-969d-2e986eb4f82d.png",
        "animate_prompt": "The knight's cloak shifts gently in the evening breeze as he looks out over the town. Birds drift slowly across the sunset sky below him. Smoke rises faintly from distant chimneys. The camera slowly zooms out and drifts sideways along the wall, revealing more of the town and hills. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "river village at golden hour",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085249_1dc51e53-a31c-4658-99c4-edc4848eb0a1.png",
        "animate_prompt": "The river flows gently beneath the stone bridge, the boats swaying slightly at their moorings. Fireflies drift and pulse softly in the shadows along the bank. Light reflects and shifts on the moving water surface. The camera drifts slowly across the bridge, revealing more of the village along the river. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight at the forest shrine",
        "has_people": True,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085316_d45405f0-32a1-4d41-9cad-526f913d560f.png",
        "animate_prompt": "Mist drifts slowly across the clearing around the shrine and the kneeling knight. Light shifts faintly through the moving canopy above. A few leaves drift down from the ancient trees. The camera slowly zooms out, revealing the full clearing and the tangled roots and trees around the shrine. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "abandoned watchtower at dusk",
        "has_people": False,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085332_02f57227-2482-473f-8cc1-39ab4f2ca679.png",
        "animate_prompt": "Tall grass sways steadily around the base of the tower in the wind. Birds circle slowly above the tower. The lit window flickers faintly. Thin clouds drift across the darkening sky. The camera slowly drifts forward and rises toward the tower, revealing more of the windswept hillside. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "grimy knight crossing the old bridge",
        "has_people": True,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085348_36ab82f4-9b1c-4c7d-88aa-ff1e445bcb57.png",
        "animate_prompt": "The knight walks slowly across the bridge, cloak shifting gently in the breeze. Mist drifts and rises steadily off the river below. Thin clouds pass overhead in the fading light. The camera tracks slowly alongside him at a calm walking pace, wide enough to keep the full bridge and valley in frame. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "quiet ruins overlooking the coast",
        "has_people": False,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085405_4db0dc38-06aa-4c50-85b5-15d31e515ac9.png",
        "animate_prompt": "Wildflowers and grass sway steadily in the sea wind around the broken walls. Birds glide slowly along the cliff edge. Waves move faintly far below. Thin clouds drift across the fading sky. The camera slowly drifts forward toward the cliff edge, revealing more of the ruins and the sea beyond. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "grimy knight repairing a fence at the farmland",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085425_97b3a395-55c8-4967-8f8e-8de510b8b733.png",
        "animate_prompt": "The knight hammers a nail into the fence post, loose straw and dust drifting around him in the breeze. Golden wheat sways gently across the fields. Distant smoke rises faintly from the farmhouse chimney. The camera slowly drifts and zooms out, revealing more of the rolling farmland. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "quiet fishing village with nets drying",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085441_33cf4cba-414b-4012-8917-98896522ada5.png",
        "animate_prompt": "Fishing nets sway gently on their wooden racks in the morning breeze. Mist drifts slowly over the still water. Small ripples move across the harbor as a boat rocks gently. The camera drifts slowly forward along the shingle beach. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight sharpening sword by campfire",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085457_79c8874f-c818-48b9-951d-32e45ea35d32.png",
        "animate_prompt": "The knight's whetstone moves slowly along the blade, sparks catching the firelight. Flames flicker and smoke drifts upward into the darkening sky. Shadows shift gently across the trees. The camera slowly zooms out, revealing more of the forest's edge around him. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "windmill village on a hill",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085513_7804ffde-e517-48c1-a2db-f4c213240646.png",
        "animate_prompt": "The windmill's sails turn slowly against the sky. Golden wheat ripples steadily in the breeze. Soft clouds drift overhead. The camera drifts slowly forward and down toward the village, revealing more of the fields. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight carrying firewood through village lane",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085531_207f5303-014c-4b41-bcf3-b9f2f3ae7096.png",
        "animate_prompt": "The knight walks steadily down the lane, firewood shifting slightly in his arms. Warm window light flickers in the cottages around him. Evening mist drifts low along the cobblestones. The camera tracks slowly alongside him, wide enough to keep the lane in frame. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "terraced hillside vineyard town",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085550_226a870c-e6a2-4452-980c-6d5ecf8739c3.png",
        "animate_prompt": "Morning haze drifts slowly over the terraced vines, thinning as the light strengthens. Leaves sway gently in the breeze. The camera slowly rises and drifts forward over the hillside, revealing more of the vineyard and town. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight at a roadside shrine",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085606_9e2a99ea-738f-4af8-a54b-4f49a9b114fa.png",
        "animate_prompt": "The knight bows his head at the shrine, wildflowers swaying gently around him. Soft daylight shifts as thin clouds pass overhead. Dust drifts along the empty road. The camera slowly zooms out, revealing the open countryside behind him. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "lantern-lit market street",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085622_d35ffd18-6fb7-4c3d-a895-14e7e8d576dc.png",
        "animate_prompt": "The hanging lanterns sway and flicker warmly above the stalls. Awnings ripple gently in the breeze. Smoke drifts up from a small fire pit. The camera drifts slowly forward down the cobblestone street, revealing more of the market. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight resting beside a wishing well",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085642_11c12d84-57d2-4095-8799-89bcf963c58f.png",
        "animate_prompt": "Butterflies drift lazily around the knight as he rests against the well. Wildflowers sway gently in the breeze. Soft daylight shifts across the square. The camera slowly zooms out, revealing more of the quiet village square around him. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "coastal cliffside village",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085658_4e31cbc2-f44f-4354-9341-13c79fdd5976.png",
        "animate_prompt": "Waves roll gently against the cliffs far below. Wildflowers sway along the cliff edge. Warm hazy light shifts softly over the whitewashed cottages. The camera drifts slowly forward along the winding path, revealing more of the village and sea. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight walking along an orchard wall",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085714_1bd7027a-9d9a-41ae-b0cc-952329c1969f.png",
        "animate_prompt": "Blossom petals drift steadily around the knight as he walks, branches swaying gently above the wall. Warm spring light shifts through the moving leaves. The camera tracks slowly alongside him, revealing the village in the soft distance. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "stone chapel on a hill",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085735_bffd0a9b-42e5-4a22-a89e-ee6d00edc851.png",
        "animate_prompt": "Wildflowers sway gently around the chapel in the morning breeze. A few birds cross the sky above. Soft light shifts over the distant countryside. The camera slowly drifts forward and rises toward the chapel, revealing more of the hillside. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight helping a farmer with a cart wheel",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085752_023c2060-0bea-4732-992f-9b2d07a7c9aa.png",
        "animate_prompt": "The knight and farmer lift the wheel together, dust rising faintly around them. Golden light shifts across the farmland as clouds drift overhead. The camera slowly zooms out, revealing more of the fields and distant farmhouse. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "quiet canal village",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085810_34530f49-059f-4ab7-8c4b-1cf5ea1566b4.png",
        "animate_prompt": "Gentle ripples move slowly across the canal water, reflections shifting softly. Morning light strengthens over the mossy rooftops. The camera drifts slowly forward along the waterway, revealing more of the footbridges and cottages. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight standing watch at the town gate",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085826_9c7fab51-dff1-41ed-b17c-dc178ca9f98f.png",
        "animate_prompt": "The knight shifts his stance slightly as he scans the misty fields. Morning mist drifts slowly past the gate. Soft pale light strengthens over the sleepy town. The camera slowly zooms out, revealing more of the gate and town behind him. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "apple orchard cottage at sunset",
       "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085843_8c67104e-5414-4fc2-ab81-d978d346e144.png",
        "animate_prompt": "Leaves and branches sway gently in the breeze, apples swaying faintly on their stems. Warm golden light dips lower on the horizon. The camera drifts slowly forward toward the cottage, revealing more of the orchard. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight feeding chickens",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085901_b91fc22e-5eaf-4cb0-a370-db277cc7464d.png",
        "animate_prompt": "The knight scatters feed as the chickens move around his feet. Soft daylight shifts gently across the yard. The wooden fence creaks faintly in the breeze. The camera slowly zooms out, revealing more of the cottage and yard around him. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "lighthouse village on a rocky coast",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085917_84898377-8834-443b-8bb6-4dc9a53cac10.png",
        "animate_prompt": "Waves break gently on the rocks below the lighthouse. Warm hazy light shifts softly over the stone cottages. A few gulls drift across the sky. The camera drifts slowly forward along the coastline, revealing more of the village and sea. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight on a rooftop watching the sunset",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085935_7f632e92-2e81-4b6f-9308-a5b11de37ead.png",
        "animate_prompt": "The knight sits still as the sunset colors shift and deepen around him. Smoke drifts faintly from nearby chimneys. A light breeze stirs his cloak. The camera slowly zooms out, revealing more of the rooftops and town below. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "flower-covered stone cottage",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_085952_6c7192bd-c31d-4050-9865-9b46ef180240.png",
        "animate_prompt": "Roses and ivy sway gently on the cottage walls. Dappled sunlight shifts softly through the nearby trees. The camera drifts slowly forward toward the cottage, revealing more of the quiet forest edge. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight leading a donkey through a village",
        "has_people": True,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090009_97126395-389a-4a37-9548-0c177986a15a.png",
        "animate_prompt": "The knight and donkey walk steadily down the street, supply sacks shifting gently. Warm midday light shifts across the stone buildings. The camera tracks slowly alongside them, wide enough to keep the street in frame. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "quiet monastery garden",
        "has_people": False,
        "mood": "light",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090027_6334caef-17c8-4d77-8acd-5586a6ff587c.png",
        "animate_prompt": "Morning mist drifts slowly between the stone archways. Wildflowers sway gently along the paths. Vines shift softly in the breeze. The camera drifts slowly forward through the garden, revealing more of the archways. A fair amount of movement throughout, calm and nostalgic, no text",
    },
    {
        "title": "grimy knight walking through a graveyard",
        "has_people": True,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090045_2ece3ba2-66c2-4b04-b78f-1caa84337727.png",
        "animate_prompt": "The knight walks slowly between the weathered markers, bare branches swaying faintly above him. Fading blue light shifts softly across the stones. The camera tracks slowly alongside him, wide enough to keep the graveyard in frame. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "crumbling castle gatehouse under a stormy sky",
        "has_people": False,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090102_01cc8ee3-6446-48b3-a18f-9b1b1f72af25.png",
        "animate_prompt": "Dark clouds roll and churn steadily overhead. Distant lightning flickers faintly on the horizon. Loose grass sways at the base of the walls. The camera slowly drifts forward toward the gatehouse, revealing more of the stormy sky. A fair amount of movement throughout, somber and dramatic, no text",
    },
    {
        "title": "grimy knight standing alone on a foggy moor",
        "has_people": True,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090121_877cdcbd-d770-4c55-9fff-26c5e0e12afa.png",
        "animate_prompt": "The knight stands still as fog drifts slowly around him. Twisted low trees sway faintly in the cool wind. Cool blue-grey light shifts softly across the moor. The camera slowly zooms out, revealing more of the empty expanse around him. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "abandoned mill beside a dark river",
        "has_people": False,        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090137_2315fa0c-6a12-4cdf-81a0-1e5d7717e028.png",
        "animate_prompt": "The broken water wheel creaks faintly as the river flows steadily past. Overgrown reeds sway along the bank. Cool fading light shifts softly over the moss-covered walls. The camera drifts slowly forward along the riverbank, revealing more of the mill. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "grimy knight lighting a torch at a cave",
        "has_people": True,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090153_7091ef6e-ff84-4bbe-96c9-a0aa3963a705.png",
        "animate_prompt": "The torch catches and flares, warm light flickering across the knight's armor. Cool dusk light settles over the jagged rocks around him. Dead branches sway faintly in the wind. The camera slowly zooms out, revealing more of the rocky hillside and cave mouth. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "stone cemetery chapel at dusk",
        "has_people": False,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090212_bbd1fb22-96ae-4976-93d2-5e6f5cbcf195.png",
        "animate_prompt": "Bare branches sway slowly above the chapel in the evening wind. Cool blue twilight deepens steadily across the overgrown grass. The camera drifts slowly forward toward the chapel, revealing more of the scattered headstones. A fair amount of movement throughout, somber and peaceful, no text",
    },
    {
        "title": "grimy knight walking past broken statues",
        "has_people": True,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090228_2e45c085-907a-4fce-98b3-2fe769908375.png",
        "animate_prompt": "The knight walks slowly between the moss-covered statues, ivy swaying faintly around the courtyard. Fading dusk light shifts softly across the broken stone. The camera tracks slowly alongside him, wide enough to keep the courtyard in frame. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "distant castle silhouette under a stormy sunset",
        "has_people": False,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090248_f4ca192a-39aa-40c7-94c8-155d9b407cae.png",
        "animate_prompt": "Dark clouds swirl and drift steadily above the ruined castle. The blood-orange sunset light shifts slowly across the empty hills. The camera slowly drifts forward over the rolling hills, revealing more of the castle silhouette. A fair amount of movement throughout, somber and dramatic, no text",
    },
    {
        "title": "grimy knight crossing a rope bridge over a gorge",
        "has_people": True,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090306_4faf11f6-ecf4-4229-99b1-6cba77cbd338.png",
        "animate_prompt": "The knight steps carefully across the swaying rope bridge, fog drifting steadily through the gorge below. Cool dusk light shifts softly across the jagged cliffs. The camera tracks slowly alongside him, wide enough to keep the bridge and gorge in frame. A fair amount of movement throughout, somber and nostalgic, no text",
    },
    {
        "title": "withered orchard with a scarecrow",
        "has_people": False,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090326_64c5b73d-a01a-4b23-a857-d8985cb8a4c5.png",
        "animate_prompt": "The scarecrow's tattered sleeves sway faintly in the cold wind. Bare twisted branches creak softly overhead. Dead leaves drift slowly across the ground. The camera drifts slowly forward through the orchard, revealing more of the grey overcast sky. A fair amount of movement throughout, somber and quiet, no text",
    },
    {
        "title": "grimy knight resting against a fallen statue",
        "has_people": True,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090344_9ba9304e-6708-4561-8390-6abb9c248d18.png",
        "animate_prompt": "The knight sits still as mist drifts slowly through the towering trees around him. Fading cool light shifts softly across the moss-covered stone. A few leaves drift down. The camera slowly zooms out, revealing more of the misty forest around him. A fair amount of movement throughout, somber and tender, no text",
    },
    {
        "title": "foggy harbor town at night with a lighthouse",
        "has_people": False,
        "mood": "dark",
        "image_url": "https://d8j0ntlcm91z4.cloudfront.net/user_3Ds4y4BMM0lylxBEO2zlV6BNZub/hf_20261002_090404_c10fd5d2-efe2-43fa-920d-301ac49a4c3d.png",
        "animate_prompt": "The lighthouse beam sweeps slowly and steadily across the dark water. Fog drifts gently along the shore. Faint stars shimmer in the deep night sky. The camera drifts slowly forward over the water, revealing more of the harbor town silhouette. A fair amount of movement throughout, somber and atmospheric, no text",
    },
]

"""Tests for description parsing."""

from mcoding_youtube.description_parsing import parts_to_description_v2, description_to_parts

sample_description_0_v1 = """Sign up on Patreon to get your donor role and early access to videos!
https://patreon.com/mCoding

Feeling generous but don't have a Patreon? Donate via PayPal! (No sign up needed.)
https://www.paypal.com/donate/?hosted_button_id=VJY5SLZ8BJHEE

IN THIS VIDEO...
---------------------------------------------------
In this follow-up video I answer some commonly asked viewer submitted questions about Python 3.10's new match statement.

― mCoding with James Murphy (https://mcoding.io)

First match statement video: https://youtu.be/-79HGfWmH_w

BE ACTIVE IN MY COMMUNITY 😄
---------------------------------------------------
Discord: https://discord.gg/Ye9yJtZQuN
Github: https://github.com/mCodingLLC/
Reddit: https://www.reddit.com/r/mCoding/
Facebook: https://www.facebook.com/james.mcoding"""

sample_description_0_v2 = """In this follow-up video I answer some commonly asked viewer submitted questions about Python 3.10's new match statement.

― mCoding with James Murphy (https://mcoding.io)

First match statement video: https://youtu.be/-79HGfWmH_w

SUPPORT ME ⭐
---------------------------------------------------
Sign up on Patreon to get your donor role and early access to videos!
https://patreon.com/mCoding

Feeling generous but don't have a Patreon? Donate via PayPal! (No sign up needed.)
https://www.paypal.com/donate/?hosted_button_id=VJY5SLZ8BJHEE

BE ACTIVE IN MY COMMUNITY 😄
---------------------------------------------------
Discord: https://discord.gg/Ye9yJtZQuN
Github: https://github.com/mCodingLLC/
Reddit: https://www.reddit.com/r/mCoding/
Facebook: https://www.facebook.com/james.mcoding"""

sample_description_1_v1_and_v2 = """Try Anvil: https://anvil.works/mcoding

IN THIS VIDEO...
---------------------------------------------------
Most programming languages use a shared standard (IEEE 754 floating point numbers) for how to represent floating point numbers like 0.1. In this video, we see how these floats are represented and how this can cause unexpected results like 0.1 + 0.2 != 0.3.

― mCoding with James Murphy (https://mcoding.io)

Source code: https://github.com/mCodingLLC/VideosSampleCode

SUPPORT ME ⭐
---------------------------------------------------
Sign up on Patreon to get your donor role and early access to videos!
https://patreon.com/mCoding

Feeling generous but don't have a Patreon? Donate via PayPal! (No sign up needed.)
https://www.paypal.com/donate/?hosted_button_id=VJY5SLZ8BJHEE

BE ACTIVE IN MY COMMUNITY 😄
---------------------------------------------------
Discord: https://discord.gg/Ye9yJtZQuN
Github: https://github.com/mCodingLLC/
Reddit: https://www.reddit.com/r/mCoding/
Facebook: https://www.facebook.com/james.mcoding"""

sample_description_2_v1 = """Sign up on Patreon to get your donor role and early access to videos!
https://patreon.com/mCoding

Feeling generous but don't have a Patreon? Donate via PayPal! (No sign up needed.)
https://www.paypal.com/donate/?hosted_button_id=VJY5SLZ8BJHEE

IN THIS VIDEO...
---------------------------------------------------
⚠️Warning! Staring may cause visual distortions when you look away.

This took my poor laptop over a week to render so please slap the subscribe button if you liked the video!

Every second, the x-axis doubles, every 2 seconds the y-axis doubles, giving zoom factors of 2^1800 and 2^900!

The colors are determined by the values on the right hand side, so on the left they are chaotic, and on the right they are ordered.

― mCoding with James Murphy (https://mcoding.io)

BE ACTIVE IN MY COMMUNITY 😄
---------------------------------------------------
Discord: https://discord.gg/Ye9yJtZQuN
Github: https://github.com/mCodingLLC/
Reddit: https://www.reddit.com/r/mCoding/
Facebook: https://www.facebook.com/james.mcoding

MUSIC
---------------------------------------------------
All music in this video (including the specific performances) is in the public domain:

0:00, 5:30, 7:42
Moonlight Sonata, Op. 27 No. 2, Movements I, II, III
Beethoven

15:58
Fantaisie-Impromptu, Op. 66
Chopin

21:24
Morceaux de fantaisie, Op. 3
Rachmaninoff

25:05
Nocturne in E flat major, Op. 9 No. 2
Chopin"""

sample_description_2_v2 = """⚠️Warning! Staring may cause visual distortions when you look away.

This took my poor laptop over a week to render so please slap the subscribe button if you liked the video!

Every second, the x-axis doubles, every 2 seconds the y-axis doubles, giving zoom factors of 2^1800 and 2^900!

The colors are determined by the values on the right hand side, so on the left they are chaotic, and on the right they are ordered.

― mCoding with James Murphy (https://mcoding.io)

SUPPORT ME ⭐
---------------------------------------------------
Sign up on Patreon to get your donor role and early access to videos!
https://patreon.com/mCoding

Feeling generous but don't have a Patreon? Donate via PayPal! (No sign up needed.)
https://www.paypal.com/donate/?hosted_button_id=VJY5SLZ8BJHEE

BE ACTIVE IN MY COMMUNITY 😄
---------------------------------------------------
Discord: https://discord.gg/Ye9yJtZQuN
Github: https://github.com/mCodingLLC/
Reddit: https://www.reddit.com/r/mCoding/
Facebook: https://www.facebook.com/james.mcoding

MUSIC
---------------------------------------------------
All music in this video (including the specific performances) is in the public domain:

0:00, 5:30, 7:42
Moonlight Sonata, Op. 27 No. 2, Movements I, II, III
Beethoven

15:58
Fantaisie-Impromptu, Op. 66
Chopin

21:24
Morceaux de fantaisie, Op. 3
Rachmaninoff

25:05
Nocturne in E flat major, Op. 9 No. 2
Chopin"""

sample_description_3_v1 = """Sign up on Patreon to get your donor role and early access to videos!
https://patreon.com/mCoding

Feeling generous but don't have a Patreon? Donate via PayPal! (No sign up needed.)
https://www.paypal.com/donate/?hosted_button_id=VJY5SLZ8BJHEE

IN THIS VIDEO...
---------------------------------------------------
The story of how I used Python and the YouTube Data API (v3) to update all of my video descriptions. This would be a great starting point for anyone else looking to get into using the YouTube Data API.

― mCoding with James Murphy (https://mcoding.io)

Source code: https://github.com/mCodingLLC/mCodingYoutube
YT API docs: https://developers.google.com/youtube/v3/docs
Official YT API sample code: https://github.com/youtube/api-samples/tree/master/python
Google Cloud console: https://console.cloud.google.com/

BE ACTIVE IN MY COMMUNITY 😄
---------------------------------------------------
Discord: https://discord.gg/Ye9yJtZQuN
Github: https://github.com/mCodingLLC/
Reddit: https://www.reddit.com/r/mCoding/
Facebook: https://www.facebook.com/james.mcoding

MUSIC
---------------------------------------------------
Local Elevator by Kevin MacLeod is licensed under a Creative Commons Attribution 4.0 license. https://creativecommons.org/licenses/by/4.0/

Source: http://incompetech.com/music/royalty-free/index.html?isrc=USUAN1300012

Artist: http://incompetech.com/

CHAPTERS
---------------------------------------------------
00:00 Intro
00:35 Set up the API
01:44 Download a video's data
04:26 Download many videos
06:03 Updating descriptions
09:52 Retrospective"""

sample_description_3_v2 = """The story of how I used Python and the YouTube Data API (v3) to update all of my video descriptions. This would be a great starting point for anyone else looking to get into using the YouTube Data API.

― mCoding with James Murphy (https://mcoding.io)

Source code: https://github.com/mCodingLLC/mCodingYoutube
YT API docs: https://developers.google.com/youtube/v3/docs
Official YT API sample code: https://github.com/youtube/api-samples/tree/master/python
Google Cloud console: https://console.cloud.google.com/

SUPPORT ME ⭐
---------------------------------------------------
Sign up on Patreon to get your donor role and early access to videos!
https://patreon.com/mCoding

Feeling generous but don't have a Patreon? Donate via PayPal! (No sign up needed.)
https://www.paypal.com/donate/?hosted_button_id=VJY5SLZ8BJHEE

BE ACTIVE IN MY COMMUNITY 😄
---------------------------------------------------
Discord: https://discord.gg/Ye9yJtZQuN
Github: https://github.com/mCodingLLC/
Reddit: https://www.reddit.com/r/mCoding/
Facebook: https://www.facebook.com/james.mcoding

MUSIC
---------------------------------------------------
Local Elevator by Kevin MacLeod is licensed under a Creative Commons Attribution 4.0 license. https://creativecommons.org/licenses/by/4.0/

Source: http://incompetech.com/music/royalty-free/index.html?isrc=USUAN1300012

Artist: http://incompetech.com/

CHAPTERS
---------------------------------------------------
00:00 Intro
00:35 Set up the API
01:44 Download a video's data
04:26 Download many videos
06:03 Updating descriptions
09:52 Retrospective"""


def test_deconstruct_reconstruct():
    assert parts_to_description_v2(description_to_parts(sample_description_0_v1)) == sample_description_0_v2
    assert parts_to_description_v2(description_to_parts(sample_description_1_v1_and_v2)) == sample_description_1_v1_and_v2
    assert parts_to_description_v2(description_to_parts(sample_description_2_v1)) == sample_description_2_v2
    assert parts_to_description_v2(description_to_parts(sample_description_3_v1)) == sample_description_3_v2

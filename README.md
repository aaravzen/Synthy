# Synthy
Hardware Audio Synthesizer, Groovebox, and Media Player (maybe lol)

# Inspiration
- [Otem Rellik](http://www.otemrellik.com/) - [Raspi Looper/Groovebox](https://youtu.be/_nBK8sAl9nw) and [Teensy Polyphonic Synth](https://youtu.be/KbcNqarBTsI)
- [Prajwal Mahesh](https://youtu.be/yj9AeDa9qw8) - Teensy OP-1 [code here](https://github.com/prajwal1121/Portable-Synth)
- [Teenage Engineering](https://teenage.engineering/) - Pocket Operators, OP-1/OP-Z
- [Synthstrom Deluge](https://synthstrom.com/product/deluge/)
- [Zack Freedman](https://www.youtube.com/channel/UCUW49KGPezggFi0PGyDvcvg) - [How to Finish Your Weekend Projects in One Weekend Macro Pad](https://www.youtube.com/watch?v=72a85tWOJVY)
- [OTTO](https://github.com/bitfieldaudio/OTTO)
- [mta.me](http://mta.me/)
- [song makers](https://musiclab.chromeexperiments.com/Song-Maker/)
- [Flip Sampler](https://www.flipsampler.com/)
- [Count to 5 Effects Pedal](https://mtlasm.blogspot.com/p/count-to.html) - pitch/speed/direction effects

# Software Options
- [Patchbox OS (raspi distro for audio projects)](https://blokas.io/patchbox-os/)
- [Automatonism (Pure Data based modular synthesis)](https://www.automatonism.com/)
- [jFugue (Java)](http://www.jfugue.org/)
- [Synthesis ToolKit (C++)](https://ccrma.stanford.edu/software/stk/)
- [Maximilian (C++ w/ js bindings)](https://github.com/micknoise/Maximilian)
- [Gamma (C++)](https://w2.mat.ucsb.edu/gamma/)
- [Good resource - musicdsp.org](https://www.musicdsp.org/en/latest/)
- [Musical Programming Langs](https://en.wikipedia.org/wiki/List_of_audio_programming_languages)

# Software Ideation
- If we can write a wrapper that surrounds some of the above software options/inspiration that provides the capability to sample and sequence/loop (basically a hardware format of [this](https://youtu.be/kxV60u_OAuI) functionality) that would be ideal.
- We probably need a way to do the following things:

|Goals|Considerations|
--- | ---
|Sampling|Be able to record up to 16 sounds on a sample pad|
|Replaying|Be able to play the samples pitched to a keyboard|
|Looping/Sequencing|Be able to record samples into loops - either by playing live or by placing notes down a la deluge|
|Effects/Automation| Be able to add Reverb, Delay, Chorus, Butcrush, etc to the loops. I'm thinking about having the 4x8 bottom section being a place to set the general shape of an envelope/automation and then having one of the knobs be able to "soften" the shape into less immediate quantization jumps|
|Sequence Ordering|Be able to arrange different sections of different instruments (samples) into a full song|
|Mixing|This should just be a reskinned view of volume automation params that are already covered by effects/sequence ordering (?)|
|Interplay|May eventually want to add [Ableton Link](https://ableton.github.io/link/)|


# Considerations
|Goals |Requirements |
--- | ---
|Sequencing/beatmaking ability|SD Storage for samples|
| |3.5mm audio jack (2x one in one out?)|
| |buttons, potentiometers, and sliders for controls.|
|Synthesis|Instead of sequencing, could use the buttons as a keyboard and synthesize sounds using eg. Pure Data|
| |I'm not certain, but I don't think this would add hardware constraints. What we can do will be limited by compute, etc, but I don't think I have any special considerations|
|Sampling|One consideration for sampling is sound inputs, it would be nice to be able to record new sounds somehow. But the bare minimum for sampling would be viable with preloaded sound files off an SD|
|MP3 Playing|If we can get audio out and we have SD storage, we should be able to play mp3 files through an audio jack as well. should be an easy stretch goal plus I can actually use one since my phone doesn't have an aux out anymore|
| |We could add playback effects or something fun? Make a spinning potentiometer record scratch or something|
|MIDI controls|Use the same buttons as a MIDI controller|
| |Needs USB out or similar to connect to computer|
|Mode switcher|Way to change between sequencer/synthesizer, mp3 player, midi controller. Maybe something like [this](https://www.adafruit.com/product/2925)|
|Screen?|Would be cool to have some amount of display, especially if we want an actually usable MP3 player and a groovebox that's easy to understand|
|Stereo In/Out|To play from an amp or in line with other 1/4" stuff. Not sure how difficult it would be to add two of [these](https://www.adafruit.com/product/1804)|
|Midi In/Out|It would be sorta based if I could route MIDI into this from, eg, my digital piano for it to translate to my computer. But it's probably not worth the effort to make this into a MIDI audio interface|
|Stretch Goals|Unimportant rn but just so I remember: we'll eventually have to get this to run Doom for it to be considered completely finished|

# Parts
|Purpose|Options|
--- | ---
|Buttons|[neotrellis pcb+buttons](https://www.adafruit.com/product/3954) are $17.50 for 4x4. I'm thinking $35 per box for those.|
| |With the neotrellis, we may need this type of [breakout board](https://www.adafruit.com/product/3657) = ~$5|
| | May also want something like [this](https://www.adafruit.com/product/4184) set of a lot of buttons|
|Pots/Sliders| ??? we probably want some, idk which yet. maybe [these](https://www.adafruit.com/product/2058) |
| |These sorta [encoders](https://www.digikey.com/en/products/detail/bourns-inc/PEC11R-4115K-S0018/4699207) with switches are what Prajwal used - $2 per, ~4 per board would be $8|
| |Sliders like [this](https://www.digikey.com/en/products/detail/bourns-inc/PTA4543-2010CIB103/3781197) would run us ~$1.5 per as well. I'd like to add at least a couple analog inputs, which these would work for.|
| |Potentially a small joystick like the [PSP ones](https://www.adafruit.com/?q=PSP+joystick&sort=BestMatch) would be good with something like [this](https://www.adafruit.com/product/3246)|
|LEDs| need these too |
|Computer and sound|Teensy 4.1 ($27) + Audio Adapter ($16) = ~43|
| |[Teensy PSRM](https://www.pjrc.com/store/psram.html)|
| |Raspi ($10-45) + Audio Bonnet ($10) = ~$45|
| |Raspi ($10-45) + Pirate Audio Audio/Screen ($25) = ~$60|
|Display|[Waveshare 1.5" colored OLED](https://www.amazon.com/1-5inch-RGB-OLED-Module-Communicating/dp/B07DB5YFGW) - $19|
| |[LED Matrix](https://www.adafruit.com/product/420) = ~$25|
| |[Colored OLED 1.3"](https://www.adafruit.com/product/1673) = ~$30-40|
| |[Monochrome OLED 1.3"](https://www.adafruit.com/product/938) = ~$20|
| |[Baby Adafruit color 1.14"](https://www.adafruit.com/product/4383) = ~$10|
| |[1.8" Color TFT with joystick and 3 button inputs] = ~$35|
| |Maybe just a way to do HDMI out?|
| |Or potentially all communication can be done via LEDs. Very retro and some cost savings|
|SD Card|$8-30 depending on storage preferences. I'll probably go on the higher end here for additional music/sample storage|
|Audio In (sampling)|[Mic breakout board](https://www.adafruit.com/product/2716) = ~$5|
| |[Or this I2S one](https://www.adafruit.com/product/3421) = ~$7|
| |We may be able to leverage the line in off the [teensy audio shield](https://www.pjrc.com/store/teensy3_audio.html) for use with an external mic|
| |Prajwal used one of [these](https://www.sparkfun.com/products/11083) FM radio tuners to sample from the radio like the OP-1. pretty neat, ~$11|
| |May need something like [these](https://www.adafruit.com/product/1699) 3.5mm jacks|

# Future Goals
- Put it inside [this](https://preview.redd.it/2ar1ehv9xvg61.jpg?width=2075&format=pjpg&auto=webp&s=27cc71307f825115af33f410c18aa719e2d52dea) and it's the future of music. This is a bazillion dollar idea, easy.

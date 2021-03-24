# Synthy
Hardware Audio Synthesizer, Groovebox, and Media Player (maybe lol)

# Inspiration
- [Otem Rellik](http://www.otemrellik.com/) - [Raspi Looper/Groovebox](https://youtu.be/_nBK8sAl9nw) and [Teensy Polyphonic Synth](https://youtu.be/KbcNqarBTsI)
- [Prajwal Mahesh](https://youtu.be/yj9AeDa9qw8) - Teensy OP-1 [code here](https://github.com/prajwal1121/Portable-Synth)
- [Teenage Engineering](https://teenage.engineering/) - Pocket Operators, OP-1/OP-Z
- [Synthstrom Deluge](https://synthstrom.com/product/deluge/)

# Considerations
|Goals |Requirements |
--- | ---
|Sequencing/beatmaking ability|SD Storage for samples|
| |3.5mm audio jack|
| |buttons, potentiometers, and sliders for controls.|
|Synthesis|Instead of sequencing, could use the buttons as a keyboard and synthesize sounds using eg. Pure Data|
| |I'm not certain, but I don't think this would add hardware constraints. What we can do will be limited by compute, etc, but I don't think I have any special considerations|
|MP3 Playing|If we can get audio out and we have SD storage, we should be able to play mp3 files through an audio jack as well. should be an easy stretch goal plus I can actually use one since my phone doesn't have an aux out anymore|
| |We could add playback effects or something fun? Make a spinning potentiometer record scratch or something|
|MIDI controls|Use the same buttons as a MIDI controller|
| |Needs USB out or similar to connect to computer|
|Mode switcher|Way to change between sequencer/synthesizer, mp3 player, midi controller. Maybe something like [this](https://www.adafruit.com/product/2925)|
|Screen?|Would be cool to have some amount of display, especially if we want an actually usable MP3 player and a groovebox that's easy to understand|

# Parts
|Purpose|Options|
--- | ---
|Buttons|[neotrellis pcb+buttons](https://www.adafruit.com/product/3954) are $17.50 for 4x4. I'm thinking $35 per box for those.|
| | May also want something like [this](https://www.adafruit.com/product/4184)|
|Pots/Sliders| ??? we need some, idk which yet. maybe [these](https://www.adafruit.com/product/2058) |
|LEDs| need these too |
|Computer and sound|Teensy 4.1 ($27) + Audio Adapter ($16) = ~43|
| |Raspi ($10-45) + Audio Bonnet ($10) = ~$45|
| |Raspi ($10-45) + Pirate Audio Audio/Screen ($25) = ~$60|
|Display|[LED Matrix](https://www.adafruit.com/product/420) = ~$25|
| |[Colored OLED 1.3"](https://www.adafruit.com/product/1673) = ~$30-40|
| |[Monochrome OLED 1.3"](https://www.adafruit.com/product/938) = ~$20|
| |Maybe just a way to do HDMI out?|
| |Or potentially all communication can be done via LEDs. Very retro and some cost savings|
|SD Card|$8-30 depending on storage preferences. I'll probably go on the higher end here for additional music/sample storage|

--- 
layout: page
title: "Project Documentation" 
description:
image: /assets/images/doc/Alien_main.jpg
author: Chris Correll
tags: 
--- 

# Emoji Earring Project 

This is the documentation website for a project I undertook in February through April of 2020. I am just now getting around to documenting everything (its December 2021) because I need to wrap up the project so I can feel good about moving on to other designs. What follows is a as comprehensive as I could manage effort to document the whole process from design to manufacturing to marketing. I made a lot of mistake, learned a lot, and over all enjoyed the process immensely (or atleast most parts of the process 😉). Enjoy! 

## Project Background
The project all began when I got my ears pierced...
![Chris with pierced ears](/assets/images/doc/pierced_ears.png)
I am a hardware nerd at heart and love all things that go blink so I figured a great project would be designing some cool interactive earings. After researching what existed out there and finding that almost everything was either lame or not my style (the folks at [CaliforniaSteam on Tindie](https://www.tindie.com/stores/californiasteam/) are doing cool things but not quite what I wanted) ![Lame earring](/assets/images/doc/prior_art.png) I figured it was best to DIY. Additionally, I wanted to know what it would be like to take multiple designs from idea to product line, as well as a personal challenge, see if I could make something that people would actually want to buy. Thusly emoji earrings was born 👂👶.

## Initial Designs

I can't remember how I first came up with the idea to use emojis specifically I think it had something to do with my limited design skills and coming across a trove of open source SVG files for emojis. Perhaps I could just say it came to me out of the ether and leave it at that. After ideating on several different ideas from simple geometric shapes to more complex fractal esque designs I decided to go with a less is more approach and pick something that was universally loved and that I could easily acquire design files for [open source emojis!](https://github.com/hfg-gmuend/openmoji).

After I had figured out the concept for my product line I began thinking about the circuit design. Originally I wanted to do something very circuit heavy with a SAMD microcontroller, a rechargable LiPo battery, and individually addressable LEDs, but I had to remind myself of my limited soldering set up (hot air gun and manual tweezers, see Assembly & Manufacturing section below) and that the focus on the project was creating and manufacturing a product to sell not winning a hacakday hardware design competition... ![Earring schematic](/assets/images/doc/devil_sch.png) I also decided that I wanted to do one of my favorite emojis the smiley devil so that maybe later on I could also do an angel as well (which I did)!

With a schematic designed I started thinking about parts and board dimensions. I knew I wanted the earrings to be light and small as well I wanted them to be cheap to make, so I scoured digikey and mouser for parts and eventually came up with a high level bill of materials (BOM) that I could base my designs around. I went ahead and ordered some of the parts for prototyping. ![Devil high level BOM](/assets/images/doc/devil_bom_ideas.png) 

With a schematic and a first pass at a BOM it was time to start designing in Eagle. The first challenge was getting the board outline and art into Eagle. Eagle is not made for PCB art but a few smart people have figured out how to finagle it into getting great results. I ended finding [this video by Hackster.io](https://www.youtube.com/watch?v=Wu3JGQQvobg) that made the process super straightforward (well maybe just kind of straight forward). I got my art design from svg to illustrator and then split it up into layers for the pcb art. For a more in depth discussion of what I had to do check out the video above. I also made sure to print my designs on paper to make sure I got a good size for the board.
![This is a design I have I split things up into layers and export them all individually](/assets/images/doc/laugh_cry_illustrator.png)
*This is a design I have in illustrator its not the devil design but one I did not end up manufacturing. I split each layer up so I can export and import them into the correct board layer in EAGLE. Its all covered in the wonderful tutorial video linked above (seriously watch that whole video its great).*

Once I got a good size in illustrator I brought my PCB art layers into Eagle starting with the dimension first. Pretty early on I nixed the cr2032 battery design as it was too big for my liking. So I had one BOM item with different foot prints crossed out but was still un decided on a switch, so I ended up designing two different boards. I spent a lot of time thinking about layout for these boards. I would constantly print and then layout my components on printouts of the front and back of the board this really helped make sure I would be able to assemble a bunch of these by hand and that I could minimize the size of the boards and maintain enough clearance for someone to change out the battery. 

![Devil final board design](/assets/images/doc/devil_dim_brd.png)
*Dimensions are in millimeters*

## First Prototypes
![First Prototype](/assets/images/doc/2devil_proto.png)
*First prototype noticed that the face plate is a little smaller than the board outline. Also this was not yet glued hence out of alignment.*

I got the details as perfect as I could manage and I put in two orders to OSH park for some boards. While I was waiting for the OSH park orders a friend of mine who had access to a cnc mill offered to mill out one of my designs for beer (thanks Zoltan!) so I ended up getting the chunkier switch design in before the boards. I soldered it up and it all worked! I then proceeded to test different resistor values and leds to find the best brightness for lowest current consumption (V=IR thanks math!). I ended settling on 2.2k, also had a lot of those around in 0603 packages. When I had the boards soldered up I had the idea of adding an acrylic faceplate to it to add some heft and more interest to the design as it was still very light. Since I already had the vector file of the outline from desiging the outline cutting it out on a friends laser cutter was pretty straight forward. Unfortunately I didn't realize that the milled circuit board dimensions were slightly larger than the design file so the first pass had the board peaking out from underneath. I went ahead and dialted the vector file slightly just in case as I was fine with a little bit of acrylic face plate over hang but not with any board showing underneath the acrylic outline.
![Clear frosted acrylic faceplate](/assets/images/doc/clear_frosted_face_plate.png)
Originally I was gonna go with a clear frosted acrylic as I thought it might diffuse some of the light interestingly but I did not really do much as the angle that the light was being emitted was not all that wide so it just shot throug the eye holes in the acrylic. So I decided on going with a pink sheet of acrylic. 

![Alien board design](/assets/images/doc/alien_dim_brd.png)
*Dimensions are in millimeters*

While I was waiting on boards to come in I also started designing my second piece an alien emoji. This design went a little quicker since I had gotten the PCB art Eagle design process down better. Once I was happy with the design I went ahead and ordered some boards from PCB Way. I love OSH park but I had to do the alien in green also I wanted to see what a thinner board felt like. With two different designs under way I decided to get organized a created some project organization bags.

![Project Organization bags post project so they are full](/assets/images/doc/project_manufacturing organization_bags.png)
*Project Organization bags post project so they are full*

Also being PCB Way where 5 boards and 50 boards have a cost differential of about $20 I went ahead and bought a bunch (like 60), a mistake I would later come to regret... 

![Tiny switch](/assets/images/doc/so_small_switch.png)
*So smol*

Around 2 weeks later I got the devil boards back from OSH park. I soldered up both a chunky switch and a small switch design they both worked great, but the small switch was very cumbersome to turn off and on so I ditched it. I had my BOM finalized so I but in an order to OSH park for 48 boards and then bought all my parts plus around 5% extra from digikey. While the boards from PCB Way's cost scaled well, parts and OSH park boards did not so I ended up spending a bunch of money, but no big deal I would recoup that cost by selling them, little did I know...

![Laser cut green faceplate](/assets/images/doc/green_face_plate.png)
Once I got the aliens back I started experimenting with laser cut face plates for them and found that I liked a transulent green finish instead of a solid green finish. I liked being able to see the pcb board underneath. This would lead to some minor issues later during assembly and manufacturing. 

## Assembly & Manufacturing

![Ready to Assemble](/assets/images/doc/ready_to_assemble.png)

Now that I had all the boards it was time to start manufacturing and assembly. This is the part of the process that I really started to loathe. Assembling over 100 circuit boards with a hot air gun and soldering iron is hell, I really feel for those factory workers. My set up could have definietly been better and eventually I did get a small reflow over from a friend (thanks again Zolatan!) and cut out some solder stencil out of kapton, but I defintely learned that while assemblying prototypes is fun, assemblying for manufacturing is work. I ended up making it through about 1/2 of the boards before throwing in the towel.
![So many boards](/assets/images/doc/so_many_boards.png)
 
All in all it was sometimes nice to get in a flow for a couple of hours and knock out 8 or 9 boards but I know now why a pick and place machine exits. I didn't have a nice microscope to aide in hand placement and I definitely got eye strain over a stretch of time. I think in the future getting a set up similar to [this guy](https://www.youtube.com/watch?v=HmPYuOIMDJs) would be useful. I still have around 50 or so unassembled baords and maybe one day I will get to making them but I am happy with having made as many earring pairs as I did.

![Laser cut sheet of alien faceplates](/assets/images/doc/laser_Cut_sheet.jpeg)
In addition to the PCB assembly process I also had to figure out an assembly process for the acrylic face plates. Laser cutting the acrylic ended up being a little trickier then I thought. I wasn't working with the best machine out their and it did take a couple of passes to get through the acrylic. As well the laser strength would sometimes leave marks on the acrylic. For the solid pink devil face plates this was not as much as of an issue. I could just flip them over and use the unmarred side but I had to trash some of the alien face plates good thing I ended up cutting like 30 extra since I had the acrylic and it was relatively unexpensive.

![Laser cut devil faceplates](/assets/images/doc/laser_cut_devil.jpg)

I also found that putting a sheet of black paper underneath the acrylic helped with some marks. In the future though I think the best bet is to tune the machine a little bit better with scraps of the material.

With all of the faceplates I had to figure out a way to glue them on to my assembled board. For the solid faceplates it was easy I would just use CA (super) glue and then clothes pin the faceplates to clamp it down in place as it dried. For the translucent acrylic though I ran into some issues with CA glue artifacts.

![Glue artifacts](/assets/images/doc/glue_artifacts.png)

Apparently CA glue has a tendency to fog plastic when it dries. I read on [the internet](https://www.reddit.com/r/modelmakers/comments/2ru0co/stupid_question_when_working_with_super_glue_how/) that this might be due to lack of air circulation so I tried pointing the heat gun at the pieces as they dried this kind of helped but still was having so issues. So I ended up going with a CA accelerator (no more clothes pins!) and a more conservative application of the super glue. This helped but still I would get some pieces that still fogged a noticable amount. I think in the future going with a bi-component cement glue or polystyrene glue would be a better bet I just had a lot of CA glue and I was not able to find the aforementioned at the local hardware store. Also I grew to kind of like the look of the fog on the face plates. That said this is one area I would definitely like to improve on if I finish the rest of the boards ever.

![Not enough glue](/assets/images/doc/not_enough_glue.png)
*Conservatively apply super glue but enough that it bonds!*

![Gluing process finalized](/assets/images/doc/gluing_final.png)
*Final gluing process*

![Hot air gun reflowing](/assets/images/doc/hot_air_reflow.png)
Eventually I figured out a nice assebly process, it ended up being as follows:
- Gather components and get ready to assemble (see photo at beginning of section)
- Apply solder paste using stencil or by hand (I found that going by hand was actually faster)
- Use tweezers to place components on bottom of boards
- Reflow components
- Fix any components that might have not seated properly during the reflow stage
- Test to make sure connections are sound
- Hand solder or use the hot air gun to reflow the leds on the top part of the board 
- Test that the board works with a test battery 
- Once the board has been confirmed to work file down the edges of the board where they were depanelized using side cutters and sand paper 
- Add marker to the exposed fr4 so it matches the solder mask color
- Apply super glue to the front of the board and accelerator to the faceplate and bind them work quickly you will only have like 1-2 seconds before it bonds
- Attach earring hardware
- Enjoy!

![Final Products](/assets/images/doc/devil_alien.jpg)
*These but like times 10*

## Standardizing the Design process
![Design check list](/assets/images/doc/design_checks.png)

Once I had gotten through the first batch of manufacturing (well half of the first batch) I was hungry to get back to designing more earrings as that was what I really enjoyed. So I took what I learnt from designing and building the first batch of devils and aliens and formalized a design checklist to help guide my design process for the board files. Things ended up going a lot faster once I had the checklist and I added to it as I made more designs!

## More Designs!
I ended up designing and manufacturing (albeit in much smaller quantities) 5 other designs, and designed 3 that I did not end up getting made. I didn't have access to a laser cutter at the time so they did not have any faceplates, but I was happy with how they turned out. 

![Skull pcbs](/assets/images/doc/all_skulls.jpg)
Continuing with emoji theme I made a couple of skulls in multiple colors as well as an angel to compliment by devil work. 

![Designs not yet made](/assets/images/doc/cry_gold.png)
I also made a couple of other designs that I did not end up making.

Check out the gallery for more pictures and [the project github](https://github.com/funkonaut/Earrings) for more pictures and design files!

![Cross with red LED](/assets/images/cross/cross_iso.jpg)
The cross didn't really fit the theme but I was feeling gothic, and wanted to see how far I could push OSH parks fabrication. It turns out really far! This also gave me some great ideas for future earring projects. I cheated on the circuit design and found some integrated LEDs and IC that had the LED color cycle... 

## Marketing
![Bedroom photography studio set up](/assets/images/doc/studio_setup.jpg)

It turns out you can get pretty solid shots with a roll of paper, some lamps and a mid level dslr (oh and photoshop...). 

I learned a lot preparing marketing shots and content, namely that its okay. I enjoy it way more then assembly and manufacturing but not as much as design. I also learned that you got to check you settings half way through the shoot I realized I was not shooting in raw so some of my images vary in quality. Most importantly I learned that you got to take more photos than you think necessary because it is hard to go back and get consistent lighting especially in a make shift studio. Oh and having a shot list help guide your photo session is very helpful!

## Sales and Logistics
![Etsy logo](/assets/images/doc/Etsy_logo.png)
With all my marketing content prepared I opened my Etsy shop. I am pretty sure all of my purchases were friends and family, though I think I had one or two strangers grab a pair which was pretty cool.

![Market set up](/assets/images/doc/market.jpg)
*I also sold at a friends out door market. I remixed some of the earrings into beaded necklaces and bracelets which was fun but I think I like them better as earrings.*

Packaging the earrings and sending them out was not too difficult. I just put them in anti static bags and had Etsy generate the shipping labels. Eventually I made the decision to close down the shop as I did not really care to promote the project much more then just to friends and family after selling around 15 pairs of earrings and giving away around 5 more. I also did not end up posting on [Tindie](https://www.tindie.com/), an option I would probably like to explore more in the future.

![Devil marketing shot](/assets/images/doc/Devil_main.jpg)
*Goodbye Etsy for now...*

## BOMbing it
![Devil final BOM and cost break down](/assets/images/doc/devil_bom_clean.png)
*Per earring cost for the devil design*

Each earring ended up costing around $4 and around 30 minutes to assemble (I am slow :/) the electronics, faceplate, and earring hardware. At $8 per pair and around an hour of labor I decided to charge $24.99 for each earring pair. 

![Expenses list](/assets/images/doc/expenses.png)
I ended up spending almost $900 for the project and made back $400. So I lost $500 when it was all said and done. I still have a fair amount of unassembled merch and if I were to assemble and sell all of those I would gross a couple of hundred of dollars, but this was never about making money, it was about learning!

## Back to the Drawing Board...
Perhaps the most valuable lesson I found after the whole ordeal of trying to sell and market things, is that I really enjoy the design and prototyping process much more than the whole selling, assembling and manufacturing the designs. I guess I could always have a PCB assembly house manufacture things but I am not sure if I feel great about that especially after experiencing how rough that work is first hand (I get they have pick and place machines but still really thankful for those manufacturing employees). Also a PCBA process costs at the cheapest like $5 extra per board so would bring the cost of the earrings closer to $20 which is a pretty alright profit margin at scale but I am not super interested in making and marketing these things at scale.

### Here is a list of my main project take aways:
- Probably dont tie large copper pours meant for aesthetics to signals to prevent accidentally shorting
- Probably coat dangling metal or large copper pours so it doesnt short things
- Defintely add short protection for that coin cell
- Go small when purchasing, just because you can buy large quantities does not mean you should!
- Gotta give myself easier tolerances for assembling these things I have bigger resistors probs should haev used them
- Documentation isnt all that bad do it as you go don't do it all at the end...
- Make sure Eagle has 3D packages attached to the parts you are designing with so you can get 3D models really easily
- Add more silkscreen assembly marks to help when manufacturing, you can always hide the marks under parts if you do not want them to show
- Add to github as you go, version control is your best friend...

Now that I can say I have wrapped up this project stay tuned for more cool earring projects with improved circuitry and even more aesthetic designs!

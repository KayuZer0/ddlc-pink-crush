label dayzero:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."
    $ s_name = "Sayori"
    show sayori 4p at t11 zorder 2
    s 4p "Haaahhh...haaahhh..."
    s "I overslept again!"
    s "But I caught you this time!"
    mc "Maybe, but only because I decided to stop and wait for you."
    show sayori at s11
    s 5c "Eeehhhhh, you say that like you were thinking about ignoring me!"
    s "That's mean, [player]!"
    mc "Well, if people stare at you for acting weird then I don't want them to think we're a couple or something."
    show sayori at t11 zorder 2
    s 1a "Fine, fine."
    s "But you did wait for me, after all."
    s "I guess you don't have it in you to be mean even if you want to~"
    mc "Whatever you say, Sayori..."
    s 1q "Ehehe~"
    show sayori at thide zorder 1
    hide sayori
    "We cross the street together and make our way to school."
    "As we draw near, the streets become increasingly speckled with other students making their daily commute."
    show sayori 3a at t11 zorder 2
    s "By the way, [player]..."
    s "Have you decided on a club to join yet?"
    mc "A club?"
    mc "I told you already, I'm really not interested in joining any clubs."
    mc "I haven't been looking, either."
    show sayori at s11
    s 4h "Eh? That's not true!"
    s "You told me you would join a club this year!"
    mc "Did I...?"
    "I'm sure it's possible that I did, in one of our many conversations where I dismissively go along with whatever she's going on about."
    "Sayori likes to worry a little too much about me, when I'm perfectly content just getting by on the average while spending my free time on games and anime."
    s 4j "Uh-huh!"
    s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
    s "Your happiness is really important to me, you know!"
    s "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
    s 4g "You trust me, right?"
    s "Don't make me keep worrying about you..."
    mc "Alright, alright..."
    mc "I'll look at a few clubs if it makes you happy."
    mc "No promises, though."
    s 1h "Will you at least promise me you'll try a little?"
    mc "Yeah, I guess I'll promise you that."
    show sayori at t11 zorder 2
    s 4r "Yaay~!"
    "Why do I let myself get lectured by such a carefree girl?"
    "More than that, I'm surprised I even let myself relent to her."
    "I guess seeing her worry so much about me makes me want to ease her mind at least a little bit - even if she does exaggerate everything inside of her head."

    scene bg class_day
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "Sayori wants me to check out some clubs."
    "I guess I have no choice but to start with the anime club..."

    s "Hellooo?"
    show sayori 1b at t11 zorder 2
    mc "Sayori...?"
    "Sayori must have come into the classroom while I was spacing out."
    "I look around and realize that I'm the only one left in the classroom."
    s 1a "I thought I'd catch you coming out of the classroom, but I saw you just sitting here and spacing out, so I came in."
    s "Honestly, you're even worse than me sometimes... I'm impressed!"
    mc "You don't need to wait up for me if it's going to make you late to your own club."
    s 1y "Well, I thought you might need some encouragement, so I thought, you know..."
    mc "Know what?"
    s 1a "Well, that you could come to my club!"
    mc "Sayori..."
    s 4r "Yeah??"
    mc "...There is no way I'm going to your club."
    show sayori at s11
    s 5d "Eeeehhhhh?! Meanie!"
    "Sayori is vice president of the Literature Club."
    "Not that I was ever aware that she had any interest in literature."
    "In fact, I'm 99\% sure she only did it because she thought it would be fun to help start a new club."
    "Since she was the first one to show interest after the one who proposed the club, she inherited the title \"Vice President\"."
    "That said, my interest in literature is guaranteed to be even less."
    mc "Yeah. I'm going to the anime club."
    show sayori at t11 zorder 2
    s 1g "C'mon, please?"
    mc "Why do you care so much, anyway?"
    s 5b "Well..."
    s "I kind of told the club yesterday I would bring in a new member..."
    s "And Natsuki made cupcakes and everything..."
    s "Ehehe..."
    mc "Don't make promises you can't keep!"
    "I can't tell if Sayori is really that much of an airhead, or if she's so cunning as to have planned all of this out."
    "I let out a long sigh."
    mc "Fine... I'll stop by for a cupcake, okay?"
    show sayori at h11
    s 4r "Yes! Let's go~!"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "And thus, today marks the day I sold my soul for a cupcake."
    "I dejectedly follow Sayori across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Sayori, full of energy, swings open the classroom door."

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "Everyone! The new member is here~!"
    mc "I told you, don't call me a 'new member--'"
    show sayori at lhide
    hide sayori
    "Eh? I glance around the room."
    show yuri 1a at t11 zorder 2
    y "Welcome to the Literature Club. It's a pleasure meeting you."
    y "Sayori always says nice things about you."
    show yuri at t22 zorder 2
    show natsuki 4c at t21 zorder 2
    n "Seriously? You brought a boy?"
    n "Way to kill the atmosphere."
    show yuri at t33 zorder 2
    show natsuki at t32 zorder 2
    show monika 1k at t31 zorder 2
    m "Ah, [player]! What a nice surprise!"
    m "Welcome to the club!"
    show monika 1a
    mc "..."
    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"

    show monika at thide zorder 1
    show yuri at thide zorder 1
    show natsuki at f32 zorder 3
    hide monika
    hide yuri

    n 2c "What are you looking at?"
    n "If you want to say something, say it."
    mc "S-Sorry..."
    show natsuki at t32 zorder 2
    show yuri 2l at f33 zorder 3
    y "Natsuki..."
    $ n_name = 'Natsuki'
    show yuri at t33 zorder 2
    show natsuki at f32 zorder 3
    n 5s "Hmph."
    show natsuki at t32 zorder 2

    "The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."
    "She is also the one who made cupcakes, according to Sayori."

    show sayori 2q at f31 zorder 3
    s "You can just ignore her when she gets moody~"
    "Sayori says that quietly into my ear, then turns back toward the other girls."
    s 1x "Anyway! This is Natsuki, always full of energy."
    s "And this is Yuri, the smartest in the club!"
    $ y_name = 'Yuri'
    show sayori at t31 zorder 2
    show yuri at f33 zorder 3
    y 4b "D-Don't say things like that..."
    "Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with people like Sayori and Natsuki."
    show yuri at t33 zorder 2
    mc "Ah... Well, it's nice to meet both of you."
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    hide yuri
    hide natsuki
    show sayori at f31 zorder 3
    s 1a "And it sounds like you already know Monika, is that right?"
    $ m_name = 'Monika'
    show sayori at t31 zorder 2
    show monika 2a at f32 zorder 3
    m "That's right."
    m "It's great to see you again, [player]."
    show monika 5a at hop
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Monika was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    "So, having her smile at me so genuinely feels a little..."
    mc "Y-You too, Monika."
    show monika at thide zorder 1
    hide monika
    show sayori at f31 zorder 3
    s 4x "Come sit down, [player]! We made room for you at the table, so you can sit next to me or Monika."
    s "I'll get the cupcakes~"
    show sayori at t31 zorder 2
    show natsuki 1e at f32 zorder 3
    n "Hey! I made them, I'll get them!"
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s 5a "Sorry, I got a little too excited~"
    show sayori at t31 zorder 2
    show yuri 1a at f33 zorder 3
    y "Then, how about I make some tea as well?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "The girls have a few desks arranged to form a table."
    "As Sayori mentioned, it's been widened so that there is one space next to Monika and one space next to Sayori."
    "Natsuki and Yuri walk over to the corner of the room, where Natsuki grabs a wrapped tray and Yuri opens the closet."
    "Still feeling awkward, I take a seat next to Sayori."
    "Natsuki proudly marches back to the table, tray in hand."
    show natsuki 2z at t32 zorder 2
    n "Okaaay, are you ready?"
    n "...Ta-daa!"
    show sayori 4m at t31 zorder 2
    show monika 2d at t33 zorder 2
    s "Uwooooah!"
    "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    "The whiskers are drawn with icing, and little pieces of chocolate were used to make ears."
    show sayori at f31 zorder 3
    s 4r "So cuuuute~!"
    show sayori at t31 zorder 2
    show monika at f33 zorder 3
    m 2b "I had no idea you were so good at baking, Natsuki!"
    show monika at t33 zorder 2
    show natsuki at f32 zorder 3
    n 2d "Ehehe. Well, you know."
    n "Just hurry and take one!"
    "Sayori grabs one first, then Monika. I follow."
    show natsuki at t32 zorder 2
    show sayori at f31 zorder 3
    s 4q "It's delicious!"
    "Sayori talks with her mouth full and has already managed to get icing on her face."
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show sayori at thide zorder 1
    show monika at thide zorder 1
    hide sayori
    hide monika
    show natsuki 1c at t32 zorder 2
    "Natsuki is quiet."
    "I can't help but notice her sneaking glances in my direction."
    "Is she waiting for me to take a bite?"
    "I finally bite down."
    "The icing is sweet and full of flavor - I wonder if she made it herself."
    mc "This is really good."
    mc "Thank you, Natsuki."
    n 5h "W-Why are you thanking me? It's not like I...!"
    "{i}(Haven't I heard this somewhere before...?){/i}"
    show natsuki at s32
    n 5s "...Made them for you or anything."
    mc "Eh? I thought you technically did. Sayori said--"
    show natsuki at t32 zorder 2
    n 12c "Well, maybe!"
    n "But not for, y-you know, {i}you!{/i} Dummy..."
    mc "Alright, alright..."
    show natsuki at thide zorder 1
    hide natsuki
    "I give up on Natsuki's weird logic and dismiss the conversation."
    "Yuri returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray."
    show yuri 1a at t21 zorder 2
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    show yuri at thide
    hide yuri
    with wipeleft
    "Yuri sits down in the empty space next to Monika."
    "The five of us calmly sit around the table, each doing their own."
    "Yuri pulls out a novel out of the bag below the table and begins to read, sipping from her cup of tea every other page."
    "Sayori and Monika each take another cupcake from the tray, and begin to eat while having a chat."
    scene bg club_day
    with wipeleft
    "We sit at the table like this for some some time, while we eat Natsuki's delicious cupcakes, with small chats in between bites."
    show natsuki 5s at t11 zorder 1
    "This whole time, I can't help but throw glances in Natsuki's direction from across the table."
    "There's... {i}something{/i} about her that doesn't let me look away."
    "It looks like she zoned out."
    show natsuki 5n
    "After a while, Natsuki seems to re-enter the real world as she glances at me."
    show natsuki 5s
    "It doesn't take a full half a second for her to look away."
    show natsuki at thide
    hide natsuki
    "Natsuki gets up from her seat and heads towards the corner of the room without saying a word."
    "Nobody but me seems to notice her leaving."
    show monika 1a at t11
    "As Monika and Sayori's chat comes to an end, Monika turns her attention to me."
    m 1b "So [player], since this is a literature club, I do have to ask: what do you like to read?"
    mc "W-well... I- Uuhhh..."
    "I was afraid of this question."
    "I really am not much of a reader."
    "Aside from the ocasional manga that I read, my experience with literature is practically non-existent."
    mc "...Manga..."
    "I mutter under my breath."
    m 2k "Not much of a reader, I guess."
    mc "Well, that can change."
    "I don't know what I'm saying."
    "I just spoke without thinking after realizing I just admitted to beeing a weeb in front of the most popular girl in school."
    mc "Anyway, what about you, Monika?"
    m 4b "Well..."
    m "I'm a big fan of the Detective and Mystery genre."
    m "You know, the kind of that make you think about a solution to the mystery along with the characters."
    m "Aside from being an exeptional read, it also tests your problem-solving skills."
    "Well, that was unexpected."
    "I never imagined that someone like Monika would be into Detective novels of all things."
    "But never judge a book by it's cover, I guess."
    m 1b "I read the classics, like 'The Adventures of Sherlock Holmes', but right now I'm midway through another title."
    m "Another good pick would be 'And Then There Were None', if you're ever interested in the genre."
    mc "Yeah, I might give them a try sometime."
    "I probably won't."
    show monika 1a
    "Monika smiles sweetly once again."
    show monika 2h
    "Yet as she turn her head to the right, she notices the seat where Natsuki was supposed to be is empty"
    m 4i "Where's Natsuki?"
    mc "Oh, she got up from the table a couple of minutes and went to the closet without anyone noticing."
    show monika 1h at f11
    "As Monika attempts to get up from her seat, I stop her."
    mc "Don't worry, I'll go talk to her and make sure everything's alright."
    show monika at t11
    m 1d "Oh, alright then."
    scene bg closet
    with wipeleft
    "I get up from my seat and make my way to the closed."
    show natsuki 1s at t11
    "As I reach the closet's door, I see natsuki sitting down on a foldable chair inside the closet, with her face burried in a book."
    mc "Hey Natsuki, is everything alright?"
    "She slowly raises her head and looks at me."
    n 1s "Yeah, everything's fine."
    "As she sais this, I take a better look at the book she's holding. Judging by the cover's flashy art, I can definitely tell it's a manga."
    mc "You read manga, Natsuki?"
    n 5o "Yeah, you have a problem with that?"
    n "If you're gonna judge me I don't wanna hear it."
    mc "Relax, I don't judge. I read manga too as a matter of fact."
    n 5s "..."
    mc "What manga are you reading?"
    n 5h "It's a new release from Parfait Girls."
    n 1w "It's my favorite series, but the new editor obviously has no idea what he's doing."
    n "He's just adding a bunch of unnecessary adult scenes and ruining the relationship between the characters."
    n "The early editions made by the old editor where a lot better that {i}this{/i}."
    mc "I know just how you feel, Natsuki. It know how it's like to have a series you love be ruined by mindless fan service."
    mc "You have your whole collection in the closet?"
    n 1k "Yeah, I can't keep it at home."
    n 5k "I don't know what my dad would do if he found out I was into stuff like this."
    n 4d "I sometimes like to look through old editions of my manga."
    n "For the nostalgia, you know?"
    mc "Yeah, I can get that."
    show natsuki 1a
    "Natsuki gets up from her chair and reaches out to a shelf above her."
    "She pulls out what appears to be another edition of the manga she was holding earlier."
    n 1d "Look, this is the first edition of Parfait Girls. I keep it on a special shelf, as it's my favorite of the series."
    mc "Maybe we could read it together one day, If you'd like."
    show natsuki 1h
    "Natsuki pauses for a moment."
    n 5t "You'd... really want to read this with me?"
    n "I mean, it {i}is{/i} a Magical Girl Manga after all."
    mc "Well it's not really my cup of tea, but I can't hurt to give it a try."
    mc "But that would have to be tomorrow, since club time is pretty much over for today."
    n 5t "Yeah, you're right."
    mc "I'll se you tomorrow then. I'm really looking forward to it."
    n 1d "Yeah, me too. See you tomorrow."
    scene bg club_day
    with wipeleft
    "I make my way to the table and pick up the backpack from the back of the chair I used to sit on."
    show sayori 1a at t11
    "I turn around once again to face Sayori."
    mc "Ready to go home together, Sayori?"
    s 1c "You go on ahead without me, [player]."
    s "There's something I want to talk to Natsuki about. In private."
    show sayori 1a
    mc "Oh that's alright. I'll see you tomorrow. Take care!"
    s 1x "See you tomorrow, [player]. Take care!"
    show sayori 1a
    scene bg residential_day
    with wipeleft
    "With that, the I depart the clubroom and make my way home."
    "The whole way, my mind wanders to petite, pink haired girl in the literature club."
    show natsuki 1a at t11
    "Natsuki."
    "Something about her makes me want to get to know her better."
    "She seems to be really passionate about her manga."
    "This might be the start of a beautiful friendship."
    "...or more than that."
    stop music fadeout 2.0
    scene bg livingroom
    with dissolve_scene_full
    call dayone from _call_dayone
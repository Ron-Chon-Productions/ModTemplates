define all_Events["modding_examples_events_Rogue_modding"] = {
    "conditions": (
        ConditionClass("Player.location in public_Locations"),
        ConditionClass("Player.location not in {Rogue.location, Rogue.destination}"),
        ConditionClass("not get_present_Characters(Player.location)"),
    ),

    "flags": "traveling",

    # Events can be setup to fire either a single time or multiple times
    # "repeatable": True,
}

label modding_examples_events_Rogue_modding:
    # This variable should get set at the start of every event. This adds the black bars at the top and prevents random events from firing
    $ ongoing_Event = True

    $ Rogue.change_face("amused")
    $ Rogue.change_arms("neutral")

    # If a behavior is set, the characters outfit will be updated to match it
    $ send_Characters(Rogue, Player.location, behavior = "wandering")

    "Looks like [Rogue.name] wants to talk about modding."
    menu:
        extend ""
        "Go talk about modding":
            pass
        "Run away quickly":
            # If you want an event to have a chance of happening again, you can reset it. 
            # This is generally done so that players can temporarily skip events
            $ EventScheduler.Events["modding_examples_events_Rogue_modding"].reset()

            $ ongoing_Event = False

            return

    # You can use an interaction to add randomness to the event
    $ interact(Rogue, "greeting", "simple")

    # Or you can directly control what characters say
    ch_Rogue "Adding new events is easy."
    ch_Rogue "Let's talk some more in your room."

    # If you want to change the location, it's generally best to clear out the destination location
    $ remove_Characters(location = Player.home)
    $ set_the_scene(location = Player.home)
    
    # behavior = None keeps the characters outfit the same when they move. 
    # This is useful for scenes where the characters will be coming/going or there are location changes.
    $ send_Characters(Rogue, Player.home, behavior = None)

    # You can directly control character's faces and arm poses
    # Full list is available in a characters expressions.rpy file
    $ Rogue.change_face("happy")
    $ Rogue.change_arms("hips")
    ch_Rogue "You can directly set my expressions in an event."

    # Or you can set their mood, this will randomize their face and arms based on their character traits
    # Full list of moods can be found in moods.rpy
    $ Rogue.change_mood("flirty")
    ch_Rogue "Or. . ."

    # Repeated calls will get a different random result
    $ Rogue.change_mood("flirty")
    ch_Rogue "Ya can randomize it."

    ch_Rogue "Ya can also bring up cutouts during events. . ."
    $ Rogue.change_face('kiss2', blush = 2)

    $ show_Character_cutout(Rogue, 'kissing')

    # Use the name variable on a character whenever possible. That way the dialog reflects the character's current name
    "[Rogue.name] gives you a quick kiss,"

    $ hide_Character_cutout(Rogue, 'kissing')

    # Same for petnames
    ch_Rogue "Bye [Rogue.Player_petname]!"

    $ send_Characters(Rogue, Rogue.home, behavior = None)

    $ ongoing_Event = False

    return
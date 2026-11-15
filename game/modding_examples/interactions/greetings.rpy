# Interactions are used to add randomness to the sandbox.
# They are generally intended for only a few lines of dialogue with little to no branching.
define CHARACTERS.Rogue.interactions |= {
    InteractionClass(
        # If no mood is provided, a default mood is picked based on the characters current status
        InstructionClass("Rogue.change_mood()"),

        DialogueClass("ch_Rogue", _("Hey [Player.name]!")),
        DialogueClass("ch_Rogue", _("Have you made much progress on your mod?")),

        # You can add conditions for when the interaction should be available
        conditions = "EventScheduler.check('ModdingExample.events.Rogue_modding')",

        flags = "greeting",

        # requirements and results are used to chain interactions together
        # the `-` in requirements indicates that these flags cannot yet be present in the chain
        requirements = {"-greated", "-mod"},
        # This adds the `greeted` and `mod` flags to the interaction chain
        results = {"greeted", "mod"},
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood()"),

        DialogueClass("ch_Rogue", _("Hey [Player.name]!")),
        DialogueClass("ch_Rogue", _("Have you come to show me your latest mod?")),

        # If you have multiple conditions for your interaction they can be added as a tuple
        conditions = (
            "EventScheduler.check('ModdingExample.events.Rogue_modding')",

            "Rogue.Location == Rogue.Home",
        ),

        flags = "greeting",

        # The `*` acts as a shorthand for indicating that the flag should not yet be in the interaction chain and will be added in after the interaction.
        # This is the same as the requirements and results in the above interaction but a bit easier to type
        results = {"*greeted", "*mod"},
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood()"),

        DialogueClass("ch_Rogue", _("I love playing on modded games.")),

        flags = "greeting",

        # this interaction will not be chained unless the `mod` flag has been added to the chain (for example after the previous 2 interactions)
        requirements = {"-playing", "mod"},
        results = "playing",
    ),

    InteractionClass(
        InstructionClass("Rogue.change_mood()"),

        DialogueClass("ch_Rogue", _("This is all I've gotta say.")),

        flags = "greeting",

        # 'any' and 'end' are reserved tags. The `any` matches all tags and `end` immediately stops the chain. In effect, this interaction will not be chained at all.
        requirements = "-any",
        results = "end",
    ),
}
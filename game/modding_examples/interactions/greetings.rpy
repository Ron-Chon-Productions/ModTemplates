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

        results = "*greeted",
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

        results = "*greeted",
    ),
}
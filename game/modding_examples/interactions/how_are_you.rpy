define CHARACTERS.Rogue.interactions |= {
    InteractionClass(
        # For texting interactions use these function class calls
        FunctionClass("receive_text", "Rogue", _("Im good")),
        FunctionClass("receive_text", "Rogue", _("trying to get Doom onto my phone")),

        FunctionClass("send_text", "Rogue", _("this this thing can play games?")),

        FunctionClass("receive_text", "Rogue", _("only if you mod them in ;)")),

        conditions = "EventScheduler.check('ModdingExample.events.Rogue_modding')",

        flags = {"chatting", "texting"},

        requirements = "-Rogue.any",
        results = "Rogue.end",
    ),
}
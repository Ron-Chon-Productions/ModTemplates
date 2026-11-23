define ALL_LOCATION_ACTIONS |= {
    LocationActionClass(
        _("Modding example - Single room"),

        instructions = InstructionClass("renpy.call('ModdingExample.location_action_id_based')"),

        # If a location_id is provided, the action will be available for the location that matches the id
        location_id = "XavierSchool.PlayerRoom",
    ),

    LocationActionClass(
        _("Modding example - Any bedroom"),

        instructions = InstructionClass("renpy.call('ModdingExample.location_action_tag_based')"),

        # If a tag is provided, the action will be available for all locations that have the tag in either it's traits or location_actions
        tag = "bedroom",
    ),

    LocationActionClass(
        _("Modding example - Conditional displaying"),

        instructions = InstructionClass("renpy.call('ModdingExample.location_conditional_display')"),

        # If this is false the action won't appear in location menu
        conditions = "time_index <= 2",

        location_id = "XavierSchool.PlayerRoom",
    ),

    LocationActionClass(
        _("Modding example - Conditional enabling"),

        instructions = InstructionClass("renpy.call('ModdingExample.location_conditional_enabled')"),

        # If this is false, the action will be disabled disabled in the location menu
        enabled_conditions = "time_index <= 2",

        location_id = "XavierSchool.PlayerRoom",
    ),
}

label ModdingExample.location_action_id_based:
    "Id based location action called"

    return

label ModdingExample.location_action_tag_based:
    "Tag based location action called"

    return

label ModdingExample.location_conditional_display:
    "Conditionally displayed location action called"

    return

label ModdingExample.location_conditional_enabled:
    "Conditionally enabled location action called"

    return
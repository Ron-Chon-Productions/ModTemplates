define always_unlocked_Locations['ModLocation'] = InstructionClass("renpy.call('travel', ModLocation)")

define ALL_LOCATION_ADJACENCIES |= {
    # Adjacencies are bi-directional by default but can be made one way
    # You can also add conditionals and rename the displayed names of the locations
    LocationAdjacencyClass(
        "ModLocation",
        "XavierSchool.Grounds",
    ),
}

#  The id of a location should be of the following format 'loc_MODULENAME_TAG'
# The name and conversational_name do not have to match the id
define ALL_LOCATIONS["ModLocation"] = {
    "name": _("Mod example location"),

    "tag": "ModLocation",

    "conversational_name": _("ModLand"),

    "traits": {
        "public": True,
        "outdoors": True,
    },
}

init -1:
    #  The variable name of location should be of the following format 'MODULENAME_TAG'
    default ModLocation = LocationClass("ModLocation")

# There needs to be a label that matches the location name in order to wander to in in the sandbox
label ModLocation:
    if Player.Destination != Player.Location:
        call events.check(flags = "traveling")

        if Player.Destination != Player.Location:
            $ set_the_scene(Location = Player.Destination, greetings = True)

    while Player.Location == ModLocation:
        if clock <= 0:
            if time_index == 3:
                $ narrator(localize("common.getting_tired_head_back"))

                call travel(Player.Room)
            else:
                call wait_around

        $ location_actions_menu(ModLocation)
        
    $ move_location(Player.Location)
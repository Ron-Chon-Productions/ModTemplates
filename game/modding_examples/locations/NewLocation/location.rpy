define always_unlocked_Locations['loc_ModdingExample_NewLocation'] = InstructionClass("renpy.call('travel', 'loc_ModdingExample_NewLocation')")

define all_LocationAdjacencies |= {
    # Adjacencies are bi-directional by default but can be made one way
    # You can also add conditionals and rename the displayed names of the locations
    LocationAdjacencyClass(
        "loc_ModdingExample_NewLocation",
        "loc_XavierSchool_Grounds",
    ),
}

#  The id of a location should be of the following format 'loc_MODULENAME_TAG'
# The name and conversational_name do not have to match the id
define all_Locations["loc_ModdingExample_NewLocation"] = {
    "name": _("Mod example location"),
    "tag": "NewLocation",

    "module": "ModdingExample",

    "conversational_name": _("ModLand"),

    "traits": {
        "public": True,
        "outdoors": True,
    },
}

#  The variable name of location should be of the following format 'MODULENAME_TAG'
default ModdingExample_NewLocation = LocationClass("loc_ModdingExample_NewLocation")

# There needs to be a label that matches the location name in order to wander to in in the sandbox
label loc_ModdingExample_NewLocation:
    if Player.destination != Player.location:
        call check_for_Events(flags = "traveling")

        if Player.destination != Player.location:
            $ set_the_scene(location = Player.destination, greetings = True)

    while Player.location == "loc_ModdingExample_NewLocation":
        if clock <= 0:
            if time_index == 3:
                $ narrator(localize("common_getting_tired_head_back"))

                call travel(Player.home)
            else:
                call wait_around

        $ location_actions_menu("loc_ModdingExample_NewLocation")
        
    $ move_location(Player.location)
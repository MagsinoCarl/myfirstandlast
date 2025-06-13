################################################################################
#  CHARACTER DEFINITIONS
################################################################################
# Define a Character class to encapsulate character properties
init python:
    class GameCharacter:
        def __init__(self, name, color, who_style):
            self.name = name
            self.color = color
            self.who_style = who_style
            # Create Ren'Py Character object
            self.character = Character(name, color=color, who_style=who_style)

        # Method to access the Ren'Py Character object
        def get_character(self):
            return self.character

# Instantiate character objects
define jus = GameCharacter("Justine", "#335a3b", "namebox").get_character()
define g   = GameCharacter("Guard", "#207476", "sec_namebox").get_character()
define k   = GameCharacter("Kim", "#e84393", "sec_namebox").get_character()
define c   = GameCharacter("Carl", "#113d29", "sec_namebox").get_character()
define n   = GameCharacter("Nurse", "#E9967A", "sec_namebox").get_character()
define ma  = GameCharacter("Mae", "#E23A32", "sec_namebox").get_character()
define m   = GameCharacter("Mae", "#E23A32", "namebox").get_character()
define s   = GameCharacter("Sophie", "#A23A32", "sec_namebox").get_character()
define l   = GameCharacter("Lyn", "#AB3A32", "sec_namebox").get_character()
define e   = GameCharacter("Ella", "#3A3AB4", "sec_namebox").get_character()
define v   = GameCharacter("Vidal", "#3A8084", "sec_namebox").get_character()
define cs  = GameCharacter("Cashier", "#09091e", "sec_namebox").get_character()
define j   = GameCharacter("Joriemer", "#519c90", "sec_namebox").get_character()
define gui.name_text_size = 100  # Change 40 to your desired font size

################################################################################
#  TRANSFORMS
################################################################################
init python:
    class Transform:
        def __init__(self, xalign, yalign, anchor, zoom):
            self.xalign = xalign
            self.yalign = yalign
            self.anchor = anchor
            self.zoom = zoom

        def to_renpy_transform(self):
            return f"""
transform {self.__class__.__name__.lower()}:
    xalign {self.xalign}
    yalign {self.yalign}
    anchor {self.anchor}
    zoom {self.zoom}
            """.strip()

    # Instantiate Transform objects
    justine_bottom_left = Transform(0.0, 1.0, (0.0, 1.0), 0.8)
    kim_bottom_right = Transform(0.75, 1.05, (0.0, 1.0), 0.8)
    justine_bottom_center = Transform(0.3, 0.9, (0.0, 1.0), 0.7)
    kim_bottom_center = Transform(0.5, 1.05, (0.05, 1.1), 0.8)
    kim_bottom_left = Transform(0.2, 1.05, (0.05, 1.1), 0.8)
    guard_bottom_right = Transform(0.75, 1.1, (0.0, 1.0), 0.8)
    mae_bottom_center = Transform(0.3, 0.9, (0.0, 1.0), 0.7)
    sophie_bottom_center = Transform(0.5, 0.9, (0.0, 1.0), 1.0)
    mae_bottom_left = Transform(0.0, 1.0, (0.0, 1.0), 0.7)

    # Generate transform definitions as strings (for manual inclusion)
    transforms = [
        justine_bottom_left,
        kim_bottom_right,
        justine_bottom_center,
        kim_bottom_center,
        kim_bottom_left,
        guard_bottom_right,
        mae_bottom_center,
        sophie_bottom_center,
        mae_bottom_left
    ]
    # Note: Removed eval() and store_dict assignment; transforms are now hardcoded below

# Ren'Py transform definitions (hardcoded based on Transform objects)

transform custom_size_transform:
    size (2580, 1520)

transform justine_bottom_left:
    xalign 0.0
    yalign 1.0
    anchor (0.0, 1.0)
    zoom 0.8

transform kim_bottom_right:
    xalign 0.75
    yalign 1.05
    anchor (0.0, 1.0)
    zoom 0.8

transform justine_bottom_center:
    xalign 0.3
    yalign 0.9
    anchor (0.0, 1.0)
    zoom 0.7

transform kim_bottom_center:
    xalign 0.5
    yalign 1.05
    anchor (0.05, 1.1)
    zoom 0.8

transform kim_bottom_left:
    xalign 0.2
    yalign 1.05
    anchor (0.05, 1.1)
    zoom 0.8

transform guard_bottom_right:
    xalign 0.75
    yalign 1.1
    anchor (0.0, 1.0)
    zoom 0.8

transform mae_bottom_center:
    xalign 0.3
    yalign 0.9
    anchor (0.0, 1.0)
    zoom 0.7

transform sophie_bottom_center:
    xalign 0.5
    yalign 0.9
    anchor (0.0, 1.0)
    zoom 1.0

transform mae_bottom_left:
    xalign 0.0
    yalign 1.0
    anchor (0.0, 1.0)
    zoom 0.7

init -1 python:
    # Class to manage all image definitions
    class ImageManager:
        def __init__(self):
            # Define all image attributes as a dictionary
            self.images = {
                # Original Backgrounds
                "bg_gate": "images/bg_gate.jpg",
                "bg_after_school_gate": "images/after_school_gate.jpg",
                "bg_pub_lib_door": "images/pub_lib_door.jpg",
                "bg_guard_house": "images/guard_house.jpg",
                "bg_room": "images/bg_room.jpg",
                "splash_bg": "images/splash_bg.png",
                "bg_far_view_entrance": "images/FarViewofEntranceArea.jpg",
                "bg_new_building1": "images/new_building1.jpg",
                "bg_new_building2": "images/new_building2.jpg",
                "bg_new_building3": "images/new_building3.jpg",
                "bg_new_building4": "images/new_building4.jpg",
                "bg_new_building5": "images/new_building5.jpg",
                "bg_new_building6": "images/new_building6.jpg",
                "bg_nearing_new_building": "images/NearingNewBuilding.jpg",
                "bg_tambayan_to_entrance": "images/TambayanAreaGoingtoEntrance.jpg",
                "bg_circle_area_lower_view": "images/CircleAreaLowerView.jpg",
                "bg_vendor": "images/vendor.jpg",
                "bg_vendor_view": "images/vendor_view.jpg",
                "Enter_choice2": "images/Enter_choice2.jpg",
                "bg_entering_hideout": "images/Entering_hideout.jpg",
                "bg_closed_hideout_gate": "images/Closed_hideout_area_gate.jpg",
                "bg_entering_the_school_lobby": "images/entering_the_school_lobby.jpg",
                "bg_pup_lobby": "images/pup_lobby.jpg",
                "bg_informationdesk": "images/informationdesk.jpg",
                "bg_window1": "images/window1.jpg",
                "floor1_hallwayright": "images/floor1_hallwayright.jpg",
                "bg_acad": "images/acad.jpg",
                "bg_sas": "images/sas.jpg",
                "bg_midstair": "images/mid_boys_stairs.jpg",
                "bg_lgbt1": "images/lgbt_cr.jpg",
                "bg_lgbt2": "images/lgbt_door.jpg",
                "bg_lgbt3": "images/lgbt_halfway.jpg",
                "bg_stair1": "images/first_stair1.jpg",
                "bg_stair2": "images/first_stair2.jpg",
                "bg_stair3": "images/first_stair3.jpg",
                "bg_stair4": "images/first_stair4.jpg",
                "bg_stair5": "images/first_stair5.jpg",
                "bg_stair6": "images/first_stair6.jpg",
                "fire_exit1": "images/fire_exit1.jpg",
                "fire_exit2": "images/fire_exit2.jpg",
                "m1": "images/m1.jpg",
                "m2": "images/m2.jpg",
                "m3": "images/m3.jpg",
                "m4": "images/m4.jpg",
                "m5": "images/m5.jpg",
                "sf1": "images/sf1.jpg",
                "sf2": "images/sf2.jpg",
                "sf3": "images/sf3.jpg",
                "sf4": "images/sf4.jpg",
                "sf5": "images/sf5.jpg",
                "sf6": "images/sf6.jpg",
                "sf7": "images/sf7.jpg",
                "sf8": "images/sf8.jpg",
                "sf9": "images/sf9.jpg",
                "sf10": "images/sf10.jpg",
                "sf11": "images/sf11.jpg",
                "sf12": "images/sf12.jpg",
                "sf13": "images/sf13.jpg",
                "sf14": "images/sf14.jpg",
                "sf15": "images/sf15.jpg",
                "sf16": "images/sf16.png",
                "sf17": "images/sf17.jpg",
                "floor1_midhallwayleft": "images/floor1_midhallwayleft.jpg",
                "floor1_hallwayleft": "images/floor1_hallwayleft.jpg",
                "left_halfway_ground1": "images/left_halfway_ground1.jpg",
                "left_halfway_ground2": "images/left_halfway_ground2.jpg",
                "left_halfway_ground3": "images/left_halfway_ground3.jpg",
                "left_halfway_ground4": "images/left_halfway_ground4.jpg",
                "left_halfway_ground5": "images/left_halfway_ground5.jpg",
                "faculty_inside": "images/faculty_inside.jpg",
                "pet_cat": "images/petcat.jpg",
                "science_lab": "images/science_lab.jpg",
                "rightside_staircase": "images/rightside_staircase.jpg",
                "chair": "images/chair.jpg",
                "chair1": "images/chair1.jpg",
                "lobbychairs": "images/lobbychairs.jpg",

                # Newly Added Images
                "hideout_fireexit": "images/hideout_fireexit.jpg",
                "hideout_extension": "images/hideout_extension.jpg",

                # Garden and Exit
                "bg_garden": "images/garden.jpg",
                "bg_garden_cat": "images/view_cat.jpg",
                "bg_garden1": "images/garden1.jpg",
                "bg_garden2": "images/garden2.jpg",
                "bg_garden3": "images/garden3.jpg",
                "bg_back_garden1": "images/back_garden1.jpg",
                "bg_exit1": "images/exit1.jpg",
                "bg_exit2": "images/exit2.jpg",
                "bg_exit3": "images/exit3.jpg",
                "bg_exit4": "images/exit4.jpg",
                "bg_exit5": "images/exit5.jpg",
                "bg_exit6": "images/exit6.jpg",
                "bg_exit7": "images/exit7.jpg",
                "bg_exit8": "images/exit8.jpg",
                "bg_exit9": "images/exit9.jpg",
                "bg_exit10": "images/exit10.jpg",
                "bg_fire_exit_inside1": "images/fire_exit_inside1.jpg",
                "bg_fire_exit_inside2": "images/fire_exit_inside2.jpg",
                "bg_fire_exit_inside3": "images/fire_exit_inside3.jpg",
                "bg_fire_exit_inside4": "images/fire_exit_inside4.jpg",
                "bg_fire_exit_inside5": "images/fire_exit_inside5.jpg",
                "library1": "images/library1.jpg",
                "library2": "images/library2.jpg",
                "discussion": "images/discussion.jpg",

                # Gallery Images
                "g1": "images/g1.jpg",
                "g2": "images/g2.jpg",
                "g3": "images/g3.jpg",
                "g4": "images/g4.jpg",
                "g5": "images/g5.jpg",
                "g6": "images/g6.jpg",
                "g7": "images/g7.jpg",
                "g8": "images/g8.jpg",
                "g9": "images/g9.jpg",
                "g10": "images/g10.jpg",
                "g11": "images/g11.jpg",
                "g12": "images/g12.jpg",

                # Floor 2
                "bg_floor2_halfwayright": "images/floor2_halfwayright.jpg",

                # Documents
                "doc1": "doc1.jpg",
                "doc2": "doc2.jpg",
                "doc3": "doc3.jpg",
                "doc4": "doc4.jpg",

                # Additional Rooms and Areas
                "bg_admin_office": "images/admin_office.jpg",
                "bg_authorized_exit": "images/authorized_personnelonlyareaexit.jpg",
                "bg_avr": "images/avr.jpg",
                "bg_avr_door": "images/avrdoor.jpg",
                "bg_beside_avr": "images/besideavr.jpg",
                "bg_beside_faculty_office": "images/besidefacultyoffice.jpg",
                "bg_cashier_window": "images/cashierwindow.jpg",
                "clinic1": "images/clinic_inside.jpg",
                "clinic2": "images/clinic_outside.jpg",

                # Up to the 3rd Floor
                "stair1": "images/stair1.jpg",
                "stair2": "images/stair2.jpg",
                "stair3": "images/stair3.jpg",
                "stair4": "images/stair4.jpg",
                "stair5": "images/stair5.jpg",

                # Third Floor Hallways
                "hallway1": "images/hallway1.jpg",
                "hallway2": "images/hallway2.jpg",
                "hallway3": "images/hallway3.jpg",
                "hallway4": "images/hallway4.jpg",
                "hallway5": "images/hallway5.jpg",
                "hallway6": "images/hallway6.jpg",
                "hallway7": "images/hallway7.jpg",
                "hallway8": "images/hallway8.jpg",
                "hallway9": "images/hallway9.jpg",

                # Room 307 Scene
                "room307_1": "images/room307_1.jpg",
                "room307_2": "images/room307_2.jpg",
                "room307_3": "images/room307_3.jpg",

                # Girl's CR
                "girls1": "images/girls1.jpg",
                "girls2": "images/girls2.jpg",
                "girls3": "images/girls3.jpg",
                "girls4": "images/girls4.jpg",

                # Rooms
                "room1": "images/room1.jpg",
                "room2": "images/room2.jpg",

                # Fourth Floor
                "1": "images/1.jpg",
                "2": "images/2.jpg",
                "3": "images/3.jpg",

                # 4th Hallway
                "f1": "images/f1.jpg",
                "f2": "images/f2.jpg",
                "f3": "images/f3.jpg",
                "f4": "images/f4.jpg",
                "f5": "images/f5.jpg",
                "f6": "images/f6.jpg",
                "f7": "images/f7.jpg",
                "f8": "images/f8.jpg",
                "f9": "images/f9.jpg",
                "f10": "images/f10.jpg",
                "f11": "images/f11.jpg",

                # Fourth Room
                "comlab": "images/comlab.jpg",
                "comhardware": "images/comhardware.jpg",
                "housekeeping_room": "images/housekeeping_room.jpg",
                "travel_and_tours_room1": "images/travel_and_tours_room1.jpg",
                "travel_and_tours_room2": "images/travel_and_tours_room2.jpg",
                "student_org1": "images/student_org1.jpg",
                "hm_storage_room1": "images/hm_storage_room1.jpg",
                "kitchen_lab2": "images/kitchen_lab2.jpg",
                "proj": "images/proj.jpg",
                "food_and_bev_room2": "images/food_and_bev_room2.jpg",
                "csc_room1": "images/csc_room1.jpg",
                "csc_room2": "images/csc_room2.jpg",
                "lab_management": "images/lab_management.jpg",
                "standard_room": "images/standard_room.jpg",
                "deluxe": "images/deluxe.jpg",

                # Roof Deck
                "rf1": "images/rf1.jpg",
                "rf2": "images/rf2.jpg",
                "rf3": "images/rf3.jpg",
                "rf4": "images/rf4.jpg",
                "rf5": "images/rf5.jpg"
            }

        # Method to register images with Ren'Py
        def register_images(self):
            for image_name, file_path in self.images.items():
                renpy.image(image_name, file_path)

    # Instantiate and register the images
    image_manager = ImageManager()
    image_manager.register_images()

default visited_sas = False
default visited_library = False
default visited_stone_circle = False

init python:
    class CharacterImages:
        """Base class for character image management."""
        def __init__(self, name, image_path, default_width, default_height):
            self.name = name
            self.image_path = image_path
            self.default_width = default_width
            self.default_height = default_height
            self.images = {}

        def add_image(self, state, file_name, width=None, height=None):
            """Add an image for a specific state with optional custom dimensions."""
            width = width or self.default_width
            height = height or self.default_height
            self.images[state] = im.Scale(f"{self.image_path}/{file_name}", width, height)

        def get_image(self, state):
            """Retrieve the image for a given state."""
            return self.images.get(state, self.images.get("normal", None))

    # Nurse
    class Nurse(CharacterImages):
        def __init__(self):
            super().__init__("Nurse", "images", 925, 1200)
            self.add_image("normal", "nurse_normal.png")

    # Cashier
    class Cashier(CharacterImages):
        def __init__(self):
            super().__init__("Cashier", "images", 925, 1200)
            self.add_image("talking", "cashier_talking.png", 1200, 1350)
            self.add_image("normal", "cashier_normal.png")

    # Carl
    class Carl(CharacterImages):
        def __init__(self):
            super().__init__("Carl", "images", 1200, 1300)
            self.add_image("normal", "Carl_normal.png", 1200, 1350)
            self.add_image("talking", "Carl_talking.png")
            self.add_image("suggesting", "Carl_suggesting.png")
            self.add_image("thinking", "Carl_thinking.png")

    # Justine
    class Justine(CharacterImages):
        def __init__(self):
            super().__init__("Justine", "images", 925, 1200)
            states = [
                "normal", "talking", "happy", "alarmed", "disappointed",
                "crying", "holding_id", "holding_phone", "waving", "sighing",
                "smiling", "realised", "sad", "laughing", "scared"
            ]
            for state in states:
                self.add_image(state, f"Justine_{state}.png")

    # Kim
    class Kim(CharacterImages):
        def __init__(self):
            super().__init__("Kim", "images", 925, 1200)
            states = ["normal", "holdingID", "smiling", "talking", "calling"]
            for state in states:
                self.add_image(state, f"kim_{state}.png")

    # Guard
    class Guard(CharacterImages):
        def __init__(self):
            super().__init__("Guard", "images", 925, 1200)
            self.add_image("normal", "guard_normal.png")
            self.add_image("happy", "guard_happy_talking.png")
            self.add_image("annoyed", "guard_talking_annoyed.png")
            self.add_image("angry", "guard_talking_angry.png")

    # Lyn
    class Lyn(CharacterImages):
        def __init__(self):
            super().__init__("Lyn", "images", 925, 1200)
            states = [
                "talking", "angry", "anya_smirk", "disgusted", "normal",
                "pouting_talking", "pouting", "smug", "worried"
            ]
            for state in states:
                self.add_image(state, f"Lyn_{state}.png")

    # Ella
    class Ella(CharacterImages):
        def __init__(self):
            super().__init__("Ella", "images", 925, 1200)
            states = ["grinning", "normal", "smiling", "talking", "whispering"]
            for state in states:
                self.add_image(state, f"Ella_{state}.png")

    # Vidal
    class Vidal(CharacterImages):
        def __init__(self):
            super().__init__("Vidal", "images", 925, 1200)
            states = ["angry_talking", "angry", "normal", "smiling", "talking"]
            for state in states:
                self.add_image(state, f"Vidal_{state}.png")

    # Sophie
    class Sophie(CharacterImages):
        def __init__(self):
            super().__init__("Sophie", "images", 925, 1200)
            states = ["normal", "smiling", "talking"]
            for state in states:
                self.add_image(state, f"Sophie_{state}.png")

    # Jorie
    class Jorie(CharacterImages):
        def __init__(self):
            super().__init__("Jorie", "images", 925, 1200)
            states = ["normal", "smiling", "talking"]
            for state in states:
                self.add_image(state, f"Jorie_{state}.png")

    # Mae
    class Mae(CharacterImages):
        def __init__(self):
            super().__init__("Mae", "images", 925, 1200)
            states = ["holding_paper", "normal", "smiling", "talking"]
            for state in states:
                self.add_image(state, f"Mae_{state}.png")

    # Faculty
    class Faculty(CharacterImages):
        def __init__(self):
            super().__init__("Faculty", "images", 925, 1200)
            states = ["normal", "talking"]
            for state in states:
                self.add_image(state, f"Faculty_{state}.png")

# Instantiate character objects
define nurse = Nurse()
define cashier = Cashier()
define carl = Carl()
define justine = Justine()
define kim = Kim()
define guard = Guard()
define lyn = Lyn()
define ella = Ella()
define vidal = Vidal()
define sophie = Sophie()
define jorie = Jorie()
define mae = Mae()
define faculty = Faculty()


label before_main_menu:
    $ apply_ui_theme()
    return

$ persistent.ui_theme = "dark"

default persistent.ui_theme = "default"  # This saves the user's selected theme

init python:

    def apply_ui_theme():
        # Use persistent color or default to white
        text_color = persistent.text_color if hasattr(persistent, "text_color") else "#5fa121"

        # Change the say dialogue text color
        style.say_dialogue.color = text_color

        # Optionally, change window background text color or other UI elements here too
        # For example, change textbox window text color or font color if needed

        # To refresh styles immediately, call:
        renpy.restart_interaction()
# Example usage in Ren'Py
label staret:
    # Show Justine in normal state
    show expression justine.get_image("normal") as justine
    "Justine" "Hello, I'm in my normal state!"

    # Show Justine in talking state
    show expression justine.get_image("talking") as justine
    "Justine" "Now I'm talking!"

    # Show Carl in thinking state
    show expression carl.get_image("thinking") as carl
    "Carl" "Hmm, I'm thinking..."

label start:
    stop music fadeout 1.0
    scene bg_room at custom_size_transform with fade
    voice "audio/carl/line1.MP3"
    show expression carl.get_image("normal") at center with dissolve
    c "Hey there."

    voice "audio/carl/line2.MP3"
    show expression carl.get_image("talking") at center with dissolve
    c "Are you new to visual novels?"

    menu:
        "I'm new at this, sorry.":
            jump tutorial
        "I already know, thank you.":
            jump skip_tutorial

label tutorial:
    voice "audio/carl/line3.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    c "No worries! I'm here to guide you around."

    voice "audio/carl/line4.MP3"
    show expression carl.get_image("talking") at center with dissolve
    c "This box below me? That's the text box."

    voice "audio/carl/line5.MP3"
    show expression carl.get_image("thinking") at center with dissolve
    c "All the story, dialogue, and narration happens here."

    voice "audio/carl/line6.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    c "Want a cleaner view of the background? Just press the H key on your keyboard to hide the UI."

    voice "audio/carl/line7.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    c "You can also roll back to dialogue with ease using your scroll wheel in you mouse!"

    voice "audio/carl/line8.MP3"
    show expression carl.get_image("talking") at center with dissolve
    c "You can press H again to bring everything back."

    voice "audio/carl/line9.MP3"
    show expression carl.get_image("thinking") at center with dissolve
    c "Now if you press the Esc key, you'll open the game menu."

    voice "audio/carl/line10.MP3"
    show expression carl.get_image("normal") at center with dissolve
    c "Let me explain the buttons there real quick!"

    voice "audio/carl/line11.MP3"
    show expression carl.get_image("talking") at center with dissolve
    c "History – lets you view past dialogue in case you missed something."

    voice "audio/carl/line12.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    c "Save and Load – save your progress or return to a previous point."

    voice "audio/carl/line13.MP3"
    show expression carl.get_image("thinking") at center with dissolve
    c "Preferences – change text speed, music volume, and other settings."

    voice "audio/carl/line14.MP3"
    show expression carl.get_image("talking") at center with dissolve
    c "About – gives info about the game."

    voice "audio/carl/line15.MP3"
    show expression carl.get_image("normal") at center with dissolve
    c "Help – shows all the controls."

    voice "audio/carl/line16.MP3"
    show expression carl.get_image("thinking") at center with dissolve
    c "And Quit – well... exits the game. Careful with that one."

    voice "audio/carl/line17.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    c "And don't forget the Return button – it brings you right back to the game."

    voice "audio/carl/line18.MP3"
    show expression carl.get_image("talking") at center with dissolve
    c "Got it? Sweet. Let's get started!"

    jump main_game

label skip_tutorial:
    voice "audio/carl/line19.MP3"
    show expression carl.get_image("normal") at center with dissolve
    c "Ah, a veteran I see. I'll leave you to it then."

    jump main_game

label main_game:
    voice "audio/carl/line20.MP3"
    show expression carl.get_image("talking") at center with dissolve
    c "This is where the real story begins..."

    scene bg_gate at custom_size_transform with fade

    show expression justine.get_image("normal") at justine_bottom_left
    jus "Wow, hindi ako makapaniwala na malapit na akong umalis sa sintang paaralang ‘to."

    # The guard appears
    show expression guard.get_image("normal") at guard_bottom_right with dissolve
    g "Good morning, iho. Asan yung I.D mo?"
    
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Sorry po kuya, naiwan ko po yung I.D ko."

    show expression guard.get_image("annoyed") at guard_bottom_right with dissolve
    g "Ayy, pasensya na iho pero bawal kang pumasok pag wala kang I.D."

    # CHOICE MENU -------------------------------------------------------------
    menu:
        "Bumalik na lang ako sa bahay":
            jump go_home
        "Tawagan si Kim para kuhanin ang I.D":
            jump call_kim

################################################################################
# CHOICE 1 – GO HOME –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
################################################################################
label go_home:
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Ayy ganon po ba… sige po kuya, uwi na lang po ako."
    show expression guard.get_image("normal") at guard_bottom_right
    g "Sa susunod, siguraduhing may I.D ka ha."
    hide expression guard.get_image("normal") at guard_bottom_right with dissolve
    show expression justine.get_image("talking") at justine_bottom_left
    $ renpy.pause(0.3)
    window hide
    show expression justine.get_image("normal") at justine_bottom_left
    hide expression justine.get_image("normal") with None
    $ renpy.pause(0.2)
    window show
    jus "(Grabe nakalimutan ko nga pala ang higpit pala ng guard pero ok lang atleast safe ang estudyante dito sa higpit ng guard,)"
    jus "(kaysa naman sa ibang school may guard nga pero wala namang pakialam pano nalang kung may insidente, at least dito samin safe naman.)"
    jus "(hayss, nu bayan pagbabalik pa ko malalate din naman ako, hindi pa nagpapapasok yung prof namin kapag late, sige na nga bukas nalang ako papasok.)"
    "THE END"
    return

    jus "(Grabe nakalimutan ko nga pala ang higpit pala ng guard pero ok lang atleast safe ang estudyante dito sa higpit ng guard,)"
    jus "(kaysa naman sa ibang school may guard nga pero wala namang pakialam pano nalang kung may insidente, at least dito samin safe naman.)"
    jus "(hayss, nu bayan pagbabalik pa ko malalate din naman ako, hindi pa nagpapapasok yung prof namin kapag late, sige na nga bukas nalang ako papasok.)"

    "THE END"
    return

################################################################################
# CHOICE 2 – CALL KIM ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
################################################################################
label call_kim:
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Ayy ganon po ba, wait lang kuya. Papakuha ko lang I.D ko."
    hide expression justine.get_image("talking") with dissolve
    show expression justine.get_image("holding_phone") at justine_bottom_left
    "Tumawag si Justine sa kanyang kaibigan…"
    hide expression justine.get_image("holding_phone") with dissolve
    jus "Hi Kim, nasaan ka ngayon?"
    k "Nasa bahay pa. Bakit?"
    jus "Pwede ka bang dumaan sa bahay ko at kunin ang I.D ko? Naiwan ko eh."
    k "Sakto, may aasikasuhin din ako sa school. Pupuntahan kita."
    "Ilang minuto ang lumipas…"
    hide expression guard.get_image("normal") at guard_bottom_right with dissolve
    show expression kim.get_image("holdingID") at kim_bottom_right with dissolve
    k "Jas! Eto na I.D mo!"
    hide expression kim.get_image("holdingID") with dissolve
    show expression justine.get_image("holding_id") at justine_bottom_left
    show expression kim.get_image("normal") at kim_bottom_left with dissolve
    jus "Ayos! Salamat!"
    hide expression kim.get_image("normal") with dissolve
    hide expression justine.get_image("holding_id") with dissolve
    show expression guard.get_image("happy") at guard_bottom_right with dissolve
    g "Hmm… sige, pwede na kayong pumasok."
    hide expression guard.get_image("happy") with dissolve
    hide expression justine.get_image("holding_phone") with dissolve
    hide expression justine.get_image("talking") with dissolve
    hide expression justine.get_image("normal") with dissolve
    show expression kim.get_image("smiling") at kim_bottom_center
    show expression justine.get_image("smiling") at justine_bottom_center
    jus "Salamat po, kuya Guard!"
    hide expression kim.get_image("smiling") with dissolve
    hide expression justine.get_image("smiling") with dissolve
    scene bg_guard_house at custom_size_transform with fade


label hub_room:
    scene bg_after_school_gate at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    jus "Mhmmmm?"
    call screen nav_door_gate
    return

label door_label:
    if visited_library:
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Sarado na ang public library. Kanina pa tayo dumaan doon."
        jump hub_room
    else:
        $ visited_library = True
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Ohhh, yung Public Library... ang dami naming alaala dito.…"
        scene bg_pub_lib_door at custom_size_transform with fade
        show expression justine.get_image("smiling") at justine_bottom_left
        jus "Dito kami lagi natambay ng mga kaibigan ko sa tuwing may vacant kami."
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Minsan sabay-sabay kaming gumagawa ng homework dito, pero mas madalas puro kwentuhan lang talaga."
        show expression justine.get_image("laughing") at justine_bottom_left
        jus "May isang beses pa nga, napagalitan kami ng librarian kasi masyado kaming maingay!"
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Kung tama ang pagka-alala ko... open to every weekdays, 8 AM to 5 PM."
        hide expression justine.get_image("Sighing") with dissolve
        show expression justine.get_image("smiling") at justine_bottom_left
        jus "Kaya minsan napapaovertime yung mga staff dito kasi di namin namamalayan — 5 na pala."
        show expression justine.get_image("smiling") at justine_bottom_left
        jus "Hay... nami-miss ko ‘yung mga ganung araw. Para bang ang gaan ng lahat."
        hide expression justine.get_image("smiling") with dissolve
        jump hub_room

label explore_new_building:
    if not persistent.visited_explore_new_building:
        $ persistent.visited_explore_new_building = True
        scene bg_nearing_new_building at custom_size_transform with fade
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Grabe... matatapos na 'yung school year, pero 'tong building na 'to, hindi pa rin tapos."
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Parang hindi rin ako makaka-graduate kung hihintayin ko 'yang matapos."
        jus "I wonder, magkakaroon kaya ng bagong program dito?"
        show expression justine.get_image("normal") at justine_bottom_left
        jus "Hay... sana naman, pagbalik ko next sem, may progreso na."
    else:
        scene bg_nearing_new_building at custom_size_transform with fade
        pause 0.1
        scene bg_new_building1 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building2 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building3 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building4 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building5 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building6 at custom_size_transform with fade
        pause 0.1
        show expression justine.get_image("talking") at justine_bottom_left with dissolve
        jus "Gina-gawa parin hanggang ngayon."
        hide expression justine.get_image("talking") with dissolve
        scene bg_new_building6 at custom_size_transform with fade
        pause
    jump callscreen

label callscreen:
    scene bg_far_view_entrance at custom_size_transform with fade
    call screen custom_choice_menu
    return

label resting_ground:
    scene bg_tambayan_to_entrance at custom_size_transform with fade
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Ang tahimik dito ngayon ha."
    hide expression justine.get_image("happy") with dissolve
    jump choicethree

label choicethree:
    scene bg_tambayan_to_entrance at custom_size_transform with fade
    call screen rest_choice_menu
    return

label stone_circle:
    if not visited_stone_circle:
        $ visited_stone_circle = True
        scene bg_tambayan_to_entrance at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Ahh, eto lagi pagkatapos ng klase."
        jus "Grabe kami makatakbo kasi inuunahan namin 'yung ibang estudyante—"
        scene bg_circle_area_lower_view at custom_size_transform with fade
        show expression justine.get_image("laughing") at justine_bottom_left
        jus "…baka mawalan kami ng pwesto, kasi dito kami kumakain tuwing lunch time."
    else:
        scene bg_tambayan_to_entrance at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Ka-miss magkipag chismis dito haha"
        hide expression justine.get_image("happy") with dissolve
    jump choicethree

label vendor:
    scene bg_vendor_view at custom_size_transform with fade
    show vendor_talking at right
    "Oyyyy, pogi bili kana"
    menu:
        "Bumili":
            jump bumili
        "Huwag bumili":
            jump huwag_bumili

label bumili:
    scene bg_vendor at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Kuya, magkano po yung softdrinks?"
    hide expression justine.get_image("talking") with dissolve
    show vendor_talking at right
    "Anong softdrinks?"
    hide vendor_talking with dissolve
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Coke po"
    hide expression justine.get_image("talking") with dissolve
    show vendor_talking at right
    "Sige, ito oh"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Salamat po"
    hide expression justine.get_image("talking") with dissolve
    jump choicethree

label huwag_bumili:
    scene bg_vendor_view at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Salamat na lang po"
    hide expression justine.get_image("talking") with dissolve
    show vendor_talking at right
    "Sure ka pogi? Baka gutom ka na?"
    hide vendor_talking with dissolve
    show expression justine.get_image("talking") at justine_bottom_left
    jus "haha... next time na lang po"
    hide expression justine.get_image("talking") with dissolve
    jump choicethree

label hideout:
    scene bg_vendor_view at custom_size_transform with fade
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "Solid netong tambayan na to! Sa dulo kaso sarado"
    menu:
        "Greet the Guard":
            jump greet_guard
        "Just walk away":
            jump walk_away
    pause

label greet_guard:
    scene bg_entering_hideout at custom_size_transform with fade
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Hmmm? Oh eto yung hideout according sa the boys"
    jus "Pero siguro ang pinaka-memorable kong time sa lugar na ito..."
    jus "is siguro yung nag open forum kami...."
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "Hays, hindi ko parin makalimutan yung memory yun, grabe ang awkward ng atmosphere"
    hide expression justine.get_image("Sighing") with dissolve
    jump choicethree

label walk_away:
    scene bg_entering_hideout at custom_size_transform with fade
    show expression guard.get_image("annoyed") at guard_bottom_right with dissolve
    g "oyy, oyy ano ginagawa mo dito?"
    hide expression guard.get_image("annoyed") with dissolve
    show expression justine.get_image("talking") at justine_bottom_left
    jus "ahh, nag-iikot ikot lang po"
    hide expression justine.get_image("talking") with dissolve
    show expression guard.get_image("angry") at guard_bottom_right
    g "di mo ba alam na bawal pumasok dito ng walang paalam?!"
    hide expression guard.get_image("angry") with dissolve
    show expression justine.get_image("scared") at justine_bottom_left
    jus "sorry po kuya guard aalis na po ako…"
    hide expression justine.get_image("scared") with dissolve
    show expression guard.get_image("annoyed") at guard_bottom_right with dissolve
    g "wag na mauulit to kung hindi i-re-report kita sa SAS"
    hide expression guard.get_image("annoyed") with dissolve
    jump choicethree


################################################################################
#  ENTER BUILDING – Lobby hub
################################################################################
label enter_buildingcampus:
    scene bg_entering_the_school_lobby at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    jus "Pasok tayo sa main building. Saan kaya pupunta ngayon?"
    scene bg_informationdesk at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    scene bg_pup_lobby at custom_size_transform with fade
    jump inside_building

label inside_building:
    scene bg_window1 at custom_size_transform with fade
    call screen inside_choice_menu
    call screen information_desk
    return

label cashier:
    scene bg_cashier_window at custom_size_transform with fade
    show expression justine.get_image("smiling") at justine_bottom_left
    jus "Cashier… mabuti na wala ako kailangan na bayarin"
    jus "Tinamad pa kasi sa ibang subjects and yan tuloy bumayad pa siya ng tuition para sa tatlong semesters…"
    show expression cashier.get_image("talking") at kim_bottom_right
    cs "Hello, may babayaran pa ba kayo ngayon?"
    hide expression cashier.get_image("talking") with dissolve
    show expression justine.get_image("smiling") at justine_bottom_left
    jus "Ay wala naman na po, pasensya na sa pagabala."
    show expression cashier.get_image("talking") at kim_bottom_right
    cs "Okay lang po. Kung may transaction kayo na gagawin,"
    cs "Pwede po kayo magbayad online sa PUP SIS..."
    cs "...o dalhin mo nalang ID mo dito para ma-verify ang transaction niyo po."
    hide expression cashier.get_image("talking") with dissolve
    jump left_ground_1

label right_hall:
    scene floor1_hallwayright at custom_size_transform with fade
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "grabe walang katao tao himala?"
    hide expression justine.get_image("Sighing") with dissolve

label floor1_right_hall:
    scene floor1_hallwayright at custom_size_transform with fade
    call screen right_hall_menu
    return

label clinic_room:
    scene clinic2 at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Clinic… ayan, tahimik pero dito sikat ang lahat ng drama sa buhay."
    show expression justine.get_image("normal") at justine_bottom_left
    jus "Dito ako tumatambay minsan dahil sa sakit ng ulo, pati na din dahil sa minsan na pasakit ng loob."
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "Minsang umupo ako d’yan"
    jus "hindi dahil sa masamang pakiramdam kundi dahil gusto ko lang ng pahinga."
    jus "At ang Nurse? Parang naging nanay ko pa."
    show expression justine.get_image("smiling") at justine_bottom_left
    jus "Palagi niya akong tinatanong, ‘Okay ka lang ba talaga?’ Nakakamiss toh talaga."
    # Start of flashback sequence
    scene clinic1 at custom_size_transform with fade
    show expression nurse.get_image("normal") at right
    show expression justine.get_image("normal") at justine_bottom_left
    n "Ay dios mio, tambay ka nanaman dito uli? Ano nanaman pakiramdam mo mijo."
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Wala po ma'am, unting sakit lang ng ulo po."
    n "Wag mo kalimutan na alagaan mo sarili mo mijo."
    # End of flashback
    scene clinic2 at custom_size_transform with fade
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Ang bait talaga ni ma'am. Sana makadalaw ako ulit dito."
    hide expression justine.get_image("happy") with dissolve
    jump floor1_right_hall

label sas:
    if not visited_sas:
        $ visited_sas = True
        scene bg_sas at custom_size_transform with fade
        show expression justine.get_image("normal") at justine_bottom_left with dissolve
        show expression justine.get_image("talking") at justine_bottom_left with dissolve
        jus "Yung SAS Office....."
        show expression justine.get_image("sad") at justine_bottom_left with dissolve
        jus "Hays.. Naalala ko tuloy tuwing enrollment"
        jus "Paunahan talaga"
        hide expression justine.get_image("talking") with dissolve
        hide expression justine.get_image("sad") with dissolve
    else:
        scene bg_sas at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left with dissolve
        jus "Buti nalang tapos na ako sa mga ganyan ganyan"
        hide expression justine.get_image("happy") with dissolve
    jump floor1_right_hall
return

label right_hall_forward2:
    scene bg_acad at custom_size_transform with fade
    call screen right_hall_menu1
    return

label show_documents:
    scene bg_acad at custom_size_transform with fade
    show doc1 with fade
    "This is the QR Code wherein you can scan thru phone"
    pause 1.0  # Added duration for pause
    show doc2 with fade
    "Here is the second request letter template"
    pause 1.0
    show doc3 with fade
    "This is the third document for the campus reservation"
    pause 1.0
    show doc4 with fade
    "Lastly, this is the final version of the form"
    pause 1.0
    jump right_hall_forward2

label director:
    scene bg_director at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Oh, ito yung director office"
    hide expression justine.get_image("talking") with dissolve
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "Hehe, naaalala ko laging busy si Direk"
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Para i-improve pa lalo yung Campus"
    hide expression justine.get_image("laughing") with dissolve
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "Huwag na natin istorbohin si Direk.. (Justine said please)"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("laughing") with dissolve
    jump right_hall_forward2

label admin:
    scene adminoffice at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Na-alala ko nung gumawa kami ng system para sa finals namin sa comprog"
    jus "pumunta kami dito para humingi ng permiso na mag-ikot sa campus at mag-picture"
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "naka-ilang balik kami dahil may proper procedure pala bago pumunta dito."
    # Start of flashback sequence
    scene lobbychairs at custom_size_transform with fade
    show expression mae.get_image("talking") at left
    show expression sophie.get_image("normal") at right
    m "Kaming dalawa nalang ni Sophie yung papasok sa loob para ipasa yung letter"
    # 1st Attempt
    scene bg_admin_office at custom_size_transform with fade
    show expression mae.get_image("smiling") at left with dissolve
    show expression sophie.get_image("smiling") at right with dissolve
    "(Left the office after a few minutes)"
    hide expression mae.get_image("smiling") with dissolve
    hide expression sophie.get_image("smiling") with dissolve
    scene lobbychairs at custom_size_transform with fade
    show expression sophie.get_image("talking") at right
    s "Guys ulitin daw mali raw yung format ng letter"
    hide expression sophie.get_image("talking") with dissolve
    show expression mae.get_image("talking") at left
    m "Ganito raw yung proper format"
    show expression mae.get_image("holding_paper") at left
    # 2nd Attempt
    scene bg_admin_office at custom_size_transform with fade
    show expression sophie.get_image("talking") at right
    show expression mae.get_image("normal") at left
    "left the office after a few minutes"
    scene lobbychairs at custom_size_transform with fade
    show expression mae.get_image("talking") at left
    m "need naman daw ng appointment sa sinta"
    # 3rd Attempt
    scene bg_admin_office at custom_size_transform with fade
    show expression sophie.get_image("talking") at right
    s "Manifesting ma-approve na to"
    show expression mae.get_image("normal") at left
    "left the office after a few minutes"
    scene lobbychairs at custom_size_transform with fade
    show expression mae.get_image("talking") at right
    ma "Finally! na-approve na rin HAHAHAHA"
    hide expression mae.get_image("talking") with dissolve
    # End of Flashback
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "Haha... naaawa ako sa kanila"
    hide expression justine.get_image("laughing") with dissolve
    menu:
        "knock and enter the admin office":
            jump adm_office1
        "Just enter the door":
            jump adm_office2
    jump right_hall_forward2

label adm_office1:
    scene bg_admin_office at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Hello po ma'am vidal"
    show expression vidal.get_image("talking") at right
    v "And you are..?"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Justine po ma’am from BSIT 4-1"
    show expression vidal.get_image("talking") at right
    v "Oh why hello Justine, what can I do for you?"
    show expression justine.get_image("talking") at justine_bottom_left
    jus " nag-iikot Ikot lang po para sa huling sandali ko as a student of this sintang paaralan"
    show expression vidal.get_image("talking") at right
    v "Kung ganon din ay, enjoyin mo na habang nandito ka"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Maraming salamat po"
    hide expression justine.get_image("talking") with dissolve
    hide expression vidal.get_image("talking") with dissolve
    jump right_hall_forward2

label adm_office2:
    scene bg_admin_office at custom_size_transform with fade
    show expression vidal.get_image("talking") at right
    v "Sino ka at bakit ka pumapasok lang ng basta basta?"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "uhmmm... Justine ma’am from BSIT 4-1 po"
    show expression vidal.get_image("angry_talking") at right
    v "Justine!!! Ilang taon ka nang nag-aaral dito pero hindi mo man lang alam ang tamang proseso bago pumasok?"
    show expression justine.get_image("scared") at justine_bottom_left
    jus "Sorry po Ma'am Vidal, hindi na po mau-ulit"
    show expression vidal.get_image("angry_talking") at right
    v "Kakatok ka lang ng 3 beses and give your greetings, ganoon ba kahirap yon?"
    show expression justine.get_image("scared") at justine_bottom_left
    jus "Maraming salamat po"
    hide expression justine.get_image("scared") with dissolve
    show expression vidal.get_image("angry_talking") at right with dissolve
    v "Labas!, marami pa kaming ginagawa at dadagdag ka pa!!!"
    scene adminoffice at custom_size_transform with fade
    "Justine was forced out"
    hide expression vidal.get_image("angry_talking") with dissolve
    jump right_hall_forward2

label mid:
    scene bg_midstair at custom_size_transform with fade
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "grabe walang katao tao himala?"
    hide expression justine.get_image("Sighing") with dissolve

label right_hall_forward3:
    scene bg_midstair at custom_size_transform with fade
    call screen right_hall_menu2

label lgbt_cr:
    scene bg_lgbt3 at custom_size_transform with fade
    scene bg_lgbt2 at custom_size_transform with fade
    scene bg_lgbt1 at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Nung nag PUPCET kami dati, nagulat ako na may LGBTQ na cr"
    jus "Kasi sa lahat ng school na napag-entrance exam ko"
    jus "Ngayon lang ako nakakita ng cr na para sa LGTBQ"
    show expression justine.get_image("talking") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "Iba talaga ang PUP"
    hide expression justine.get_image("talking") with dissolve
    hide expression justine.get_image("laughing") with dissolve
    jump lgbt_cr_menu

label lgbt_cr_menu:
    scene bg_lgbt1 at custom_size_transform with fade
    call screen lgbt_cr

label garden_back:
    menu:
        "Back Garden and Greet the Guard":
            jump back_garden
        "Back Garden and Didn't Greet the GUard":
            jump back_garden_1

label back_garden:
    scene bg_garden at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Hmmmm, naaalala ko sa banda rito namin nilagay yung mga project na halaman"
    jus "Noong first year kami"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve
    show expression guard.get_image("normal") at guard_bottom_right
    show expression guard.get_image("talking_annoyed") at guard_bottom_right
    g "Oyyy oyy, bawal pumunta rito ng walang paalam"
    hide expression guard.get_image("normal") with dissolve
    hide expression guard.get_image("talking_annoyed") with dissolve
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Ahhh sige po kuya, alis na lang ako"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve
    return

label back_garden_1:
    scene bg_garden at custom_size_transform with fade
    scene g1 at custom_size_transform with fade
    scene g2 at custom_size_transform with fade
    scene g3 at custom_size_transform with fade
    scene g4 at custom_size_transform with fade
    scene g5 at custom_size_transform with fade
    scene g6 at custom_size_transform with fade
    scene g7 at custom_size_transform with fade
    scene g8 at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    jus "Hmmmm, naaalala ko banda rito namin nilagay yung mga project na halaman"
    jus "Noong first year kami"
    hide expression justine.get_image("normal") with dissolve
    show expression guard.get_image("annoyed") at right
    g "Ang kulit mo ah! Diba sinabi ko na bawal dito?!"
    hide expression guard.get_image("annoyed") with dissolve
    show expression justine.get_image("normal") at justine_bottom_left
    jus "Sorry po kuya, promise hindi na po mauulit"
    hide expression justine.get_image("normal") with dissolve
    show expression guard.get_image("annoyed") at right
    g "Talagang hindi na mau-ulit to"
    g "Dahil dadalhin na kita sa Admin Office"
    hide expression guard.get_image("annoyed") with dissolve
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Sorry po talaga kuya, hindi na talaga to uulit promise"
    jus "Gusto ko lang naman pong mag-ikot"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve
    show expression guard.get_image("annoyed") at right
    g "Magpaliwanag ka nalang sa Admin Office"
    hide expression guard.get_image("annoyed") with dissolve
    scene bg_admin_office at custom_size_transform with fade
    show expression guard.get_image("annoyed") at right
    g "Good morning po Ma'am, irereklamo ko lang po ito"
    g "Paulit-ulit na kasi at hindi sumusunod"
    g "Pumupunta sa mga lugar na hindi dapat puntahan ng walang permiso"
    hide expression guard.get_image("annoyed") with dissolve
    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("talking") at right
    v "Ano pangalan, year at section mo iho?"
    hide expression vidal.get_image("normal") with dissolve
    hide expression vidal.get_image("talking") with dissolve
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Justine po and BSIT 4-1"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve
    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("talking") at right
    v "Okay Justine, is that true?"
    hide expression vidal.get_image("normal") with dissolve
    hide expression vidal.get_image("talking") with dissolve
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Pasensya na po Ma'am"
    jus "Gusto ko lang naman po mag-ikot"


    show expression guard.get_image("annoyed") at right
    g "Magpaliwanag ka nalang sa Admin Office"
    hide expression guard.get_image("annoyed") with dissolve

    scene bg_admin_office at custom_size_transform with fade
    show expression guard.get_image("annoyed") at right
    g "Good morning po Ma'am, irereklamo ko lang po ito"
    g "Paulit-ulit na kasi at hindi sumusunod"
    g "Pumupunta sa mga lugar na hindi dapat puntahan ng walang permiso"
    hide expression guard.get_image("annoyed") with dissolve

    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("talking") at right
    v "Ano pangalan, year at section mo iho?"
    hide expression vidal.get_image("normal") with dissolve
    hide expression vidal.get_image("talking") with dissolve

    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Justine po and BSIT 4-1"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve

    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("talking") at right
    v "Okay Justine, is that true?"
    hide expression vidal.get_image("normal") with dissolve
    hide expression vidal.get_image("talking") with dissolve

    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Pasensya na po Ma'am"
    jus "Gusto ko lang naman po mag-ikot"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve

    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("talking") at right
    v "Dahil diyan magkakaroon ka ng punishment dahil sa hindi pagsunod at paglabag"
    v "Kinakailangan mo na gawin ang mga dapat na i-utos o i-aassign sayong gawain"
    v "Kailangan mo itong matapos at magawa kung hindi malalate ang pag-graduate mo"
    hide expression vidal.get_image("normal") with dissolve
    hide expression vidal.get_image("talking") with dissolve

    show expression justine.get_image("talking") at justine_bottom_left
    show expression justine.get_image("Sighing") at justine_bottom_left
    show expression justine.get_image("scared") at justine_bottom_left
    jus "Pero po Ma'am...."
    hide expression justine.get_image("talking") with dissolve
    hide expression justine.get_image("Sighing") with dissolve
    hide expression justine.get_image("scared") with dissolve

    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("angry") at right
    show expression vidal.get_image("angry_talking") at right
    v "No more buts, you may go now"
    hide expression vidal.get_image("normal") with dissolve
    hide expression vidal.get_image("angry") with dissolve
    hide expression vidal.get_image("angry_talking") with dissolve

    "THE END"

    jump right_hall_forward3

label garden_1:
    scene bg_garden at custom_size_transform with fade
    
label garden_view_menu:
    scene bg_garden at custom_size_transform with fade
    call screen garden_view

label garden_view_menu1:
    scene bg_garden1 at custom_size_transform with fade
    call screen cat

label garden_view2:
    scene bg_garden2 at custom_size_transform with fade
    pause 1.0
    scene bg_garden3 at custom_size_transform with fade
    pause 1.0
         
    jump back_garden_view

label back_garden_view:
    scene bg_garden3 at custom_size_transform with fade
    call screen back_garden

label g:
    scene g1 at custom_size_transform
    scene g2 at custom_size_transform
    scene g3 at custom_size_transform
    scene g4 at custom_size_transform
    scene g5 at custom_size_transform
    scene g6 at custom_size_transform
    scene g7 at custom_size_transform
    scene g8 at custom_size_transform
    scene g9 at custom_size_transform
    scene g10 at custom_size_transform
    scene g11 at custom_size_transform
    scene g12 at custom_size_transform
    call screen entrance_hideout
    return

label right_exit:
    scene bg_exit1 at custom_size_transform with fade
    scene bg_exit2 at custom_size_transform with fade
    scene bg_exit3 at custom_size_transform with fade
    scene bg_exit4 at custom_size_transform with fade
    scene bg_exit5 at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Ohhh.. ito yung short cut palabas sa gate"
    jus "Pero usually kasi naka-sara to."
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve

    menu:
        "Pet the Cat":  # _____Choice 1_______
            jump pet_cat
        "Do not Pet the Cat":
            jump donotpet
        "Proceed to the Main Gate":
            jump maingate

label pet_cat:
    scene pet_cat at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "Wow! Ang cute naman ng pusa"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("laughing") with dissolve

    jump right_exit_menu

label donotpet:
    scene bg_exit5 at custom_size_transform with fade
    jump right_exit_menu

label maingate:
    scene bg_after_school_gate at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "ang daming ko naging memorya dito"
    jus "may maganda pero may mga part na gusto ko din kalimutan"
    jus "pero masasabi ko talaga na ma mi-miss ko talaga to sa susunod ulit sintang paaralan"
    "THE END"
    jump outside_exit_menu

label right_exit_menu:
    scene bg_exit6 at custom_size_transform with fade
    pause 1.0
    scene bg_exit7 at custom_size_transform with fade
    call screen right_exit_menu1

label outside_exit:
    scene bg_exit8 at custom_size_transform with fade
    pause 1.0
    scene bg_exit9 at custom_size_transform with fade
    pause 1.0
    scene bg_exit10 at custom_size_transform with fade
    pause 1.0
    jump outside_exit_menu

label fire_exit_inside1:
    scene bg_fire_exit_inside1 at custom_size_transform with fade
    scene bg_fire_exit_inside2 at custom_size_transform with fade
    scene bg_fire_exit_inside3 at custom_size_transform with fade
    scene bg_fire_exit_inside4 at custom_size_transform with fade
    scene bg_fire_exit_inside5 at custom_size_transform with fade

label fire_exit_inside_menu:
    scene bg_fire_exit_inside5 at custom_size_transform with fade
    call screen fire_exit_inside_menu1

label outside_exit_menu:
    scene bg_after_school_gate at custom_size_transform with fade
    call screen nav_door_gate

label upstairs:
    scene bg_stair1 at custom_size_transform with fade
    pause 1.0
    scene bg_stair2 at custom_size_transform with fade
    pause 1.0
    scene bg_stair3 at custom_size_transform with fade
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "Ba yan! Wait nga!"
    hide expression justine.get_image("Sighing") with dissolve

    jump second_floor_stair

label second_floor_stair:
    scene bg_stair4 at custom_size_transform with fade
    scene bg_stair5 at custom_size_transform with fade
    jump second_floor_stair1

label second_floor_stair1:
    scene bg_stair6 at custom_size_transform with fade
    call screen fire
    return

label male_bathroom1:
    scene m1 at custom_size_transform with fade
    scene m2 at custom_size_transform with fade
    scene m3 at custom_size_transform with fade
    scene m4 at custom_size_transform with fade
    scene m5 at custom_size_transform with fade
    call screen male_bathroom
    return

label fire_exit:
    if not visited_fire_exit:
        $ visited_fire_exit = True
        scene fire_exit2 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Na-aalala ko rito lagi pumupunta si Mae"
        jus "Tuwing nag-aantay kami sa last subject"
        hide expression justine.get_image("talking") with dissolve
        hide expression justine.get_image("happy") with dissolve
        # Start of Flashback Scene____
        scene fire_exit1 at custom_size_transform with fade
        show expression mae.get_image("smiling") at kim_bottom_right
        show expression mae.get_image("talking") at kim_bottom_right
        m "grabe ang sarap ng hangin"
        m "nakaka relax pwede ka mag emote dito oh hahaha"
        hide expression mae.get_image("smiling") with dissolve
        hide expression mae.get_image("talking") with dissolve
        # End of Flashback
    else:
        # IRL
        show expression justine.get_image("smiling") at justine_bottom_left
        show expression justine.get_image("happy") at justine_bottom_left
        jus "hmmm.. Nakakrelax nga"
        # Justine Monologue
        jus "Pero alis na tayo rito kasi hindi dapat tinatambayan 'to"
        hide expression justine.get_image("smiling") with dissolve
        hide expression justine.get_image("happy") with dissolve
        # End of Justine Monologue
    jump second_floor_menu

label second_floor_menu:
    scene bg_floor2_halfwayright at custom_size_transform with fade
    call screen right_hall_menu3

label floor2_1:
    scene sf1 at custom_size_transform with fade
    scene sf2 at custom_size_transform with fade
    scene sf3 at custom_size_transform with fade
    scene sf4 at custom_size_transform with fade
    scene sf5 at custom_size_transform with fade
    scene sf6 at custom_size_transform with fade
    call screen room
    return

label floor2_2:
    scene sf6 at custom_size_transform with fade
    call screen room
    return

label room_204:
    if not visited_room_204:
        $ visited_room_204 = True
        scene chair at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        show expression justine.get_image("talking") at justine_bottom_left
        jus "madami akong memory dito"
        jus "ang pinaka paborito ko siguro yung nag pra-practice kami para sa chorale"
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Na-aalala ko tuloy si Carl nung huling practice namin"
        show expression justine.get_image("laughing") at justine_bottom_left
        hide expression justine.get_image("happy") with dissolve
        hide expression justine.get_image("talking") with dissolve
        # Start of the Flashback
        scene chair1 at custom_size_transform with fade
        show expression justine.get_image("suggesting") at kim_bottom_right
        jus "kabayo ay di natin problema~  pulot at damo lang ay tama na~"
        show expression justine.get_image("talking") at kim_bottom_right
        hide expression justine.get_image("suggesting") with dissolve
        hide expression justine.get_image("talking") with dissolve
        # End of Flashback
    else:
        # IRL
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Kahit 2 days lang practice namin na-clutch pa rin namin"
        show expression justine.get_image("laughing") at justine_bottom_left
        hide expression justine.get_image("happy") with dissolve
        hide expression justine.get_image("laughing") with dissolve
    jump floor2_2

label floor2_3:
    scene sf7 at custom_size_transform with fade
    call screen pup
    return

label pup_library:
    if not visited_pup_library:
        $ visited_pup_library = True
        scene library1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left with dissolve
        jus "Dito sa library na 'to"
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Naaalala ko lagi kaming nag-tatambay dito"
        jus "Kapag may vacant time o kaya kapag nags-study kami rito"
        show expression justine.get_image("talking") at justine_bottom_left
        jus "na alala ko tuloy yung sinabi ni jorie"
        hide expression justine.get_image("talking") with dissolve
        hide expression justine.get_image("happy") with dissolve
        # Start of the Flashbacks
        scene library1 at custom_size_transform with fade
        show expression justine.get_image("smiling") at kim_bottom_right
        jus "At sobrang lamig sa room nato dahil may aircon kaya ang ganda tambayan."
        show expression justine.get_image("talking") at kim_bottom_right
        jus "Lalo na kung sa room namin pag mag klase ang init"
        jus "kaya after ng klase namin punta agad sa library."
        hide expression justine.get_image("smiling") with dissolve
        hide expression justine.get_image("talking") with dissolve
        # End of flashback
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Justine: well, totoo naman malamig dito"
        show expression justine.get_image("talking") at justine_bottom_left
        jus "at pwede ka din humiram ng libro para pang palipas oras din"
        hide expression justine.get_image("happy") with dissolve
        hide expression justine.get_image("talking") with dissolve
    else:
        scene library2 at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Tambayan at Studyhan namin dito"
        show expression justine.get_image("talking") at justine_bottom_left
        hide expression justine.get_image("talking") with dissolve
        hide expression justine.get_image("happy") with dissolve
    return
    # Note: 'jump floor2_3' was moved before 'return' in the original to avoid unreachable code; kept as 'return' here per your input

label floor_1:
    scene sf7 at custom_size_transform with fade
    scene sf8 at custom_size_transform with fade
    scene sf9 at custom_size_transform with fade
    scene sf10 at custom_size_transform with fade
    scene sf11 at custom_size_transform with fade
    scene sf12 at custom_size_transform with fade
    scene sf13 at custom_size_transform with fade
    call screen discussion
    return

label discussion_room:
    scene discussion at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Pagkakatanda ko, pwede tong room na to"
    jus "Basta magpapaalam lang sa librarian"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve
    jump floor_2

label floor_2:
    scene sf13 at custom_size_transform with fade
    call screen discussion
    return

label floor__1:
    scene sf14 at custom_size_transform with fade
    scene sf15 at custom_size_transform with fade
    scene sf16 at custom_size_transform with fade
    scene sf17 at custom_size_transform with fade
    call screen second_last_floor
    return

label floor__2:
    scene sf17 at custom_size_transform with fade
    call screen second_last_floor
    return

label second_floor:
    scene bg_second_floor at custom_size_transform
    call screen second_floor_menu

label halfwayground:
    scene left_halfway_ground1 at custom_size_transform with fade
    call screen left_halfway_menu

label nstp:
    scene bg_nstp with fade
    call screen nstp_room
    return

label faculty_lounge:
    scene faculty_inside at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left with dissolve
    show expression justine.get_image("normal") at justine_bottom_left
    jus "Ang tagal ko ring hindi nakatapak dito sa faculty… pero parang walang nag bago."
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Dito ako laging nakatambay."
    jus "Dito ako palagi nakikiusap sa professor namin nung Discrete Structures para makapa consult sa project."
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "Minsan, nakikipag kwentuhan o nakiki chismis lang pagkatapos ng klase."
    hide expression justine.get_image("laughing") with dissolve
    # Start of flashback
    "(Flashback Sequence)"
    show expression justine.get_image("normal") at kim_bottom_right
    show expression justine.get_image("talking") at kim_bottom_right
    jus "Yan naman, nakalimutan mo pa kasi ipasa yung assignment mo."
    show expression justine.get_image("normal") at kim_bottom_right
    show expression justine.get_image("talking") at kim_bottom_right
    jus "Swerte ka na pagbibigyan kita dito ah,"
    show expression justine.get_image("normal") at kim_bottom_right
    show expression justine.get_image("talking") at kim_bottom_right
    jus "wag mo naman kalimutan sa susunod ha?"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Opo ma'am, pasensya na."
    show expression justine.get_image("scared") at justine_bottom_left
    show expression justine.get_image("sad") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Ramdam ko pa din ‘yung kaba tuwing kumakatok ako sa pinto."
    hide expression justine.get_image("talking") with dissolve
    hide expression justine.get_image("scared") with dissolve
    hide expression justine.get_image("sad") with dissolve
    jump left_ground_2

default visited_room_302 = False
default visited_girls_cr = False

label left_ground1:
    scene left_halfway_ground1 at custom_size_transform with fade
    scene left_halfway_ground2 at custom_size_transform with fade
    call screen left_ground_menu1

label left_ground_1:
    scene left_halfway_ground2 at custom_size_transform with fade
    call screen left_ground_menu1
    return

label left_ground2:
    scene left_halfway_ground3 at custom_size_transform with fade
    scene left_halfway_ground4 at custom_size_transform with fade
    scene left_halfway_ground5 at custom_size_transform with fade
    call screen left_ground_menu2
    return

label left_ground_2:
    scene left_halfway_ground5 at custom_size_transform with fade
    call screen left_ground_menu2
    return

label avr_room:
    scene bg_avr_door at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Ah, yung AVR... Naalala ko si Sophie tuloy. Na high blood pa siya noon dahil pinalinis pa siya nung nakalat namin yung AVR..."
    # Start of flashback
    scene bg_avr with fade
    show expression sophie.get_image("angry") at kim_bottom_right
    show expression justine.get_image("shocked") at justine_bottom_left
    soph "Ano ba yan, itatapon nalang eto! Mas lalo na ikaw Justin! Lagot ka sa akin mamaya!"
    hide expression sophie.get_image("angry") with dissolve
    hide expression justine.get_image("shocked") with dissolve
    # End of flashback
    scene bg_avr with fade
    show expression justine.get_image("shivering") at justine_bottom_left
    jus "Inabangan niya pa ako sa gate nung uwian... Nakakaiba talaga yung galit netong babae na 'to…"
    hide expression justine.get_image("shivering") with dissolve
    jump left_ground_3

label left_ground3:
    scene left_halfway_ground6 at custom_size_transform with fade
    scene left_halfway_ground7 at custom_size_transform with fade
    call screen left_ground_menu3
    return

label left_ground_3:
    scene left_halfway_ground7 at custom_size_transform with fade
    call screen left_ground_menu3
    return

label third1:
    scene stair1 at custom_size_transform with fade
    scene stair2 at custom_size_transform with fade
    scene stair3 at custom_size_transform with fade
    scene stair4 at custom_size_transform with fade
    scene stair5 at custom_size_transform with fade
    call screen third_floor1
    return

label third1_1:
    scene stair5 at custom_size_transform with fade
    call screen third_floor1
    return

label thirdfloor_hall:
    scene hallway1 at custom_size_transform with fade

label room_302:
    if visited_room_302:
        $ visited_room_302 = True  # Fixed syntax, assuming intent was to set it true
        scene room1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Room 302…"
        show expression justine.get_image("laughing") at justine_bottom_left
        jus "naalala ko tuloy yung nangyari dati hahaha"
        hide expression justine.get_image("talking") with dissolve
        hide expression justine.get_image("laughing") with dissolve
        # Start of the Flashback
        scene room2 at custom_size_transform with fade
        show expression kim.get_image("calling") at right with dissolve
        k "Nasaan kayo guys? (nag-call sa gc)"
        hide expression kim.get_image("calling") with dissolve
        show expression justine.get_image("holding_phone") at justine_bottom_left
        jus "Nasa room 303 po"
        hide expression justine.get_image("holding_phone") with dissolve
        "(After a few minutes, Kim entered the room a bit irritated)"
        show expression kim.get_image("normal") at right
        hide expression kim.get_image("normal") with dissolve
        show expression carl.get_image("talking") at left
        c "Ay… room 303 kase nakalagay sa table eh"
        hide expression carl.get_image("talking") with dissolve
        show expression kim.get_image("talking") at right
        k "Pagsilip ko sa room 303 te"
        show expression kim.get_image("normal") at right
        k "ibang estudyante nakita ko tas nakatitigan ko pa."
        k "Nakakahiya.."
        hide expression kim.get_image("talking") with dissolve
        hide expression kim.get_image("normal") with dissolve
    else:
        scene room1 at custom_size_transform with fade
        show expression justine.get_image("laughing") at justine_bottom_left
        jus "Yung table talaga may kasalanan"
        hide expression justine.get_image("laughing") with dissolve
    jump turn_right_4

label room_305:
    scene room307_2 at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Room 305… ilang klase rin natin dito ginanap."
    hide expression justine.get_image("talking") with dissolve
    show expression mae.get_image("talking") at right
    ma "Oo, dito ako unang na tawag sa graded recitation"
    hide expression mae.get_image("talking") with dissolve
    show expression mae.get_image("smiling") at right
    ma "wala pa akong review noon. Haha."
    hide expression mae.get_image("smiling") with dissolve
    show expression justine.get_image("alarmed") at justine_bottom_left
    jus "Oh Mae andito ka pala"
    hide expression justine.get_image("alarmed") with dissolve
    show expression mae.get_image("smiling") at right
    ma "Oo HAHAHA"
    hide expression mae.get_image("smiling") with dissolve
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "Naalala ko rin ‘yung lecture na walang kuryente."
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Ang init, pero tuloy pa rin."
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "‘Yun ang tunay na dedication"
    hide expression justine.get_image("Sighing") with dissolve
    hide expression justine.get_image("happy") with dissolve
    hide expression justine.get_image("laughing") with dissolve
    menu:
        "Peek through the Window":
            jump peek_window
        "Walk away":
            jump walk_away1
    jump turn_right_2

label peek_window:
    "Justine looks through the glass window in the door"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Parang hindi na siya kasing gulo gaya nung dati"
    hide expression justine.get_image("talking") with dissolve
    show expression mae.get_image("talking") at right with dissolve
    ma "Oo. Pero kahit paano, may sentimental value pa rin."
    hide expression mae.get_image("talking") with dissolve
    jump turn_right_2

label walk_away1:
    scene hallway3 at custom_size_transform with fade
    "Justine smiles faintly and continues walking down the hallway."
    show expression justine.get_image("waving") at justine_bottom_left
    jus "Salamat, Room 305."
    hide expression justine.get_image("waving") with dissolve
    show expression justine.get_image("sad") at justine_bottom_left
    jus "Kahit minsan stressful, naging parte ka ng journey."
    hide expression justine.get_image("sad") with dissolve
    show expression mae.get_image("talking") at right
    ma "Sige na nga"
    hide expression mae.get_image("talking") with dissolve
    show expression mae.get_image("smiling") at right with dissolve
    ma "Baka maiyak pa tayo riyan"
    hide expression mae.get_image("smiling") with dissolve
    jump turn_right_2

label room_307:
    "(Pumasok si Justine sa ROOM 307)"
    scene room307_1 at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus " ayy naalala ko tong room na ‘to."
    hide expression justine.get_image("talking") with dissolve
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Ito yung isa sa mga room na ‘di ko makalimutan."
    hide expression justine.get_image("happy") with dissolve
    scene room307_3 at custom_size_transform with fade
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "dito kami nagpatay ng oras para sa PE namin hahaha."
    hide expression justine.get_image("laughing") with dissolve
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "Tapos wala palang klase"
    hide expression justine.get_image("Sighing") with dissolve
    show expression justine.get_image("disappointed") at justine_bottom_left
    jus "Prinactice pa naman namin mga excercises namin."
    hide expression justine.get_image("disappointed") with dissolve
    jump turn_right_1

label turn_right_2:
    scene hallway3 at custom_size_transform with fade
    call screen third_floor3
    return

label boys_cr:
    scene m1 at custom_size_transform with fade
    scene m2 at custom_size_transform with fade
    scene m3 at custom_size_transform with fade
    scene m4 at custom_size_transform with fade
    scene m5 at custom_size_transform with fade
    "(Pumasok si Justine sa boys' CR)"
    show expression justine.get_image("scared") at justine_bottom_left
    "Amoy linis pero may halong luma—parang floor wax na natuyuan ng pawis."
    show expression justine.get_image("smiling") at justine_bottom_left
    jus "Yung salamin, andito pa rin."
    show expression justine.get_image("talking") at justine_bottom_left
    jus "At mga urinal wala paring pagbabago. Classic."
    show expression justine.get_image("laughing") at justine_bottom_left
    jus "Dito ako minsang nagtago noon. Para makapag isip isip."
    hide expression justine.get_image("scared") with dissolve
    hide expression justine.get_image("smiling") with dissolve
    hide expression justine.get_image("talking") with dissolve
    hide expression justine.get_image("laughing") with dissolve
    call screen boy_bathroom

label turn_right:
    scene hallway1 at custom_size_transform with fade
    scene hallway2 at custom_size_transform with fade

label turn_right_1:
    scene hallway2 at custom_size_transform with fade
    call screen third_floor2
    return

label girls_cr:
    if not visited_girls_cr:
        $ visited_girls_cr = True
        scene girls1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "hmm? Eto yung CR for girls, ano kaya itsura neto sa loob?"
        hide expression justine.get_image("talking") with dissolve
        show expression justine.get_image("laughing") at justine_bottom_left
        jus "naalala ko tuloy yung sinabi ni Lyn"
        hide expression justine.get_image("laughing") with dissolve
        # Start of the Flashback
        scene girls2 at custom_size_transform with fade
        show expression lyn.get_image("talking") at right
        l "ano itsura ng cr ng boys justine?"
        show expression lyn.get_image("smug") at right
        l "Kasi samin may salamin na may tubig pa yung sa inyo?"
        hide expression lyn.get_image("talking") with dissolve
        hide expression lyn.get_image("smug") with dissolve
        # End of Flashback
    else:
        # IRL
        scene girls1 at custom_size_transform with fade
        show expression justine.get_image("realised") at justine_bottom_left
        jus "na-curious tuloy ako ano itsura ng loob"
        hide expression justine.get_image("realised") with dissolve
        "Ella suddenly appear"
        show expression ella.get_image("talking") at right
        e "huyy, ano ginagawa mo dyan?"
        show expression ella.get_image("smiling") at right
        e "Bat ka nakatitig sa cr?"
        hide expression ella.get_image("talking") with dissolve
        hide expression ella.get_image("smiling") with dissolve
        show expression justine.get_image("alarmed") at justine_bottom_left
        jus "Hu-huh?"
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Kung ano man ang iniisip mo mali yun"
        show expression justine.get_image("talking") at justine_bottom_left
        jus "na alala ko lang yung sinabi ni Lyn tungkol sa CR ng girls"
        hide expression justine.get_image("alarmed") with dissolve
        hide expression justine.get_image("Sighing") with dissolve
        hide expression justine.get_image("talking") with dissolve
        show expression ella.get_image("grinning") at right
        e "ayy!"
        hide expression ella.get_image("grinning") with dissolve
        show expression ella.get_image("talking") at right
        e "Speaking of cr ng girls"
        hide expression ella.get_image("talking") with dissolve
        show expression ella.get_image("whispering") at right
        e "alam mo ba…"
        hide expression ella.get_image("whispering") with dissolve
        show expression ella.get_image("talking") at right
        e "kasi one time, mag isa lang akong pumunta"
        hide expression ella.get_image("talking") with dissolve
        show expression ella.get_image("whispering") at right
        e " tas may nafeel ako na kakaiba"
        e "kaya sumilip ako"
        hide expression ella.get_image("whispering") with dissolve
        show expression ella.get_image("grinning") at right
        e "sa door ng cr tas wala naman tas pag tingin ko ulit…"
        hide expression ella.get_image("grinning") with dissolve
        show expression justine.get_image("scared") at justine_bottom_left
        jus "ta-tapos…?"
        hide expression justine.get_image("scared") with dissolve
        show expression ella.get_image("whispering") at right
        e "…si Lyn lang pala "
        hide expression ella.get_image("whispering") with dissolve
        show expression ella.get_image("grinning") at right
        e "kala mo nakakatakot noh"
        hide expression ella.get_image("grinning") with dissolve
        show expression ella.get_image("smiling") at right
        e "kala ko rin e hahahah"
        hide expression ella.get_image("smiling") with dissolve
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "hayss ano ba yan"
        hide expression justine.get_image("Sighing") with dissolve
        show expression justine.get_image("laughing") at justine_bottom_left
        jus "akala ko kung ano na hahaha…"
        hide expression justine.get_image("laughing") with dissolve
        show expression ella.get_image("talking") at right
        e "well anyway alis na ako may pupuntahan pa ako"
        hide expression ella.get_image("talking") with dissolve
        show expression justine.get_image("waving") at justine_bottom_left
        jus "ok bye"
        hide expression justine.get_image("waving") with dissolve
    jump third1_1

label turn_right1:
    scene hallway4 at custom_size_transform with fade
    scene hallway5 at custom_size_transform with fade
    call screen third_floor6
    return

label turn_right_3:
    scene hallway5 at custom_size_transform with fade
    call screen third_floor6
    return

label turn_right_4:
    scene hallway6 at custom_size_transform with fade
    call screen third_floor4
    return

label turn_right5:
    scene hallway7 at custom_size_transform with fade
    scene hallway8 at custom_size_transform with fade
    scene hallway9 at custom_size_transform with fade
    call screen third_floor5
    return

label turn_right_5:
    scene hallway9 at custom_size_transform with fade
    call screen third_floor5

label science_lab:
    scene science_lab at custom_size_transform with fade
    call screen science_lab1
    return


label turn_left:
    scene rightside_staircase at custom_size_transform with fade
    call screen turn_left_1
    return

label fourth_floor:
    scene 1 at custom_size_transform with fade
    scene 2 at custom_size_transform with fade
    scene 3 at custom_size_transform with fade
    call screen fourth_floor1
    return

label fourth_floor_1:
    scene 3 at custom_size_transform with fade
    call screen fourth_floor1
    return

label m_bathroom:
    scene m1 at custom_size_transform with fade
    scene m2 at custom_size_transform with fade
    scene m3 at custom_size_transform with fade
    scene m4 at custom_size_transform with fade
    scene m5 at custom_size_transform with fade
    call screen ma_bathroom
    return

label fourth_floors1:
    scene f1 at custom_size_transform with fade
    call screen fourth
    return

default visited_comlab = False
default visited_project_proposal = False
default visited_lab_management = False
default visited_food_beverage = False
default visited_org = False
default visited_housekeeping_room = False
default visited_csc = False

label comlab:
    if not visited_comlab:
        $ visited_comlab = True
        scene comlab at custom_size_transform with fade
        show expression justine.get_image("alarmed") at justine_bottom_left
        jus "Ay! naalala ko bigla"
        jus "nung first time pa lang namin pumasok dito"
        jus "nung freshman pa lang kami"
        hide expression justine.get_image("alarmed") with dissolve

        show expression justine.get_image("laughing") at justine_bottom_left
        jus "nakita ko si carl binuksan yung pc at nagdrawing ng pasimple."
        hide expression justine.get_image("laughing") with dissolve

        # Flashback
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Uy carl ano ginagawa mo?"
        hide expression justine.get_image("talking") with dissolve

        show expression carl.get_image("talking") at right
        c "shhh wag kang maingay, mamaya makita tayo ni sir"
        hide expression carl.get_image("talking") with dissolve
    else:
        show expression justine.get_image("laughing") at justine_bottom_left
        jus "grabe ang tapang talaga nya hahaha…"
        hide expression justine.get_image("laughing") with dissolve

    jump fourth_floors1

label computer_hardware:
    scene comhardware at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Dito kami pumupunta kapag may hands on activity"
    jus "ang maintenance at repair ng mga equipment dito lalo na pag computer."
    hide expression justine.get_image("talking") with dissolve

    show expression justine.get_image("happy") at justine_bottom_left
    jus "Naalala ko tuloy dati si Ella"
    jus " Halos sya lang ang naka ayos ng mga computer na pinapaayos sa amin noon"
    hide expression justine.get_image("happy") with dissolve

    jump fourth_floors1

label project_proposal:
    if not visited_project_proposal:
        $ visited_project_proposal = True
        scene proj at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Dito kami pumunta nung nag project defense kami"
        hide expression justine.get_image("talking") with dissolve

        show expression justine.get_image("scared") at justine_bottom_left
        jus "Naalala ko grabe yung kaba ko nung proposal defense"
        jus "pero mas malala parin yung kaba ni Mae non"
        jus "hanggang ngayon hindi ko parin nalilimutan."
        hide expression justine.get_image("scared") with dissolve

        # Flashback
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Mae try mo kumalma, nanginginig kana"
        hide expression justine.get_image("talking") with dissolve

        show expression mae.get_image("talking") at justine_bottom_left
        m "Tinatry ko ok?"
        m "Pero what if ma-reject yung proposal?"
        m "What if ma blanko ako? What if-"
        hide expression mae.get_image("talking") with dissolve
    else:
        show expression justine.get_image("laughing") at justine_bottom_left
        jus "Grabe ang pag overthink nya"
        jus "halos nanginginig buong katawan nya noon HAHAHAHA"
        hide expression justine.get_image("laughing") with dissolve

    jump fourth_floors2

label lab_management:
    if not visited_lab_management:
        $ visited_lab_management = True
        scene lab_management at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Pagkakaalam ko dito nagluluto ang mga HM"
        jus "Lagi akong nagugutom sa tuwing napapadaan ako dito"
        jus "lalo na pag nagluluto ang mga HM"
        hide expression justine.get_image("talking") with dissolve
    else:
        scene lab_management at custom_size_transform with fade
        show expression justine.get_image("realised") at justine_bottom_left
        jus "Ohh IT lab"
        hide expression justine.get_image("realised") with dissolve

        show expression justine.get_image("talking") at justine_bottom_left
        jus "Ito yung admin or control room"
        jus "para sa lahat ng IT-related laboratories sa campus tulad ng Comlab"
        hide expression justine.get_image("talking") with dissolve

        show expression justine.get_image("sad") at justine_bottom_left
        jus "pero until now di pa rin ako nakakapasok dyan."
        hide expression justine.get_image("sad") with dissolve

        show expression lyn.get_image("pout") at right
        l "actually same"
        hide expression lyn.get_image("pout") with dissolve

        show expression justine.get_image("alarmed") at justine_bottom_left
        jus "WAH!! Lyn?! San ka nanggaling?"
        hide expression justine.get_image("alarmed") with dissolve

        show expression lyn.get_image("talking") at right
        l "i-kalma mo tih hahaha, may pinapakuha lang sakin na drive si kim"
        hide expression lyn.get_image("talking") with dissolve

        show expression justine.get_image("talking") at justine_bottom_left
        jus "ah oo nga pala may nabanggit nga na ganyan si kim kanina"
        jus "pero grabe ka naman bat bigla bigla ka sumusulpot?"
        hide expression justine.get_image("talking") with dissolve

        show expression lyn.get_image("Anya_smirk") at right
        l "sorry na HAHAHAHA"
        l "Anyway, bye, kukunin ko pa yung drive"
        hide expression lyn.get_image("Anya_smirk") with dissolve

        show expression justine.get_image("waving") at justine_bottom_left
        jus "bye"
        hide expression justine.get_image("waving") with dissolve

    jump kitchen_lab

label food_beverage:
    scene food_and_bev_room2 at custom_size_transform with fade
    if not visited_food_beverage:
        $ visited_food_beverage = True
        scene s at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Pag napapadaan ako rito"
        jus "feel ko lagging may birthday dahil sa ganda ng pagkakaayos"
        jus "naalala ko yung sinabi ni Jorie tungkol sa room na to"
        hide expression justine.get_image("talking") with dissolve
        # Flashback
        show expression jorie.get_image("talking") at right
        j "Kaya pala ganyan"
        j "ang ayos nyan kase dyan nag t-training ang mga HM Students"
        hide expression jorie.get_image("talking") with dissolve

        show expression jorie.get_image("smiling") at right
        j "kung ano nga ba ang dapat nilang gawin pag sila ay natatrabaho na."
        hide expression jorie.get_image("smiling") with dissolve
    else:
        show expression justine.get_image("talking") at justine_bottom_left
        jus "feel ko ang intense ng training nila dyan"
        hide expression justine.get_image("talking") with dissolve

    jump fourth_floors3

label kitchen_lab:
    scene kitchen_lab2 at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Kung may storage room sila, syempre may kitchen din"
    hide expression justine.get_image("talking") with dissolve

    show expression lyn.get_image("talking") at right
    l "Dito naman nagluluto ang mga HM Students kaya pag napapadaan ako rito"
    l "nagugutom agad ako dahil sa bango ng mga niluluo nila."
    hide expression lyn.get_image("talking") with dissolve

    show expression justine.get_image("alarmed") at justine_bottom_left
    jus "TALAGA NAMAN LYN ??"
    jus "BIBIGYAN MO BA AKO NG SAKIT SA PUSO?"
    hide expression justine.get_image("alarmed") with dissolve

    show expression lyn.get_image("talking") at right
    l "HAHAHA… SORRRY NA ANYWAY BABALIK NA SANA AKO KASO NA KITA KITA MYBAD"
    l "Minsan gusto ko nalang tumayo dyan nang matagal"
    l "dahil di nakakasawang amuyin ang mga niluluo nila"
    hide expression lyn.get_image("talking") with dissolve

    show expression justine.get_image("talking") at justine_bottom_left
    jus "sa totoo lang"
    hide expression justine.get_image("talking") with dissolve

    show expression lyn.get_image("talking") at right
    l "anyway bibigay ko papala tong drive kay kim"
    l "Bye~"
    hide expression lyn.get_image("talking") with dissolve

    jump fourth_floors3

label HM_storage:
    scene hm_storage_room1 at custom_size_transform with fade
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Ang ganda talaga rito."
    jus "Andito yung mga plato,baso, at uniform na ginagamit ng mga HM Students."
    jus "Pag nakikita ko nga silang may dalang lutong pagkain ay naiinggit ako"
    jus "kase akala ko dati puro lang sila linis"
    jus "yung parang mga House keeping yun pala may halong pagkain din"
    hide expression justine.get_image("happy") with dissolve

    jump fourth_floors3

label student_org:
    if not visited_org:
        $ visited_org = True
        scene student_org1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Hmm, org room"
        jus "eto yung room na ginagamit nila pag kaylangan ng mga org."
        jus "Andito din mga gamit ng iba’t ibang org."
        jus "naalala ko sabi ni Ella nung first year kami"
        hide expression justine.get_image("talking") with dissolve
    else:
        show expression justine.get_image("talking") at justine_bottom_left
        jus "grabe, ang strict talaga ng school na ito"
        hide expression justine.get_image("talking") with dissolve

    jump fourth_floors4

label housekeeping_room:
    if not visited_housekeeping_room:
        $ visited_housekeeping_room = True
        scene housekeeping_room at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Housekeeping Room."
        jus "Parang ilang beses ko nang nadadaanan"
        jus "‘to pero never ko pa rin siya napapasok"
        jus "Naalala ko yung sabi ni Mae dati…"
        hide expression justine.get_image("talking") with dissolve

        # Flashback
        show expression justine.get_image("smiling") at justine_bottom_left
        jus "Para saan kaya ‘to?"
        hide expression justine.get_image("smiling") with dissolve

        show expression mae.get_image("talking") at justine_bottom_left
        m "Ah, ‘yan?"
        m "Diyan raw nagpa-practice yung HM students ng mga housekeeping tasks"
        m "like bed making, towel folding, at room cleaning."
        m "Parang mini-hotel room training area."
        m "May mga gamit d’yan like mop, linen, tsaka mga hotel-grade supplies."
        m "Parang combo siya ng storage at simulation room."
        m "Hindi halata, pero malaking tulong ‘to sa training nila"
        m "Diyan nila natututunan ‘yung mga standard na pang-hotel service."
        m "Kaya malinis din sa paligid—sanay sila"
        hide expression mae.get_image("talking") with dissolve
    else:
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Oo nga, makes sense yung sinabi ni Mae..."
        hide expression justine.get_image("talking") with dissolve

        scene f6 at custom_size_transform with fade
        menu:
            "Try to Open the Door":
                jump door_open
            "Continue walking":
                jump continue_walking

label continue_walking:
    scene housekeeping_room at custom_size_transform with fade
    "(Justine glanced at the door one last time, then walked on.)"
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Wala rin naman akong kailangan dito"
    jus "Pero nice na malaman na hindi lang siya simpleng storage"
    jus "room—training room pala talaga"
    hide expression justine.get_image("happy") with dissolve

    jump fourth_floors4

label door_open:
    scene housekeeping_room at custom_size_transform with fade
    show expression justine.get_image("smiling") at justine_bottom_left
    jus "Locked. Yeah... expected"
    jus "Siguro bawal talaga pumasok kung wala kang activity dito"
    jus "Sensitive din kasi gamit—di biro ang linen at cleaning tools ng HM."
    hide expression justine.get_image("smiling") with dissolve
    jump fourth_floors4

label fourth_floors2:
    scene f2 at custom_size_transform with fade
    call screen fourth1
    return

label fourth_floors3:
    scene f3 at custom_size_transform with fade
    call screen fourth2
    return

label fourth_floors4:
    scene f4 at custom_size_transform with fade
    call screen fourth3
    return

label fourth_floors4_1:
    scene f5 at custom_size_transform with fade
    call screen fourth3
    return

label fourth_floors5:
    scene f6 at custom_size_transform with fade
    call screen fourth4
    return

label fourth_floors6:
    scene f7 at custom_size_transform with fade
    call screen fourth5
    return

label csc:
    if not visited_csc:
        $ visited_csc = True
        scene csc_room2 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "CSC Room."
        jus "Laging naka-lock ‘to tuwing dumadaan ako."
        jus "Pero parang may aura siya na… ‘di ka basta-basta puwedeng pumasok"
        hide expression justine.get_image("talking") with dissolve
        # Flashback
        scene csc_room1 at custom_size_transform with dissolve
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Sophie, anong meron dito? Para kasing... ‘secret base."
        hide expression justine.get_image("Sighing") with dissolve
        show expression sophie.get_image("talking") at right
        s "Haha! In a way, oo."
        s "‘Yan yung office ng Central Student Council."
        s "Diyan ginagawa lahat ng plans, meetings, at minsan drama rin—lalo pag elections."
        s "May mga whiteboard, mga files, event permits,"
        s "tapos minsan may snacks pa kasi hindi sila natatapos agad."
        s "Diyan naka-base yung mga officers para ayusin events, policies, at minsan..."
        s "mga chismis ng orgs"
        hide expression sophie.get_image("talking") with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Kaya pala parang ang tahimik pero busy sa loob"
        hide expression justine.get_image("talking") with dissolve
        show expression sophie.get_image("smiling") at right
        s "Exactly. Kung may problemang student-related"
        s "malamang dito napag-uusapan ‘yon bago makarating sa admin."
        hide expression sophie.get_image("smiling") with dissolve
        # End Flashback
        scene csc_room2 at custom_size_transform with fade
    else:
        scene csc_room1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "So, dito ginagawa ang lahat ng desisyon ng CSC"
        hide expression justine.get_image("talking") with dissolve
    jump fourth_floors5



default visited_deluxe_room = False
default visited_travel_tours = False
default visited_standard_room = False

label deluxe_room:
    if not visited_deluxe_room:
        $ visited_deluxe_room = True
        scene deluxe at custom_size_transform with fade
        show expression justine.get_image("realised") at justine_bottom_left
        jus "De Luxe Room…"
        jus "Grabe, kahit yung pangalan palang, parang bawal mag-ingay, no?"
        hide expression justine.get_image("realised") with dissolve
        # Flashback
        scene deluxe at custom_size_transform with dissolve
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Uy, parang hotel room yung vibe."
        jus "Ano 'to?"
        hide expression justine.get_image("happy") with dissolve
        show expression kim.get_image("talking") at right
        k "Ay, ‘yan yung De Luxe Room!"
        k "Pang-simulation ‘yan ng hotel setup para sa HM students."
        k "Diyan sila natututo kung paano mag-set up ng real hotel room"
        k "from bed sheets to lighting, pati na rin ‘yung guest interaction."
        k "Kompleto ‘yann—may bed"
        k "CR, vanity area, towels, pillows, like sa real hotels"
        hide expression kim.get_image("talking") with dissolve
        show expression justine.get_image("realised") at justine_bottom_left
        jus "Whoa. Kala ko parang show room lang."
        jus "Training area pala talaga."
        hide expression justine.get_image("realised") with dissolve
        show expression kim.get_image("happy") at right
        k "Yup! Parang practice stage nila para maging legit hotel staff someday"
        k "Kaya sobrang linis at bawal basta-basta pumasok"
        hide expression kim.get_image("happy") with dissolve
        # End Flashback
        scene deluxe at custom_size_transform with fade
    else:
        scene deluxe at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        jus "High-end training space pala talaga"
        jus "May pagka-exclusive… pero inspiring rin."
        hide expression justine.get_image("happy") with dissolve
    jump fourth_floors6

label floor1_2:
    scene sf17 at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    jus "This leads to the other side of the roofdeck entrance"
    jus "its closed"
    hide expression justine.get_image("normal") with dissolve
    call screen second_last_floor
    jump fourth_floors6  # Kept jump before return as per your input
    return

label travel_tours:
    if not visited_travel_tours:
        $ visited_travel_tours = True
        scene travel_and_tours_room1 at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Travel and Tours Room"
        hide expression justine.get_image("happy") with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Every time I pass by this room"
        jus "parang naiisip ko agad yung mga airport, plane, at beach."
        jus "Vibe pa lang, parang may adventure"
        hide expression justine.get_image("talking") with dissolve
        # Flashback
        scene travel_and_tours_room2 at custom_size_transform with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Anong meron dito, Jorie?"
        jus "Bakit may mga mini flags saka posters ng mga bansa?"
        hide expression justine.get_image("talking") with dissolve
        show expression jorie.get_image("talking") at right
        j "Ah, ‘yan yung Travel and Tour Room."
        j "Dito nagpa-practice yung Tourism students kung paano maging travel agents"
        j "May mga props pa nga like luggage, destination brochures, at uniforms."
        j "Super hands-on dito!"
        hide expression jorie.get_image("talking") with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Ayos ah. Parang biyahe without leaving the room."
        hide expression justine.get_image("talking") with dissolve
        # End Flashback
        scene travel_and_tours_room1 at custom_size_transform with fade
    else:
        scene travel_and_tours_room1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Kaya pala sobrang themed sa loob."
        jus "May mapa pa ng buong mundo sa pader"
        hide expression justine.get_image("talking") with dissolve
    jump fourth_floors6

label standard_room:
    if not visited_standard_room:
        $ visited_standard_room = True
        scene standard_room at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Mas simple compared sa Deluxe"
        jus "pero may charm parin"
        jus "Parang 'yung classic na kwarto sa probinsya na may aircon"
        hide expression justine.get_image("happy") with dissolve
        # Flashback
        scene standard_room at custom_size_transform with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Akala ko bodega lang ‘to dati. Standard Room pala ang tawag?"
        hide expression justine.get_image("talking") with dissolve
        show expression mae.get_image("smiling") at right
        m "Haha! Hindi ‘yan bodega, uy. Training room ‘yan ng HM students."
        m "Mas basic siya kaysa sa De Luxe, pero dito muna sila nagpa-practice bago dun"
        m "Diyan nila unang natutunan ‘yung bed making, towel folding, guest essentials setup."
        m "Halos lahat ng firsts nila bilang hotelier, dito nagsisimula"
        hide expression mae.get_image("smiling") with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        jus "So parang ‘foundations room’?"
        hide expression justine.get_image("talking") with dissolve
        show expression mae.get_image("talking") at right
        m "Exactly. ‘Pag nagkamali ka dito, okay lang"
        m "Dito ka muna matututo bago ka iharap sa mas sosyal na kwarto."
        hide expression mae.get_image("talking") with dissolve
        # End Flashback
        scene standard_room at custom_size_transform with fade
    else:
        scene standard_room at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Makes sense. Dito pala pinapanday ang hospitality skills."
        jus "Every detail counts"
        hide expression justine.get_image("talking") with dissolve
    jump fourth_floors6

label stair_roofdeck:
    scene rf1 at custom_size_transform with fade
    scene rf2 at custom_size_transform with fade
    scene rf3 at custom_size_transform with fade
    scene rf4 at custom_size_transform with fade
    scene rf5 at custom_size_transform with fade
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "Di pa ko nakakaalis pero namimiss ko na agad dito."
    hide expression justine.get_image("Sighing") with dissolve
    show expression justine.get_image("sad") at justine_bottom_left
    jus "Dito kami lagging nag p-p.e at seminar"
    jus "yung tipong di pa nagsisimula ang event o class"
    jus "pero pagod ka na agad sa taas ng a-akysatin mo."
    hide expression justine.get_image("sad") with dissolve
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Pero worth it naman dahil ma-e-enjoy mo ang view"
    jus "na makikita mo sa galling sa itaas."
    hide expression justine.get_image("happy") with dissolve
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Makikita mo rito yung mga naglalakihang eroplano at mga magagandang gusali."
    hide expression justine.get_image("talking") with dissolve
    menu:
        "Go back":
            jump fourth_floors2
        "Don't go back":
            jump main_gate_last

label main_gate_last:
    scene rf6 at custom_size_transform with fade
    show expression justine.get_image("sad") at justine_bottom_left
    jus "Grabe... tapos ko na lahat."
    jus "Parang ang dami palang lugar dito na dinaanan ko lang dati,"
    jus "pero ngayon… iba na."
    hide expression justine.get_image("sad") with dissolve
    show expression justine.get_image("crying") at justine_bottom_left
    jus "Lahat ng tawanan, pagod, kaba, iyak, at ingay… "
    jus "naiwan na dito sa mga pader, sa sahig, sa hangin"
    jus "Hindi lang pala ito basta campus."
    jus "Ito yung naging background ng halos lahat ng memories ko nitong mga nakaraang taon"
    hide expression justine.get_image("crying") with dissolve
    show expression justine.get_image("sad") at justine_bottom_left
    jus "ang hirap pala magpaalam…"
    jus "pero ang sarap din sa puso"
    hide expression justine.get_image("sad") with dissolve
    show expression justine.get_image("happy") at justine_bottom_left
    jus "kapag alam mong hindi mo sayang ‘yung bawat araw na nandito ka"
    hide expression justine.get_image("happy") with dissolve
    show expression justine.get_image("sad") at justine_bottom_left
    jus "Salamat, PUP Parañaque."
    hide expression justine.get_image("sad") with dissolve
    show expression justine.get_image("waving") at justine_bottom_left
    jus "Sa alaala, sa mga taong nakilala ko, at sa kung sino ako ngayon."
    hide expression justine.get_image("waving") with dissolve
    scene black with fade
    "THE END"
    return
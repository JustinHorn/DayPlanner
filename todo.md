# goal
make a closed day planer, that is hardcoded to operate in given directories
that way I might actually use it

# What should be done next
maybe refactor load & change cause very simualar
load template sgain after change!
need to give templates Versions - only show the newest version
it is not a new Version when its renamed then it is a different type


 
programm is not allowed to crash

do tests 11:00

make templates out of plans?

give templates of structure their own widget with delete, rename and split option

add "00:00" to textinput on enter
make show next update structure hotkey
add hot_keys to switch between plans 
activate programm via console
make template split on update
add weekly plan function with only the template names [maybe even color]
add context dependend save function

# Features that could be added:
make .kv more dynamic
make centralize rules for reading files
plan rediscovers its structure in text
save plan structure into plan.txt in order to reload it
add gui widgets like file-name, director(showing current file directory)
check templates for guidelines
save and write to directory by console demand path
addhotkeys for everything
automatic updating
give tests a centralized point to execute them all
make text in buttons dynamic to structure
fix popmenu bugg: clicking next to split butto also splits
add tests to test helper


# Try
Is it enough to write root.dismiss in popmenu.kv


# DONE:
add equals method to plan & co
change main.py - do not use pop ups!
100 % synchronize Plan and Structure in 
popup window close on delete and split
refactor
make logic folders
create new files
create new templates
load old files
updating
line insertion on updat
refactor test_plan
restructure test_plan test_update vs test_template
refactor tests ones more
fix create plan bugg
refacor plan update & co.
make textinput grey and text white
automaticly start with data name of next day.
make the hardcoded directories
refactor Testhelper createPlan
make update work in gui
make on big Testsuite
make font roboto
update on hotkey
be able to rename templates in structure
add str+s to save
load plan for the next day instantly when already made
save and load structure from file
add additionale Headlines for plan. Planstructure and co.
text in TextInput and plan should alwas be sync! check
there must be some form of auto update check
add swap mode option( swap: plan->template->plan) 
fully implement save as template
template t_name = template.theme + "template"
plan t_name = date of plan = plan.theme 
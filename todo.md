# goal
make a DayPlanner MVP

# What should be done next
#fix static time bugg on delete
add robust tests

change version names to major.minor.patch
show week plan// be able to make a weekly plan
add Tests to load and extract entries!

be able to plan the week & the next one -
-- plans of the week shall contain the structure
        Monday 01.01....:
            what is supposed to be according to plans of the week
            ---
            actual structure
            -- 
            what actually happend
        Thurstday 02.01..:
    
    plan Monday: 
    what is supposed to be done according to weekly plan
    how it is planed// 
    what actually happend
get the plans on your phone - and make them visible in one click


save plans into weekly folders
create templates from plan - by marking and then parsing
allow to create temporary templates for recursive activities
try using pip packages instead of sys path
render only a single file out of pyinstaller
add "00:00"/time to textinput on enter
load templates again after change!


#what if I wanna make dankbarkeits-liste?
--> you have got to do that somewhere else
--> same for goal files 

# Features that could be added:
show the directoriess
maybe refactor load & change cause very simualar
make template split on update
need to give templates Versions - only show the newest version
it is not a new Version when its renamed then it is a different type
mehrere Entries zusammen unter einer Stunde --> Template
give templates of structure their own widget with delete, rename and split option
add hot_keys to switch between plan
be able to create templates directly from plan
color code text in textinput(übersicht)

rücke template sachen ein
make .kv more dynamic
make centralize rules for reading files
plan rediscovers its structure in text
make text in buttons dynamic to structure
fix popmenu bugg: clicking next to split butto also splits
add tests to test helper
add context dependend save function
add weekly plan function with only the template names [maybe even color]


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
addhotkeys for everything
automatic updating
check templates for guidelines
give tests a centralized point to execute them all
add gui widgets like file-name, directory(showing current file directory)
save plan structure into plan.txt in order to reload it
make show next update structure hotkey
no error while loading file theme start
load templates again after change!
s
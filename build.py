#################################
####### SET UP FILES HERE #######
#################################

# Name of NewGRF, as it appears in file names
newgrf_name = "chuffing_stations"

# Files which should be first, in order (header, cargotable, etc)
header_stuff = ["header", "squares", "wooden", "stone", "stone_extra", "redbrick", "suburban", "darkbrick", "modern", "express", "city"]

# Files to place in alphabetical order below
unordered_stuff = []

# Do you want to copy the completed NewGRF to your OpenTTD folder? (If in the typical location at "~/Documents/OpenTTD/newgrf")
copy_bool = True

#################################
# NO NEED TO CHANGE STUFF BELOW #
#################################

# Thanks to Andythenorth for much of this code

import codecs
import subprocess
import shutil
import os

# Get the path of a typical OpenTTD installation
openttd_path = os.path.expanduser("~/Documents/OpenTTD/newgrf")

# Create an empty list where all the NML code will be placed
sections = []

# Function for copying code from .nml files
def append_code(file):
    filename = "src/{}.nml"
    stuff = codecs.open(filename.format(file),'r','utf8')
    print("Merging", filename.format(file))
    sections.append(stuff.read())
    stuff.close()

# Append header stuff which should always be first
for i in header_stuff:
    append_code(i)

# Sort the unordered list for readability in the printout, then append to the list
unordered_stuff.sort()
for i in unordered_stuff:
    append_code(i)

merged_nml_path = newgrf_name + ".nml"
grf_name = newgrf_name + ".grf"

# Write the content of 'sections' into a file and save it
processed_nml_file = codecs.open(merged_nml_path,'w','utf8')
processed_nml_file.write('\n'.join(sections))
processed_nml_file.close()

print("#### nmlc ####")

# Run
nmlc = subprocess.run(["nmlc", "-c", "-t", f"src{os.path.sep}custom_tags.txt", "-l", f"src{os.path.sep}lang", "--grf", grf_name, merged_nml_path], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text=True)
print(nmlc.stdout)
print(nmlc.stderr)

if copy_bool == True:
    print("Copying NewGRF to OpenTTD folder")
    shutil.copy(grf_name, openttd_path )
else:
    print("Complete. Did not copy.")

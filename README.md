# Chuffing Stations Set

![Image showing a selection of the available station tiles](/banner.png)

Inspired by the diverse history of rail transport across the United Kingdom, **Chuffing Stations** is intended to provide players with a wide range of modular station tiles. It features platform and building designs from the pioneering days of the Industrial Revolution through to the cutting-edge technology of modern high-speed trains.

Chuffing Stations is designed to be highly flexible while also matching the charm and character of the classic OpenTTD graphics.

I hope you enjoy this set.

Andy


## Features
- Eight distinct station types, from basic wooden constructions, to contemporary glass and steel structures.
- Over 30 unique station buildings, available in multiple orientations.
- A variety of platform styles, sizes and styles.
- Many distinct bridges, signal boxes and trackside objects.
- Bridges as waypoints for non-stop tracks.
- A huge range of platform items, such as fences, benches, shelters and more...


### Getting Started
To play with Chuffing Stations, you can download the latest version using the OpenTTD in-game downloader.


### Thanks
Many thanks to everyone who has contributed to maintaining and developing OpenTTD over the years. Thank you to the various artists, coders and contributors of the many newGRFs that keep me playing. Special thanks to **andythenorth** and **Chris Sawyer**. I'd also like to thank **2TallTyler** for their help with the build process and bug reporting.

### Credits
Chuffing Stations contains some elements from [FIRS](https://github.com/andythenorth/firs) and [CHIPS](https://github.com/andythenorth/chips).

### Changelog
**1.0**
- Initial release

**1.1**
- Some minor graphical fixes.

**1.2**
- Tiles now aligned according to OTTD conventions.
- Platform height changed to 3px for better compatibility with other station sets.
- Parameter added to disable station introduction dates (Thanks, Iris-Persephone).
- Some signal boxes moved to the correct side.
- Significant graphical fixes.
- Cargo aware graphics disabled for now. These will be back in future version...

## The Stations
**Wooden**
These basic platforms are typical of early railways and smaller branch lines. A few items of platform furniture are included, as well as some simple structures.

**Stone**
More sophisticated stations are often found on busier lines. Many of these stone buildings are inspired by the early buildings in the Great Western region.

**Red Brick**
The elegant brick designs from around the Midland region inspired this station type.

**Suburban**
From around 1910, this clean, geometric style was typical of stations in and around London.

**Dark Brick**
Beginning in the 1950s, the West Coast Modernisation Programme triggered the reconfiguration of many key stations. Many were rebuilt using brutalist designs.

**Modern Stations**
The utilitarian, modular stations from the CLASP building programmes of the 1960s and 1970s inspired these stations.

**Express Stations**
Angular structures featuring bright colours were commonplace in the late 1980s and early 1990s onwards.

**City Stations**
Glass and metal are used in these contemporary designs.



## Modifying Chuffing Stations
Chuffing Stations is released under the **GPLv2 license**.

### Stations in NML
I'd recommend checking out my [example_stations](https://github.com/andybiotic/example_stations) project first. This project contains a simplified station newGRF with a similar structure to Chuffing Stations. You can also find some instructions on compiling the newGRF using NMLC and other useful information and samples.

### Compiling Chuffing Stations
Chuffing Stations is written by hand in NML. This probably isn't optimal, but here we are...
A Python script copies the contents of each of the NML files and compiles the GRF file. Some options are set in `header.nml`. 

### Artwork and Workflow
The png files are provided as-is, and licensed as above. Feel free to modify these. The graphics were created using the iPad app 'Pixaki'. These were exported in to GIMP where they were converted to the OTTD 8bpp palette. More information on my art workflow can be found in [example_stations](https://github.com/andybiotic/example_stations).

### Reporting Issues
Please report any bugs on the Github page.






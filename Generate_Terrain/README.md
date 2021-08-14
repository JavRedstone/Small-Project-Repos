**Terrain Generator**

This terrain generator does not use Perlin noise and can acheive something that is *similar* (to some extent).

It uses double arrays in order to damp randomly generated values from 0 to 1, to create a sort of terrain strip.

To visualize this, an html document is needed, which can be seen here: 

https://htmlpreview.github.io/?https://github.com/JavRedstone/Small-Project-Repos/blob/main/Generate_Terrain/index.html

Here is a demo image:

![Example mountain output in html document](https://github.com/JavRedstone/Small-Projects-Repos/blob/main/Generate_Terrain/terrain.png)

You can download this yourself and open the html document in browser to view the results too.

*To customize this*

You can change the values inside `generate_terrain(n, a)`, where `n` is the size of the terrain, and `a` is the desired amount of damping (it's a little wonky so I think the values: `generate_terrain(50, 5)` work best)

Enjoy!

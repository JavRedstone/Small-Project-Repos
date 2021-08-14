**Mountain Generator**

This mountain generator uses random values as well as divisibility in order to determine the rate of ascension.

To visualize the mountain, an html document is needed. Beware of higher values in the function call.

To visualize this, an html document is needed, which can be seen here: 

https://htmlpreview.github.io/?https://github.com/JavRedstone/Generate-Mountain/blob/main/index.html

Here is a demo image:

![Example mountain output in html document](https://github.com/JavRedstone/Generate-Mountain/blob/main/mountain.png)

You can download this yourself and open the html document in browser to view the results too.

*To customize this*

You can change the values inside `generate_mountain(n, a, b)`, where `n` is the size of the terrain, `a` is the desired amount of smoothness (a larger value of a means there is more steps and a smoother transition), and `b` is the divisibility amount (a larger value of b means that the mountain will be steeper, a lower value means the opposite). (at certain values of a and n some stripes appear (rendering issue), so I think the values: `generate_mountain(100, 100, 3)` work best)

Enjoy!
gescape
=======

'Genetic Escape'
Genetic Algorithm and other AI testing.

This is a 'game' that will employ Genetic and other algorithms to generate enemies.

Tests:

# nosetests --with-coverage                                                                                                                                                             [1:25:44 PM]
....
Name    Stmts   Miss  Cover   Missing
-------------------------------------
hex        33      1    97%   50
path      113     15    87%   72, 74-76, 96, 140-150
-------------------------------------
TOTAL     146     16    89%
----------------------------------------------------------------------
Ran 4 tests in 0.008s

OK


TODO:
-----
- Smooth travel. Units currently leap
- Enemy Genetic Algorithm
- Click to tile translation
- Dijkstra code refactor
- Super GFX and particle effects (Probably never going to happen)
- Possibly switch to another display framework other than pygame
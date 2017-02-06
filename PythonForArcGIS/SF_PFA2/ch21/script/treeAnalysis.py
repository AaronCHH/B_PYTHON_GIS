# treeAnalysis.py
# Purpose: Define and use a Tree class to support tree data analysis
# Input: No arguments needed.

### Create a class called Tree

    ### Define an __init__ method.  It should assign 4 properties: block, plot, species, and dbh
    '''Initialize tree object properties.'''

    ### Define a calculateDIB method which returns diameter inside bark (DIB)
    '''Calculate DIB, assuming DIB is diameter breast height times 0.917.'''

    ### Define a calculateHeight method which returns the tree height
        '''Calculate height, assuming that height is 86.6 plus 0.025 times the
        diameter breast height for loblolly pines (LP)
        and height is 98.8 plus 0.15 times the diameter breast height for all
        other species.'''

    def report(self, num):
        '''Print tree properties.'''
        print '\nReport Tree', num
        print '-------------'
        print 'Block: {0}'.format(self.block)
        print 'Plot: {0}'.format(self.plot)
        print 'Species: {0}'.format(self.species)
        print 'DBH: {0}'.format(self.dbh)
        print 'DIB: {0}'.format(self.calculateDIB())
        ### Print the Height as calculated by the calculateHeight method.
        print '\n'


if __name__ == '__main__':
    t1 = Tree(5, 91, 'SG', 14)  # Create a tree object t1 from record 1 of rdu_forest.txt
    print 'Tree 1 Species:', t1.species  # Print t1's species.
    dib = t1.calculateDIB()  # Calculate t1's DIB.
    print 'Tree 1 DIB:', dib  # Print t1's DIB.
    t1.report(1)  # Report t1 information.

    t2 = Tree(5, 91, 'LP', 23)  # Create a tree object t2 from record 2 of rdu_forest.txt
    ### Print t2's DBH
    ### Calculate t2's height
    ### Print t2's height

    ### Create a tree object t3 from record 3 of rdu_forest.txt
    ### Print t3's block
    ### Print t3's plot

    ### Create a tree object t4 from record 4 of rdu_forest.txt
    ### report t4 information

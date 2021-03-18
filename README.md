# data_structures_and_algorithms_2

### This is a project for some university coursework. The goal was to build a python program that would be capable of the following:

- Import and validate data from a file
- Design and utilize a hashmap instead of using Python's build in hashmap
- Using the imporated data, determine an acceptable route for two trucks to take to deliver packages within the local area.
  - What defines "acceptable" here is:
      - Each package may have a set deliver by time. All packages that have a set deliver by time must be delivered no later than that time
      - The summation of distance traveled by each truck must be within a specified distance
      - All packages must be delivered
      
### Design considerations:

In determining how to best go about finding an acceptable route, I designed the program to be reuseable to an extent.
The current implementtion uses a nearest neighbor graph algorithm. This of course comes with drawbacks of potentially not having an ideal or minimized distance solution.
Also, the packages chosen to go on each truck are hard-coded as it wasn't a requirement that the program must factor in what packages are to go on what truck and when.


### Potential improvements:

If I were to implement this for a more realistic case, I would like to change up the following:
- Instead of using nearest neighbors, I would use a more robust traveling salesman algorithm that is more likely to achieve a minimal distance traveled.
- I would remove the hard coded packages and incorporate a decision making process of which package is allocated to which truck at which time. In order to achieve a true approximate minimal distance traveled, this would be a key element to consider alongside the path the truck is to travel.
- Instead of using a custom hashmap, for efficiency purposes, I would use Python's built in hashmap

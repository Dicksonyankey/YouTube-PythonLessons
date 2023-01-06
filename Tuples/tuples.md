## Tuples and their methods in python

**WHAT YOU WILL LEARN**
1. What is tuple in python?.
2. How to create a tuple.
3. Tuples containing different data types.
4. How to convert other data types into a tuples.
5. Converting a lsit into a tuple.
6. Converting a string into a tuple.
7. Converting a dictionary into a tuple.
8. Slicing a sub element in tuples.
9. Traversing a tuple.
10. Tuple methods.
11. difference between tuple and a list.
12. Main Takeaway.



**difference between tuple and a list.**

Lists are mutable, Python needs to allocate an extra memory block in case there is a need to extend the size of the list object after it is created. However tuples are immutable and are fixed. if they are initialized and created, elements in the tuple can not be altered or changed.


**Main Takeaway.**

1. If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected and will not accidently change.
 2. Tuple doesn't not also support data updating or changing the state once it is created
3. use list if you know that the data will grow and shrink during the runtime of the application,you need to go with the list data type.
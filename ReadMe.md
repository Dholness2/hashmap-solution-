# Problem
Implement a hashmap (with amortized constant time look-ups) in Python without using a hashmap primitive.
Please include an executable testing framework for your data structure.

#Approach
  To achieve a hashmap implementation with amortized constant time look-ups, this project relys on Python's list data
 structure to store a fixed amount of buckets that will contain link-lists. The link-lists contain nodes containg keys
 and associated values. In situations of hash collisions a new entry node is added to the link list.The base list  contiaing the buckets  of
 link lists is dynamic and will double in size every time the number of hashmap entries / list size rises to a ratio of 1. As a result
 we have a amortized constant time look-ups.

##Requirments
 1. Python 3
 2. pytest version = '3.3.2'
 3. Mac OS X

## Setup

 1. To install Homebrew, open Terminal
  `$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

 2.`$ brew install python3`

 3. `pip install pytest`

## To Runt Tests

1. Move to Dir:
 `$ cd hashmap`

2. Run tests:
 `$ pytest`




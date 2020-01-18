# KnowledgeTechnologies_Project1
This project requires five files namely: -
1. stringMatcher.py
2. dataComparer.py
3. misspell.txt
4. dictionary.txt
5. correct.txt

The names of the .txt files should be in lowercase with exact spelling. 

Running the code
Compile and run the file dataComparer.py. This file will use the .txt files to create 
the following new files:- 

1. misspellSoundexStrings.txt
Stores all the corresponding soundex strings for the file misspell.txt

2. dictionarySoundexStrings.txt
Stores all the corrsponding strings for the file dictionary.txt

3. neelmanWunschResults.txt
Stores the results of Needleman-Wunsch algorithm. 
The file is self explanatory with header describing each column. 
The number in the recall column tells about the number of elements found in the best match list.

4. smithWatermanResults.txt
Stores the results of Smith-Waterman algorihm. 
The file is self explanatory with header describing each column. 
The number in the recall column tells about the number of elements found in the best match list.

5. soundexResults.txt
Stores the results of Soundex algorithm. 
The file is self explanatory with header describing each column. 
The number in the recall column tells whether the correct string was found in the best match list. 

6. soundexWithNeedlemanResults.txt
Stores the results of Soundex algorithm with Needleman as string matching. 
The file is self explanatory with header describing each column. 
The number in the recall column tells whether the correct string was found in the best match list. 

Note: - 
    "The Accuracy and Recall scores at the bottom are in percentage. The files will be output 
    in the directory of the dataComparer.py file. The files mentioned at the start of this readme
    all be in the same directory for the code to run."
 


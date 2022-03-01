# Letter_Frequency_Counter
This program was built in Python 3.9. It functions by first taking in a single command-line argument specified by the user, which is the absolute or relative path of a readable text file. The program will open the file and sum the amount of each letter character e.g. [Aa-Zz]. The program will first convert all text to lowercase, therefore capital ‘A’ and lowercase ‘a’ will be treated identically and both will be added to the same cumulative sum. 

The program then calculates the total sum of all letter characters and calculates each character’s frequency by way of a decimal number. For example, if there are 1000 total letters in a text file, and there are 683 occurrences of ‘e’/’E,’ then the program will calculate 683/1000 (rounded to 4 decimal places) to give a final answer of {e: 0.683}.

Each character’s letter frequency is appended to a single dictionary, which is then written to the “Frequencies.txt” text file

## Compatability
Made in Python 3.9
Tested on Windows 10

## Options
* -h                 Displays Help Regarding how to run the cmd
* -f/--filename      Required: Specify a textfile to analyze, by absolute or relative path e.g. C:\Users\<User>\Documents\file.txt

## Quickstart
1) Download the .ZIP File and extract to a directory of your choice
2) ```python3 main.py -f file.txt```
3) i.e. ``` sudo python3 main.py -f ..\textfiles\dracula.txt```

# Purpose
This purpose of this program is to assist in letter frequency analysis as a cryptanalysis technique when looking at substitution ciphers. While ciphers such as the Caesar Cipher or Mono-alphabetic Ciphers may provide some level of obscurity, they are still vulnerable to frequency analysis, assuming the original plaintext was in English text. This is because certain letters appear far more frequently than others in the English language, such as the letter’s ‘e’, ‘t’, ‘a’ etc. 

# Example Output
![image](https://user-images.githubusercontent.com/77559638/156243922-8453c8d8-45d3-4423-9af6-95439c7219a1.png)


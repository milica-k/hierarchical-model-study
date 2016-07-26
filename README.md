# hierarchical-model-study
This is the code I used for a psychology class in November of 2015 to conduct a study on the hierarchical model of memory proposed by Collins and Quillian in 1969.

`collector` is used to collect data. The basic commands are `intro` (to run the intro), `new` (to run a new test), and `exit` (to exit). The data for each test run will be saved in a file with the previously provided ID number.

`analyst` goes through all the collected data and calculates a few statistics. The `saveBasicInfo` function saves some selected information to a text file. It uses the `analyze` function, which admits parameters based on the restrictions we want to apply to the data (e.g. correct responses only).

The repo also contains the results in text form and as a graph, as well as a sample output file.

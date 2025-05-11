Hi,

This is my biochemistry honours project github repository. There are three things that you need in order to try this out:
- Python3 or later installed
- NumPy installed (see the [NumPy Website for this](https://numpy.org/install/))
- The attached python file
- The attached star file
- A unix system (Mac or Linux. This script is bash deployable only, so if you have a windows OS you will have to change from powershell to bash. [Instructions here](https://sps-lab.org/post/2024_windows_bash/#:~:text=If%20you're%20in%20PowerShell%20but%20want%20to,allowing%20you%20to%20run%20any%20bash%20commands.))

Run the file through bash using this command: 

```sh
python3 ctf_normaliser.py Sample_CTF_File.star
```

Alternatively, you can add a third argument to name the file. Otherwise it will produce a file called unnamed_numpy_output.csv

```sh
python3 ctf_normaliser.py Sample_CTF_File.star your_own_csv_name.csv
```

Your terminal should print out parameters with names and instructions on how to implement changes in RELION. These parameters are upper and lower Z-filter bounds used to remove micrographs that may be harmful to reconstructions. It will also produce a csv file that can be easily loaded into programs such as excel. This is what I used to produce my figures. 

# ctf_normaliser.py
import numpy as np
import argparse

def extract_ctf_outputs(file_path):
    ctf_outputs = []
    in_data = False
    with open(file_path, 'r') as file:
        for line in file:
            if in_data:
                data = line.split()
                # double checks that the line is valid. All valid lines start with a filepath, which come from the MotionCorr directory in RELION
                if data and data[0].startswith("MotionCorr/"): 
                    #storage of list parsed as numpy floating point array
                    ctf_outputs.append(np.array(data[3:], dtype=float)) 
            elif "_rlnCtfIceRingDensity #10" in line:
                print(f' escaped at line: {line}')
                in_data = True
        ctf_outputs = np.vstack(ctf_outputs)
    return ctf_outputs


def print_output_message(array):
    categories = ["rlnDefocusU", "rlnDefocusV", "rlnCtfAstigmatism", "rlnDefocusAngle", "rlnCtfFigureOfMerit", "rlnCtfMaxResolution", "rlnCtfIceRingDensity"]
    np.set_printoptions(suppress=True)
    # Get all of the values
    mu = np.mean(array, axis=0).astype(float)
    sigma = np.std(array, axis=0).astype(float)
    # Print the outputs so that you can put everything back into RELION
    print("TO REMOVE ALL MICROGRAPHS BY Z-SCORE FILTERING, GO TO 'Subset selection' IN THE RELION GUI. GO TO 'Subsets', \nTURN ON METADATA VALUES, AND THEN ENTER EACH OF THESE INTO THE FIELDS: 'Metadata label:   Minimum,   Maximum'. \nAS A NOTE TO MY FUTURE SELF, I WOULD STRONGLY ADVISE THAT YOU DOUBLE CHECK THE LOGFILE OUTPUTS BEFORE DOING THIS \n \nRELION INPUTS BELOW \n")
    for n in range(7): # Prints out each value
        print(f'{categories[n]},   {mu[n] - 3 * sigma[n]},   {mu[n] + 3 * sigma[n]}')

def write_output_csv(array, output_name):
    np.savetxt(output_name, array, fmt="%.6f", delimiter=",", header="_rlnDefocusU, _rlnDefocusV, _rlnCtfAstigmatism, _rlnDefocusAngle, _rlnCtfFigureOfMerit, _rlnCtfMaxResolution, _rlnCtfIceRingDensity")
    print(f"NUMPY ARRAY WRITTEN AS: {output_name} \n")

def main():
    parser = argparse.ArgumentParser(description="Extract CTF outputs and save them as a readable numpy array.")
    parser.add_argument("input_file")
    parser.add_argument("output_file", nargs="?", default="unnamed_numpy_output.csv") 
    args = parser.parse_args()
    try:
        result = extract_ctf_outputs(args.input_file)
        if result.any():
            write_output_csv(result, args.output_file)
            print_output_message(result)
        else:
            print("Something went wrong. There was no output to write to a csv file. Double check your code or your inputs.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


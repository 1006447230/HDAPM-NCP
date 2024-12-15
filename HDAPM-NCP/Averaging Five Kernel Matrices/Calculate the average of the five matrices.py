
import numpy as np

folders = ["corr", "Cos", "GIP", "Jacc", "MI"]
herb_files = [f"Herb-kernel{i}.txt" for i in range(1, 6)]
disease_files = [f"Disease-kernel{i}.txt" for i in range(1, 6)]
herb_output_files = [f"avg/Five_herbs_average{i}.txt" for i in range(1, 6)]
disease_output_files = [f"avg/Five_disease_average{i}.txt" for i in range(1, 6)]

def calculate_and_save_average(input_files, output_files):
    for input_file, output_file in zip(input_files, output_files):
        matrices = []
        for folder in folders:
            filepath = f"{folder}\{input_file}"
            try:
                matrix = np.genfromtxt(filepath, delimiter=",", dtype=float, invalid_raise=False)
                matrices.append(matrix)
            except Exception as e:
                print(f"Error reading file {filepath}: {e}")
        if matrices:
            average_matrix = np.mean(matrices, axis=0)
            np.savetxt(output_file, average_matrix, fmt="%.6f", delimiter=',')
calculate_and_save_average(herb_files, herb_output_files)
calculate_and_save_average(disease_files, disease_output_files)

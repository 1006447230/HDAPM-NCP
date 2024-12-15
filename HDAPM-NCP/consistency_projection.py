import numpy as np


class NSP(object):
    def __init__(self, herb_similarity, disease_similarity, adjacency_matrix):
        self.herb_similarity = herb_similarity
        self.disease_similarity = disease_similarity
        self.adjacency_matrix = adjacency_matrix


    def diseaseSP(self):
        temp_matrix = np.dot(self.adjacency_matrix, self.disease_similarity)
        modulus = np.linalg.norm(self.adjacency_matrix, axis=1).reshape(-1, 1)
        return temp_matrix / modulus

    def herbSP(self):
        temp_matrix = np.dot(self.herb_similarity, self.adjacency_matrix)
        modulus = np.linalg.norm(self.adjacency_matrix, axis=0).reshape(1, -1)
        return temp_matrix / modulus

    def calculate_modulus_sum(self):
        index_modulus = np.linalg.norm(self.herb_similarity, axis=1).reshape(-1, 1)
        columns_modulus = np.linalg.norm(self.disease_similarity, axis=0).reshape(1, -1)
        return index_modulus + columns_modulus

    def network_NSP(self):
        result = np.nan_to_num((np.nan_to_num(self.diseaseSP())+np.nan_to_num(self.herbSP()))/self.calculate_modulus_sum())
        return result



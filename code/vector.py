import numpy as np

class Vector:
    def __init__(self, components = []):
        self.vector_components = components
        self.vector_norm = self.norm()

    def norm(self):
        return np.linalg.norm(self.vector_components)

    def components(self):
        return self.vector_components
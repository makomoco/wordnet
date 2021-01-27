import numpy as np
import evaluate

X = np.array([[1,2],[-1,2],[2,4]])

x0 = X[0]
x1 = X[1]
x2 = X[2]

print(evaluate.cosine_similarity_normalized(evaluate.vector_normalized(x0), evaluate.vector_normalized(x1)))
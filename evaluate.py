import numpy as np

# コサイン類似度
def cosine_similarity(x, y):
    return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))

# コサイン類似度（正規化）
def cosine_similarity_normalized(x, y):
    return np.dot(x, y)

# ベクトル正規化
def vector_normalized(x):
    return x / np.linalg.norm(x)

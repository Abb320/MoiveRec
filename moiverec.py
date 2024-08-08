import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def getTitleFromIndex(index):
  return(df[df.index== index]["title"].values[0])

def getIndexFromTitle(title):
  return(df[df.title== title]["index"].values[0])



df = pd.read_csv("movie s_dataset.csv")
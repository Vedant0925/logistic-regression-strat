import yfinance as yf, pandas as pd, shutil, os, time, glob
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from get_all_tickers import get_tickers as gt
from ta import add_all_ta_features
from ta.utils import dropna

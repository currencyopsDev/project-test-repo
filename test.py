import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import yfinance as yf

def build():
    f=open("cryptocurrencies","r")
    for line in f.readlines():
        parity=yf.download(str(line).strip(),period="7d",interval="1d",progress=False)
        parity.info
build()

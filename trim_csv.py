# -*- coding: utf-8 -*-
import pandas as pd

news_csv = pd.read_csv("3000days_of_DR_with_afinn.csv")

news_text_list = news_csv[["title", "afinn"]]

news_text_list.to_csv("list.csv")

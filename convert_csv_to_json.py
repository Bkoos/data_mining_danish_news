# -*- coding: utf-8 -*-
import pandas as pd

news = pd.read_csv("list.csv")

new_news = news[["title", "afinn"]]

very_pos = new_news.loc[new_news["afinn"] >= 3]
very_neg = new_news.loc[new_news["afinn"] <= -3]

very_pos.insert(1, "label", "pos")
very_neg.insert(1, "label", "neg")

all_news = pd.concat([very_neg, very_pos], ignore_index=True)

#print(all_news[["title", "label"]])
new_all_news = all_news.sample(frac=1)

new_all_news[["title", "label"]].to_json("news.json", orient="records", lines=True, force_ascii=False)

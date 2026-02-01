import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn import tree
from sklearn import metrics

df = pd.read_csv(r"C:\Users\Auguxto\Desktop\Ciencia de Dados\raw.csv")

features = df.columns[1:-1]
target = "Churn"

x = pd.get_dummies(df[features], drop_first=True)
y = df[target].map({"Yes": 1, "No": 0})

## Treino sem Feature
x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y, random_state=42, test_size=0.2)
arvore = tree.DecisionTreeClassifier(random_state=42, max_depth=4, min_samples_leaf=20)
arvore.fit(x_train,y_train)

## Treino com Feature
features_importance = pd.Series(arvore.feature_importances_,index=x_train.columns).sort_values(ascending=False)

features_boa = features_importance[features_importance>0.01].index

x_train_sel = x_train[features_boa]
x_test_sel = x_test[features_boa]

arvore_sel = tree.DecisionTreeClassifier(random_state=42, max_depth=4, min_samples_leaf=20)
arvore_sel.fit(x_train_sel,y_train)

## Metricas

y_predict = arvore_sel.predict(x_test_sel)
y_proba = arvore_sel.predict_proba(x_test_sel)[:, 1]

acc_train = metrics.accuracy_score(y_test, y_predict)
auc_train = metrics.roc_auc_score(y_test, y_proba)

## DF decisão

df_result = df.loc[x_test_sel.index].copy()

df_result["churn_score"] = y_proba
df_result["churn_real"] = y_test.values

df_rank = df_result.sort_values("churn_score", ascending=False)

top_20 = int(0.2 * len(df_rank))
df_top20 = df_rank.head(top_20)

recall_top20 = df_top20["churn_real"].sum() / df_rank["churn_real"].sum()
recall_top20

df_rank["faixa_risco"] = pd.qcut(
    df_rank["churn_score"],
    q=3,
    labels=["Baixo", "Médio", "Alto"]
)

df_rank.to_csv(r"C:\Users\Auguxto\Desktop\Ciencia de Dados\churn_output.csv", index=False)



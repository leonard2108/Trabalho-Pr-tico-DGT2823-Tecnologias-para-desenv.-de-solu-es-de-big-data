import pandas as pd

# =========================
# CONFIGURAÇÃO PANDAS
# =========================

pd.options.display.max_rows = 9999

# =========================
# LEITURA CSV
# =========================

df = pd.read_csv(
    "dataset.csv",
    sep=";",
    engine="python"
)

# =========================
# EXIBIR DADOS
# =========================

print("\nDATAFRAME ORIGINAL:\n")
print(df.to_string())

# =========================
# SUBCONJUNTO
# =========================

sub = df[["Duration", "Pulse", "Calories"]]

print("\nSUBCONJUNTO:\n")
print(sub)

# =========================
# PRIMEIRAS E ÚLTIMAS LINHAS
# =========================

print("\nPRIMEIRAS 10 LINHAS:\n")
print(df.head(10))

print("\nÚLTIMAS 10 LINHAS:\n")
print(df.tail(10))

# =========================
# INFORMAÇÕES GERAIS
# =========================

print("\nINFORMAÇÕES:\n")
print(df.info())

# =========================
# CÓPIA DO DATAFRAME
# =========================

novo_df = df.copy()

# =========================
# TRATAMENTO CALORIES
# =========================

novo_df["Calories"] = novo_df["Calories"].fillna(0)

print("\nCALORIES TRATADO:\n")
print(novo_df)

# =========================
# TRATAMENTO DATE
# =========================

novo_df["Date"] = novo_df["Date"].fillna("1900/01/01")

print("\nDATE TRATADO:\n")
print(novo_df)

# =========================
# CORREÇÃO DATAS
# =========================

novo_df["Date"] = novo_df["Date"].replace(
    "1900/01/01",
    pd.NaT
)

novo_df["Date"] = novo_df["Date"].replace(
    "20201226",
    "2020/12/26"
)

novo_df["Date"] = pd.to_datetime(
    novo_df["Date"],
    format="%Y/%m/%d",
    errors="coerce"
)

print("\nDATAS CONVERTIDAS:\n")
print(novo_df)

# =========================
# REMOVER NULOS
# =========================

novo_df.dropna(subset=["Date"], inplace=True)

print("\nDATAFRAME FINAL:\n")
print(novo_df)
"""
@gitsil10
@file main.py
@brief application driver
@details A file to run the application
@version 0.1
@date 2024-03-20
"""
#imports
from utils.dataframe_mgmt import DataframeMgmt
from include.financial_security_mgmt import FinancialSecurityMgmt
from utils.process_mgmt import ProcessMgmt
import pandas as pd

#main
def main():
    url = "c:/users/silva/onedrive/documents/personal/data/excel/financedata.xlsx"
    df_trans = pd.read_excel(url, sheet_name="TRANSACTION")
    df_trans = df_trans[["DATE", "META", "AMOUNT"]]
    df_trans.set_index("DATE", inplace=True)
    df_statement = pd.read_excel(url, sheet_name="STATEMENT")
    df_statement.set_index("META", inplace=True)
    df = df_trans[df_trans["META"].isin(df_statement.index[df_statement["TYPE"]=="income"])]
    df = df[["AMOUNT"]]
    df_mgmt = DataframeMgmt(df)
    #print(df_mgmt.group_by_year_month())
    print(df_mgmt.info_data())

    #fsm = FinancialSecurityMgmt("GOOGL")
    #df = fsm.income_statement_10k.loc[["Total Revenue", "Cost Of Revenue"]].T
    #isa = DataframeMgmt(df)
    #print(isa.grow_rate())

#driver
if __name__ == "__main__":
    main()
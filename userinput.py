from tkinter import *
import pandas as pd

root = Tk()

# LEFT SIDE


NO_label = Label(root, text="NO")
TGL_label = Label(root, text="TGL")
DEBIT_label = Label(root, text="DEBIT PIUTANG")
KET_label = Label(root, text="KET")
OBAT_label = Label(root, text="OBAT")
KAMAR_label = Label(root, text="KAMAR PERAWATAN")
KONSULTASI_label = Label(root, text="KONSULTASI")
EKG_label = Label(root, text="EKG")
NEBU_label = Label(root, text="NEBU")
LABORATORIUM_label = Label(root, text="LABORATORIUM")
USG_label = Label(root, text="USG")
OKS_label = Label(root, text="OKS/DARAH")
ADM_label = Label(root, text="ADM")
TOTAL_label = Label(root, text="TOTAL")

NO_label.grid(row=0, column=0)
TGL_label.grid(row=1, column=0)
DEBIT_label.grid(row=2, column=0)
KET_label.grid(row=3, column=0)
OBAT_label.grid(row=4, column=0)
KAMAR_label.grid(row=5, column=0)
KONSULTASI_label.grid(row=6, column=0)
EKG_label.grid(row=7, column=0)
NEBU_label.grid(row=8, column=0)
LABORATORIUM_label.grid(row=9, column=0)
USG_label.grid(row=10, column=0)
OKS_label.grid(row=11, column=0)
ADM_label.grid(row=12, column=0)
TOTAL_label.grid(row=13, column=0)


# INPUT  SIDE

NO_ENTRY = Entry(root)
TGL_ENTRY = Entry(root)
DEBIT_ENTRY = Entry(root)
KET_ENTRY = Entry(root)
OBAT_ENTRY = Entry(root)
KAMAR_ENTRY = Entry(root)
KONSULTASI_ENTRY = Entry(root)
EKG_ENTRY = Entry(root)
NEBU_ENTRY = Entry(root)
LABORATORIUM_ENTRY = Entry(root)
USG_ENTRY = Entry(root)
OKS_ENTRY = Entry(root)
ADM_ENTRY = Entry(root)
TOTAL_ENTRY = Entry(root)


NO_ENTRY.grid(row=0, column=1)
TGL_ENTRY.grid(row=1, column=1)
DEBIT_ENTRY.grid(row=2, column=1)
KET_ENTRY.grid(row=3, column=1)
OBAT_ENTRY.grid(row=4, column=1)
KAMAR_ENTRY.grid(row=5, column=1)
KONSULTASI_ENTRY.grid(row=6, column=1)
EKG_ENTRY.grid(row=7, column=1)
NEBU_ENTRY.grid(row=8, column=1)
LABORATORIUM_ENTRY.grid(row=9, column=1)
USG_ENTRY.grid(row=10, column=1)
OKS_ENTRY.grid(row=11, column=1)
ADM_ENTRY.grid(row=12, column=1)
TOTAL_ENTRY.grid(row=13, column=1)


# SAVE BUTTON


# SAVE FUNCTION

def Input():

    NO = NO_ENTRY.get()
    TGL = TGL_ENTRY.get()
    DEBIT = DEBIT_ENTRY.get()
    KET = KET_ENTRY.get()
    OBAT = OBAT_ENTRY.get()
    KAMAR = KAMAR_ENTRY .get()
    KONSULTASI = KONSULTASI_ENTRY.get()
    EKG = EKG_ENTRY.get()
    NEBU = NEBU_ENTRY.get()
    LABORATORIUM = LABORATORIUM_ENTRY.get()
    USG = USG_ENTRY.get()
    OKS = OKS_ENTRY.get()
    ADM = ADM_ENTRY.get()
    TOTAL = TOTAL_ENTRY.get()

    global array
    array = [NO,
             TGL,
             DEBIT,
             KET,
             OBAT,
             KAMAR,
             KONSULTASI,
             EKG,
             NEBU,
             LABORATORIUM,
             USG,
             OKS,
             ADM,
             TOTAL]
    print(array)
    df = pd.DataFrame(array).T
    df.to_excel(excel_writer="C:/Users/micha/OneDrive/Documents/excel/test.xlsx")


Button(root, text="submit",
       command=Input).grid(row=14, column=1)

# RUN
root.mainloop()

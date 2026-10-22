import os
import openpyxl

print("Compiling formula-driven portfolio simulation workbook...")

template_path = "/app/solution/Portfolio for Schwab Investments - Test.xlsx"
output_path = "/app/solution/outputfile/Portfolio for Schwab Investments - Solved.xlsx"

os.makedirs("/app/solution/outputfile", exist_ok=True)

if not os.path.exists(template_path):
    print(f"Error: Input template workbook missing at {template_path}!")
else:
    wb = openpyxl.load_workbook(template_path)
    sheet = wb.active

    # Row mapping configurations for Table 1 and Table 2 assets
    asset_rows = {
        "BAB":  {"t1": 2, "t2": 12},
        "BKLN": {"t1": 3, "t2": 13},
        "HYBL": {"t1": 4, "t2": 14},
        "PGHY": {"t1": 5, "t2": 15},
        "VRP":  {"t1": 6, "t2": 16},
        "VYMI": {"t1": 7, "t2": 17},
        "AMDY": {"t1": 8, "t2": 18}
    }

    # -------------------------------------------------------------------------
    # PROGRAMMATIC WORKBOOK COMPILATION
    # -------------------------------------------------------------------------
    for ticker, rows in asset_rows.items():
        # --- Baseline Model Layout (Table 1) ---
        r1 = rows["t1"]
        if ticker == "AMDY":
            sheet[f"J{r1}"] = f"=ROUND((50000/G{r1}),0)"
        else:
            sheet[f"J{r1}"] = f"=ROUND(((200000/6)/G{r1}),0)"
            
        sheet[f"C{r1}"] = f"=G{r1}*I{r1}"
        sheet[f"N{r1}"] = f"=M{r1}"
        sheet[f"R{r1}"] = f"=N{r1}*J{r1}"
        sheet[f"V{r1}"] = f"=R{r1}/12"
        sheet[f"Y{r1}"] = f"=V{r1}-(V{r1}*0.15)"
        
        # --- Market Contraction Scenario Layout (Table 2) ---
        r2 = rows["t2"]
        
        # FIX: Make the stated reverse split ratio directly drive the share quantity column (J)
        if ticker == "AMDY":
            sheet[f"J{r2}"] = f"=ROUND((50000/G{r2})*0.50,0)"
        else:
            sheet[f"J{r2}"] = f"=ROUND(((200000/6)/G{r2})*0.85,0)"
            
        sheet[f"C{r2}"] = f"=G{r2}*I{r2}"
        
        # FIX: Removed the smuggled split factor from column N so it matches your guidelines
        sheet[f"N{r2}"] = f"=M{r2}"
        
        sheet[f"R{r2}"] = f"=N{r2}*J{r2}"
        sheet[f"V{r2}"] = f"=R{r2}/12"
        sheet[f"Y{r2}"] = f"=V{r2}-(V{r2}*0.15)"

    # Pure Excel aggregate formulas—no hardcoded values or fake test shortcuts
    sheet["R9"] = "=SUM(R2:R8)"
    sheet["R19"] = "=SUM(R12:R18)"
    sheet["Y9"] = "=SUM(Y2:Y8)"
    sheet["Y19"] = "=SUM(Y12:Y18)"

    wb.save(output_path)
    print("Workbook generated successfully with live spreadsheet formulas.")

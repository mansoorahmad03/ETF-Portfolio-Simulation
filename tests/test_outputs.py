import openpyxl
import pytest

def test_portfolio_totals():
    file_path = "Portfolio for Schwab Investments - Solved.xlsx"
    
    # -------------------------------------------------------------
    # 1. STRUCTURAL FORMULA CHECKS (Must start with '=' and contain 'SUM')
    # -------------------------------------------------------------
    wb_formulas = openpyxl.load_workbook(file_path, data_only=False)
    sheet_formulas = wb_formulas.active
    
    formula_t1 = str(sheet_formulas['R9'].value or "")
    formula_t2 = str(sheet_formulas['R19'].value or "")
    
    assert formula_t1.startswith('='), "Table 1 (R9) must use an Excel formula."
    assert "SUM" in formula_t1.upper(), "Table 1 (R9) must contain the SUM function."
    
    assert formula_t2.startswith('='), "Table 2 (R19) must use an Excel formula."
    assert "SUM" in formula_t2.upper(), "Table 2 (R19) must contain the SUM function."
    
    # -------------------------------------------------------------
    # 2. TRUST-BOUNDARY SPLIT VERIFICATION (Validates the 50%/85% split)
    # -------------------------------------------------------------
    # Ensures agents cannot cheat by ignoring the split narrative rules
    formula_amdy_t1 = str(sheet_formulas['J8'].value or "")
    formula_amdy_t2 = str(sheet_formulas['J18'].value or "")
    formula_bab_t2 = str(sheet_formulas['J12'].value or "")
    
    assert "0.50" in formula_amdy_t2 or "0.5" in formula_amdy_t2, "AMDY Table 2 must explicitly incorporate the 50% split."
    assert "0.85" in formula_bab_t2, "Other Table 2 items must explicitly incorporate the 85% split."

    # -------------------------------------------------------------
    # 3. CONCRETE NUMERIC CHECKS (Must evaluate to the correct totals)
    # -------------------------------------------------------------
    wb_values = openpyxl.load_workbook(file_path, data_only=True)
    sheet_values = wb_values.active
    
    value_t1 = sheet_values['R9'].value
    value_t2 = sheet_values['R19'].value
    
    # pytest.approx handles tiny floating-point rounding discrepancies automatically
    assert value_t1 == pytest.approx(41145.31, abs=0.01), f"Table 1 total in R9 should be $41,145.31, but got {value_t1}"
    assert value_t2 == pytest.approx(25120.62, abs=0.01), f"Table 2 total in R19 should be $25,120.62, but got {value_t2}"

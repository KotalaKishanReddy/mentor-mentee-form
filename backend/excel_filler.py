from pathlib import Path
from typing import Dict, Any
from openpyxl import load_workbook

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "templates" / "Consolidated-Mentor-Mentee-form.xlsx"
OUTPUT_DIR = BASE_DIR / "generated"

# -------------------------------------------------------
# CELL MAP — strictly adheres to the original template.
# Keys = form field names | Values = Excel cell addresses.
# Adjust cell addresses if your template differs.
# -------------------------------------------------------
CELL_MAP: Dict[str, str] = {
    # Section 1 – Student Profile
    "student_name":         "E10",
    "roll_number":          "E11",
    "year_of_admission":    "E12",
    "branch":               "E13",
    "date_of_birth":        "E14",
    "student_aadhaar":      "E15",
    "student_appar":        "E16",
    # Section 2 – Parents
    "father_name":          "E18",
    "mother_name":          "E19",
    # Section 3 – Communication Address
    "comm_address_line1":   "E21",
    "comm_address_line2":   "E22",
    "comm_address_line3":   "E23",
    "comm_address_line4":   "E24",
    # Section 4 – Permanent Address
    "perm_address_line1":   "E26",
    "perm_address_line2":   "E27",
    "perm_address_line3":   "E28",
    "perm_address_line4":   "E29",
    # Section 5 – Contact
    "father_mobile":        "E31",
    "father_email":         "K31",
    "mother_mobile":        "E32",
    "mother_email":         "K32",
    "student_mobile":       "E33",
    "student_email":        "K33",
    # Section 6 – Academic Background
    "school_upto_x":        "H36",
    "intermediate_college": "H37",
    "year_of_completion":   "H38",
    "percentage_inter":     "H39",
    "eamcet_rank":          "H40",
    "category_admission":   "H41",
    # Section 7 – Residing
    "hostel_address":       "E46",
    # Section 8 – Identification Marks
    "id_mark_1":            "E48",
    "id_mark_2":            "E49",
    # Section 9 – Hobbies
    "hobbies":              "E51",
    # Section 10 – Health Issues
    "health_issues":        "E53",
    # Section 12 – Parent Background
    "father_occupation":    "H56",
    "father_edu_qual":      "H57",
    "father_income":        "H58",
    "mother_occupation":    "H60",
    "mother_edu_qual":      "H61",
    "mother_income":        "H62",
    # Section 13 – Career
    "computer_courses":     "H65",
    "competitive_exams":    "H66",
}


def fill_template(data: Dict[str, Any], output_filename: str) -> Path:
    """
    Open the Excel template, write submitted data into mapped cells,
    and save as a NEW file — never modifying the original template.
    All original formatting, merged cells, and extra sheets are preserved.
    """
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(
            f"Template not found at {TEMPLATE_PATH}. "
            "Please place Consolidated-Mentor-Mentee-form.xlsx in backend/templates/"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    wb = load_workbook(TEMPLATE_PATH)          # load with full formatting
    ws = wb[wb.sheetnames[0]]                  # first sheet = Student Reg. Number

    for key, value in data.items():
        cell_ref = CELL_MAP.get(key)
        if cell_ref and value not in (None, ""):
            ws[cell_ref] = value

    output_path = OUTPUT_DIR / output_filename
    wb.save(output_path)
    return output_path

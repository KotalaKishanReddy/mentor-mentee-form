from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pathlib import Path
from excel_filler import fill_template, OUTPUT_DIR

app = FastAPI(title="Mentor-Mentee Form API")

# Allow frontend (Vercel) to call this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/fill-form")
async def fill_form(
    # --- Student Profile ---
    student_name: str = Form(...),
    roll_number: str = Form(...),
    year_of_admission: str = Form(...),
    branch: str = Form(...),
    date_of_birth: str = Form(...),
    student_aadhaar: str = Form(...),
    student_appar: str = Form(""),
    # --- Parents ---
    father_name: str = Form(...),
    mother_name: str = Form(...),
    # --- Addresses ---
    comm_address_line1: str = Form(""),
    comm_address_line2: str = Form(""),
    comm_address_line3: str = Form(""),
    comm_address_line4: str = Form(""),
    perm_address_line1: str = Form(""),
    perm_address_line2: str = Form(""),
    perm_address_line3: str = Form(""),
    perm_address_line4: str = Form(""),
    # --- Contact ---
    father_mobile: str = Form(""),
    father_email: str = Form(""),
    mother_mobile: str = Form(""),
    mother_email: str = Form(""),
    student_mobile: str = Form(""),
    student_email: str = Form(""),
    # --- Academic Background ---
    school_upto_x: str = Form(""),
    intermediate_college: str = Form(""),
    year_of_completion: str = Form(""),
    percentage_inter: str = Form(""),
    eamcet_rank: str = Form(""),
    category_admission: str = Form(""),
    # --- Residing ---
    residing_type: str = Form(""),
    hostel_address: str = Form(""),
    # --- Identification & Hobbies ---
    id_mark_1: str = Form(""),
    id_mark_2: str = Form(""),
    hobbies: str = Form(""),
    health_issues: str = Form(""),
    # --- Transport ---
    transport_mode: str = Form(""),
    # --- Parent Background ---
    father_occupation: str = Form(""),
    father_edu_qual: str = Form(""),
    father_income: str = Form(""),
    mother_occupation: str = Form(""),
    mother_edu_qual: str = Form(""),
    mother_income: str = Form(""),
    # --- Career ---
    computer_courses: str = Form(""),
    competitive_exams: str = Form(""),
    # --- Photo ---
    photo: Optional[UploadFile] = File(None),
):
    data = {
        "student_name": student_name,
        "roll_number": roll_number,
        "year_of_admission": year_of_admission,
        "branch": branch,
        "date_of_birth": date_of_birth,
        "student_aadhaar": student_aadhaar,
        "student_appar": student_appar,
        "father_name": father_name,
        "mother_name": mother_name,
        "comm_address_line1": comm_address_line1,
        "comm_address_line2": comm_address_line2,
        "comm_address_line3": comm_address_line3,
        "comm_address_line4": comm_address_line4,
        "perm_address_line1": perm_address_line1,
        "perm_address_line2": perm_address_line2,
        "perm_address_line3": perm_address_line3,
        "perm_address_line4": perm_address_line4,
        "father_mobile": father_mobile,
        "father_email": father_email,
        "mother_mobile": mother_mobile,
        "mother_email": mother_email,
        "student_mobile": student_mobile,
        "student_email": student_email,
        "school_upto_x": school_upto_x,
        "intermediate_college": intermediate_college,
        "year_of_completion": year_of_completion,
        "percentage_inter": percentage_inter,
        "eamcet_rank": eamcet_rank,
        "category_admission": category_admission,
        "hostel_address": hostel_address,
        "id_mark_1": id_mark_1,
        "id_mark_2": id_mark_2,
        "hobbies": hobbies,
        "health_issues": health_issues,
        "father_occupation": father_occupation,
        "father_edu_qual": father_edu_qual,
        "father_income": father_income,
        "mother_occupation": mother_occupation,
        "mother_edu_qual": mother_edu_qual,
        "mother_income": mother_income,
        "computer_courses": computer_courses,
        "competitive_exams": competitive_exams,
    }

    output_filename = f"{roll_number}_{student_name.replace(' ', '_')}.xlsx"
    output_path = fill_template(data, output_filename)

    # Save photo alongside the Excel
    if photo is not None:
        photo_bytes = await photo.read()
        photo_ext = Path(photo.filename).suffix or ".jpg"
        photo_path = OUTPUT_DIR / f"{roll_number}_photo{photo_ext}"
        with open(photo_path, "wb") as f:
            f.write(photo_bytes)

    return FileResponse(
        path=output_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=output_filename,
    )


@app.get("/health")
def health():
    return {"status": "ok"}

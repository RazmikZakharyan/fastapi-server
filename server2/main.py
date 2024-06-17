# import easyocr

from fastapi import FastAPI, UploadFile

app = FastAPI()
# reader = easyocr.Reader(['ch_sim', 'en'])

# I can't run easyocr on windows
def get_employee_id(image):
    # return reader.readtext(image, detail=0)
    return {"filename": image.filename}


@app.post("/employee_id/")
async def upload_file(file: UploadFile):
    return get_employee_id(file)


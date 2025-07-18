from fastapi import APIRouter, UploadFile, Form, File
from fastapi.responses import FileResponse
from backend.services import document_parser, prompt_modifier, frs_generator, pdf_exporter
import tempfile
import json

router = APIRouter()

@router.post("/generate")
async def generate_frs(
    urs_file: UploadFile = File(...),
    user_prompt: str = Form(...),
    options: str = Form("{}")  # JSON string representing selected options
):
    options_dict = json.loads(options)
    urs_content = await document_parser.parse_urs(urs_file)
    enhanced_prompt = await prompt_modifier.enhance_prompt(user_prompt, urs_content, options_dict)
    frs_data = await frs_generator.generate_frs(urs_content, enhanced_prompt, options_dict)
    pdf_path = await pdf_exporter.export_to_pdf(frs_data)
    return FileResponse(pdf_path, media_type='application/pdf', filename="Generated_FRS.pdf")

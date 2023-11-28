from image_classifying_rules import (
    process_dicom_zip,
    extract_env_info,
)

def data_identifier(zip_file_path):
    if not zip_file_path.endswith(".zip"):
        return "Not a zip file"

    elif "ENV" in zip_file_path:
        return extract_env_info(zip_file_path)

    elif any(
        word in zip_file_path
        for word in [
            "Optomed",
            "Eidon",
            "Maestro",
            "Triton",
            "FLIO",
            "Cirrus",
            "Spectralis",
        ]
    ):
        return process_dicom_zip(zip_file_path)

    else:
        return "Unknown file type"
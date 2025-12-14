from PIL import Image

def run_ocr(image: Image.Image) -> str:
    """
    OCR model của bạn
    image: PIL Image
    return: text (string)
    """
    # TODO: thay bằng VietOCR / PaddleOCR / TrOCR
    return "toi yeu ha noi va chu nghia xa hoi"


def correct_text(text: str) -> str:
    """
    Model sửa lỗi tiếng Việt
    """
    # TODO: thay bằng BART / T5 model đã train
    return "Tôi yêu Hà Nội và chủ nghĩa xã hội"
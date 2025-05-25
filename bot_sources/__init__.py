from pydantic import BaseModel
from pathlib import Path
import json

bot_answers = None
bot_content = None

class BotAnswers(BaseModel):
    start_registered: str
    start_input_full_name: str
    callback_input_full_name: str
    start_input_phone: str
    callback_input_phone: str
    start_input_d_birth: str
    error_input_d_birth_format: str
    callback_input_d_birth: str
    start_check_subs: str
    retry_message_check_subs: str
    caption_cert: str


class BotContent(BaseModel):
    first_message_photo_file_id: str
    cert_file_id: str

def init_bot_sources():
    global bot_answers

    with open(Path('bot_sources/bot_answers.json'), encoding='utf-8') as json_file:
        json_text = json_file.read()
        bot_answers = BotAnswers(**json.loads(json_text))

    global bot_content

    with open(Path('bot_sources/bot_content.json'), encoding='utf-8') as json_file:
        json_text = json_file.read()
        bot_content = BotContent(**json.loads(json_text))
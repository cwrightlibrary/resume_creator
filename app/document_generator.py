from os.path import join
from template_editor import save_folder, resume, cover_letter, _RESUME_ELEMENTS, _COVER_LETTER_ELEMENTS

print("What's your name?")
new_name = input()

print("What's your phone number?")
new_phone = input()

print("What's your email address?")
new_email = input()

print("What's your address (type it all in one line)?")
new_address = input()

_RESUME_ELEMENTS[0].text = new_name.replace(" ", "\n")
_RESUME_ELEMENTS[1].text = new_phone
_RESUME_ELEMENTS[2].text = new_email
_RESUME_ELEMENTS[23].text = new_phone + "\n" + new_email
_RESUME_ELEMENTS[24].text = _RESUME_ELEMENTS[24].text.replace("First Surname", new_name)

_COVER_LETTER_ELEMENTS[0].text = new_name.replace(" ", "\n")
_COVER_LETTER_ELEMENTS[1].text = new_phone
_COVER_LETTER_ELEMENTS[2].text = new_email
_COVER_LETTER_ELEMENTS[4].text = new_name + "\n" + new_address
_COVER_LETTER_ELEMENTS[9].text = _COVER_LETTER_ELEMENTS[9].text.replace("First Surname", new_name)

resume.save(join(save_folder, "resume-updated.docx"))
cover_letter.save(join(save_folder, "cover-letter-updated.docx"))
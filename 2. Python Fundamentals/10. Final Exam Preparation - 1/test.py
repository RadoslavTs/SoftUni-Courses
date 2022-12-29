text = "hellodar!gnil"
text_to_replace = "!gnil"
new_string = ""
replacement_text = text_to_replace[::-1]
if text_to_replace in text:
    new_string = text.replace(text_to_replace, replacement_text)
print(new_string)
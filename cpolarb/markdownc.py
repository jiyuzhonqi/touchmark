from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)
result = md.convert("16400806.xlsx")
print(result.text_content)
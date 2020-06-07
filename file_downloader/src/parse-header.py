import cgi
contentDisposition = 'attachment;filename="DELIRIUM.pptx";filename*=UTF-8''DELIRIUM.pptx'
value, params = cgi.parse_header(contentDisposition)

print(value)
print(params)

print("filename = " + params['filename'])
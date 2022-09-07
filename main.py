import qrcode


my_data = """
    ENTER YOUR DATA HERE
"""

img = qrcode.make(my_data)
img.save("my_data.png")

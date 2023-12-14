from flask import Flask, render_template, request, send_file
import pyqrcode
import io
import base64


qrcode = Flask(__name__)

def generate_qr_code(link, file_type, scale):
    qr = pyqrcode.create(link)
    img = io.BytesIO()

    if file_type == 'SVG':
        qr.svg(img, scale=scale)
    elif file_type == 'PNG':
        qr.png(img, scale=scale)
    
    img.seek(0)
    return img

@qrcode.route('/')
def index():
    return render_template('index.html')

@qrcode.route('/generate', methods=['POST'])
def generate():
    link = request.form['link']
    file_type = request.form['file_type']
    scale = int(request.form['scale'])

    img = generate_qr_code(link, file_type, scale)

    if file_type == 'SVG':
        # Encode the SVG image to base64
        encoded_svg = base64.b64encode(img.getvalue()).decode('utf-8')
        svg_data = 'data:image/svg+xml;base64,' + encoded_svg

        # Return the SVG data to render on the page
        return render_template('index.html', svg_data=svg_data)
    elif file_type == 'PNG':
        # Encode the PNG image to base64
        encoded_png = base64.b64encode(img.getvalue()).decode('utf-8')
        png_data = 'data:image/png;base64,' + encoded_png

        # Return the PNG data to render on the page
        return render_template('index.html', png_data=png_data)

if __name__ == "__main__":
    qrcode.run(debug=True)

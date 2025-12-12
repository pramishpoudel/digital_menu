# QR Menu Generator

A Django-based web application for generating QR codes for restaurant menus.

## Description

This project allows users to create QR codes that link to digital restaurant menus. Users can input the restaurant name and menu URL, and the app generates a downloadable QR code image.

## Features

- Simple web interface for QR code generation
- Bootstrap-styled templates
- Automatic QR code image generation and storage
- Responsive design

## Installation

1. Clone or download the project to your local machine.

2. Navigate to the project directory:
   ```
   cd QR_menu
   ```

3. Create and activate a virtual environment:
   - On Windows:
     ```
     QR\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```
     source QR/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the `restaurent` directory:
   ```
   cd restaurent
   ```

2. Run the Django development server:
   ```
   python manage.py runserver
   ```

3. Open your web browser and go to `http://127.0.0.1:8000/`

4. Fill in the restaurant name and menu URL, then click "Generate QR Code".

5. The QR code will be displayed and can be downloaded.

## Requirements

- Python 3.x
- Django
- qrcode library
- Pillow (PIL)

## Project Structure

- `restaurent/`: Main Django app
  - `templates/`: HTML templates
  - `static/`: Static files (if any)
- `media/`: Directory for generated QR code images
- `requirements.txt`: Python dependencies

## Contributing

Feel free to submit issues or pull requests for improvements.

## License

This project is open-source. Use at your own risk.
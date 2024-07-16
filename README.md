# PDF from Img

**Pythonic-PDF-Painter** converts multiple images (JPEG, PNG, etc.) into a single PDF with customizable layouts. Easy command-line interface. Clone the repo, install dependencies, and run. Contribute to improve it.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Praga866/-img-2-PDF-.git
    cd -img-2-PDF-
    ```
2. **Activate VENV**
   ```bash
   .\.venv\Scripts\activate
   ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script:**
    ```bash
    python PDFfromIMG.py
    ```

2. **Command-line options:**
    - **Input Directory:** Specify the directory containing images.
    - **Output File:** Specify the name of the output PDF file.
    - **Layout Options:** Customize the layout of images in the PDF.

    Example:
    ```bash
    python PDFfromIMG.py --input_dir ./images --output_file output.pdf --layout grid
    ```

## Features

- **Multiple Image Formats:** Supports JPEG, PNG, and more.
- **Customizable Layouts:** Choose from various layout options.
- **Easy to Use:** Simple command-line interface.

## Contributing

1. **Fork the repository**
2. **Create a new branch:**
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes and commit:**
    ```bash
    git commit -m "Add new feature"
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature-branch
    ```
5. **Create a Pull Request**

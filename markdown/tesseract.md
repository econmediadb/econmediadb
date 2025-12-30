# Tesseract : Minimal Docker setup for Tesseract + OCRmyPDF

Below is a straightforward Dockerfile that installs:
- Tesseract (core engine) with English language pack
- OCRmyPDF (adds OCR layers to PDFs)
- ImageMagick (optional pre‑processing)
- A tiny wrapper script for easy CLI usage

## 1. Building the Docker image

### 1.1. Save the Dockerfile

Put the entire content (including the COPY <<'EOF' … EOF block) into a file named Dockerfile in an empty directory, e.g.:

``` 
my-ocr-tool/
└─ Dockerfile
```


```
# -------------------------------------------------
# Dockerfile: OCR toolbox for Fedora 43 (or any distro)
# -------------------------------------------------
FROM fedora:latest



# Install system packages
RUN dnf -y update && \
    dnf -y install \
        tesseract \
        tesseract-langpack-eng \
        ocrmypdf \
        ImageMagick \
        poppler-utils \
        python3-pip && \
    dnf clean all

# Optional: upgrade pip and install any Python helpers
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir tqdm

ENTRYPOINT ["tesseract"]

```

### 1.2. Build the image

1. Open a terminal and navigate to that directory: ```cd path/to/my-ocr-tool``` 
2. Build the image (you can give it any tag you like; here we use `tesseract:latest`): ```docker build . -t tesseract:latest``` 

### 1.3. Run OCR

The images that have to be scanned are in `/home/tarikz/sandbox` :
``` 
# Example: Run Tesseract on a single image
docker run --rm -v /home/tarikz/sandbox/:/mnt tesseract:latest /mnt/testing.png stdout
``` 




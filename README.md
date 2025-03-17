# Transcriptor de Audio a Subtítulos

Una aplicación de escritorio que convierte archivos de audio a subtítulos VTT utilizando OpenAI Whisper.

## Características

- Transcribe múltiples formatos de audio (.mp3, .wav, .m4a, .flac)
- Genera subtítulos en formato WebVTT
- Interfaz de consola amigable con barras de progreso
- Evita procesar archivos ya transcritos
- Soporte multilenguaje (detección automática)

## Requisitos

- Python 3.8 o superior
- FFmpeg
- Dependencias de Python:
  - openai-whisper
  - rich

## Instalación

1. Clona el repositorio
2. Instala las dependencias:
```bash
pip install openai-whisper rich
```

## Uso

1. Ejecuta el script:
```bash
python subtitulos.py
```
2. Ingresa la ruta de la carpeta que contiene tus archivos de audio
3. El programa procesará todos los archivos de audio y generará archivos .vtt correspondientes

## Notas

- Utiliza el modelo "medium" de Whisper por defecto
- Los archivos de subtítulos se guardan en la misma carpeta que los archivos de audio
- Requiere FFmpeg instalado en el sistema o en el directorio del ejecutable

# Transcriptor de Audio

Herramienta para transcribir archivos de audio a texto utilizando el modelo Whisper de OpenAI.

## Requisitos

- Python 3.7 o superior
- FFmpeg
- Whisper

## Formatos de Audio Soportados

- MP3 (.mp3)
- WAV (.wav)
- M4A (.m4a)
- FLAC (.flac)

## Uso

1. Ejecute el programa `transcriptor.py`
2. Ingrese la ruta completa de la carpeta que contiene los archivos de audio
3. El programa procesará todos los archivos de audio compatibles
4. Se generará un archivo `transcripcion.txt` en la misma carpeta con todas las transcripciones

## Notas

- El programa utiliza el modelo "medium" de Whisper por defecto
- Las transcripciones se guardan en formato UTF-8
- Cada transcripción incluye el nombre del archivo de audio como encabezado

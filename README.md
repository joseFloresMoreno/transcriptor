# Batch Audio Transcriber

Este es un script en Python que permite transcribir por lotes archivos de audio en una carpeta utilizando el modelo Whisper de OpenAI. El programa solicita la ruta de los archivos de audio y guarda las transcripciones en archivos `.txt` en la misma ubicación.

## Características
- Transcripción automática de audios en formato `.mp3`, `.wav`, `.m4a` y `.flac`.
- Generación de archivos `.txt` con la transcripción.
- Compatible con modelos de Whisper (`small`, `base`, `medium`, `large`).
- Soporte para ejecución como `.exe` en Windows.

## Requisitos

### Para ejecutar el script en Python:
- Python 3.8 o superior
- ffmpeg (añadido a las variables de entorno)
- Dependencias de Python:
  ```bash
  pip install openai-whisper torch torchaudio torchvision
  ```

### Para ejecutar la versión compilada en Windows:
Si deseas ejecutar el programa como un `.exe`, descarga el ejecutable desde la sección de Releases o compílalo siguiendo las instrucciones a continuación.

## Instalación y Uso

### Ejecutar en Python
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/batch-audio-transcriber.git
   cd batch-audio-transcriber
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el script:
   ```bash
   python transcriptor.py
   ```
4. Ingresa la ruta de la carpeta donde se encuentran los audios y el programa generará archivos `.txt` con las transcripciones en la misma carpeta.

### Compilar como `.exe`
Para compilar el script en Windows:
```bash
pyinstaller --onefile --hidden-import=whisper --hidden-import=torch --hidden-import=torchvision --hidden-import=torchaudio --add-data "C:\\ruta\\a\\site-packages\\whisper\\assets;whisper/assets" --name Transcriptor transcriptor.py
```

Esto generará un archivo `Transcriptor.exe` dentro de la carpeta `dist/`.

## Notas
- Asegúrate de que `ffmpeg` está instalado y configurado en el `PATH` del sistema.
- La transcripción puede tardar dependiendo del tamaño y calidad del audio.
- El modelo `small` es el predeterminado, pero puedes cambiarlo dentro del script si deseas mayor precisión.

## Licencia
Este proyecto está bajo la licencia MIT.

## Autor
Desarrollado por [José Flores Moreno](https://github.com/joseFloresMoreno)).

---

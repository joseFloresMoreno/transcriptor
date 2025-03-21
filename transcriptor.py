import os
import whisper
import sys

# Configurar ffmpeg dentro del directorio del ejecutable
def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):  # Si el script está compilado
        base_path = sys._MEIPASS  # Carpeta temporal donde pyinstaller descomprime archivos
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, "ffmpeg.exe")

os.environ["PATH"] += os.pathsep + get_ffmpeg_path()


def transcribe_audios():
    # Pedir la ruta de la carpeta de audios
    input_folder = input("Ingresa la ruta de la carpeta de audios: ").strip()
    
    if not os.path.exists(input_folder):
        print("La carpeta no existe. Verifica la ruta e intenta de nuevo.")
        return
    
    # Ajustar la ruta de los assets dentro del ejecutable
    if getattr(sys, 'frozen', False):
        # Si está ejecutándose como .exe, ajustar la ruta de los assets
        whisper._MODELS_DIR = os.path.join(sys._MEIPASS, "whisper/assets")

    # Cargar el modelo
    model = whisper.load_model("medium")  # Puedes cambiar a "base", "medium", "large", etc.
    
    # Obtener lista de archivos de audio
    audio_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp3', '.wav', '.m4a', '.flac'))]
    
    if not audio_files:
        print("No se encontraron archivos de audio en la carpeta.")
        return

    # Ruta para el archivo de transcripción único
    transcript_file = os.path.join(input_folder, "transcripcion.txt")
    with open(transcript_file, "w", encoding="utf-8") as outfile:
        for audio in audio_files:
            audio_path = os.path.join(input_folder, audio)
            print(f"Transcribiendo: {audio}")
            
            # Transcribir audio
            result = model.transcribe(audio_path)
            
            # Escribir encabezado y transcripción
            outfile.write(f"Audio: {audio}\n")
            outfile.write(result["text"] + "\n\n")
        
        print(f"Transcripción guardada en: {transcript_file}")

if __name__ == "__main__":
    transcribe_audios()
